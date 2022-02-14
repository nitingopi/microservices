# amqps://ubsknfmh:i-5h_JNkuUZgwthlqE1nULYibt-V91m9@beaver.rmq.cloudamqp.com/ubsknfmh
import json

import  pika
params = pika.URLParameters('amqps://ubsknfmh:i-5h_JNkuUZgwthlqE1nULYibt-V91m9@beaver.rmq.cloudamqp.com/ubsknfmh')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='main')

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties )
