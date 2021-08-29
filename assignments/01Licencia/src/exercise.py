
def main():

    def tramite_licencia():
    
        edad = int(input("Ingresa tu edad: "))
        ident = input("¿Tienes identificación oficial? (usar si o no): ")
        
        if edad >= 18 and ident == "si":
            print("**Trámite de licencia concedido**")
            
        elif 0 < edad < 18:
            print("**No se cumplen los requisitos**")
            
        elif edad >= 18 and ident == "no":
            print("**No se cumplen los requisitos**")    
            
        else:
            print("**Respuesta Incorrecta**")
        
    tramite_licencia()    
    pass 


if __name__ == '__main__':
    main()
