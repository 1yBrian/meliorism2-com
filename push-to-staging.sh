#!/bin/bash
# ─────────────────────────────────────────────────────────────────────────────
# Meliorism2 · push-to-staging.sh
# Pushes a draft issue from _engine/staging/ to the staging branch on GitHub.
# Cloudflare Pages auto-deploys staging → preview URL for phone review.
#
# USAGE:
#   ./push-to-staging.sh _engine/staging/2026-05-28-the-tide-pool-survey-draft.html
#
# The draft is published to the archive/ path (same URL structure as live),
# so Brian sees it exactly as it will appear when deployed to main.
#
# STAGING URL pattern (after Cloudflare Pages is configured):
#   https://staging.meliorism2-com.pages.dev/archive/YYYY-MM-DD-slug.html
# ─────────────────────────────────────────────────────────────────────────────

set -e
[ -f "$HOME/.zshrc" ] && source "$HOME/.zshrc" 2>/dev/null || true

REPO="1yBrian/meliorism2-com"
BRANCH="staging"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TOKEN_FILE="$HOME/.config/meliorism2/github-token"
API="https://api.github.com"

# ── Token ─────────────────────────────────────────────────────────────────────
if [ ! -f "$TOKEN_FILE" ]; then
  echo "✗ No github-token found at $TOKEN_FILE" && exit 1
fi
TOKEN=$(cat "$TOKEN_FILE" | tr -d '[:space:]')

# ── Args ──────────────────────────────────────────────────────────────────────
DRAFT_PATH="$1"
if [ -z "$DRAFT_PATH" ]; then
  echo "Usage: ./push-to-staging.sh _engine/staging/YYYY-MM-DD-slug-draft.html"
  exit 1
fi

if [ ! -f "$SCRIPT_DIR/$DRAFT_PATH" ]; then
  echo "✗ Draft not found: $SCRIPT_DIR/$DRAFT_PATH"
  exit 1
fi

# ── Derive archive path from draft filename ────────────────────────────────────
# _engine/staging/2026-05-28-the-tide-pool-survey-draft.html
#   → archive/2026-05-28-the-tide-pool-survey.html
BASENAME=$(basename "$DRAFT_PATH")
ARCHIVE_NAME="${BASENAME/-draft.html/.html}"
ARCHIVE_PATH="archive/$ARCHIVE_NAME"

echo "→ Staging: $DRAFT_PATH"
echo "  Preview path: $ARCHIVE_PATH"

# ── Truth gate — MOVED LEFT ───────────────────────────────────────────────────
# Catch over-promises at draft/staging time, not at deploy. Same gate deploy uses;
# blocking here means a draft never reaches the archive carrying an unsupported claim.
if [[ "$ARCHIVE_NAME" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}-.+\.html$ ]] && [ -f "$SCRIPT_DIR/_engine/truth_agent.py" ] && command -v python3 &>/dev/null; then
  set +e
  python3 "$SCRIPT_DIR/_engine/truth_agent.py" "$SCRIPT_DIR/$DRAFT_PATH"
  TRUTH_STATUS=$?
  set -e
  if [ "$TRUTH_STATUS" -eq 1 ]; then
    echo ""
    echo "  ✗ Staging blocked at draft time — fix the over-promises above, then re-push."
    echo "    (Gate moved left: cheaper to fix now than after it is in the archive.)"
    exit 1
  fi
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
    "$API/$endpoint" -d "$@"
}
api_patch() {
  local endpoint="$1"; shift
  curl -sf -X PATCH \
    -H "Authorization: token $TOKEN" \
    -H "Accept: application/vnd.github.v3+json" \
    -H "Content-Type: application/json" \
    "$API/$endpoint" -d "$@"
}

# ── Get staging HEAD ──────────────────────────────────────────────────────────
echo "→ Fetching staging branch state..."
REF_DATA=$(api_get "repos/$REPO/git/refs/heads/$BRANCH")
HEAD_SHA=$(echo "$REF_DATA" | python3 -c "import sys,json; print(json.load(sys.stdin)['object']['sha'])")
COMMIT_DATA=$(api_get "repos/$REPO/git/commits/$HEAD_SHA")
BASE_TREE=$(echo "$COMMIT_DATA" | python3 -c "import sys,json; print(json.load(sys.stdin)['tree']['sha'])")
echo "  staging HEAD: ${HEAD_SHA:0:7}"

# ── Create blob ───────────────────────────────────────────────────────────────
echo "→ Uploading draft..."
CONTENT_B64=$(base64 < "$SCRIPT_DIR/$DRAFT_PATH" | tr -d '\n')
BLOB=$(api_post "repos/$REPO/git/blobs" "{\"content\":\"$CONTENT_B64\",\"encoding\":\"base64\"}")
BLOB_SHA=$(echo "$BLOB" | python3 -c "import sys,json; print(json.load(sys.stdin)['sha'])")

# ── Create tree ───────────────────────────────────────────────────────────────
echo "→ Creating tree..."
NEW_TREE=$(api_post "repos/$REPO/git/trees" \
  "{\"base_tree\":\"$BASE_TREE\",\"tree\":[{\"path\":\"$ARCHIVE_PATH\",\"mode\":\"100644\",\"type\":\"blob\",\"sha\":\"$BLOB_SHA\"}]}")
NEW_TREE_SHA=$(echo "$NEW_TREE" | python3 -c "import sys,json; print(json.load(sys.stdin)['sha'])")

# ── Create commit ─────────────────────────────────────────────────────────────
echo "→ Creating commit..."
SLUG="${ARCHIVE_NAME%.html}"
MSG="staging: $SLUG"
MSG_ESC=$(echo "$MSG" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read().strip()))")
NEW_COMMIT=$(api_post "repos/$REPO/git/commits" \
  "{\"message\":$MSG_ESC,\"tree\":\"$NEW_TREE_SHA\",\"parents\":[\"$HEAD_SHA\"]}")
NEW_COMMIT_SHA=$(echo "$NEW_COMMIT" | python3 -c "import sys,json; print(json.load(sys.stdin)['sha'])")

# ── Advance staging ref ───────────────────────────────────────────────────────
echo "→ Updating staging branch..."
api_patch "repos/$REPO/git/refs/heads/$BRANCH" \
  "{\"sha\":\"$NEW_COMMIT_SHA\",\"force\":false}" > /dev/null

echo ""
echo "✓ Draft staged: $ARCHIVE_PATH"
echo "  Cloudflare will build the preview in ~60 seconds."
echo ""
echo "  Preview URL (once Cloudflare Pages staging is configured):"
echo "  https://staging.meliorism2-com.pages.dev/$ARCHIVE_PATH"
echo ""
echo "  Share this link with yourself for phone review."
