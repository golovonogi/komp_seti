from socket import socket, AF_INET, SOCK_STREAM


def tcp_server():
    serverPort = 12000

    # Сервер создает TCP-сокет.
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Затем мы связываем номер порта сервера (переменная serverPort) с нашим сокетом
    serverSocket.bind(('', serverPort))

    # После подготовки входной «двери» мы будем ожидать клиентов, стучащихся в нее.
    # 1 - максимальное число поставленных в очередь соединений.
    serverSocket.listen(1)
    print('The server is ready to receive')
    while True:
        # Когда клиент стучится в дверь, программа запускает для серверно- го сокета метод accept(), и тот создает новый
        # сокет на сервере — сокет соединения, который предназначен для этого конкретного клиента.
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024)
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence)
        # После отправки измененной строки клиенту мы закрываем сокет соединения. Но так как серверный сокет остается
        # открытым, любой другой клиент может постучаться в дверь и отправить серверу новую строку для изменения.
        connectionSocket.close()
