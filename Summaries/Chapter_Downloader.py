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
                text = content_div.get_text(separator='\n', strip=True)
                print(f"Section {section} Summary:\n{text}\n")
                
                # Save the text to a file in the specified directory
                file_path = os.path.join(save_dir, f"gatsby_section{section}_summary.txt")
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(text)
            else:
                print(f"Content not found for section {section}.")
        else:
            print(f"Failed to download section {section}.")

        time.sleep(0.5)  # Adhere to the crawl-delay directive

# Base URL without the section part
base_url = "https://www.sparknotes.com/lit/gatsby/"
sections = 9  # Total number of sections
save_dir = "Summaries"  # Relative path to the save directory

download_summary(base_url, sections, save_dir)



