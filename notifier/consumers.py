from channels.generic.websocket import AsyncJsonWebsocketConsumer


class NoseyConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("gossip", self.channel_name)
        print(f"Added {self.channel_name} channel to gossip")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("gossip", self.channel_name)
        print(f"Removed {self.channel_name} channel to gossip")

    async def book_gossip(self, event):
        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")



class SentenceConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("announcement", self.channel_name)
        print(f"Added {self.channel_name} channel to announcement")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("announcement", self.channel_name)
        print(f"Removed {self.channel_name} channel to announcement")

    async def sentence_announcement(self, event):
        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")
