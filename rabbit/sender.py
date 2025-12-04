import pika

# Conexión al servidor RabbitMQ en Debian
credentials = pika.PlainCredentials('usuario', 'password')
parameters = pika.ConnectionParameters(
    host='192.168.68.104',  # IP del equipo Debian
    credentials=credentials
)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Crear/asegurar la cola
channel.queue_declare(queue='saludos')

# Enviar mensaje
mensaje = 'Hola Mundo desde Windows!'
channel.basic_publish(exchange='', routing_key='saludos', body=mensaje)
print(f" [x] Enviado: {mensaje}")

connection.close()