def tarjetas(pliegos,plumones):
    
    tarjetasPliegos = pliegos*12
    tarjetasPlumones = plumones*35

    if tarjetasPliegos<=tarjetasPlumones:
        return tarjetasPliegos
    else:
        return tarjetasPlumones

def main():
    #escribe tu código abajo de esta línea
    pliegos = int(input("Dame la cantidad de pliegos de papel albanene: "))
    plumones = int(input("Dame la cantidad de plumones: "))

    num = tarjetas(pliegos,plumones)

    print("El número máximo de tarjetas que se pueden hacer es:",num)

if __name__=='__main__':
    main()
