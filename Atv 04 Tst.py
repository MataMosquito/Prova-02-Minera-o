def calcSuporte(transacoes,produtos):
    numProdutos = produtos.__len__()
    a = transacoes.__len__()
    num_Contem = transacoes.__len__()
    i = 1;
    for i in range(i,a+1):
        k = 0;
        for k in range(k,numProdutos):
            if(produtos[k] in transacoes[i]):
                num_Contem;
            else:
                num_Contem = num_Contem-1;
                break;
    return (num_Contem/a);

#Calculo da Confiança
def calcConfianca(transacoes,produtos,produtosX):
    numProdutos = produtos.__len__()
    numProdutosX = produtosX.__len__()
    a = transacoes.__len__()
    num_Contem = transacoes.__len__()
    num_ContemX = transacoes.__len__()
    i = 1;
    for i in range(i,a+1):
        k = 0;
        for k in range(k,numProdutos):
            if(produtos[k] in transacoes[i]):
                num_Contem;
            else:
                num_Contem = num_Contem-1;
                break;
    i = 1;
    for i in range(i,a+1):
        k = 0;
        for k in range(k,numProdutosX):
            if(produtosX[k] in transacoes[i]):
                num_ContemX;
            else:
                num_ContemX = num_ContemX-1;
                break;
    return (num_Contem/num_ContemX);

#Calculo do lift
def calcLift(transacoes,produtos,produtosX,produtosY):
     return (calcSuporte(transacoes,produtos)/(calcSuporte(transacoes,produtosX)*calcSuporte(transacoes,produtosY)))

#Transações efetuadas
transacoes = {1: {"Maizena", "Fralda"},
              2: {"Sabão", "Cerveja"},
              3: {"Sabão", "Arroz","Suco"},
              4: {"Maizena", "Fralda", "Sabão", "Suco"}
              }

ouroX = ["Provavel"];
ouroY = ["Nao_Provavel"];
ouro = ouroX + ouroY;

#Chama funções
prc = calcPorcentagem(transacoes,ouro);
an = calcAno(transacoes,ouro,ouroX)
pr = calcPreco(transacoes,ouro,ouroX,ouroY)

#Printa os resultados obridos
print("Porcentagem = ",prc*100,"%");
print("Ano = ",an*100,"%")
print("Preço = ",pr)