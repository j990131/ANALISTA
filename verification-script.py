import os
import re

def verify_file(filepath):
    print(f"Verifying {filepath}...")
    with open(filepath, 'r') as f:
        content = f.read()

    # Simple check for aria-label
    if 'aria-label=' in content:
        print(f"SUCCESS: Found aria-label in {filepath}")
    else:
        print(f"FAILED: No aria-label found in {filepath}")

verify_file('dental-promo.html')
verify_file('src/components/DentalPromo/DentalPromoPage.jsx')
