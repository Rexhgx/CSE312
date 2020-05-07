import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room']
        self.room_group_name = 'share_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        operation = text_data_json['operation']

        if operation == 'chat':
            sender_name = text_data_json['sender_name']
            receiver_name = text_data_json["receiver_name"]
            content = text_data_json["content"]

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'add_message',
                    'operation': 'chat',
                    'sender_name': sender_name,
                    'receiver_name': receiver_name,
                    'content': content,
                }
            )

    # Receive message from room group (chat)
    async def add_message(self, event):
        operation = event['operation']
        sender_name = event['sender_name']
        receiver_name = event['receiver_name']
        content = event['content']
        print(sender_name, receiver_name)

        await self.send(text_data=json.dumps({
            'operation': operation,
            'sender_name': sender_name,
            'receiver_name': receiver_name,
            'content': content,
        }))