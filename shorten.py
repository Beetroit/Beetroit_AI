from chatterbot.logic import LogicAdapter
#URL shortener

class Shorten(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.confidence=0
    
    def can_process(self, statement):
        return bool(statement.text.lower().startswith('shorten'))

    def process(self, statement, additional_response_selection_parameters=None):
        from chatterbot.conversation import Statement
        import requests,re
        url=re.compile(r"\S+\.com[\S+]*").findall(statement.text.lower())
        def shorten(url):
            cookies = {
                'anon_u': 'cHN1X2M4NjNiOGYwLTRiNTMtYmNiYi1iOTdmLWU4NWQwMTA0MWI4MA==|1671901057|4bed3cd3b93a3820697e9f76789d702db5d98fca',
                '_xsrf': 'f1cee806-8dfd-0274-cb32-d6e08f43bd75',
                '_gcl_au': '1.1.1751955701.1671901067',
                    'optimizelyEndUserId': 'oeu1671901067587r0.18986070346258033',
                    '_sp_id.741f': 'dfbd6f6c-9036-493d-a5b1-8cfbf4784b39.1671901069.1.1671901069.1671901069.0bc0a0df-605d-40e2-a682-bb7a7618559e',
                    '_fbp': 'fb.1.1671901074015.2070941931',
                    '_ga': 'GA1.2.1782543612.1671901069',
                    '_ga_567GCTL9BB': 'GS1.1.1671901069.1.1.1671901138.60.0.0',
                    'anon_shortlinks': 'https://bit.ly/3VoaU24,https://bit.ly/3G4JHvU',
                }
            # 'cookie': 'anon_u=cHN1X2M4NjNiOGYwLTRiNTMtYmNiYi1iOTdmLWU4NWQwMTA0MWI4MA==|1671901057|4bed3cd3b93a3820697e9f76789d702db5d98fca;_xsrf=f1cee806-8dfd-0274-cb32-d6e08f43bd75; _gcl_au=1.1.1751955701.1671901067; optimizelyEndUserId=oeu1671901067587r0.18986070346258033; _sp_id.741f=dfbd6f6c-9036-493d-a5b1-8cfbf4784b39.1671901069.1.1671901069.1671901069.0bc0a0df-605d-40e2-a682-bb7a7618559e; _fbp=fb.1.1671901074015.2070941931; _ga=GA1.2.1782543612.1671901069; _ga_567GCTL9BB=GS1.1.1671901069.1.1.1671901138.60.0.0; anon_shortlinks=https://bit.ly/3VoaU24,https://bit.ly/3G4JHvU',

            headers = {
                'authority': 'bitly.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'dnt': '1',
                    'origin': 'https://bitly.com',
                    'referer': 'https://bitly.com/',
                    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                    'x-requested-with': 'XMLHttpRequest',
                    'x-xsrftoken': 'f1cee806-8dfd-0274-cb32-d6e08f43bd75',
                }

            data = {
                'url': url,
                }
            try:
                response = requests.post(
                    'https://bitly.com/data/anon_shorten', headers=headers, data=data,cookies=cookies)
                self.confidence=1
                return response.json().get("data").get("link")
            except:
                self.confidence=1
                return "Unavailable internet"

        text=(f"shortened link is {shorten(url[0])}")if len(url)==1 else f"shortened links are {' '.join([shorten(link) for link in url])}"
        response=Statement(text=text) if "unavailable" not in text.lower() else Statement(text=f"{shorten(url)}")
        response.confidence=self.confidence
        return response

