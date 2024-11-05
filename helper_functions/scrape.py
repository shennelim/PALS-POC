from langchain_community.document_loaders import TextLoader

from bs4 import BeautifulSoup

# Import libraries
import requests
#from bs4 import BeautifulSoup

# URL from which pdfs to be downloaded
url = "https://www.nparks.gov.sg/avs/resources"

i = 0

#list_of_documents_loaded = []

# From all links check for pdf link and
# if present download file
page = 1
pagesize = 25

for page < 4:
  next = f"?section=All&type=All&category=All&page={page}&pageSize={pagesize}"

  # Requests URL and get response object
  response = requests.get(url+next)

  # Parse text obtained
  soup = BeautifulSoup(response.text, 'html.parser')

  # Find all hyperlinks present on webpage
  links = soup.find_all('a')

  for link in links:
    try:
        if ('.pdf' in link.get('href', [])):
          i += 1
          
          #loader = TextLoader(requests.get(url+"/"+link.get('href')).content)

          response = requests.get(url+"/"+link.get('href'))
          file_Path = f".\data\{i}.pdf"

        if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
            print('File downloaded successfully')
        else:
            print('Failed to download file')


    except Exception as e:
          # if there is an error loading the document, print the error and continue to the next document
          print(f"Error loading {link.get('href')}: {e}")
          continue

  page += 1

print(f"All {i} PDF files downloaded")