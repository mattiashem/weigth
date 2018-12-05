#
#
#  Feeder of Data !!
#  Feer of data to api 
#
#  Read from que and send data to the api endpoint for storage

import urllib.request
import json
import pika
import time
import socket
import sys
from coolname import generate_slug
from random import randint



 


def wait_net_service(server, port, timeout=None):
	""" Wait for network service to appear 
	    @param timeout: in seconds, if None or 0 wait forever
	    @return: True of False, if timeout is None may return only True or
	             throw unhandled network exception
	"""
	while True:
		result=""
		try:
			connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
			channel = connection.channel()
			print("Connected")

			return
		except:
			print("Service not up")
			time.sleep(10)


#Wait untill we have service up
wait_net_service('rabbitmq',5672)




connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',heartbeat_interval=500))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

def add_to_que(message):
	'''
	Adding message to the que
	'''
	
	channel.basic_publish(exchange='',
	                      routing_key='task_queue',
	                      body=message,
	                      properties=pika.BasicProperties(
	                         delivery_mode = 2, # make message persistent
	                      ))
	print(" [x] Sent %r" % message)






