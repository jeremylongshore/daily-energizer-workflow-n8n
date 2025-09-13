#!/usr/bin/env python3

import os
from weasyprint import HTML, CSS

# CSS for beautiful PDF styling
css_content = """
@page {
    margin: 1in;
    size: letter;
}

body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: #333;
}

h1 {
    color: #2c3e50;
    border-bottom: 3px solid #3498db;
    padding-bottom: 10px;
    margin-top: 0;
    page-break-after: avoid;
}

h2 {
    color: #34495e;
    margin-top: 30px;
    border-bottom: 1px solid #ecf0f1;
    padding-bottom: 5px;
    page-break-after: avoid;
}

h3 {
    color: #555;
    margin-top: 20px;
    page-break-after: avoid;
}

code {
    background: #f4f4f4;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 0.9em;
    font-family: 'Courier New', monospace;
}

pre {
    background: #f8f8f8;
    padding: 15px;
    border-radius: 5px;
    border-left: 4px solid #3498db;
    page-break-inside: avoid;
}

pre code {
    background: none;
    padding: 0;
}

ul, ol {
    margin-left: 20px;
}

li {
    margin-bottom: 5px;
}

strong {
    color: #2c3e50;
    font-weight: bold;
}

em {
    color: #666;
    font-style: italic;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
    page-break-inside: avoid;
}

th, td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
}

th {
    background-color: #3498db;
    color: white;
    font-weight: bold;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

blockquote {
    border-left: 4px solid #3498db;
    padding-left: 15px;
    color: #666;
    font-style: italic;
    margin: 20px 0;
}

/* Status indicators */
li:first-child {
    page-break-after: avoid;
}

/* Prevent orphans and widows */
p {
    orphans: 3;
    widows: 3;
}
"""

def convert_to_pdf(html_file, pdf_file, title):
    """Convert HTML to PDF with custom styling"""
    print(f"Converting {title}...")

    try:
        # Read HTML file
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Create PDF with custom CSS
        HTML(string=html_content).write_pdf(
            pdf_file,
            stylesheets=[CSS(string=css_content)]
        )

        print(f"✅ Created: {pdf_file}")
        return True
    except Exception as e:
        print(f"❌ Error converting {html_file}: {e}")
        return False

def main():
    print("🚀 Creating beautiful PDFs from feature documentation...\n")

    # Define files to convert
    files = [
        ("FEATURE-1-RSS-SOURCE-TRACKING.html",
         "FEATURE-1-RSS-SOURCE-TRACKING.pdf",
         "RSS Feed Source Tracking System"),

        ("FEATURE-2-SCORING-VISIBILITY.html",
         "FEATURE-2-SCORING-VISIBILITY.pdf",
         "Comprehensive Scoring Visibility System"),

        ("OUTPUT-PARSER-CONFIG.html",
         "OUTPUT-PARSER-CONFIG.pdf",
         "Structured Output Parser Configuration Guide")
    ]

    success_count = 0

    for html_file, pdf_file, title in files:
        if os.path.exists(html_file):
            if convert_to_pdf(html_file, pdf_file, title):
                success_count += 1
        else:
            print(f"⚠️  HTML file not found: {html_file}")

    print(f"\n✅ Successfully created {success_count} PDF files!")

    # List created PDFs
    print("\n📄 PDF files ready for Brent:")
    for _, pdf_file, _ in files:
        if os.path.exists(pdf_file):
            size = os.path.getsize(pdf_file) / 1024  # Size in KB
            print(f"   - {pdf_file} ({size:.1f} KB)")

if __name__ == "__main__":
    main()