import asyncio
import time

# in start i will do it in classic
print('Поточное')
x = 2
def func1(x):
    print(x**2)
    time.sleep(x)
    print('func1 is finish')

def func2(x):
    print(x**2)
    time.sleep(x)
    print('func2 is finish')
    
def main():
    func1(x)
    func2(x)
    
start = time.time()
main()
print(f'{int(time.time() - start)} секунды')
print('Ассинхронное')
# create func1 
async def func1(x):
    print(x**2)
    # is way to out of function while func is sleep is name (coroutine)
    
    await asyncio.sleep(x)
    # continue after x second and end!
    print('func1 is finish')
    
async def func2(x):
    print(x**2)
    await asyncio.sleep(x)
    print('func2 is finish')
    
async def main():
    task1 = asyncio.create_task(func1(x))
    task2 = asyncio.create_task(func2(x))
    
    await task1
    await task2

a = time.time()
asyncio.run(main())
print(f'{int(time.time()-a)} секунды' )


'''
вывод говорит сам за себя!

Поточное
4
func1 is finish
4
func2 is finish
4 секунды

Ассинхронное
4
4
func1 is finish
func2 is finish
2 секунды
'''