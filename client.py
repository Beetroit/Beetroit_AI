from whatsapp_api_client_python import GreenAPI
ID = "1101786402"
token = "dfc7ece2b61b420d875ad74ec76ca3186ba343f8707041e8b6"
client = GreenAPI(id_instance=ID, api_token_instance=token)


def send(message,file='None'):
    img_ext=['png','jpg','mpeg']
    if type(message)== str:
        res=client.sending.send_message(chatId='2348078807660@c.us', message=message)
    elif any([x in message.split() for x in img_ext]):
        client.sending.send_file_by_upload(chatId="2348078807660@c.us",file=file,fileName=message)
send("qrcode",'frame.png')