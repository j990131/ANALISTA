import re

with open('dental-promo.html', 'r') as f:
    content = f.read()

# Check for aria-labels on buttons
if 'aria-label=' in content:
    print("aria-label found!")
else:
    print("NO aria-labels found on buttons.")

# Check for aria-labels in JS
if 'setAttribute("aria-label"' in content:
    print("JS aria-label found!")
else:
    print("NO JS aria-labels found.")
