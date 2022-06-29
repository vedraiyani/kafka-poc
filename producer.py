# importing the required libraries  
from time import sleep  
from json import dumps  
from kafka import KafkaProducer  
import kafka
print(kafka.__version__)
# # initializing the Kafka producer  
# my_producer = KafkaProducer(  
#     bootstrap_servers = ['localhost:9092'],  
#     api_version=(0,11,5),
#     value_serializer = lambda x:dumps(x).encode('utf-8')  
#     )  

# # generating the numbers ranging from 1 to 500  
# for n in range(10):  
#     my_data = {'num' : n}  
#     my_producer.send('test', value = my_data)  
#     sleep(5)  

producer = KafkaProducer(bootstrap_servers='localhost:9092', api_version=(3,2,0))
for i in range(10):
    producer.send('test', b'some_message_bytes')
    producer.flush()
    print(i)