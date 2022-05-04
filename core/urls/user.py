from django.urls import path

from ..views import user

urlpatterns = [
    path('user', user.home, name='user_home'),
    path('user/edit', user.edit, name='user_edit'),
    path('user/<id>', user.profile, name='user_profile'),
    path('user/<id>/history', user.history, name='user_history'),
    path('user/<id>/messages', user.messages, name='user_messages'),
]
