
def hilos_threading():
    import time
    import threading

    def print_hello_three_times():
        for i in range(3):
            print("hilo simple")
            time.sleep(1)
        print("fin")

    def print_hi_three_times():
        for i in range(3):
            print("Python es hermoso")
            time.sleep(1)
        print("fin")

    t1 = threading.Thread(target=print_hello_three_times)
    t2 = threading.Thread(target=print_hi_three_times)

    t1.start()
    t2.start()

def funcion_dormir_simple():
    import asyncio
    async def sleep(time = 5):
        await asyncio.sleep(time)
        print('sleep')
    asyncio.run(sleep())
    asyncio.run(sleep())
    print("10 seg")


def funcion_hilos():
    import time
    import asyncio
    async def sleep(delay, what):
        await asyncio.sleep(delay)
        print(what)
    async def hilos_sumultaneos():
        task1 = asyncio.create_task(
            sleep(5, 'hello'))  # aqui  si son hilos, pasan los 2 al mismo tiempo
        task2 = asyncio.create_task(
            sleep(10, 'world'))
        print(f"started at {time.strftime('%X')}")
        await task1
        await task2
        print(f"finished at {time.strftime('%X')}")
    asyncio.run(hilos_sumultaneos())

def auto_destruccion_de_hilo():
    import asyncio
    import datetime

    async def display_date():
        loop = asyncio.get_running_loop()
        end_time = loop.time() + 5.0  # forzar_detencion
        # de hilo a sepues de cierto tiempo (5 seg)
        while True:
            print(datetime.datetime.now().time())
            if (loop.time() + 1.0) >= end_time:
                break
            await asyncio.sleep(1)  # operacion real

    asyncio.run(display_date())


def funcion_hilos_juntos():
    import asyncio
    async def hilo_tarea(name, number):  # actualizacion de tareas asicronas
        for i in range(0, number):
            print(f"Hilo {name} {i} segundos")
            await asyncio.sleep(1)
        print("----")
        print(f"Tarea {name} termino en {number} segundos")
    async def hilos_juntos():
        await asyncio.gather(
            hilo_tarea("A", 2),
            hilo_tarea("B", 3),
            hilo_tarea("C", 4),
            hilo_tarea("D", 5), )
    asyncio.run(hilos_juntos())


def funcion_time_out():

    import asyncio

    async def mucho_tiempo():
        await asyncio.sleep(60)
        print('yay!')

    async def hilo_time_out():
        try:
            await asyncio.wait_for(mucho_tiempo(), timeout=10)  # forsar que se cierre el hilo a los 10 seg
        except asyncio.TimeoutError:
            print('timeout!')

    asyncio.run(hilo_time_out())

    extraer_dato = int(input("Introduce un numero: "))
    print(extraer_dato)


def funcion_hora():
    import time

    result = time.localtime()
    print("result:", result)
    print("year:", result.tm_year)
    print("tm_hour:", result.tm_hour)

    t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)
    local_time = time.mktime(t)
    print("Local time:", local_time)

    # while True:
    for a in range(0, 10):
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        print(result)
        time.sleep(1)

# la estructura para llamar siempre es...  asyncio.algo(nombre_de_funcion())
# la estructura de la funcion siempre es...  async def nombre_de_funcion():
