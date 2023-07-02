from Compile import compile
from Expression import processarExpressao

# Exemplo de código A
codigo_a = """
FUNCTION SOMAR : a, b
    VAR resultado
    resultado = a + b * 10 - 5
    RETURN resultado
END

VAR x
VAR y
x = LER
y = LER
x = SOMAR(x, y)
ESCREVER x
"""

# Quebra o código em linhas
lines = codigo_a.strip().split("\n")

# Lista para armazenar as expressões a serem processadas
expressions = []

assembly_code = "JUMP main \n"

posLastEnd = -1
for line in lines:
    if line == "END":
        posLastEnd = lines.index(line)+1

# Percorre as linhas para identificar as expressões aritméticas
for line in lines:
    if lines.index(line) == posLastEnd:
        assembly_code += "main:"

    if "=" in line:
        # Processa as expressões aritméticas:
        assembly_code += processarExpressao(line.strip(), compile)
    else:
        # Compila o código A restante
        assembly_code += compile(line) + "\n"

# Imprime o código assembly resultante
print(assembly_code)
