import pandas as pd
import numpy as np

Tabela_prov_atual = np.array([[2843.51, 3142.06, 3471.99, 3836.54, 4239.37, 4684.50, 5176.38, 5719.90], 
                              [2985.66, 3299.16, 3645.59, 4028.37, 4451.35, 4918.74, 5435.21, 6005.90],
                              [3134.96, 3464.13, 3827.87, 4229.79, 4673.91, 5164.68, 5706.97, 6306.20],
                              [3291.70, 3637.33, 4019.26, 4441.28, 4904.61, 5422.91, 5992.32, 6621.52],
                              [3456.28, 3819.20, 4220.22, 4663.34, 5152.98, 5694.05, 6291.93, 6952.59],
                              [3629.11, 4010.16, 4431.23, 4896.51, 5410.64, 5978.76, 6606.52, 7300.22],
                              [3810.57, 4210.67, 4652.78, 5141.35, 5681.16, 6277.70, 6936.85, 7665.23],
                              [4001.09, 4421.20, 4885.44, 5398.39, 5965.23, 6591.57, 7283.71, 8048.48]])

Faixas = (1,2,3,4,5,6,7,8)
Niveis = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

#Entrada de dados (faixa do servidor)
Faixa = (int(input('Digite sua faixa: ')))

#verificação da faixa.    
while Faixa not in Faixas:
    Faixa = (int(input('Número da faixa está incorreto!!! Digite sua faixa: ')))

F = Faixa - 1

#Entrada de dados (Nível do Servidor.)
Nivel = input('Digite seu Nível: ')

#verificação do Nível     
while Nivel not in Niveis:
  Nivel = input('Número do Nível incorreto!!! Digite seu Nível: ')

N = Nivel

if Nivel == 'A' or Nivel == 'a':
  N = 0
elif Nivel == 'B' or Nivel == 'b':
  N = 1
elif Nivel == 'C' or Nivel == 'c':
  N = 2
elif Nivel == 'D' or Nivel == 'd':
  N = 3
elif Nivel == 'E' or Nivel == 'e':
  N = 4
elif Nivel == 'F' or Nivel == 'f':
  N = 5
elif Nivel == 'G' or Nivel == 'g':
  N = 6
else:
  N = 7

#Buscando salário base na tabela usando informações de entrada faixa/nível    
Salario_Base = Tabela_prov_atual[N, F]
print()
print('==> Valor do salário base atual: R${:.2f}.'.format(Salario_Base))
print()

#Calculando abono de acordo com salário base
Abono = 3845.63 - float(Salario_Base)
if Abono > 0:
  print('==> O valor do seu abono será de R${:.2f}.'.format(Abono))
  print()
else:
  Abono = 0
  print('==> Seu salário base é maior que o piso nacional, logo você não tem direito a abono.')
  print()

#Entrada de dados (tempo de serviço)
tempo_servico = int(input('Digite seu tempo de serviço em anos completos (exemplo: 6 anos e 11 meses = 6 anos. \nTempo de Serviço: '))
print()

#verificando entrada de dados
while tempo_servico not in range(50):
    tempo_servico = int(input('Tempo de serviço incorreto!!!Digite seu tempo de serviço em anos completos (exemplo: 6 anos e 11 meses = 6 anos. Tempo de Serviço: '))


#Calculando quinquênio de acordo com o tempo de serviço.   
if tempo_servico >= 5:
  Numero_quinquenios = (tempo_servico//5)
  Valor_quinquenios = Salario_Base*(0.05*Numero_quinquenios)
  print('==> Você possui {} quinquênio(s) cujo valor total é de R${:.2f}.'.format(Numero_quinquenios, Valor_quinquenios))
else:
  Numero_quinquenios = 0
  Valor_quinquenios = 0.00
  print()
  print('==> Você ainda não possui quinquênios.')
print()

#Calculando sexta-parte de acordo com o tempo de serviço.  
if tempo_servico >= 20:
  Valor_sexta_parte = (Salario_Base + Valor_quinquenios)/6
  print('==> O valor recebido pela sexta-parte é de R${:.2f}.'.format(Valor_sexta_parte))
  print()
else:
  Valor_sexta_parte = 0.00
  print('Você ainda não possui direito a sexta parte.')
  print()

#calculando salário bruto professores da PEI. 
#Entrada de dados
pei = int(input('Você é professor em uma escola integral? [1] sim  [2] Não : '))
print()

while pei not in (1, 2):
  pei = int(input('Opção incorreta!!! Você é professor em uma escola integral? [1] sim  [2] Não : '))

if pei == 1:
  gratificacao = 2000
  print('De acordo com o seu salário base, sua gratificação é de R${:.2f}.'.format(gratificacao))
  print()
else:
  gratificacao = 0
  print('Você não possui gratificação.')
  print()

#Calculando salário bruto sem PEI
Salario_Bruto = Salario_Base + Abono + Valor_quinquenios + Valor_sexta_parte
print('==> O valor do seu salário bruto sem gratificação PEI é de R${:.2f}.'.format(Salario_Bruto))
print('--'*50)

#Calculando o salário bruto com PEI
if pei == 1: 
  Salario_Bruto_pei = Salario_Base + Abono + Valor_quinquenios + Valor_sexta_parte + gratificacao
  print()
  print('==> O valor do seu salário bruto com gratificação PEI é de R${:.2f}.'.format(Salario_Bruto_pei))
  print('--'*50)


#Classificação para a nova carreira
#entrada de dados 
titulacao = int(input('Qual a sua titulação: [1] Licenciado [2] Mestre [3] Doutor'))

#Validação dado de entrada
while titulacao not in (1, 2, 3):
  titulacao = int(input('Titulação inexistente!!! Qual a sua titulação: [1] Licenciado [2] Mestre [3] Doutor'))

#Dados fornecidos pelo governo (tabela oficial)
Lic = (5000.00, 5500.00, 6100.00, 6800.00, 7200.00, 7700.00, 8300.00, 8800.00, 9400.00, 9900.00, 10500.00, 11000.00, 11800.00, 12300.00, 13000.00)
Mestre = (5775.00, 6495.00, 6930.00, 7580.00, 8085.00, 8715.00, 9240.00, 9870.00, 10395.00, 11025.00, 11550.00, 12180.00, 12915.00, 13650.00)
Dout = (6050.00, 6710.00, 7280.00, 7920.00, 8470.00, 9130.00, 9680.00, 10340.00, 10690.00, 11550.00, 12100.00, 12750.00, 1520.00, 14300.00)

#Contadores
L = 15
M = 14
D = 14
i = -1

#Calculo de Salário tabelado para licenciados
if titulacao == 1:
  if Salario_Bruto < Lic[0]:
    print('Você será classificado em L1 (Licenciatura Nível 1) e seu salário tabelado será de R${:.2f}.'.format(Lic[0]))
  else:
    while Salario_Bruto <= Lic[i]:
      Salario_tabelado = Lic[i-1]
      L = L - 1
      i = i - 1
    print()
    print('Você será classificado em L{} (Licenciatura Nível {}) e seu salário tabelado será de R${:.2f}.'.format(L, L, Salario_tabelado))

   
#Calculo de Salário tabelado para mestres
if titulacao == 2:
  if Salario_Bruto <= Mestre[0]:
    Salario_tabelado = Mestre[0]
    print('Você será classificado em M2 (Mestrado Nível 2) e seu salário tabelado será de R${:.2f}.'.format(Salario_tabelado))
  else:
    while Salario_Bruto <= Mestre[i]:
      Salario_tabelado = Mestre[i-1]
      M = M - 1
      i = i - 1
    print()
    print('Você será classificado em M{} (Mestrado Nível {}) e seu salário tabelado será de R${:.2f}.'.format(M, M, Salario_tabelado))

   
#Calculo de Salário tabelado para doutores
if titulacao == 3:
  if Salario_Bruto <= Dout[0]:
    Salario_tabelado = Dout[0]
    print('Você será classificado em D2 (Doutorado Nível 2) e seu salário tabelado será de R${:.2f}.'.format(Dout[0]))
  else:
    while Salario_Bruto <= Dout[i]:
      Salario_tabelado = Dout[i-1]
      D = D - 1
      i = i - 1
    print()
    print('Você será classificado em D{} (Doutorado Nível {}) e seu salário tabelado será de R${:.2f}.'.format(D, D, Salario_tabelado))


#Calculando abono e Salario Bruto Final na nova carreira
Sal_tab = Salario_tabelado
if Salario_Bruto > Sal_tab:
    Comp_sal = Salario_Bruto - Sal_tab
    Salario_Bruto_novo = Sal_tab + Comp_sal
else:
    Comp_sal = 0.00
    Salario_Bruto_novo = Sal_tab

print('**'*50)
print('Você receberá uma complementação salarial no valor de R${:.2f}. Assim, seu salário bruto na nova carreira sem gratificação da PEI será de R${:.2f} e com gratificação (GDPI) será de R${:.2f}.'.format(Comp_sal, Salario_Bruto_novo, Salario_Bruto_novo + 2000.00))





