def generarTabla(tabla):
    for i in range(10):
        print('{} * {} = {} '.format(tabla, i+1, (tabla*(i+1)))) 

def run():
    tabla = int(input('What multiplication table'))
    generarTabla(tabla)

if __name__ == '__main__':
    run()