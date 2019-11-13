# -*- coding: utf8 -*-
from contactoBook import ContactoBook


def run():
    listBook = ContactoBook() 

    while True:
        command = str(input('''
            Que deseas hacer?

            [1] Agregar
            [2] Actualizar
            [3] Eliminar
            [4] Listar

            [9] Salir
        '''))
        
        if command == '1':
            listBook.add()
        if commad == '4':
            listBook.showAll()    
        elif command == '9':
            break                    

if __name__ == '__main__':
    run()