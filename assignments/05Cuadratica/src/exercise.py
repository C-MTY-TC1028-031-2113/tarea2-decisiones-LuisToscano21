import math

def main():
    # Escribe tu código abajo de esta línea
    def ecuaciones_cuadraticas():
    
        from math import sqrt
        
        a = float(input("Dame el valor de a: "))
        b = float(input("Dame el valor de b: "))
        c = float(input("Dame el valor de c: "))
        
        t = (b**2)-(4*a*c)
        
        if t < 0:
            print("Raices complejas")
            
        elif t == 0:
            print(-b/2*a)
        
        if a == 0 and b != 0:
            print(-c/b)
                
        if a == 0 and b == 0:
            print("La ecuación no tiene solución")
        
                
        e = sqrt(t)
        x = (-b + e)/(2*a)
        z = (-b - e)/(2*a)

            
        if a != 0 and b != 0:
            print(x)
            print(z)
        
    

    ecuaciones_cuadraticas() 

    pass

if __name__ == '__main__':
    main()
