import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader

def fetch_and_extract(source):
    """
    Extract text from a URL, PDF file, or text file.
    Writes result to Selected_Document.txt and returns extracted text.
    """
    try:
        # URL
        if source.startswith('http'):
            response = requests.get(source)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                content_div = soup.find('article')
                if not content_div:
                    print("The expected content container was not found.")
                    return ""

                paragraphs = content_div.find_all('p')
                extracted_text = '\n\n'.join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
            else:
                print(f"Failed to retrieve the page. HTTP Status Code: {response.status_code}")
                return ""

        # PDF
        elif source.endswith('.pdf'):
            reader = PdfReader(source)
            extracted_text = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text + "\n\n"
            extracted_text = extracted_text.strip()

        # Text file
        else:
            with open(source, 'r', encoding='utf-8') as file:
                extracted_text = file.read()

        # Write output
        with open('Selected_Document.txt', 'w', encoding='utf-8') as file:
            file.write(extracted_text)

        print(f"Content successfully extracted and saved to 'Selected_Document.txt'.")
        return extracted_text

    except requests.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
        return ""
    except FileNotFoundError:
        print(f"File not found: {source}")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

def main():
    # Change this to your source: URL, PDF path, or text file path
    source = "Master Java Design Patterns with Examples.pdf"
    fetch_and_extract(source)

if __name__ == '__main__':
    main()
