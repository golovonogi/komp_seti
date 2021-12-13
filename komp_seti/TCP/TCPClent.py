from socket import socket, AF_INET, SOCK_STREAM


def tcp_client():
    serverName = '127.0.0.1'
    serverPort = 12000
    # Мы не задаем номер порта клиентского сокета при его создании — позволяем это сделать за нас операционной системе.

    # AF_INET указывает, что мы будем использовать протокол IPv4
    # SOCK_STREAM - тип сокета TCP-сокет
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Инициирует соединение между клиентом и сервером
    clientSocket.connect((serverName, serverPort))
    # После исполнения этой строки кода осуществляется тройное рукопожатие,
    # и между клиентом и сервером устанавливается TCP-соединение.

    sentence = input('Input lowercase sentence: ')

    # Данная строка отправляет строковую переменную sentence через клиентский сокет в TCP-соединение.
    # Заметим, что программа явно не создает пакет и не прикрепляет адрес назначения к нему, как это было в случае
    # с UDP-сокетами.
    clientSocket.send(sentence.encode('utf-8'))

    # Ожидаем получения данных от сервера.
    modifiedSentence = clientSocket.recv(1024)
    print('From Server:', modifiedSentence.decode('utf-8'))

    # Последняя строка закрывает сокет, а, следовательно, закрывает TCP-соединение между клиентом и сервером.
    clientSocket.close()
