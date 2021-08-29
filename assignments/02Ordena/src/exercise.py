def main():
    # Escribe el código adecuado para completar el programa

    def ordenar_numeros():
    
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    c = float(input("Ingresa el tercer número: "))
    
    if a > b > c:
        print("El orden de los números acomodados de menor a mayor es:")
        print(c)
        print(b)
        print(a)
        
    elif a > c > b:
        print("El orden de los números acomodados de menor a mayor es:")
        print(b)
        print(c)
        print(a)    
        
    elif b > a > c:
        print("El orden de los números acomodados de menor a mayor es:")
        print(c)
        print(a)
        print(b)
        
    elif b > c > a:
        print("El orden de los números acomodados de menor a mayor es:")
        print(a)
        print(c)
        print(b)
        
    elif c > a > b:
        print("El orden de los números acomodados de menor a mayor es:")
        print(b)
        print(a)
        print(c)
        
    else:
        print("El orden de los números acomodados de menor a mayor es:")
        print(a)
        print(b)
        print(c)
          
        
    
        
ordenar_numeros() 
   
    


if __name__=='__main__':
    main()
