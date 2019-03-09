# algebra-de-conjuntos
Operações da álgebra de conjuntos

var:  
inteiro Conjunto  
inteiro A = {2,3,5,6,8}  
inteiro B = {6,8}  
var temp = Uniao(A,B)  

início  
função **AdicionarElemento** (conjunto,elemento: inteiro): inteiro  
se tamanho conjunto == 0 então  
conjunto recebe elemento  
retorne conjunto  
senão  
inteiro a recebe tamanho conjunto + 1  
para i=0 até i < tamanho de a faça  
se i < tamanho do conjunto então  
a[i] = conjunto[i]  
senão  
a[i] = elemento  
fimse  
fimpara  
retorne a  
fimse  
fimfuncao  
fim  


inicio  
função **RemoverElemento** (conjunto,elemento: inteiro): inteiro  
inteiro a recebe tamanho conjunto - 1  
boleano passou = false  
para i=0 até i < tamanho a faça  
se conjunto[i] diferente elemento então  
se diferente passou então  
a[i] = conjunto[i]  
senão  
a[i] = conjunto[i+1]  
fimse  
senão  
a[i] = conjunto[i+1]  
passou = true  
fimse  
fimpara  
retorne a  
fim  


inicio  
função **Pertinencia** (conjunto,elemento: inteiro): boleano  
para i=0 até i < tamanho conjunto faça  
se conjunto[i] == elemento então  
retorne verdadeiro  
fimse  
fimpara  
retorne falso  
fim  


início  
função **Continencia** (conjuntoA,conjuntoB: inteiro): boleano  
inteiro cont = 0  
se tamanho conjuntoA <= tamanho conjuntoB então  
para i=0 até i < tamanho conjuntoA faça  
para j=0 até j < tamanho conjuntoB faça  
se conjuntoB[j] == conjuntoA[i] então  
cont++  
fimse  
fimpara  
fimpara  
fimse  
se cont == tamanho conjuntoA então  
retorne verdadeiro  
fimse  
retorne falso  
fim  


início  
função **Disjuncao** (conjuntoA,conjuntoB: inteiro): boleano  
inteiro cont = 0  
se tamanho conjuntoA <= tamanho conjuntoB então  
para i=0 até i < tamanho conjuntoA faça  
para j=0 até j < tamanho conjuntoB faça  
se conjuntoB[j] == conjuntoA[i] então  
cont++  
fimse  
fimpara  
fimpara  
fimse  
se cont == 0 então  
retorne verdadeiro  
fimse  
retorne falso  
fim  


início  
função **UniaoDisjunta** (conjuntoA,conjuntoB: UniaoDisjunta): lista caracter  
lista caracter c  
para i=0 até i < tamanho conjunto do conjuntoA faça  
adiciona em c conjunto[i] do conjuntoA + nomeConjunto do conjuntoA  
fimpara  
para i=0 até tamanho conjunto do conjuntoB faça  
adiciona em c conjunto[i] do conjuntoB + nomeConjunto do conjuntoB  
fimpara  
retorne c  
fim  


início  
função **Uniao** (conjuntoA,conjuntoB: inteiro): lista inteiro  
lista inteiro a  
para i=0 até i < tamanho conjuntoA faça  
adiciona em a conjuntoA[i]  
fimpara  
boleano temp = falso  
para i=0 até i < tamanho conjuntoB faça  
para j=0 até j < contador de a faça  
se conjuntoB[i] == a[j] então  
tem = verdadeiro  
pausa  
fimse  
fimpara
se diferente temp então  
adiciona a conjuntoB[i]  
fimse  
fimpara  
retorne a  
fim  


início  
função **Diferenca** (A,B: inteiro): lista inteiro  
lista inteiro listaTemp  
para i=0 até i < tamanho B faça  
boleano temp = falso  
para j=0 até j < tamanho A faça  
se A[j] == B[i] então  
temp = verdadeiro
fimse  
fimpara  
se diferente temp então  
adiciona listaTemp B[i]  
fimse  
fimpara  
para i=0 até i < tamanho A faça  
boleano temp = falso  
para j=0 até j < tamanho B faça  
se A[i] == B[j] então  
temp = verdadeiro  
fimse  
fimpara  
se diferente temp então  
adiciona listaTemp A[i]  
fimse  
fimpara  
retorne listaTemp  
fim  


início  
função **ConjuntoDasPartes** (A: inteiro): lista inteiro  
lista inteiro listaTemp  
para i=0 até i < tamanho A faça  
adiciona em listaTemp inteiro A[i]  
fimpara  
para i=0 até i < tamanho A faça  
para j = tamanho A - 1 até j >= 0 faça  
se A[i] diferente A[j] então  
adiciona listaTemp inteiro A[i], A[j]  
fimse  
fimpara  
fimpara  
retorne listaTemp  
fim  


início  
função **Complemento** (A,B: inteiro): lista inteiro  
lista inteiro C  
para i=0 até i < tamanho A faça  
adiciona C A[i]  
fimpara  
boleano temp = falso  
para i=0 até i < tamanho B faça  
para j=0 até j < contador C faça  
se B[i] == C[j] então  
remove C j  
pausa  
senão  
temp = verdadeiro  
fimse  
fimpara  
se diferente temp então  
adiciona C B[i]  
fimse  
fimpara  
retorne C  
fim  
