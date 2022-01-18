def decobasic(entrada_bin, entrada_bin2):
    stringbin = str(entrada_bin)
    stringbin2 = str(entrada_bin2)
    lista_bin = list(stringbin2)
    juntar = stringbin + lista_bin[0] + lista_bin[1]

    return juntar


def Deco2Basic(entrada_bin, entrada_bin2):
    stringbin = str(entrada_bin)
    stringbin2 = str(entrada_bin2)
    lista_bin = list(stringbin)
    lista_bin2 = list(stringbin2)
    juntar = lista_bin[2] + lista_bin[3] + lista_bin2[0] + lista_bin2[1] + lista_bin2[2]
    return juntar    


def Deco3Basic(entrada_bin, entrada_bin2):
    stringbin = str(entrada_bin)
    stringbin2 = str(entrada_bin2)
    lista_bin = list(stringbin)
    lista_bin2 = list(stringbin2)
    juntar = lista_bin[3] + lista_bin2[0] + lista_bin2[1] + lista_bin2[2] + lista_bin2[3]
    return juntar


def Deco4Basic(entrada_bin, entrada_bin2):
    stringbin = str(entrada_bin)
    stringbin2 = str(entrada_bin2)
    lista_bin = list(stringbin)
    lista_bin2 = list(stringbin2)
    juntar = lista_bin[0] + lista_bin[1] + lista_bin[2] + lista_bin[3] + lista_bin2[0]
    return juntar


def Deco5Basic(entrada_bin, entrada_bin2):
    stringbin = str(entrada_bin)
    stringbin2 = str(entrada_bin2)
    lista_bin = list(stringbin)
    lista_bin2 = list(stringbin2)
    juntar = lista_bin[1] + lista_bin[2] + lista_bin[3] + lista_bin2[0] + lista_bin2[1]
    return juntar


def Deco6Basic(entrada_bin, entrada_bin2):
    stringbin = str(entrada_bin)
    stringbin2 = str(entrada_bin2)
    lista_bin = list(stringbin)
    lista_bin2 = list(stringbin2)
    juntar = lista_bin[2] + lista_bin[3] + stringbin2
    return juntar


def DecoADDI(entrada_bin, entrada_bin2):
    stringbin = str(entrada_bin)
    stringbin2 = str(entrada_bin2)
    lista_bin = list(stringbin)
    lista_bin2 = list(stringbin2)

    juntar = lista_bin[2] + lista_bin[3] + lista_bin2[0] + lista_bin2[1] + lista_bin2[2]
    return juntar


def DecoADDI2(entrada_bin, entrada_bin2):
    stringbin = str(entrada_bin)
    stringbin2 = str(entrada_bin2)
    lista_bin = list(stringbin)
    lista_bin2 = list(stringbin2)

    juntar = lista_bin[3] +lista_bin2[0] + lista_bin2[1] + lista_bin2[2] + lista_bin2[3]
    return juntar


def DecoADDI3(entrada_bin, entrada_bin2, entrada_bin3, entrada_bin4):
    stringbin = str(entrada_bin)
    stringbin2 = str(entrada_bin2)
    stringbin3 = str(entrada_bin3)
    stringbin4 = str(entrada_bin4)

    juntar = stringbin + stringbin2 + stringbin3 + stringbin4
    return juntar    


def DecoDiv(entrada_bin, entrada_bin2):
    stringbin = str(entrada_bin)
    stringbin2 = str(entrada_bin2)
    lista_bin = list(stringbin)
    lista_bin2 = list(stringbin2)
    juntar = lista_bin[2] + lista_bin[3] + lista_bin2[0] + lista_bin2[1] + lista_bin2[2]
    return juntar    


def Deco2Div(entrada_bin, entrada_bin2):
    stringbin = str(entrada_bin)
    stringbin2 = str(entrada_bin2)
    lista_bin = list(stringbin)
    lista_bin2 = list(stringbin2)
    juntar = lista_bin[3] + lista_bin[0] + lista_bin2[1] + lista_bin2[2] + lista_bin2[3]
    return juntar


def find_letter(letter, lst):
    return any(letter in word for word in lst)


def converterbin(entrada):
    checkup = entrada.isalpha()
    if checkup:
        valor_hex_int = int(entrada, base=16)

        convint = int(valor_hex_int)
        convbin = bin(convint).replace("0b", "")
        formatnum = "{:0>4}".format(convbin)
        return formatnum
    else:
        convint = int(entrada)
        convbin = bin(convint).replace("0b", "")
        formatnum = "{:0>4}".format(convbin)
        return formatnum


def f(conteudo, contador):
    contador_linha = 0
    contador_func = 1
    for valor in conteudo:
        if "0x" in valor:
            splitar = valor.split("0x")
            segVal = splitar[1]
            lista_valor = list(segVal)
        else:
            lista_valor = list(valor)

        valor1 = converterbin(lista_valor[0])
        valor2 = converterbin(lista_valor[1])
        valor3 = converterbin(lista_valor[2])
        valor4 = converterbin(lista_valor[3])
        valor5 = converterbin(lista_valor[4])
        valor6 = converterbin(lista_valor[5])
        valor7 = converterbin(lista_valor[6])
        valor8 = converterbin(lista_valor[7])

        indexar = contador
        contador += 1
        transcricao(valor1, valor2, valor3, valor4, valor5, valor6, valor7, valor8, conteudo, indexar)
    tamanho = len(conteudo)
    for linha in conteudo:
        if linha.find("beq") == 0:
            y = linha.split(",")
            y = int(y[2].replace(" ", ""))
            a = conteudo.index(linha)

            if y < 0:
                z = conteudo[contador_linha].split(",")
                conteudo[contador_linha] = f"{z[0]}{z[1]}, func{contador_func}"
                x = (conteudo.index(conteudo[contador_linha]))
                x = (a + y)
                conteudo[x] = f"func{contador_func}: {conteudo[x]}"

                contador_func += 1
        contador_linha += 1


def transcricao(valor1, valor2, valor3, valor4, valor5, valor6, valor7, valor8, conteudo, indexar):
    match decobasic(valor1, valor2):
        case "000000":
            transcricao_000000(valor2, valor3, valor4, valor5, valor6, valor7, valor8, conteudo, indexar)

        case "001000":
            rs = int(DecoADDI(valor2, valor3), 2)
            rt = int(DecoADDI2(valor3, valor4), 2)
            imediato = int(DecoADDI3(valor5, valor6, valor7, valor8), 2)
            if imediato >= 65535:
                imediato = imediato - 65536
            conteudo[indexar] = f"addi ${rt}, ${rs}, {imediato}"

            return conteudo[indexar]
        case "000100":
            rs = int(Deco2Basic(valor2, valor3), 2)
            rt = int(Deco3Basic(valor3, valor4), 2)
            offset = int((valor5 + valor6 + valor7 + valor8), 2)
            if offset < 0:
                offset = (abs(offset) - 65536) + 1
            else:
                offset = offset - 65536

            conteudo[indexar] = f"beq ${rs}, {rt}, {offset}"

            return conteudo[indexar]
        case "000010":
            valor2 = list(valor2)
            instr_index = valor2[2] + valor2[3] + valor3 + valor4 + valor5 + valor6 + valor7 + valor8

        case _:
            return 0


def transcricao_000000(valor2, valor3, valor4, valor5, valor6, valor7, valor8, conteudo, indexar):
    match Deco6Basic(valor7, valor8):
        case "100000":

            rs = int(Deco2Basic(valor2, valor3), 2)
            rt = int(Deco3Basic(valor3, valor4), 2)
            rd = int(Deco4Basic(valor5, valor6), 2)
            conteudo[indexar] = f"add ${rd}, ${rs}, ${rt}"

            return conteudo[indexar]

        case "100010":

            rs = int(Deco2Basic(valor2, valor3), 2)
            rt = int(Deco3Basic(valor3, valor4), 2)
            rd = int(Deco4Basic(valor5, valor6), 2)
            conteudo[indexar] = f"sub ${rd}, ${rs}, ${rt}"

            return conteudo[indexar]

        case "100101":
            rs = int(Deco2Basic(valor2, valor3), 2)
            rt = int(Deco3Basic(valor3, valor4), 2)
            rd = int(Deco4Basic(valor5, valor6), 2)
            conteudo[indexar] = f"or ${rd}, ${rs}, ${rt}"

            return conteudo[indexar]

        case "100100":
            rs = int(Deco2Basic(valor2, valor3), 2)
            rt = int(Deco3Basic(valor3, valor4), 2)
            rd = int(Deco4Basic(valor5, valor6), 2)
            conteudo[indexar] = f"and ${rd}, ${rs}, ${rt}"

            return conteudo[indexar]

        case "100111":
            rs = int(Deco2Basic(valor2, valor3), 2)
            rt = int(Deco3Basic(valor3, valor4), 2)
            rd = int(Deco4Basic(valor5, valor6), 2)
            conteudo[indexar] = f"nor ${rd}, ${rs}, ${rt}"

            return conteudo[indexar]

        case "100110":
            rs = int(Deco2Basic(valor2, valor3), 2)
            rt = int(Deco3Basic(valor3, valor4), 2)
            rd = int(Deco4Basic(valor5, valor6), 2)
            conteudo[indexar] = f"xor ${rd}, ${rs}, ${rt}"

            return conteudo[indexar]
        case "011010":
            rs = int(DecoDiv(valor2, valor3), 2)
            rt = int(Deco2Div(valor4, valor5), 2)

            conteudo[indexar] = f"div ${rs}, ${rt}"

            return conteudo[indexar]
        case "011000":
            rs = int(DecoDiv(valor2, valor3), 2)
            rt = int(Deco2Div(valor3, valor4), 2)

            conteudo[indexar] = f"mult ${rs}, ${rt}"

            return conteudo[indexar]
        case "101010":
            rs = int(Deco2Basic(valor2, valor3), 2)
            rt = int(Deco3Basic(valor3, valor4), 2)
            rd = int(Deco4Basic(valor5, valor6), 2)
            conteudo[indexar] = f"slt ${rd}, ${rs}, ${rt}"

            return conteudo[indexar]
        case "000000":
            rd = int(Deco4Basic(valor5, valor6), 2)
            rt = int(Deco3Basic(valor3, valor4), 2)
            sa = int(Deco5Basic(valor6, valor7), 2)
            conteudo[indexar] = f"sll ${rd}, ${rt}, {sa}"

            return conteudo[indexar]
        case "000010":
            rd = int(Deco4Basic(valor5, valor6), 2)
            rt = int(Deco3Basic(valor3, valor4), 2)
            sa = int(Deco5Basic(valor6, valor7), 2)
            conteudo[indexar] = f"srl ${rd}, ${rt}, {sa}"

            return conteudo[indexar]
        case "000011":
            rd = int(Deco4Basic(valor5, valor6), 2)
            rt = int(Deco3Basic(valor3, valor4), 2)
            sa = int(Deco5Basic(valor6, valor7), 2)
            conteudo[indexar] = f"sra ${rd}, ${rt}, {sa}"

            return conteudo[indexar]
        case _:
            return 0


def operar(valor, registradores):
    auxvalor = valor.split(" ")
    comando = auxvalor[0]

    match comando:
        case "add":
            reg01 = int((auxvalor[1].replace("$", "")).replace(",", ""))
            reg02 = int((auxvalor[2].replace("$", "")).replace(",", ""))
            reg03 = int((auxvalor[3].replace("$", "")).replace(",", ""))

            registradores[reg01 - 1] = registradores[reg02 - 1] + registradores[reg03 - 1]

            return registradores[reg01 - 1]

        case "addi":
            reg01 = int((auxvalor[1].replace("$", "")).replace(",", ""))
            reg02 = int((auxvalor[2].replace("$", "")).replace(",", ""))
            valor = int((auxvalor[3]).replace(",", ""))

            registradores[reg01 - 1] = registradores[reg02 - 1] + valor

            return registradores[reg01 - 1]

        case "sub":
            reg01 = int((auxvalor[1].replace("$", "")).replace(",", ""))
            reg02 = int((auxvalor[2].replace("$", "")).replace(",", ""))
            reg03 = int((auxvalor[3].replace("$", "")).replace(",", ""))

            registradores[reg01 - 1] = registradores[reg02 - 1] - registradores[reg03 - 1]

            return registradores[reg01 - 1]

        case _:
            return 0
