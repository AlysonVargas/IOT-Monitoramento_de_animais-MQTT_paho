import paho.mqtt.client as mqtt

# Define a função de callback para quando o cliente se conectar ao broker MQTT
def on_connect(client):
   
    client.subscribe('temp-ani/V1')
    print("deu certo")
    
# Cria um novo cliente MQTT
client = mqtt.Client()
print('passei por qaui')
# Define as funções de callback para o cliente MQTT
client.on_connect = on_connect
print('esteve aqui')
# Conecta-se ao broker MQTT
client.connect('localhost', 8080)
print('passei por qaui')
client.username_pw_set("admin", "hivemq")
print('passei por qaui')



# Inicia um loop que mantém a conexão com o broker MQTT ativa
client.loop_forever()

#///////////////////////////////////////





