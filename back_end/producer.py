import pika 
import os

MSG_USER=os.environ.get("MSG_USER")
MSG_PASS=os.environ.get("MSG_PASS")
NAME=os.environ.get("TEST")
HOST=os.environ.get("MESSAGING_HOST")

credentials = pika.PlainCredentials(MSG_USER,MSG_PASS)

parameters = pika.ConnectionParameters(HOST,5672,"/",credentials=credentials)

connection = pika.BlockingConnection(parameters=parameters)

channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange="",routing_key="hello",body="Hello World")

connection.close()
