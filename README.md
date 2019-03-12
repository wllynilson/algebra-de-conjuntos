# Álgebra de Conjuntos
#### Alunos: Ewerton Santiago, Gustavo Siqueira, Wllynilson Carneiro
##### Operações da álgebra de conjuntos

var:  
> **Conjunto:** 
    _vetor de inteiros_    
    A: `vetor[2,3,5,6,8]` de inteiros    
    B: `vetor[6,8]` de inteiros    
    temp: `Uniao(A,B)` inteiros    

    início  
    função AdicionarElemento (conjunto[], elemento: inteiro): vetor de inteiro  
        se o tamanho do conjunto = 0 então  
            conjunto na primeira posição <- elemento.  
            retorne o conjunto  
        senão  
            vetor de inteiro a <- tamanho do conjunto + 1  
            para i<-0 até i < tamanho de a faça  
                se i < tamanho do conjunto então  
                    a[i] <- conjunto[i]  
                senão  
                    a[i] <- elemento  
                fimse  
            fimpara  
            retorne a  
        fimse  
    fim  


    inicio  
    função RemoverElemento (conjunto[],elemento: inteiro): vetor de inteiro  
        vetor de inteiro a <- tamanho conjunto - 1  
        lógico passou <- false  
        para i<-0 até i < tamanho de a faça  
            se conjunto[i] diferente do elemento então  
                se passou diferente de falso então  
                    a[i] <- conjunto[i]  
                senão  
                    a[i] <- conjunto[i+1]  
                fimse  
            senão  
                a[i] <- conjunto[i+1]  
                passou <- true  
            fimse  
        fimpara  
        retorne a  
    fim  


    inicio  
    função Pertinencia (conjunto[],elemento: inteiro): lógico  
        para i<-0 até i < tamanho conjunto faça  
            se conjunto[i] = elemento então  
                retorne verdadeiro  
            fimse  
        fimpara  
        retorne falso  
    fim  


    início  
    função Continencia (conjuntoA,conjuntoB: vetor de inteiro): lógico  
        inteiro cont <- 0  
        se tamanho do conjuntoA <= tamanho do conjuntoB então  
            para i<-0 até i < tamanho conjuntoA faça  
                para j<-0 até j < tamanho conjuntoB faça  
                    se conjuntoB[j] = conjuntoA[i] então  
                        incrementa cont  
                    fimse  
                fimpara  
            fimpara  
        fimse  
        se cont = tamanho do conjuntoA então  
            retorne verdadeiro  
        senão  
            retorne falso  
        fimse  
    fim  


    início  
    função Disjuncao (conjuntoA,conjuntoB: vetor de inteiro): lógico  
        inteiro cont <- 0  
        se tamanho do conjuntoA <= tamanho do conjuntoB então  
            para i<-0 até i < tamanho do conjuntoA faça  
                para j<-0 até j < tamanho do conjuntoB faça  
                    se conjuntoB[j] = conjuntoA[i] então  
                        incrementa cont  
                    fimse  
                fimpara  
            fimpara  
        fimse  
        se cont = 0 então  
            retorne verdadeiro  
        senão  
            retorne falso  
        fimse   
    fim  


    início  
    função UniaoDisjunta (conjuntoA,conjuntoB: classe UniaoDisjunta): lista de caracter  
        c: lista de caracter  
        para i<-0 até i < tamanho do atributo Conjunto do conjuntoA faça  
            adiciona em c conjuntoA.Conjunto[i] + atributo nomeConjunto do conjuntoA  
        fimpara  
        para i<-0 até tamanho do atributo Conjunto do conjuntoB faça  
            adiciona em c conjuntoB.Conjunto[i] + atributo nomeConjunto do conjuntoB  
        fimpara  
        retorne c  
    fim  


    início  
    função Uniao (conjuntoA,conjuntoB: vetor de inteiro): lista de inteiro  
        a: lista inteiro    
        para i<-0 até i < tamanho do conjuntoA faça  
            adiciona em a conjuntoA[i]  
        fimpara  
        lógico temp <- falso  
        para i<-0 até i < tamanho do conjuntoB faça  
            para j<-0 até j < contador de a faça  
                se conjuntoB[i] = a[j] então  
                    temp <- verdadeiro  
                    pausa  
                fimse  
            fimpara
            se diferença de temp então  
                adiciona em a conjuntoB[i]  
            fimse  
        fimpara  
        retorne a  
    fim  


    início  
    função Diferenca (A,B: vetor de inteiro): lista de inteiro  
        listaTemp: lista inteiro    
        para i<-0 até i < tamanho de B faça  
            lógico temp <- falso  
            para j<-0 até j < tamanho de A faça  
                se A[j] = B[i] então  
                    temp <- verdadeiro
                fimse  
            fimpara  
            se diferença temp então  
                adiciona em listaTemp B[i]  
            fimse  
        fimpara  
        para i<-0 até i < tamanho de A faça  
            lógico temp <- falso  
            para j<-0 até j < tamanho de B faça  
                se A[i] = B[j] então  
                    temp <- verdadeiro  
                fimse  
            fimpara  
            se diferença temp então  
                adiciona na listaTemp A[i]  
            fimse  
        fimpara  
        retorne listaTemp  
    fim  


    início  
    função ConjuntoDasPartes (A: vetor de inteiro): lista de vetor de inteiro  
        listaTemp: lista de vetor de inteiro    
        para i<-0 até i < tamanho de A faça  
            adiciona na listaTemp A[i]  
        fimpara  
        para i<-0 até i < tamanho de A faça  
            para j <- tamanho A - 1 até j >= 0 faça  
                se A[i] diferente A[j] então  
                    adiciona na listaTemp A[i], A[j]  
                fimse  
            fimpara  
        fimpara  
        retorne listaTemp  
    fim  


    início  
    função Complemento (A,B: vetor de inteiro): lista inteiro  
        C: lista inteiro    
        para i<-0 até i < tamanho de A faça  
            adiciona em C A[i]  
        fimpara  
        lógico temp <- falso  
        para i<-0 até i < tamanho de B faça  
            para j<-0 até j < contador C faça  
                se B[i] = C[j] então  
                    remove de C j  
                    pausa  
                senão  
                    temp <- verdadeiro  
                fimse  
            fimpara  
            se diferença temp então  
                adiciona em C B[i]  
            fimse  
        fimpara  
        retorne C  
    fim  


    início  
    classe UniaoDisjunta  
        NomeConjunto: caracter  
        Conjunto: vetor de inteiro  
        construtor UniaoDisjunta (nomeConjunto: caracter, conjunto: vetor de inteiro)  
            NomeConjunto <- nomeConjunto  
            Conjunto <- conjunto  
    fim  
