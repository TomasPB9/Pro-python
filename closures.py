# hola 3 => holaholahola
# tomas 2 => tomastomas
# platzi 4 => platziplatziplatziplatzi

from timeit import repeat


def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar texto"
        return string * n
    return repeater


#challenge
def make_division_by(num):
    def division_by(divisor):
        return divisor/num
    return division_by


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))

    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_18 = make_division_by(18)
    print(division_by_18(54))



if __name__ == '__main__':
    run()