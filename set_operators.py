def run():
    #UNION----------------
    print()
    print("UNION: ")
    set_1 = {1, 2, 3}
    set_2 = {3, 4, 5}
    set_3 = set_1 | set_2 
    print(set_3)

    # O de forma mas explicita
    print(set_1.union(set_2) )

    #INTERSECCION ------------------
    print()
    print("INTERESECCION: ")
    set_1 = {1, 2, 3}
    set_2 = {3, 4, 5}
    set_3 = set_1 & set_2 
    print(set_3)

    # O de forma mas explicita
    print(set_1.intersection(set_2))

    #DIFERENCIA----------------------
    print()
    print("DIFERENCIA: ")
    my_set1 = { 3, 4, 5}
    my_set2 = { 5, 6, 7}

    my_set3 = my_set1 - my_set2 
    my_set4 = my_set2 - my_set1
    print(my_set3)
    print(my_set4)

    # O de forma mas explicita
    print(set_1.difference(my_set2)) 


    #DIFERENCIA SIMETRICA----------------------
    print()
    print("DIFERENCIA SIMETRICA: ")
    set_1 = {1, 2, 3}
    set_2 = {3, 4, 5}
    set_3 = set_1 ^ set_2 
    print(set_3)

    # O de forma mas explicita
    print(set_1.symmetric_difference(set_2))




if __name__=='__main__':
    run()