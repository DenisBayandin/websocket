import json

from datetime import datetime
from channels.generic.websocket import AsyncWebsocketConsumer


class CustomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.send(text_data=json.dumps({
            'message': f"{data['message']}. Created at: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}"
        }))
