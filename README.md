							Beetroit
A friendly chatbot made more for personal use but integrating to whatsapp soon.
Built using the chatterbot framework by Gunther Cox https://github.com/gunthercox/ChatterBot, all rights go to their respective owners.

To start the bot create a virtualenv with
python -m venv Beetroit

Then Install dependencies
pip install -r requirements.txt

Then start the bot with 
python bot.py

To use the _pdf feature, you will need to download chromedriver executable into the same folder the bot resides.
#NB It must be the same version as your chromebrowser or it'll throw errors.

To use the ask feature, you will need an api_key from wolframalpha.com, it's a temporal solution for reponses, i will integrate an LLM soon, probably one of GPT series, BERT or Bloom.

The bot is still under active development so expect some bugs, however you can report them and i will try to fix as quickly as possible. I am working to host it on replit or huggingface, then integrate into whatsapp, haven't had much time to do that yet.
