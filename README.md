# Assembly-Compiler
Trabalho de Linguagens de Programação

A linguagem para a qual iremos processar tem
as seguintes especificações:

1) Todas as variáveis são inteiras.

2) A linguagem permitirá a declaração de variáveis (uma variável por linha) no formato:

VAR <nome da variável>

3) Todos os identificadores só poderão usar letras minúsculas ou maiúsculas, sendo a linguagem case sensitive.

4) Os operadores presentes na linguagem são os seguintes: =, +, -, *, /, == (igual), <, >, && (and) e || (or)

5) Os comandos da linguagens são os seguintes:

WHILE (expressão booleana)
     <INSTRUÇÕES>
END_WHILE

IF (expressão booleana)
    <INSTRUÇÕES>
END_IF

6) A linguagem permite a definição de funções que retornam ao final valores inteiros. Elas devem ser declaradas antes do seu uso e não será necessário implementar uma stack para o seu funcionamento (i.e., as variáveis
terão posições estáticas)

FUNCTION <nome> : <param1>, <param2> ...
     <INSTRUÇÕES>
     RETURN <variável> ou <literal>
END_FUNCTION

7) Para a leitura e escrita, a linguagem tem as funções:

<variável> = LER 
ESCREVER <variável>


Exemplo de Código
===============


FUNCTION SOMAR : a, b
     VAR resultado
      resultado = a + b
      RETURN resultado
END

VAR x
VAR y
x = LER
y = LER
x = SOMAR(x,y)
ESCREVER x
