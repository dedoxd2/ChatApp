from django.urls import path
from chat import views


urlpatterns = [
    path("my-messages/<user_id>/",views.MyInbox.as_view()),
    path("get-messages/<sender_id>/<reciever_id>/", views.GetMessages.as_view(), ) , 

    path ("send-message/" ,views.SendMessage.as_view()),
]