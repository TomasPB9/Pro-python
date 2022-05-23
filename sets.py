#eliminar duplicados de una lista

# [1 ,1 , 2, 2, 4 ] => [1, 2, 4]

def remove_duplicates(somelist):
    without_duplicates = []
    for element in somelist:
        #si el elemento no esta en la lista "without_duplicatest"
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


#challenge with sets, remove duplicates from a list, but dont use for loop only use sets

def remove_set(list_example):
    my_set = set(list_example)
    without_duplicates = []
    without_duplicates = my_set
    return without_duplicates

#shorter way
def removerduplicados(lista):
    return list(set(lista))




def run():
    random_list = [1 ,1 , 2, 2, 4 ]
    print(remove_duplicates(random_list))

    print()
    print("CHALLENGE WITH SET")
    list_exmaple = [1 ,1 , 2, 2, 4 ]
    print(remove_set(list_exmaple))

    print()
    print("CHALLENGE WITH SET WITH A SHORTER WAY")
    lista = [1 ,1 , 2, 2, 4 ]
    print(remove_duplicates(lista))

if __name__=='__main__':
    run()