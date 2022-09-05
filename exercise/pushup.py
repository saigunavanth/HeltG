import cv2,os,urllib.request
import numpy as np

from imutils.video import VideoStream
import imutils



import tensorflow as tf
from tensorflow import Graph
from keras.preprocessing import image
from tensorflow.keras.models import load_model

model_graph = Graph()
with model_graph.as_default():
	tf_session = tf.compat.v1.Session()
	with tf_session.as_default():
		model = load_model('./weights/pushups_final.h5')


class VideoCamerap(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)
	def __del__(self):
		self.video.release()

	def get_frame(self):
		_,first_frame = self.video.read()
		prev_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY) 
		mask = np.zeros_like(first_frame) 
		mask[..., 1] = 255
		count=10
		#p=0
		while(self.video.isOpened()):
			ret, frame = self.video.read()
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			flow = cv2.calcOpticalFlowFarneback(prev_gray,gray,None,0.5,3,100,3,7,1.1,0)
			magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])
			mask[..., 0] = angle * 180 / np.pi / 2
			mask[..., 2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
			rgb = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)
			img = cv2.resize(rgb,(128,128))
			img = image.img_to_array(img)
			img = img.reshape(1,128,128,3)
			with model_graph.as_default():
				with tf_session.as_default():
					pred = model.predict(img)
			if pred[0][0]>0.5:
				label="pushdown"
				frame = cv2.putText(frame,label,(30,30),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,255,0),2)
			if pred[0][1]>0.5:
				label="Nothing"
				frame = cv2.putText(frame,label,(30,30),cv2.FONT_HERSHEY_COMPLEX,1.5,(255,0,0),2)
			if pred[0][2]>0.5:
				label="pushup"
				frame = cv2.putText(frame,label,(30,30),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,255),2)


			__,jpeg = cv2.imencode('.jpg',frame)
			return jpeg.tobytes()
			prev_gray = gray
			


