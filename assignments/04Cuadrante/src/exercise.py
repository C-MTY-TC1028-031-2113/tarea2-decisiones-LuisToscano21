def main():
    # Escribe tu código abajo de esta línea

    def grados_cuadrantes():
    
        a = float(input("Introduce la cantidad de grados: "))
        
        if 0 < a < 90:
            print("El ángulo se encuentra en el cuadrante 1")
            
        elif 90 < a < 180:
            print("El ángulo se encuentra en el cuadrante 2")
            
        elif 180 < a < 270:
            print("El ángulo se encuentra en el cuadrante 3")
            
        elif 270 < a < 360:
            print("El ángulo se encuentra en el cuadrante 4")
            
        elif a == 90:
            print("Eje 1")
            
        elif a == 180:
            print("Eje 2")
            
        elif a == 270:
            print("Eje 3")
            
        elif a == 360 or a == 0:
            print("Eje 4")
            
        else:
            print("El ángulo no está dentro del cuadrante")
            
    grados_cuadrantes()
    pass

if __name__ == '__main__':
    main()
