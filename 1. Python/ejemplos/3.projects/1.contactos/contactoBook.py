class Contacto:
    def __init__(self, name, phone, email):
        self._name = name
        self._phone = name
        self._email = email

class ContactoBook:
    def __init__(self):
        self._contactos = []

    def add(self):
        name = str(input("Ingrese el nombre: "))
        phone = str(input("Ingrese el telefono: "))
        email = str(input("Ingrese el email: "))

        contacto = Contacto(name, phone, email)
        self._contactos.append(contacto)

        print('name: {}, phone: {}, email: {}'.format(name, phone, email))          

    def showAll(self):
        for contacto in self._contactos:
            _print_contato(contacto)

    
    def _print_contato(self, _contacto):
        print('name: {}, phone: {}, email: {}'.format(_contacto.name, _contacto.phone, _contacto.email))    
            