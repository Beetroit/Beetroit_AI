from chatterbot.logic import LogicAdapter
import requests
class WolframResponder(LogicAdapter):
	def __init__(self, chatbot,**kwargs):
		super().__init__(chatbot,**kwargs)
		try:
			with open('wolf_key.txt','r') as file:
				self.appid=file.read()
		except:
			self.appid=input('PASTE YOUR WOLFRAM API KEY HERE:\n')
			with open('wolf_key.txt','w') as file:
				file.write(self.appid)
		self.url="http://api.wolframalpha.com/v1/result?"
		self.confidence = 0
		
		
	def can_process(self,statement):
		"""TODO:enlarge word list
		probably make an interation of q tags and aux"""
		#words=["what","who","why","when","does","is","can","should","how","which","must","might","discovered","may","have","has","did"]
		
		#return bool(any(x in statement.text.lower().split() for x in words))
		return bool(statement.text.lower().startswith("ask"))
	
	
	def process(self,statement,additional_response_selection_parameters=None):
		from chatterbot.conversation import Statement
		query = " ".join(statement.text.split()[1:])
		param={"appid":self.appid,"i":query}
		try:
			r=requests.get(url=self.url,params=param)
			
			if "wolfram" in r.text.lower():
				resp="Beetroit"
			elif r.status_code == 501 or r.status_code== 404:
				resp="i am unequipped for this question, perhaps when i'm smarter"
			else:
				resp= r.text
		except:
			resp="you have unavailable internet"
			
	
		# Let"s base the self.confidence value on if the request was successful and understood
		if self.can_process(statement) or "wolfram" in r.text.lower():
			self.confidence=1

		response = Statement(text=f"I think {resp}")
		response.confidence=self.confidence
		return response if "beetroit" not in resp.lower() else Statement("Beetroit")
