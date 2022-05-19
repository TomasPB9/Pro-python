def dividendo(dividen):
    def divisor(diviso):
        return diviso/dividen
    return divisor  


def run():
    div = dividendo(5)
    print(div(450))



if __name__=='__main__':
    run()