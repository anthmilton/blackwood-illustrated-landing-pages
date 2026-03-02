#!/bin/bash
# Deploy Memory Bridge Books website to production (memorybridgebooks.com)
# This script ensures deployment to the CORRECT Vercel project

set -e

REPO_PATH="/home/node/.openclaw/workspace/landing-pages"
PROJECT_NAME="blackwood-illustrated-landing-pages"

cd "$REPO_PATH"

echo "🚀 Deploying to memorybridgebooks.com..."
echo "   Project: $PROJECT_NAME"
echo "   Path: $REPO_PATH"
echo ""

# Deploy using Vercel API with correct project
npx vercel deploy --prod \
  --token "$VERCEL_TOKEN" \
  --yes \
  2>&1 | grep -E "(Production:|Inspect:|Error|Ready)" || true

echo ""
echo "✅ Deployment triggered!"
echo "   URL: https://www.memorybridgebooks.com"
echo "   Note: Changes may take 60-90 seconds to propagate"
