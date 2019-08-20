import turtle

def main():
    windows = turtle.Screen()
    pino = turtle.Turtle()

    for x in range(20):
        make_square(pino, x * 10)

    turtle.mainloop()

def make_square(pino, length):
    #length = int(raw_input("El tamaño del cuadrado es:"))
    #length = int(20)

    for i in range(4):
        make_line_and_turn(pino, length)

def make_line_and_turn(pino, length):
    pino.forward(length)
    pino.left(90)

if __name__ == "__main__":
    main()    



