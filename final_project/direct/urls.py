from django.urls import path
from direct.views import (inbox, Directs, SendDirect, UserSearch, NewConversation, ExploreUser)
urlpatterns = [
   	path('', inbox, name='inbox'),
    path('directs/<username>', Directs, name='directs'),
    path('send/', SendDirect, name='send_direct'),
    path('new/', UserSearch, name='usersearch'),
    path('explore/', ExploreUser, name='explore'),
    path('new/<username>', NewConversation, name='newconversation'),
]
