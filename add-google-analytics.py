#!/usr/bin/env python3
"""
Add Google Analytics 4 tracking to all Memory Bridge Books pages
"""

import re

# GA4 tracking code
ga4_code = '''    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-5YVNB4NMFG"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-5YVNB4NMFG');
    </script>
'''

# All HTML pages that need tracking
files = [
    'index.html',
    'downloads.html',
    'good-times.html',
    'bass-fishing.html',
    'gothic.html',
    'kawaii.html',
    'memorycare.html',
    'privacy.html',
    'free-guide.html',
    'hub.html'
]

for filename in files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if GA4 already added
        if 'G-5YVNB4NMFG' in content or 'gtag' in content:
            print(f"✓ GA4 already in {filename}")
            continue
        
        # Add GA4 code right after <head>
        if '<head>' in content:
            content = content.replace('<head>', '<head>\n' + ga4_code, 1)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Added GA4 to {filename}")
        else:
            print(f"⚠️  No <head> tag found in {filename}")
            
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")

print("\n✅ Google Analytics 4 installation complete!")
print("Measurement ID: G-5YVNB4NMFG")
print("\nNext steps:")
print("1. git add .")
print("2. git commit -m 'Add Google Analytics 4 tracking'")
print("3. git push origin main")
print("4. Wait ~60 seconds for auto-deploy to memorybridgebooks.com")
