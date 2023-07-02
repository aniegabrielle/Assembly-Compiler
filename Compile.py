from Operator import *
from Variable import *
from Register import *
from Literal import *
from Expression import *

memoryFreePosition = 0
lastFunction = ""

def processFunction(args):
    global lastFunction

    code = ""
    if args[1] == ":":
        code = args[0] + args[1] + " "

        if len(args) > 2:
            param_code = ""
            for arg in args[2:]:
                param_code = param_code + arg

            params = param_code.split(",")
            for param in params:
                VARIABLES.append(param)

        function = []
        function.append( params )
        FUNCTIONS.append([args[0], function] )

        lastFunction = args[0]
    else:
        raise Exception(f"Declaração da função inválida: {args[0]}")

    return code

def translate_line(line):
    global memoryFreePosition
    global lastFunction

    if line.strip() == "":
        return ""
    tokens = line.split()
    command = tokens[0]
    args = tokens[1:]
    if command == "VAR":
        VARIABLES.append(args[0])
        memoryFreePosition += 1
        return f"VAR {args[0]}, {memoryFreePosition}\n"
    elif command == "RETURN":
        code = ""
        code += f"JUMP fim_{lastFunction}\n"
        for function, funcParameters in FUNCTIONS:
            if ( function == lastFunction):
                funcParameters.append(args[0])
        return code
    elif command == "END":
        return ""
    elif command == "FUNCTION":
        return processFunction(args)
    elif command in table:
        return table[command](args)
    elif "=" in line:
        expressao_aritmetica = line.split("(")[0].strip()
        tokens = breakTokens(expressao_aritmetica)
        tokens = analiseLexica(tokens)
        code = ""
        for token in tokens:
            if isinstance(token, Variable):
                code += f"MOVE {token}, {get_register()}\n"
                code += f"MOVE {get_register()}, {args[0]}\n"
            elif isinstance(token, Operator):
                code += token.write(get_register(), args[1])
                code += f"MOVE {token.getLeftRegister()}, {args[0]}\n"
        return code
    else:
        raise Exception(f"Comando desconhecido: {command}")

def compile(expression):
    lines = expression.strip().split("\n")
    assembly_code = ""
    for line in lines:
        assembly_code += translate_line(line) + "\n"

    return assembly_code.strip()
