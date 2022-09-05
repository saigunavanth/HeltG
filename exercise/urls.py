from django.urls import path
from . import views
urlpatterns = [
	path('squat/',views.squat,name= 'squat'),
	path('pushup/',views.pushup,name= 'pushup'),
	path('video/',views.video_feed,name='video_feed'),
	path('videop/',views.video_feedp,name='video_feedp'),
]