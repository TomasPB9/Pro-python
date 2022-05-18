def primalidad(num:int) -> bool:
    conteo = 0
    for i in range(1,num+1):
        #print(i)
        if(num%i == 0 or num==1):
            conteo+=1
        else:
            continue
    if conteo>2:
        #print("No es primo")
        return False
    else:
        #print("Si es primo !!!")
        return True

def run():
    #num = int(input("Ingresa un numero: "))
    #primalidad(num)

    print(primalidad(29))



if __name__=='__main__':
    run()