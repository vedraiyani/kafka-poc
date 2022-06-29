# importing the required modules  
from json import loads  
from kafka import KafkaConsumer

# # generating the Kafka Consumer  
# my_consumer = KafkaConsumer(  
#     'test',
#      api_version=(0,11,5),
#      bootstrap_servers = ['localhost:9092'],  
#      auto_offset_reset = 'earliest',  
#      enable_auto_commit = True,  
#      group_id = 'my-group',  
#      value_deserializer = lambda x : loads(x.decode('utf-8'))  
#      )  

# for message in my_consumer:  
#     message = message.value  
#     print(message + " recieved")  

consumer = KafkaConsumer('test',
    api_version=(3,2,0), 
    bootstrap_servers='localhost:9092', 
    fetch_max_wait_ms=0,
    group_id="None",
    fetch_min_bytes=1,
    fetch_max_bytes=10,
    auto_offset_reset='earliest',
    enable_auto_commit=True)
print("before")
consumer.poll(timeout_ms=1000)
print("after")
for msg in consumer:
    print (msg)
    print (msg.value.decode('utf-8'))
consumer.close()
