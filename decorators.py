from datetime import datetime
import re

#tiempo que tarda en ejecutarse la aplicacion
def exectuion_time(func):
    #no importa la cantidad de argumentos posicionales que se le envien, la funcion los va a recibir
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron: "+ str(time_elapsed.total_seconds()) + " segundos.")
    return wrapper

@exectuion_time
def random_fun():
    for _ in range(1, 1000000):
        pass

@exectuion_time
def suma(a: int, b: int) -> int:
    return print(a+b)


@exectuion_time
def saludos(nombre = "Cesar"):
    print("Hola "+ nombre)

random_fun()
suma(5, 5)
saludos()

#-----------------------------------------------------------
#free challenge with decorators
print("")
print("challenge with decorator")
print("")

def decorador(func):
    def inserta_msg():
        print("Esto inserta un mensaje")
        func()
        print("Esto inserta un mensaje 2∫")
    return inserta_msg

@decorador
def harry():
    print("Yo soy harry")


harry()


def run():
    pass



if __name__=='__main__':
    run()