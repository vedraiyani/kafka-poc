from pykafka import KafkaClient
client = KafkaClient(hosts="localhost:29092")
print(client.topics)

print("produce")
topic = client.topics['test']
with topic.get_sync_producer() as producer:
     for i in range(4):
         print(i)
         producer.produce(f'test message {str(i ** 2)}'.encode('utf-8'))
print("consume")
consumer = topic.get_simple_consumer()
for message in consumer:
     if message is not None:
        #  print(message)
         print(message.offset, message.value.decode('utf-8'))