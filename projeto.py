# Memória e registradores
memoria = [0] * 64
R0 = R1 = R2 = 0
PC = 0
instrucoes = []

def carregar_programa(nome_arquivo):
    global instrucoes
    with open(nome_arquivo, "r") as f:
        for linha in f:
            linha = linha.strip()
            if linha == "" or linha.startswith("#"):
                continue
            if "#" in linha:
                linha = linha.split("#")[0].strip()
            instrucoes.append(linha)

def executar(instrucao):
    global R0, R1, R2, PC, memoria

    partes = instrucao.split()
    op = partes[0]

    try:
        if op == "LOAD":
            reg, val = instrucao.split(" ", 1)[1].split(",")
            reg = reg.strip()
            val = val.strip()

            if val.startswith("[") and val.endswith("]"):
                endereco = int(val[1:-1])
                val = memoria[endereco]
            else:
                val = int(val)

            if reg == "R0":
                R0 = val
            elif reg == "R1":
                R1 = val
            elif reg == "R2":
                R2 = val

        elif op == "STORE":
            endereco, reg = instrucao.split(" ", 1)[1].split(",")
            endereco = int(endereco.strip()[1:-1])
            reg = reg.strip()

            if reg == "R0":
                memoria[endereco] = R0
            elif reg == "R1":
                memoria[endereco] = R1
            elif reg == "R2":
                memoria[endereco] = R2

        elif op == "ADD":
            reg1, reg2 = instrucao.split(" ", 1)[1].split(",")
            reg1 = reg1.strip()
            reg2 = reg2.strip()

            if reg1 == "R0":
                if reg2 == "R1": R0 += R1
                elif reg2 == "R2": R0 += R2
            elif reg1 == "R1":
                if reg2 == "R0": R1 += R0
                elif reg2 == "R2": R1 += R2
            elif reg1 == "R2":
                if reg2 == "R0": R2 += R0
                elif reg2 == "R1": R2 += R1

        elif op == "HLT":
            return False  # Fim do programa
    except Exception as e:
        print(f"Erro na instrução {op}: {instrucao} - {e}")
    
    return True

def mostrar_estado():
    print(f"PC: {PC} | R0: {R0}, R1: {R1}, R2: {R2} | Mem[30]: {memoria[30]}")

def main():
    global PC
    carregar_programa("exemplo.txt")

    while PC < len(instrucoes):
        if not executar(instrucoes[PC]):
            break
        mostrar_estado()
        PC += 1

main()
         