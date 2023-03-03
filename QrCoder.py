from chatterbot.logic import LogicAdapter
class QR(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.confidence =0
    def can_process(self, statement):
        return bool(statement.text.startswith("qr"))
    def process(self, statement, additional_response_selection_parameters=None):
        import qrcode
        from PIL import Image
        import os
        from client import send
        from chatterbot.conversation import Statement
        data=statement.text.replace(r"qr ","")
        text_list=['http','.com',"/"]
        qr=qrcode.QRCode(version=10,box_size=6)
        qr.add_data(data)
        qr.make(fit=True)
        pic=qr.make_image(fill_color='black',back_color="white")
        file=f"{data.split('/')[1]}.png" if any([x in data for x in text_list]) else f"{data.split()[0]}.png"
        pic.save(file)
        im=Image.open(file)
        send(message=im.filename)# type: ignore #TODO edit to use im instead of file name
        im.show()
        self.confidence=1
        resp=f"Here's your QR Code"
        response=Statement(resp)
        response.confidence=self.confidence
        os.remove(file)
        return response
        


