import selenium,os,requests,shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options=Options()
options.headless=True
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#text="https://www.facebook.com/watch/?v=855633485562075"
#url="https://godownloader.com/"
class PdfDownload:
    def __init__(self,url) -> None:
        self.driver=webdriver.Chrome(options=options)
        self.url=url
    def get_file(self,url):
        self.driver.get(url)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Download")))
        pdf=element.get_attribute("href")
        file_name=self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/h1/a')
        return pdf,file_name.text

    def download_file(self,url,file_name):
        with requests.get(url, stream=True) as r:
            with open(f"{file_name}.pdf", 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        return file_name

    def main(self):
        print("Starting download")
        file=self.get_file(self.url)
        print(f"File obtained {file[1]}")
        self.download_file(url=file[0],file_name=file[1])
        print(f"File saved as {file[1]} to {os.getcwd()}")
        self.driver.close()
