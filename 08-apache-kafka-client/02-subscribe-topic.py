from kafka import KafkaConsumer

topic = 'test'


consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                            auto_offset_reset="latest",
                            consumer_timeout_ms=1000)
consumer.subscribe([topic])

while not isDestroyTriggered:
    for message in consumer:
        messageTopic = message.topic
        jsonMsg = message.value.decode("utf-8") 
        print(messageTopic +" "+ jsonMsg)
        if isDestroyTriggered:
            break

consumer.close()