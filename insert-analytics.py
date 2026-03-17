import re

analytics_code = '''    <!-- Vercel Analytics -->
    <script>
      window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
    </script>
    <script defer src="/_vercel/insights/script.js"></script>
'''

files = [
    'index.html', 'downloads.html', 'good-times.html', 'bass-fishing.html',
    'gothic.html', 'kawaii.html', 'memorycare.html', 'privacy.html', 'free-guide.html'
]

for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
        
        # Check if analytics already added
        if 'vercel/insights' in content:
            print(f"✓ Analytics already in {filename}")
            continue
        
        # Add analytics before </body>
        content = content.replace('</body>', analytics_code + '\n</body>')
        
        with open(filename, 'w') as f:
            f.write(content)
        
        print(f"✓ Added analytics to {filename}")
    except FileNotFoundError:
        print(f"✗ File not found: {filename}")
