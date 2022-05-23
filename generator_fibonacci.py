import time

#creacion del generador
def fibo_gen(max: int):
    n1 = 0
    n2 = 1
    counter = 0
    #ciclo infinito
    while True:
        if counter == 0:
            counter += 1
            yield n1   #devuelve 0
        elif counter == 1:
            counter += 1
            yield n2   #devuelve 1
        elif not max or counter <= max:
            aux = n1 + n2
            #swapping
            n1 , n2 = n2 , aux
            counter += 1
            yield aux   #devuelve los demas elementos de la suscesion fibonacci
        else:
            #sucesion fibonacci finita
            break


if __name__=='__main__':
    #instancia del generador (fibogen retorna un generador) se guarda en la variable "fibonacci"  
    fibonacci = fibo_gen(5)
    #recorrer cada uno de los elementos del generador
    for element in fibonacci:
        print(element)
        time.sleep(1)