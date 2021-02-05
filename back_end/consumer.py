import sys
import os
import pika 

MSG_USER=os.environ.get("MSG_USER")
MSG_PASS=os.environ.get("MSG_PASS")
HOST=os.environ.get("MESSAGING_HOST")

def main():

    credentials = pika.PlainCredentials(MSG_USER,MSG_PASS)
    parameters = pika.ConnectionParameters(HOST,5672,"/",credentials=credentials)
    connection = pika.BlockingConnection(parameters=parameters)
    
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def on_message_callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())

    channel.basic_consume(queue='hello', on_message_callback=on_message_callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
        