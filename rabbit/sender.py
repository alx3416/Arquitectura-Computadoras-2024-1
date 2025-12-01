import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='saludos')

mensaje = "hola mundo"
channel.basic_publish(exchange='', routing_key='saludos', body=mensaje)
print(" [x] Enviado:", mensaje)