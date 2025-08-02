from django.urls import path
from .views import ChatbotAPIView, chat_home

urlpatterns = [
    path('', chat_home, name='chat-home'),  # <- Root path
    path('api/chat/', ChatbotAPIView.as_view()),
]
