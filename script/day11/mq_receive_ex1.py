import pika,time
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello2',durable=True)
def callback(ch,method,properties,body):  #回调函数
    time.sleep(10)
    print("[x] received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(#消费信息
                    callback, #如果收到消息就调用CallBack函数处理消息
                    queue='hello',
                    #no_ack=True, #不确认消息是否发送成功

                        )

print('[*] waiting for messages.to exit press ctrl+c')
channel.start_consuming()