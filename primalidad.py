def primalidad(num):
    conteo = 0
    for i in range(1,num+1):
        #print(i)
        if(num%i == 0 or num==1):
            conteo+=1
        else:
            continue
    if conteo>2:
        print("No es primo")
    else:
        print("Si es primo !!!")

def run():
    num = int(input("Ingresa un numero: "))
    primalidad(num)



if __name__=='__main__':
    run()