#Definimos una expresion Lambda para retornar la cadena invertida
palindromo = lambda cadena: cadena[::-1]

#leeremos la palabra y la almacenamos en la variable palabra
#Y la comvertimos a minuscula
def main():
    palabra = input("\nIngresa la palabra a validar: ")
    validar = palabra.lower()

    if validar == palindromo(validar):
        print(f"{palabra} es un palindromo")
    else:
        print("No es un palindromo")


if __name__ == '__main__':
    main()
