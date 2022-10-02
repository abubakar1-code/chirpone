# cahte app with static group name


from asyncio import events
from email.charset import Charset
import json
from channels.consumer import AsyncConsumer , SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

from .models import MChat, MChatSms
from .serial import mchatsms_serial
import json.scanner
from django.utils.timezone import now


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        # print('websocket connected......',event)
        # print ('Channel Layer...',self.channel_layer)
        
        # print ('Channel Name...',self.channel_name)
        async_to_sync( self.channel_layer.group_add)('programer',self.channel_name)
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self,event):
        # print('Message received from client......',event['text'])
        
        # print('Type of Message received from client......',type( event['text']))
        
        # chatobj = MChatSms.objects.all()
        # serialize = mchatsms_serial(chatobj,many=True)
        # print(serialize.data)
        # print('_________')
        async_to_sync(self.channel_layer.group_send)(
            'programer',
            {
                'type':'chat.message',
                'message':event['text']
                
            }
        )
    def chat_message(self,event): 
        print('Event...',event['message'])
        chatobj = MChatSms.objects.all()
        # serialize = mchatsms_serial(chatobj,many=True)
        # print(serialize.data)
        # print('_________')
        self.send({
            'type':'websocket.send',
            'text':event['message'],
        })
    
    
    def websocket_disconnect(self,event):
        print('Web socket disconected......',event)
        
        print ('Channel Layer...',self.channel_layer)
        
        print ('Channel Name...',self.channel_name)
        async_to_sync(self.channel_layer.group_discard)('programer',self.channel_name)
        raise StopConsumer()
    
    
    # that we required
    
class MessengerChat(SyncConsumer):
    def websocket_connect(self,event):
        # print('websocket connected......',event)
        # print ('Channel Layer...',self.channel_layer)
        
        # print ('Channel Name...',self.channel_name)
    
        chatobj = MChatSms.objects.all()
        serialize = mchatsms_serial(chatobj,many=True)
        # print(serialize.data)
        # print('_________')
    
        async_to_sync( self.channel_layer.group_add)('programer',self.channel_name)
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self,event):
        # print('Message received from client......',event['text'])
        
        # print('Type of Message received from client......',type( event['text']))
        
        # chatobj = MChatSms.objects.all()
        # serialize = mchatsms_serial(chatobj,many=True)
        # print(serialize.data)
        # print('_________')
        
        # print('Event for recieve tag ...',event['text'])
        # data = json.loads(event['text'])
        # group = data['group']
        # print(data)
        # print(type(group))
        # # chat = MChat.objects.get(mchat_id=group)
        # # print(chat.mchat_id)
        # chat = MChatSms(
        #     sms_text = data['message'],
        #     sms_mchat = group,
        #     sms_timestamp = now()
        # )
        # chat.save()
        async_to_sync(self.channel_layer.group_send)(
            'programer',
            {
                'type':'chat.message',
                'message':event['text']
                
            }
        )
    def chat_message(self,event): 
        # print('Event of the chat...',event['message'])
        # chatobj = MChatSms.objects.all()
        # serialize = mchatsms_serial(chatobj,many=True)
        # print(serialize.data)
        # print('_________')
        # print(type(event['message']))
        
        # data = json.dump(event['message'])
        # print('data',type(data))
        data = json.loads(event['message'])
        print(data)
        chat = MChatSms(
            sms_text = data['message'],
            sms_mchat = MChat.objects.get(mchat_id=int(data['group'])),
            sms_timestamp = now()
        )
        chat.save()
        self.send({
            'type':'websocket.send',
            'text':event['message']
            
        })
    
    
    def websocket_disconnect(self,event):
        print('Web socket disconected......',event)
        
        print ('Channel Layer...',self.channel_layer)
        
        print ('Channel Name...',self.channel_name)
        async_to_sync(self.channel_layer.group_discard)('programer',self.channel_name)
        raise StopConsumer()
    
    
    