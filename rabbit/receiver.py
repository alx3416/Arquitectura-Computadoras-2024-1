import pika

# Conexión al servidor RabbitMQ local
credentials = pika.PlainCredentials('miusuario', 'mipassword')
parameters = pika.ConnectionParameters(
    host='localhost',  # En Debian puede seguir siendo localhost
    credentials=credentials
)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Crear/asegurar la cola
channel.queue_declare(queue='saludos')

# Función que procesa los mensajes
def callback(ch, method, properties, body):
    print(" [x] Recibido:", body.decode())

print(" [*] Esperando mensajes. Ctrl+C para salir.")
channel.basic_consume(queue='saludos', on_message_callback=callback, auto_ack=True)

channel.start_consuming()