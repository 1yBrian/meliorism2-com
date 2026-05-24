#!/bin/bash
# ─────────────────────────────────────────────────────────────────────────────
# Signal-OS · deploy-api.sh
# Push files to GitHub via the API — never touches git lock files.
#
# ONE-TIME SETUP (run once in Terminal, never again):
#   echo 'ghp_YourTokenHere' > ~/Documents/Claude/Projects/Signal-OS.org/.github-token
#   chmod 600 ~/Documents/Claude/Projects/Signal-OS.org/.github-token
#
#   Token needs: repo → Contents → Read and Write
#   Create at: https://github.com/settings/tokens → Fine-grained tokens
#   Repository: 1yBrian/signal-os
#
# USAGE (Claude or Terminal):
#   ./deploy-api.sh "commit message" file1 file2 ...
#   ./deploy-api.sh "Fix mobile button" index.html archive/index.html
#
# If no files are listed, stages ALL changed/untracked files (like git add -A).
# ─────────────────────────────────────────────────────────────────────────────

set -e

REPO="1yBrian/meliorism2-com"
BRANCH="main"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TOKEN_FILE="$SCRIPT_DIR/.github-token"
API="https://api.github.com"

# ── Token ────────────────────────────────────────────────────────────────────
if [ ! -f "$TOKEN_FILE" ]; then
  echo ""
  echo "  ✗ No .github-token found."
  echo ""
  echo "  ONE-TIME SETUP:"
  echo "    1. Go to: https://github.com/settings/tokens"
  echo "    2. New fine-grained token → Repository: 1yBrian/signal-os"
  echo "    3. Permissions: Contents → Read and Write"
  echo "    4. Run: echo 'ghp_yourtoken' > $TOKEN_FILE && chmod 600 $TOKEN_FILE"
  echo ""
  exit 1
fi

TOKEN=$(cat "$TOKEN_FILE" | tr -d '[:space:]')
if [[ -z "$TOKEN" ]]; then
  echo "✗ .github-token is empty. Re-run setup." && exit 1
fi

# ── Args ─────────────────────────────────────────────────────────────────────
MSG="${1:-Deploy: $(date '+%Y-%m-%d %H:%M')}"
shift || true

# If no files given, use git to find changed/new files vs HEAD
if [ $# -eq 0 ]; then
  echo "→ Detecting changed files..."
  cd "$SCRIPT_DIR"
  FILES=$(git diff --name-only HEAD 2>/dev/null; git ls-files --others --exclude-standard 2>/dev/null)
  if [[ -z "$FILES" ]]; then
    echo "  Nothing to deploy (no changed files detected)."
    exit 0
  fi
  echo "  Found: $(echo "$FILES" | tr '\n' ' ')"
else
  FILES="$@"
  cd "$SCRIPT_DIR"
fi

# ── API helpers ───────────────────────────────────────────────────────────────
api_get() {
  curl -sf -H "Authorization: token $TOKEN" -H "Accept: application/vnd.github.v3+json" "$API/$1"
}

api_post() {
  local endpoint="$1"; shift
  curl -sf -X POST \
    -H "Authorization: token $TOKEN" \
    -H "Accept: application/vnd.github.v3+json" \
    -H "Content-Type: application/json" \
    "$API/$endpoint" \
    -d "$@"
}

api_patch() {
  local endpoint="$1"; shift
  curl -sf -X PATCH \
    -H "Authorization: token $TOKEN" \
    -H "Accept: application/vnd.github.v3+json" \
    -H "Content-Type: application/json" \
    "$API/$endpoint" \
    -d "$@"
}

# ── Get current HEAD commit + tree ────────────────────────────────────────────
echo "→ Fetching HEAD state..."
REF_DATA=$(api_get "repos/$REPO/git/refs/heads/$BRANCH")
HEAD_SHA=$(echo "$REF_DATA" | python3 -c "import sys,json; print(json.load(sys.stdin)['object']['sha'])")
COMMIT_DATA=$(api_get "repos/$REPO/git/commits/$HEAD_SHA")
BASE_TREE=$(echo "$COMMIT_DATA" | python3 -c "import sys,json; print(json.load(sys.stdin)['tree']['sha'])")
echo "  HEAD: ${HEAD_SHA:0:7} / tree: ${BASE_TREE:0:7}"

# ── Create blobs for each file ────────────────────────────────────────────────
echo "→ Creating blobs..."
TREE_ENTRIES=""
FIRST=1

for f in $FILES; do
  if [ ! -f "$SCRIPT_DIR/$f" ]; then
    echo "  ⚠ Skipping $f (not found)"
    continue
  fi
  echo "  blob: $f"
  CONTENT_B64=$(base64 < "$SCRIPT_DIR/$f" | tr -d '\n')
  BLOB=$(api_post "repos/$REPO/git/blobs" "{\"content\":\"$CONTENT_B64\",\"encoding\":\"base64\"}")
  BLOB_SHA=$(echo "$BLOB" | python3 -c "import sys,json; print(json.load(sys.stdin)['sha'])")

  ENTRY="{\"path\":\"$f\",\"mode\":\"100644\",\"type\":\"blob\",\"sha\":\"$BLOB_SHA\"}"
  if [ $FIRST -eq 1 ]; then
    TREE_ENTRIES="$ENTRY"
    FIRST=0
  else
    TREE_ENTRIES="$TREE_ENTRIES,$ENTRY"
  fi
done

if [[ -z "$TREE_ENTRIES" ]]; then
  echo "  Nothing to upload." && exit 0
fi

# ── Create new tree ───────────────────────────────────────────────────────────
echo "→ Creating tree..."
NEW_TREE=$(api_post "repos/$REPO/git/trees" \
  "{\"base_tree\":\"$BASE_TREE\",\"tree\":[$TREE_ENTRIES]}")
NEW_TREE_SHA=$(echo "$NEW_TREE" | python3 -c "import sys,json; print(json.load(sys.stdin)['sha'])")
echo "  tree: ${NEW_TREE_SHA:0:7}"

# ── Create commit ─────────────────────────────────────────────────────────────
echo "→ Creating commit..."
MSG_ESCAPED=$(echo "$MSG" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read().strip()))")
NEW_COMMIT=$(api_post "repos/$REPO/git/commits" \
  "{\"message\":$MSG_ESCAPED,\"tree\":\"$NEW_TREE_SHA\",\"parents\":[\"$HEAD_SHA\"]}")
NEW_COMMIT_SHA=$(echo "$NEW_COMMIT" | python3 -c "import sys,json; print(json.load(sys.stdin)['sha'])")
echo "  commit: ${NEW_COMMIT_SHA:0:7}"

# ── Advance branch ref ────────────────────────────────────────────────────────
echo "→ Updating $BRANCH..."
api_patch "repos/$REPO/git/refs/heads/$BRANCH" \
  "{\"sha\":\"$NEW_COMMIT_SHA\",\"force\":false}" > /dev/null
echo "  ✓ $BRANCH → ${NEW_COMMIT_SHA:0:7}"

echo ""
echo "✓ Deployed: \"$MSG\""
echo "  Cloudflare Pages will update in ~60 seconds."
echo "  Live: https://meliorism2.com"
