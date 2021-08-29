def main():
    #escribe tu código abajo de esta línea
    pass

    def peso_imc():
    
        a = float(input("Dame el peso del individuo en kilos: "))
        b = float(input("Dame la altura del individuo en metros: "))
    
        if b <= 0:
            print("Revisa tus datos, alguno de ellos es erróneo")
    
        c = a/(b**2)
        
        if 0 < c < 20:
            print("PESO BAJO")
            
        elif 20 <= c < 25:
            print("PESO NORMAL")
            
        elif 25 <= c < 30:
            print("SOBREPESO")
            
        elif 30 <= c < 40:
            print("OBESIDAD")
            
        else:
            print("OBESIDAD MORBIDA")
        
    
    
    peso_imc()
    

if __name__=='__main__':
    main()