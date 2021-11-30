import json
from channels.generic.websocket import WebsocketConsumer
#from asgiref.sync import async_to_sync
#from django.utils import timezone


class ChatConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def connect(self):
        # accept connection
        self.accept()

    def disconnect(self, close_code):
        pass

    # receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # send message to WebSocket
        self.send(text_data=json.dumps({'message': message}))
