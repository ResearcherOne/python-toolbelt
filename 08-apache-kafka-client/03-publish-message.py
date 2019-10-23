from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

topic = 'test'

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# produce json messages
jsonData = {'key': 'first'}
jsonMessage = json.dumps(jsonData).encode('ascii')
producer.send(topic, jsonMessage)


def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception

# produce asynchronously with callbacks
producer.send(topic, jsonMessage).add_callback(on_send_success).add_errback(on_send_error)

# block until all async messages are sent
producer.flush()

# configure multiple retries
producer = KafkaProducer(retries=5)