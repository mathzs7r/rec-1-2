# COPIE E COLE ESTE ENUNCIADO NO TERMINAL EM UM ARQUIVO .py. 
# Para executar no terminal use "python3 nome_arquivo.py"
# Use somente o Classroom e o GitHub. Uso do Google ou qualquer tipo de IA = zero!
# Link GitHub professor: https://github.com/profpatrickoli/1TRI-DesSistemas
# 1) (0,5 p) Crie variáveis para armazenar seu nome, nota da prova escrita, série e turma. Após isso, mostre no terminal uma mensagem personalizada se apresentando.

nome = "matheus"
nota = 2.3
serie = "3º"
turma = "DS C"
media = 1.8

print("Olá, meu nome é", nome , "eu tirei", nota, "estou no ", serie,"ano ,turma ",turma)
# 2) (0,5 p) Crie uma lista com 3 atividades que você gosta de fazer no final de semana.

atividades = ["dormir","comer","existir"]
# 3) (1,0 p) Crie uma condição que verifica se sua nota da prova é maior que a média 1,8. 

if nota >= 1.8:
    print("Parabéns não fez mais que sua obrigação")
else:
    print("HAHAHAHAH seu perdedor")
# 4) (1,0 p) Crie uma função mostra no terminal a quantidade de litros de água que devem ser consumidos diariamente por uma pessoa. Depois execute a função colocando um peso como parâmetro.
# Para calcular, siga a fórmula: qtd_litros = 0,035 * peso.

peso = 68

def agua ():
    qtd_litros = 0.035 * peso 
    print("você deve beber",qtd_litros,"por dia ")
agua ()

# 5) (1,0 p) Crie um código que verifica se "estudar" existe na lista criada da questão 2. Use o laço de repetição que preferir.
# Lista baseada no contexto da questão
atividades = ["trabalhar", "descansar", "treinar"]

encontrado = False
for item in atividades:
    if item == "estudar":
        encontrado = True
        break 

if encontrado:
    print("Sim tem estudar ai!")
else:
    print("Estudar coisa de beta, então não esta na lista!!!!!!!")


# 6) (1,0 p) Crie um laço de repetição que conta de 1 a 128, mas ao invés de somar 1 no contador, multiplique-o por 2.
contador = 1
while (contador <= 128):
    print(contador)
    contador = contador * 2