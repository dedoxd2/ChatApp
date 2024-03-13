from django.shortcuts import render
from chat.models import User, ChatMessage
from chat.serializer import ChatMessageSerializer
from django.db.models import Subquery , OuterRef , Q
from rest_framework import generics
from django.db.models import Max

# Create your views here.

class MyInbox(generics.ListAPIView):
    
    serializer_class = ChatMessageSerializer

    def get_queryset(self):
        # user_id = self.kwargs["user_id"] ## 127.1/userid

        # messages= ChatMessage.objects.filter(
        #     id__int=Subquery(
        #         User.objects.filter(
        #             Q(sender__reciever=user_id)|
        #             Q(reciever__sender=user_id)
        #         ).distinct().annotate(
        #             last_msg=Subquery(
        #                 ChatMessage.objects.filter(
        #                     Q(sender=OuterRef('id'), reciever=user_id) |
        #                     Q(reciever=OuterRef('id'),sender=user_id)
        #                 ).order_by("-id")[:1].values("id",flat=True)
        #             )
        #         ).values_list("last_msg",flat=True)
        #     )

        # ).order_by('-id')

        # return messages
        user_id = self.kwargs["user_id"]

        # Subquery to get the latest message for each sender or receiver
        subquery = ChatMessage.objects.filter(
            Q(sender=user_id) | Q(reciever=user_id)
        ).values('sender', 'reciever').annotate(
            last_msg=Max('date')
        ).values('last_msg')

        messages = ChatMessage.objects.filter(date__in=subquery).order_by('-id')

        return messages    




class GetMessages(generics.ListAPIView):
    serializer_class = ChatMessageSerializer
    def get_queryset(self):
        sender_id = self.kwargs['sender_id']
        reciever_id = self.kwargs["reciever_id"]

        messages = ChatMessage.objects.filter(
            sender__in=[sender_id,reciever_id],
            reciever__in=[sender_id,reciever_id])

        return messages




class SendMessage(generics.CreateAPIView):
    serializer_class = ChatMessageSerializer