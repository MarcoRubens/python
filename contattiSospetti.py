infilePresenze = open('presenze.txt', 'r', encoding='utf-8')
infileSospetti = open('sospetti.txt', 'r', encoding='utf-8')

dictPresenze = {}
for line in infilePresenze:
    line = line.rstrip()
    line = line.split(',')
    dictPresenze[line[0]] = line[1:]

listaSospetti = []
for line in infileSospetti:
    line = line.rstrip()
    listaSospetti.append(line)

infileSospetti.close()
infilePresenze.close()

dictContatti = {}
for sospetto in listaSospetti:
    if sospetto in dictPresenze:
        soggiorno = [int(dictPresenze[sospetto][1]), int(dictPresenze[sospetto][2])]
        listaContatti = []
        for ospite in dictPresenze:
            if ospite != sospetto:
                soggiornoOspite = [int(dictPresenze[ospite][1]), int(dictPresenze[ospite][2])]
                if soggiorno[0] <= soggiornoOspite[1] and soggiorno[1] >= soggiornoOspite[0]:
                    listaContatti.append(f'Contatto con {ospite}, telefono {dictPresenze[ospite][0]}')
        if listaContatti:
            dictContatti[f'**Contatti del cliente: {sospetto}: **'] = listaContatti
        else:
            listaContatti.append(f'Il cliente {sospetto} non ha avuto contatti')
            dictContatti[f'**Contatti del cliente: {sospetto}: **'] = listaContatti
    else:
        dictContatti[f'**Contatti del cliente: {sospetto}: **'] = [f'{sospetto} non presente in archivio']

for key in dictContatti:
    print(key)
    for i in dictContatti[key]:
        print(i)
    print()


