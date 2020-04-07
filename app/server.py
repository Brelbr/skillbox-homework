#
# Серверное приложение для соединений
# С изменениями по домашнему заданию
#
#
import asyncio
from asyncio import transports


class ServerProtocol(asyncio.Protocol):
    login: str = None
    server: 'Server'
    transport: transports.Transport

    def __init__(self, server: 'Server'):
        self.server = server

    def data_received(self, data: bytes):
        decoded = data.decode()
        if self.login is not None:
            self.send_message(decoded)
        else:
            if decoded.startswith("login:"):
                offer_login = decoded.replace("login:", "").replace("\r\n", "")
                for user in self.server.clients:
                    if user.login == offer_login:
                        self.transport.write(f"Логин {offer_login} занят, попробуйте другой!".encode())
                        self.transport.close()
                        return

                self.login = offer_login
                self.transport.write(
                    f"Привет, {self.login}!\n".encode()
                )
                self.send_history()
            else:
                self.transport.write("Неправильный логин\n".encode())

    def connection_made(self, transport: transports.Transport):
        self.server.clients.append(self)
        self.transport = transport
        address = self.transport.get_extra_info("peername")     # Получаем адрес подключившегося
        print(f"Пришел новый клиент {address}")

    def connection_lost(self, exception):
        self.server.clients.remove(self)
        print("Клиент вышел")

    def send_message(self, content: str):
        message = f"{self.login}: {content}"
        print(f"{message}")
        self.server.history.append(message)     # Заполненение истории
        if len(self.server.history) > 10:       # Ограничение по количеству сообщений в истории
            self.server.history.pop(0)

        for user in self.server.clients:
            user.transport.write(message.encode())

    def send_history(self):     # Функция отправки истории
        for message in self.server.history:
            self.transport.write(message.encode())

class Server:
    clients: list
    history: list   # Добавляем список для сохранения истории сообщений

    def __init__(self):
        self.clients = []
        self.history = []
    def build_protocol(self):
        return ServerProtocol(self)

    async def start(self):
        loop = asyncio.get_running_loop()

        coroutine = await loop.create_server(
            self.build_protocol,
            '127.0.0.1',
            8888
        )

        print("Сервер запущен ...")

        await coroutine.serve_forever()


process = Server()

try:
    asyncio.run(process.start())
except KeyboardInterrupt:
    print("Сервер остановлен вручную")
