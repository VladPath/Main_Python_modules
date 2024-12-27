import asyncio

# create func1 
async def func1(x):
    print(x**2)
    # is way to out of function while func is sleep
    await asyncio.sleep(x)
    # continue after x second and end!
    print('func1 is finish')

async def func2(x):
    print(x**2)
    await asyncio.sleep(x)
    print('func2 is finish')
    
async def main():
    task1 = asyncio.create_task(func1(3))
    task2 = asyncio.create_task(func2(2))
    
    await task1
    await task2

asyncio.run(main())