from socket import *  # Включив эту строку, мы сможем создавать сокеты внутри нашей программы.


def client():
    serverName = '127.0.0.1'
    serverPort = 12000
    # Мы не задаем номер порта клиентского сокета при его создании — позволяем это сделать за нас операционной системе.

    # AF_INET указывает, что мы будем использовать протокол IPv4
    # SOCK_DGRAM - тип сокета UDP-сокет
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    # При выполнении raw_input() пользователю на клиентской стороне предлагается подсказка со
    # словами «Input lowercase sentence».
    message = input('Input lowercase sentence: ')

    # В этой строке с помощью метода sendto() к сообщению добавляется адрес назначения (serverName, serverPort),
    # и весь результирующий пакет отправляет в сокет процесса — clientSocket.
    clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))

    # После отправки пакета клиент ожидает получения данных с сервера.
    # Данные пакета, прибывающего из Интернета на сокет клиента, помещаются в переменную modifiedMessage,
    # а адрес источника пакетов — в переменную serverAddress.
    # Метод recvfrom() генерирует входной буфер размером 2048 байт.
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode('utf-8'))

    # Здесь мы закрываем сокет, и процесс завершается.
    clientSocket.close()
