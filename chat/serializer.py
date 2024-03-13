from chat.models import User , ChatMessage, Profile
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Profile
        fields =  ["id", "user","full_name","image"]

class ChatMessageSerializer(serializers.ModelSerializer):
    reciever_profile = ProfileSerializer(read_only= True)
    sender_profile = ProfileSerializer(read_only= True)
    class Meta:
        model = ChatMessage
        fields = ['id',"user","sender" , "reciever", "message", "is_read","date","sender_profile","reciever_profile"]