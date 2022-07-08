# from asgiref.sync import sync_to_async
# from django.urls import re_path
# from django.core.asgi import get_asgi_application
# from channels.generic.websocket import AsyncJsonWebsocketConsumer
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.db import database_sync_to_async
# from channels.auth import AuthMiddlewareStack
# from .models import Factory
# from django.contrib.gis.geos import Point

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter([
#             re_path(r"^front(end)/$", consumers.AsyncChatConsumer.as_asgi()),
#         ])
#     ),
# })


# class LocationConsumer(AsyncJsonWebsocketConsumer):
#     async def connect(self):
#         # do auth and other stuffs
#         self.user = userObj     

#     # Receive message from WebSocket
#     async def receive_json(self, content):
#         if content.get("type", None) == "location_update":

#             latitude = content["latitude"]

#             longitude = content["longitude"]

#             await self.channel_layer.group_send(
#                 "factory",
#                 {
#                     "type": "location_update",
#                     "latitude": latitude,
#                     "longitude": longitude,
#                     "user_id": self.user.id,
#                 },
#             )


# # Event handler to broadcast locations to web clients based on a factory
# # instance
# class FactoryConsumer(AsyncJsonWebsocketConsumer):
#     groups = ["factory"]
#     factory = None

#     async def connect(self):
#         # Extract distance from websocket url query param
#         query_string = self.scope["query_string"]
#         query_string_arr = query_string.decode("utf-8").split("=")
#         if query_string_arr and query_string_arr[0] == "distance":
#             self.distance = float(query_string_arr[1])

#         # Extract factory id from websocket url path param
#         # We would receive the factory id from websocket url path params
#         if "factory_id" in self.scope["url_route"]["kwargs"]:
#             self.factory_id = self.scope["url_route"]["kwargs"]["factory_id"]
#             self.factory = await database_sync_to_async(Factory.objects.get)(pk=self.factory_id)

#         await self.accept()

#     async def disconnect(self, code):
#         pass

#     # Receive message from WebSocket
#     async def receive_json(self, content):
#         # Passing this since location_update function 
#         # would get the events
#         pass

#     async def location_update(self, event):
#         # Add map analysis here
#         """
#         .contains
#         This function checks if a target shape is inside the source shape. 
#         It is useful in scenarios where you want to track a device is inside a geofence. 
#         """

#         latitude = event["latitude"]
#         longitude = event["longitude"]
#         user_id = event["user_id"]

#         point = Point(latitude, longitude, srid=4326)
#         """
#         .distance
#         Extending the above example, what if we want to consider a point inside if
#         it comes within x distance of our factory's geofence. 
#         The .distance comes handy for this scenario. 
#         This functions returns the distance of a target shape from the source shape:
#         """
#         if hasattr(self,"distance"):
#             is_inside = self.factory.geofence.distance(point) <= self.distance
#         else:
#             is_inside = self.factory.geofence.contains(point)
#         """
#         The above code checks if the distance between the point and geofence is less than 
#         the distance specified as the query parameter in the web socket URL. 
#         If the distance query parameter is not provided,
#         simply check if the point lies strictly inside the factory's geofence.
#         """
#         # Send data to web listeners
#         await self.send_json(
#             {
#                 "latitude": latitude,
#                 "longitude": longitude,
#                 "user_id": user_id,
#                 "is_inside": is_inside
#             }
#         )
        
#     async def location_update(self, event):
#         # Add map analysis here

        

#         # Send data to web listeners
#         await self.send_json(
#             {
#                 "latitude": latitude,
#                 "longitude": longitude,
#                 "user_id": user_id,
#                 "is_inside": is_inside
#             }
#         )
        

