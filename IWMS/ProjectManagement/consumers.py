from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .views import models_dict, time_pattern
import random, time, json,datetime

class RealTimeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        #print(text_data)
        text_data_json = json.loads(text_data)
        item = await database_sync_to_async(models_dict[text_data_json["Model"]].objects.filter(Station__name=text_data_json['station']).last)()
        if item == None:
            self.close()
            return
        await self.send(text_data=json.dumps({
            'date':datetime.datetime.fromtimestamp(item.date_time).strftime(time_pattern[3]),
            'value':item.value
        }))



class PoolIMGConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    
    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        #text_data包括，model，timestamp，station
        text_data_json = json.loads(text_data)
        #print(text_data_json)
        #获取需要的item
        item = await database_sync_to_async(models_dict[text_data_json['model']].objects.filter(Station__name=text_data_json['station']).get)(date_time=int(text_data_json['timestamp']))
        #print(item.date_time)
        await self.send(text_data=json.dumps({
            "base64":item.value
        }))
