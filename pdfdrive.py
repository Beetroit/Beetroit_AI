# Import necessary libraries
from bs4 import BeautifulSoup
import requests, re
from lxml import etree
from PDFDownload import PdfDownload

# Set HTTP headers for the request
headers = {
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://www.google.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9"
}

def start(query):
    # Prompt user to enter search text and construct search link
    base_url = "https://www.pdfdrive.com"
    year=re.findall(r'\d+',query)
    #query = "+".join(input("Enter search text: ").strip().split())
    link = f"https://www.pdfdrive.com/search?q={query}&pagecount=&pubyear={year}&searchin=en&em=1"
    print(link)

    # Send GET request to the search link and parse the HTML response with BeautifulSoup
    try:
        r = requests.get(link, headers=headers, timeout=10)
    except ConnectionError as c:
        print(f'Error: {c}')
    soup = BeautifulSoup(r.text, "html5lib")
    dom = etree.HTML(str(soup))

    # Extract PDF document information from the HTML response using XPath
    pdf_info = {}
    links = dom.xpath('//div[@class="file-right"]/a/@href')
    pages = dom.xpath('//div[@class="file-right"]/div[@class="file-info"]/span[1]/text()')
    year = dom.xpath('//div[@class="file-right"]/div[@class="file-info"]/span[3]/text()')
    size = dom.xpath('//div[@class="file-right"]/div[@class="file-info"]/span[5]/text()')

    # Store the PDF document information in a dictionary
    global pdf
    pdf = {}
    for i, j in enumerate(links):
        link = base_url+j
        info = [link, pages[i], size[i], year[i]]
        print(i, info, "\n")
        pdf[i] = info



def main(query):
    start(query)
    # Prompt user to select a PDF document to download
    choice = int(input("Enter a number that corresponds to your choice: "))
    while choice not in pdf:
        choice = int(input("Try again, your choice is invalid: "))
        if choice ==None or choice in ('exit','quit'):
            quit()
    # Define a function to convert the PDF download link from 'e' to 'd'
    def d_url(url):
        pattern = r"e(?=\d+)"
        return re.sub(pattern, "d", url)
    # Download the selected PDF document using the PdfDownload class from the PDFDownload module
    html = pdf.get(choice, "Invalid")[0]
    downloader = PdfDownload(d_url(html))
    downloader.main()
