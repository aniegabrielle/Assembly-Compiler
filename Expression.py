from Operator import *
from Variable import *
from Register import *
from Literal import *

FUNCTIONS = []

table = {
    "LER": lambda args: f"INT 1 {args[0]}",
    "IF": lambda args: f"CMP {args[0]}, {args[1]}\nJFALSE {args[2]}",
    "END_IF": lambda args: f"JUMP {args[0]}",
    "ESCREVER": lambda args: f"INT 2, {args[0]}"
}

def getIndex(object):
    return object[0]

def breakTokens(exp):
    tokens = exp.split(" ")

    # Retirando os tokens 'vazios'
    tokens = [token for token in tokens if token != ""]

    # Se o número de tokens é par, então ==> ERRO
    if len(tokens) % 2 == 0:
        raise Exception("Expressão Inválida: " + exp)

    return tokens

def analiseLexicaDoToken(token):
    # Verifico se o token corresponde a uma variável
    if token in VARIABLES:
        return Variable(token)
    # Verifico se o token corresponde a um operador
    if token in OPERATORS:
        return Operator(token)
    # Verifico se o token corresponde a uma literal
    if token.isdigit():
        return Literal(token)
    # Verifico se o token corresponde a um registrador
    if token in REGISTERS:
        return Register(token)
    if token in table:
        return token
    if token in map(getIndex,FUNCTIONS):
        return token
    else:
        raise Exception("ERRO LÉXICO: O token " + token + " é inválido na expressão")

def analiseLexica(tokens):
    arrayTokens = []
    for token in tokens:
        arrayTokens.append(analiseLexicaDoToken(token))

    return arrayTokens

def processarExpressao(expression, compile_fn):
    line = expression.split("(")[0].strip()

    # Quebra a Expressão em Tokens de Strings
    tokens = breakTokens(line)

    # Transforma o array de strings em array de tokens classificados
    tokens = analiseLexica(tokens)

    code = ""
    # Processando os operadores presentes na expressão
    while len(tokens) > 1:
        # Descobrindo qual é o operador com maior precedência
        posMaiorPrecedencia = None
        for token in tokens:
            if token in map(getIndex,FUNCTIONS):
                parameters = expression.split(")")[0].split("(")[1].strip().split(",")

                func = None
                for function, funcParameters in FUNCTIONS:
                    if ( function == token):
                        if len(funcParameters[0]) != len(parameters):
                            raise Exception(f"ERRO SINTÁTICO: Quantidade de parâmetros da função {token} inválidos")

                        for parameter in parameters:
                            index = parameters.index(parameter)
                            code += compile_fn(f"VAR {funcParameters[0][index]}") + "\n"
                            code += f"MOVE {funcParameters[0][index]}, {parameter.strip()}\n"
                code += f"JUMP {token}\n"

                reg = getFreeRegister()
                reg.setUsed(True)

                code += f"fim_{function}: MOVE {reg.toString()}, {funcParameters[1]}\n"
                tokens[tokens.index(token)] = reg.toString()
            elif token in table:
                if ( token == "LER"):
                    reg = getFreeRegister()
                    reg.setUsed(True)
                    code += compile_fn(f"{token} {reg.toString()}" ) + "\n"
                    tokens[tokens.index(token)] = reg.toString()
            elif isinstance(token, Operator):
                if posMaiorPrecedencia is None:
                    posMaiorPrecedencia = tokens.index(token)
                elif token.hasHighestPrecedence(tokens[posMaiorPrecedencia]):
                    posMaiorPrecedencia = tokens.index(token)

        # Se não encontrei operador...
        if posMaiorPrecedencia is None:
            raise Exception("ERRO SINTÁTICO: Expressão inválida, pois não encontrei operador: " + expressao)

        tokenOperator = tokens[posMaiorPrecedencia]

        # Se o operador está em uma posição inválida
        if posMaiorPrecedencia % 2 == 0:
            raise Exception("Operador em posição inválida!" + str(tokens[posMaiorPrecedencia]))

        # Testando os operandos
        tokenEsq = tokens[posMaiorPrecedencia - 1]
        if isinstance(tokenEsq, Operator):
            raise Exception("Operando inválido! " + str(tokenEsq))

        tokenDir = tokens[posMaiorPrecedencia + 1]
        if isinstance(tokenDir, Operator):
            raise Exception("Operando inválido! " + str(tokenDir))

        # Escreve operador
        code += tokenOperator.write(tokenEsq, tokenDir) + "\n"
        # Coloco no lugar um token Registrador
        tokens[posMaiorPrecedencia - 1] = tokenOperator.getLeftRegister()

        # Retiro os tokens antigos
        tokens.remove(tokens[posMaiorPrecedencia])
        tokens.remove(tokens[posMaiorPrecedencia])

    # Compila o código restante
    for token in tokens:
        if isinstance(token, Variable):
            code += compile_fn(token.getName()) + "\n"

    return code
