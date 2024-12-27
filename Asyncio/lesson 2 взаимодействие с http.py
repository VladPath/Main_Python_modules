import http
import asyncio
import time

# имитация  асинхронного соединения с некой периферией
async def get_connect(host,port):
    class Conn:
        async def put_data(self):
            print('Отправка данных...')
            await asyncio.sleep(2)
            print('Данные отправлены')
        async def get_data(self):
            print("Получение данных...")
            await asyncio.sleep(2)
            print("Данные получены")
        async def close(self):
            print('Закрытие сервера...')
            await asyncio.sleep(2)
            print('Сервер закрыт')
    print('Устанавлеваем соединение...')
    await asyncio.sleep(3)
    print('Соединение установлено')
    return Conn()

class Connection:
    # этот конструктор будет выполнен в заголовке with
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # этот метод будет неявно выполнен при входе в with
    async def __aenter__(self):
        self.conn = await get_connect(self.host, self.port)
        return self.conn

    # этот метод будет неявно выполнен при выходе из with
    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()

async def main():
    async with Connection('LockalHost',9001) as conn:
        send_data = asyncio.create_task(conn.put_data())
        get_data = asyncio.create_task(conn.get_data())
        
        await send_data
        await get_data

a = time.time()
asyncio.run(main())
print(int((time.time())-a), 'секунд')
