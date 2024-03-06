import requests

# URL of the text file
url = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt' # The Great Gatsby

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Decode the content and save it to a file within the 'Novels' directory
    with open('Novels/novel.txt', 'w', encoding='utf-8') as file:
        content = response.content.decode('utf-8')
        file.write(content)
    print("The file has been successfully downloaded and saved in the 'Novels' folder.")
else:
    print("Failed to download the file. Status code:", response.status_code)