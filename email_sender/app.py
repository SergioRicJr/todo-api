import pika
import dotenv
import json
import os
dotenv.load_dotenv()
import logging
from send_email import send_email
credentials = pika.PlainCredentials(username=os.getenv("USERNAME"), password=os.getenv("PASSWORD"))
connetion = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=credentials))
channel = connetion.channel()

channel.exchange_declare(exchange='email_confirm_exchange', exchange_type='direct')

channel.queue_declare(queue='email_confirm_queue', exclusive=True)

channel.queue_bind(exchange='email_confirm_exchange', queue='email_confirm_queue', routing_key=os.getenv("ROUTING_KEY"))

def callback(ch, method, properties, body):
    dict_body = json.loads(body)
    send_email(
        token=dict_body['token'],
        email_receiver=dict_body['email']
    )

channel.basic_consume(queue='email_confirm_queue', on_message_callback=callback, auto_ack=True)
channel.start_consuming()