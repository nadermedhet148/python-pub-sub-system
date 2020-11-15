import pika
import sys


def publish(channel_name, message):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange=channel_name, exchange_type='fanout')
    try:
        channel.basic_publish(exchange=channel_name, routing_key='', body=message)
        connection.close()
    except Exception as ex:
        print(ex)
