from socket import *


def server():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)

    # Данная строка назначает порт под номером 12000 сокету сервера
    serverSocket.bind(('', serverPort))
    print("The server is ready to receive")

    # Бесконечный цикл while, который позволяет получать и обрабатывать пакеты от клиентов в неограниченном количестве.
    while 1:
        message, clientAddress = serverSocket.recvfrom(2048)

        # Здесь мы берем введенную клиентом строку и, используя метод upper(), меняем ее символы на заглавные.
        modifiedMessage = message.upper()

        # Данная последняя строка кода присоединяет адрес клиента (IP-адрес и номер порта) к измененному сообщению и
        # отправляет результирующий пакет в сокет сервера. Затем Интернет доставляет пакет на этот клиентский адрес.
        serverSocket.sendto(modifiedMessage, clientAddress)
