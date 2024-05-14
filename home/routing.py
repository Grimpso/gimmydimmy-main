from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from home.consumers import ChatConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('chat/', ChatConsumer.as_asgi()),
    ]),
})

async def receive(self, text_data):
    await self.send(text_data)
