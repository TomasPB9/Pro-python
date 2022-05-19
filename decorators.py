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
        print("Mensaje 1 desde DECORADOR ")
        func()
        print("Mensaje 2 desde DECORADOR ")
    return inserta_msg

@decorador   #con sugar sintax
def harry():
    print("Mensaje desde la funcion original")

# harry = decorador(harry)  ------ sin sugar sintax

harry()   #execute function


#challenge 2 -------------------------------------
print("")
print("Challenge 2 ------------")
print("")



def decorator_2(func):
    def all_upper(name):
        print("Hola : " + name.upper())
        
    return all_upper

@decorator_2
def names(name):
    pass

names("Tomas")



#challenge 3 -------------------------------------
print("")
print("Challenge 3 ------------")
print("")

def decorator_3(func):
    def wrapper(name):
        func(name)
        func(name.upper())
        func(name.lower())
        print("edfgegr")
    return wrapper

@decorator_3
def challenge_3(name):
    print("Holaaaaa " + name)


challenge_3("Carlos")


def run():
    pass



if __name__=='__main__':
    run()