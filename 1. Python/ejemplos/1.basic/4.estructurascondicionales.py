def estudiante(nota):
    if nota < 1:
        print('Deficiente')
    elif nota > 1 and nota < 2:
        print('insuficiente') 
    elif nota < 2.6:
        print('Reprobo') 
    elif nota < 3:
        print('Refuerzo') 
    elif nota < 3.5:
        print('Aprobo') 
    elif nota < 4:
        print('Notable') 
    elif nota < 4.5:
        print('Sobresaliente')
    else:
        print('Excelente')      

def run():
    print('Estructuras condicionales')
    nota = float(input('Ingrese la nota: '))
    estudiante(nota)

if __name__ == '__main__':
    run()