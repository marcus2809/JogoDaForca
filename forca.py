import random

lista = ['petcomputacao', 'protelar', 'prescrever', 'proscrever', 'paralelepipedo', 'preeminente', 'proeminente', 'preposicao', 'proposicao', 'prolatar']
lista_letras = []
sorteio = random.choice(lista)
tentativas = 3
ganhou = False

palavra = ['_']*len(sorteio)

print('Bem vindo ao jogo da forca, a palavra é a seguinte:')

while tentativas > 0 and not ganhou:
	print(palavra)

	letra = input('Digita a letra desejada: ')

	while (not letra.isalpha()) or len(letra) > 1:
		print('Insira apenas uma LETRA, por favor')
		letra = input('Digita a letra desejada: ')

	while letra in lista_letras:
		print('Letra já utilizada, tente novamente.')
		letra = input('Digita a letra desejada: ')

	if letra in sorteio:
		for contador in range(0, len(sorteio)):
			if letra == sorteio[contador]:
				palavra[contador] = letra
		print('Essa letra pertence à palavra')

	else:
		tentativas -= 1
		print(palavra)
		print('Essa letra não pertence à palavra')
		print('Tentativas restantes:', tentativas)

	lista_letras.append(letra)

	if tentativas == 0:
		print('Você perdeu, a palavra era:', sorteio)

	if '_' not in palavra:
		ganhou = True
		print(palavra)
		print('Você ganhou!!!')







