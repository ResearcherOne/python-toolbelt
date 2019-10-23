from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

topic = 'test'

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# produce json messages
producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
producer.send(topic, {'key': 'first'})


def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception

# produce asynchronously with callbacks
producer.send(topic, {'key': 'second'}).add_callback(on_send_success).add_errback(on_send_error)

# block until all async messages are sent
producer.flush()

# configure multiple retries
producer = KafkaProducer(retries=5)