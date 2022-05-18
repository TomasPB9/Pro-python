# hola 3 => holaholahola
# tomas 2 => tomastomas
# platzi 4 => platziplatziplatziplatzi

from timeit import repeat


def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar texto"
        return string * n
    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))

if __name__ == '__main__':
    run()