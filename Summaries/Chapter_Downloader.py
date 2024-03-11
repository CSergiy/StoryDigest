import os
import requests
from bs4 import BeautifulSoup
import time

def download_summary(base_url, sections, save_dir):
    os.makedirs(save_dir, exist_ok=True)
    
    for section in range(1, sections + 1):
        url = f"{base_url}section{section}/"
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            content_div = soup.find('div', class_='mainTextContent main-container')
            
            if content_div:
                # Initialize a flag to start capturing <p> tags after first <h3>
                capture = False
                summary_texts = []
                
                for elem in content_div.children:
                    if elem.name == 'h3':
                        # Toggle capture on if it's off, or break loop if it's on
                        if capture:
                            break
                        capture = True
                    elif capture and elem.name == 'p':
                        summary_texts.append(elem.get_text(strip=True))
                
                # Join the captured text paragraphs
                summary_text = '\n'.join(summary_texts)
                
                if summary_text:
                    print(f"Section {section} Summary:\n{summary_text}\n")
                    
                    # Save the summary text to a file
                    file_path = os.path.join(save_dir, f"gatsby_section{section}_summary.txt")
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(summary_text)
                else:
                    print(f"No summary content captured for section {section}.")
            else:
                print(f"Content div not found for section {section}.")
        else:
            print(f"Failed to download section {section}.")

        time.sleep(0.5)  # Adhere to the crawl-delay directive

# Base URL without the section part
base_url = "https://www.sparknotes.com/lit/gatsby/"
sections = 9  # Total number of sections
save_dir = "Summaries"  # Relative path to the save directory

download_summary(base_url, sections, save_dir)