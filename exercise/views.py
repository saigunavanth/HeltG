from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from .squats import *
from .pushup import *
# Create your views here.
def squat(request):
	return render(request,'exercise/squat.html')
def pushup(request):
	return render(request,'exercise/pushup.html')

def gen(camera):
	while True:
		frame= camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')


def genp(camera):
	while True:
		frame= camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feedp(request):
	return StreamingHttpResponse(genp(VideoCamerap()),
					content_type='multipart/x-mixed-replace; boundary=frame')