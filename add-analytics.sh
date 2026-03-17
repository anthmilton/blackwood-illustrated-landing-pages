#!/bin/bash
# Add Vercel Analytics to all HTML pages

ANALYTICS_SCRIPT='    <!-- Vercel Analytics -->
    <script>
      window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
    </script>
    <script defer src="/_vercel/insights/script.js"></script>'

for file in index.html downloads.html good-times.html bass-fishing.html gothic.html kawaii.html memorycare.html privacy.html free-guide.html; do
  if [ -f "$file" ]; then
    # Check if analytics already added
    if grep -q "vercel/insights" "$file"; then
      echo "✓ Analytics already in $file"
    else
      # Add analytics before </body>
      sed -i "s|</body>|$ANALYTICS_SCRIPT\n</body>|" "$file"
      echo "✓ Added analytics to $file"
    fi
  fi
done
