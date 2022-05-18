def is_palindrome(string: str) -> bool:
    string = string.replace(" ","").upper()
    return string == string[::-1]

def run():
    #cadena = input("Ingresa una frase: ")
    #print(is_palindrome(cadena))

    print(is_palindrome(1000))


if __name__=='__main__':
    run()