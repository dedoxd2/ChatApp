from django.contrib import admin
from chat.models import ChatMessage , User, Profile



class ChatMessageAdmin(admin.ModelAdmin):
    list_editable= ['is_read']
    list_display= ["sender","reciever","message","is_read"]

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


class ProfileAdmin(admin.ModelAdmin):
    list_editable= ['verified']
    list_display= ["user","full_name","verified" ]


admin.site.register(ChatMessage,ChatMessageAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Profile,ProfileAdmin)