def next_primo(number):
    for x in range(number + 1, 1000):
        if x == 2 or x == 3:
            return x
        elif not(x % 2 == 0 or x % 3 == 0 or x % 5 == 0):
            return x      

def generarPrimos(q):
    number = 0
    for i in range(q):
        number = next_primo(number)
        print('{}. {} '.format(i,number))

def run():
    print('Numeros primos')
    q = int(input('Cuantos nùmeros deseas ver??? '))
    generarPrimos(q)

if __name__ == '__main__':
    run()