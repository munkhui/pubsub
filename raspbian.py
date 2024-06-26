import paho.mqtt.client as mqtt
import time

def on_connect(mqtt_client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("connected successfully")
        mqtt_client.subscribe('9fmrvy5679/')
    else:
        print("bad connection. Code :", rc)

def on_message(mqtt_client, userdata, msg):
    print(f"Received message on topic :{msg.topic} with payload:{str(msg.payload)}")

def on_publish(mqtt_client, userdata, mid, qos, properties=None):
    print("Message published")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.username_pw_set("9fmrvy5679", "2agmoprtvx")

client.connect(
  host = "b37.mqtt.one",
  port = 1883,
  keepalive = 60,
)

# Number of cycles to perform
num_cycles = int(input("heden udaa msg ywuulahwe: "))

for _ in range(num_cycles):
    # Ask user for the message to be published
    message = input("Enter the message to publish: ")
    topic = "9fmrvy5679/"

    # Publish the message to the topic
    client.publish(topic, message)
    
    # Delay between cycles
    time.sleep(1)  # Adjust the delay as needed

client.loop_forever()
