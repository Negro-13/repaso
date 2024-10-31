print('Elija su numero de sublistas')
lista = []
cantlist = int(input())

def lists (cantlist, lista):
    for i in range(cantlist):
        print(f'Selecione los numeros de la sublista {i + 1}')
        num = int(input())
        sublist = []
        if num == -1:
            lista.append(sublist)
            i += 1
        else:
            sublist.append(num)
            num = int(input())
    return lista

print(lists (cantlist, lista))