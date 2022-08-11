def Main():
    lista=[]
    
    n = int(input("Digite el numero de elementos para la lista: "))
    
    for i in range(n):
        lista.append(int(input("Digite un elemento para la lista: ")))
    
    print("\nELEMENTOS DE LA LISTA: ")
    for i in lista:
        print(i)
    
    print("METODO DE ORDENAMIENTO BURBUJA")
    for i in range(n):
        for j in range(n):
            if lista[i]>lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                
    print("IMPRIMIRE EL NUMERO")
                

if __name__ =='__main__':
    Main()