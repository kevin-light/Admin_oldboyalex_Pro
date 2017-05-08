import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel() #声明一个管道

channel.queue_declare(queue='hello2',durable=True) #声明一个queue
channel.basic_publish(exchange='',
                      routing_key='hello',  #queue名字
                      body='Hello World===',
                    properties=pika.BasicProperties(
                    delivery_mode=2, #make message persistent造个持久信息

                      )
                      )

print("[x] Sent 'Hello woeld")
connection.close()