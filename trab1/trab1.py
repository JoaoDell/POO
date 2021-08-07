#João Victor Dell Agli Floriano - 10799783

d = 1 #inserir o numero do teste ao final do arquivo "test{d}"

filename = "test" + str(d)
arc = open(filename, encoding = "utf-8")



texto = arc.read()

dic = {}



lista = texto.split("\n")

    

for j in range (0, len(lista)):
    lista[j] = lista[j].lower() #deixa tudo em minusculo

lista.pop() #popa o último elemento da lista, que é um elemento vazio

for j in range(0, len(lista)):
    dic[lista[j]] = []


lista1 = []
#reordenando a ordem das letras das palavras na lista 
#em ordem alfabetica para facilitar e otimizar a busca por anagramas
r = 0
y = 0
for j in range(0, len(lista)):
    lista1.append(''.join(sorted(lista[j])))


    #atualizando o usuário do status do programa
    r += 1
    ra = (r/len(lista))*100
    y += 1
    if(y == 0):
        print("Organizando lista de palavras    (" + (str("%.2f" % ra) + "%" + ")"))
    elif(y == 12):
        print("Organizando lista de palavras.   (" + (str("%.2f" % ra) + "%" + ")"))
    elif(y == 24):
        print("Organizando lista de palavras..  (" + (str("%.2f" % ra) + "%" + ")"))
    elif(y == 36):
        print("Organizando lista de palavras... (" + (str("%.2f" % ra) + "%" + ")"))
        y = 0




#procurando por anagramas
r = 0
y = 0
for j in range (0, len(lista)):
    for k in range(0, len(lista)):

        if(len(lista[k]) == len(lista[j]) and lista[k] != lista[j] and lista1[k] == lista1[j]):
            
            dic[lista[j]].append(lista[k])


    #atualizando o usuário do status do programa
    r += 1
    ra = (r/len(lista))*100
    y += 1
    if(y == 0):
        print("Procurando por anagramas    (" + (str("%.2f" % ra) + "%" + ")"))
    elif(y == 12):
        print("Procurando por anagramas.   (" + (str("%.2f" % ra) + "%" + ")"))
    elif(y == 24):
        print("Procurando por anagramas..  (" + (str("%.2f" % ra) + "%" + ")"))
    elif(y == 36):
        print("Procurando por anagramas... (" + (str("%.2f" % ra) + "%" + ")"))
        y = 0


listaux = dic.keys()

#filtro de palavras repetidas
r = 0
y = 0
for j in range(0, len(lista)):
    for k in range(0, len( dic[lista[j]] )):
        if( dic[ lista[j] ][k] in listaux):
            del dic[lista[j]]
            break


    #atualizando o usuário do status do programa
    
    r += 1
    ra = (r/len(lista))*100
    y += 1
    if (y == 0):
        print("Filtrando palavras repetidas    (" + (str("%.2f" % ra) + "%" + ")"))
    elif (y == 12):
        print("Filtrando palavras repetidas.   (" + (str("%.2f" % ra) + "%" + ")"))
    elif (y == 24):
        print("Filtrando palavras repetidas..  (" + (str("%.2f" % ra) + "%" + ")"))
    elif (y == 36):
        print("Filtrando palavras repetidas... (" + (str("%.2f" % ra) + "%" + ")"))
        y = 0
                
listaux2 = list(dic.keys())
    
#gerando o arquivo de saída
outputname = "testejoao" + str(d) + ".ana"
a = open(outputname, mode = "w", encoding = "utf-8")


for j in range(len(listaux2)):
    if(len(dic[listaux2[j]]) > 0):
        listaux3 = []
        listaux3.append(listaux2[j])
        for k in range(len(dic[listaux2[j]])):
            listaux3.append(dic[listaux2[j]][k])
        a.write(", ".join(sorted(listaux3)) + "\n") #escrevendo a lista de palavras em ordem alfabetica no arquivo
    else:
        a.write(listaux2[j] + "\n")
a.close()
    
#Eu resolvi implementar uma atualização ao usuário pois, para alguns exemplos muito grandes como o 3 o qual não consegui otimizar
#esta atualização era de bom uso pois me informava o status do programa e me tranquilizava quanto ao seu funcionamento.


arc.close()