infile1 = open('C:\\Users\\marco\\OneDrive - Politecnico di Torino\\informatica\\esami\\astrologia_calciatori\\sportivi.csv', 'r', encoding='utf-8')
infile2 = open('C:\\Users\\marco\\OneDrive - Politecnico di Torino\\informatica\\esami\\astrologia_calciatori\\zodiaco.csv', 'r', encoding='utf-8')

dictCalciatori = {}
for line in infile1:
    line = line.rstrip()
    line = line.split(',')
    line[3] = line[3].split('/')
    line[3] = line[3][1] + line[3][0]
    if line[3][0] == '0':
        line[3] = line[3].lstrip('0')
    line[3] = int(line[3])
    line[1] = int(line[1])
    dictCalciatori[line[0]] = (line[1], line[3])

# print(dictCalciatori)
segniZodiacali = {}
for line in infile2:
    line = line.rstrip()
    line = line.split(',')
    line[1] = line[1].split('/')
    line[2] = line[2].split('/')
    line[1] = line[1][1] + line[1][0]
    if line[1][0] == '0':
        line[1] = line[1].lstrip('0')
    line[1] = int(line[1])
    line[2] = line[2][1] + line[2][0]
    if line[2][0] == '0':
        line[2] = line[2].lstrip('0')
    line[2] = int(line[2])
    segniZodiacali[line[0]] = (line[1], line[2])

golPerSegno = []
for segno in segniZodiacali:
    nGol = 0
    for calciatore in dictCalciatori:
        if segniZodiacali[segno][0] <= dictCalciatori[calciatore][1] <= segniZodiacali[segno][1]:
            nGol += dictCalciatori[calciatore][0]
    golPerSegno.append((nGol, segno))

infile1.close()
infile2.close()

golPerSegno.sort(reverse=True)
golPerStella = golPerSegno[1][0] // 50

for i in golPerSegno:
    print(f'{i[1] : <10}', f'{"("+ str(i[0]) + ")" : >7}', '*' * (i[0]//golPerStella))

