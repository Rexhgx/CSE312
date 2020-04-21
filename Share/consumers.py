import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ShareConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['user_name']
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

        if operation == 'post':
            post_id = text_data_json['post_id']
            post_text = text_data_json["post_text"]
            post_photo_url = text_data_json["post_photo_url"]

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'add_post',
                    'operation': 'post',
                    'post_id': post_id,
                    'post_text': post_text,
                    'post_photo_url': post_photo_url,
                }
            )

        if operation == 'comment':
            post_id = text_data_json['post_id']
            commenter = text_data_json["commenter"]
            comment_text = text_data_json['comment_text']

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'add_comment',
                    'operation': 'comment',
                    'post_id': post_id,
                    "commenter": commenter,
                    'comment_text': comment_text,
                }
            )

        if operation == 'like':
            post_id = text_data_json['post_id']
            liker = text_data_json["liker"]

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'add_like',
                    'operation': 'like',
                    'post_id': post_id,
                    "liker": liker,
                }
            )

    # Receive message from room group (post)
    async def add_post(self, event):
        operation = event['operation']
        post_id = event['post_id']
        post_text = event['post_text']
        post_photo_url = event['post_photo_url']

        await self.send(text_data=json.dumps({
            'operation': operation,
            'post_id': post_id,
            'post_text': post_text,
            'post_photo_url': post_photo_url,
        }))

    # Receive message from room group (comment)
    async def add_comment(self, event):
        operation = event['operation']
        post_id = event['post_id']
        commenter = event['commenter']
        comment_text = event['comment_text']

        await self.send(text_data=json.dumps({
            'operation': operation,
            'post_id': post_id,
            "commenter": commenter,
            'comment_text': comment_text,
        }))

    # Receive message from room group (like)
    async def add_like(self, event):
        operation = event['operation']
        post_id = event['post_id']
        liker = event['liker']

        await self.send(text_data=json.dumps({
            'operation': operation,
            'post_id': post_id,
            "liker": liker,
        }))