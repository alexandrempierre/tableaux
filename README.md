# tableaux

Implementação do Tableux para Lógica Clássica de Primeira Ordem.

Por questão de conforto em relação ao material e ao código que foi lido para escrever o programa, ele está em Inglês assim como toda a interação do programa com o usuário.

O arquivo a ser executado deve ser o main.py que já está pronto para execução por linha de comando no Linux (a menos de um chmod) (a main.py tem shebang).

## Tecnologias

* Arch Linux

### Dependências:

* Python 3.1.6
* Biblioteca `nltk`

	O `nltk` foi escolhido pelo seu _parser_. Mas por mais completo que seja o parser do `nltk`, apenas uma parte dele vai ser usado. As únicas operações reconhecidas nesse programa são conjunção, disjunção, negação unária, implicação e os quantificadores existencial e universal. Essas operações podem ser feitas entre fórmulas, ou seja, podem aparecer umas dentro das outras (de uma forma um tanto específica). No código do programa não há menção a palavra "literal", optei por seguir o padrão e chamar de átomo negado ou `n_atom` no contexto.

	O parser do nltk reconhece outras operações como o "se e somente se", no caso de operações como essa o comportamento do Tableaux não está garantido, pois não foi feito tendo essa operação em mente, nem nenhuma outra que não tenha sido citada no parágrafo anterior.

## Como utilizar

Após instalar o `Python 3` e a biblioteca `nltk`, basta atribuir ao seu usuário a permissão de execução sobre o arquivo `main.py` e executá-lo.

	$ chmod a+x main.py 	// permite que qualquer usuário execute o arquivo

Há duas formas possíveis de usar o `tableaux`: 

* Passando um arquivo (caminho relativo ou completo) como argumento de linha de comando para ao rodar o programa:
	
	```
	$ ./main.py <nome do arquivo>
	```

* Passando os tableauxs a serem resolvidos para o programa durante sua execução
	
	```
	$ ./main.py
	```

	Nesse caso o programa tem textos de orientação ao usuário pedindo a informação necessária a cada passo. Esses textos foram escritos em Inglês.

### Formato da Entrada

1. número de tablôs a serem resolvidos
2. Pergunta
3. número de afirmações no BD
4. BD (com um "Enter" ao final de cada afirmação do BD) (este passo se repete de acordo com o número digitado no passo 3)

As partes 2, 3 e 4 se repetirão de acordo com o valor digitado no passo 1.

#### Exemplo de entrada válida

```
2
A(a)
1
A(a)
exists x.A(x)
1
all x.A(x) | exists x.A(x)
```

Obs: no arquivo de entrada não há problema em colocar quebras de linha entre um tableaux e outro, mas na entrada direta há, em caso de dúvida quebras de linha significam que algo terminou (uma afirmação, por exemplo) e não deve haver quebras de linha que resultem em linhas vazias.
