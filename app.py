import os
import markdownify
from bs4 import BeautifulSoup

DIRECTORY = './posts'

# Read each file in the directory
files = os.listdir(DIRECTORY)

# Filter out the files that are not html
html_files = [file for file in files if file.endswith('.html')]

for html_file in html_files:
    # Filter out the files that start with "draft_"
    if not html_file.startswith('draft_'):
        with open(os.path.join(DIRECTORY, html_file), 'r', encoding='utf8') as file:
            content = file.read()

            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(content, 'html.parser')

            if soup.find('h3') is not None:
                # convert the content of the section[data-field="body"] to markdown
                section = soup.select_one('section[data-field="body"]')
                if section:
                    markdown_content = markdownify.markdownify(str(section))

                    # Save the file with the same name but with .md extension
                    md_file = os.path.splitext(html_file)[0] + '.md'
                    with open(os.path.join(DIRECTORY, md_file), 'w', encoding='utf8') as md_file:
                        md_file.write(markdown_content)