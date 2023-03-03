from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import random
from pyjokes import jokes_en


class JokeLogic(LogicAdapter):
	def __init__(self,chatbot,**kwargs):
		super().__init__(chatbot, **kwargs)
		self.confidence=0
		
	def can_process(self,statement):
		words=["tell me","say something","something funny","laugh","bored","joke"]
		return bool(any(x in statement.text.lower().split() for x in words))
	
	def process(self,statement,additional_response_selection_parameters=None):
		
		# Let"s base the confidence value on if the keywords match
		if self.can_process(statement):
			self.confidence = 0.9
		self.jokes = jokes_en.neutral + jokes_en.chuck
		self.joke = random.choice(self.jokes)
		self.joke = self.joke[0].lower()+self.joke[1:]
		response = Statement("Check this, " + self.joke)
		#edit
		response.confidence =self.confidence
		return response
