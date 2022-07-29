from Funcionalidad.BiblotecaHexadecimal import Hexadecimal, Hexadecimal2
#from BiblotecaHexadecimal import Hexadecimal, Hexadecimal2


def BinDec(cadena):
    PotenciaBinaria = 0
    conta = 0
    cadena = cadena[::-1]
    for i in cadena:
        if i == "1":
            PotenciaBinaria = (2**conta)+PotenciaBinaria
        elif i == "0":
            pass
        else:
            PotenciaBinaria = 0
            break
        conta += 1
    return PotenciaBinaria


def BinOct(cadena):
    ContResu = ""
    Resultado = 0
    conta = 0
    cadena = cadena[::-1]
    if cadena == "":
        ContResu = "0"
        return ContResu
    while(len(cadena) % 3 != 0):
        cadena += "0"

    for i in cadena:
        if conta == 3:
            Resultado = 0
            conta = 0
        if i == "1":
            Resultado += (2**conta)
            if conta == 2:
                ContResu += str(Resultado)
        elif i == "0":
            if conta == 2:
                ContResu += str(Resultado)
            pass
        else:
            ContResu = "0"
            return ContResu

        conta += 1
    ContResu = ContResu[::-1]
    return ContResu


def BinHexa(cadena):
    ContResu = ""
    Resultado = 0
    conta = 0
    cadena = cadena[::-1]
    if cadena == "":
        ContResu = "0"
        return ContResu
    while(len(cadena) % 4 != 0):
        cadena += "0"

    for i in cadena:
        if conta == 4:
            Resultado = 0
            conta = 0
        if i == "1":
            Resultado += (2**conta)
            if conta == 3:
                if Resultado > 9:
                    ContResu += Hexadecimal(Resultado)
                else:
                    ContResu += str(Resultado)
        elif i == "0":
            if conta == 3:
                if Resultado > 9:
                    ContResu += Hexadecimal(Resultado)
                else:
                    ContResu += str(Resultado)
            pass
        else:
            ContResu = "0"
            return ContResu

        conta += 1
    ContResu = ContResu[::-1]
    return ContResu


def DeciBin(dato):
    total = ""
    if dato == "":
        total = "0"
        return total
    else:
        dato = int(dato)
    while(dato != 0):
        total += str(dato % 2)
        dato = dato//2
    return total


def DecOct(dato):
    if dato == "":
        total = "0"
        return total
    else:
        dato = int(dato)
    dato = DeciBin(dato)
    dato = dato[::-1]  # correcion
    dato = BinOct(dato)
    return dato


def DecHexa(dato):
    if dato == "":
        total = "0"
        return total
    else:
        dato = int(dato)
    dato = DeciBin(dato)
    dato = dato[::-1]  # correcion
    dato = BinHexa(dato)
    return dato


def OctBin(dato):
    if dato == "":
        total = "0"
        return total
    total = ""
    for i in dato:
        total += DeciBin(i)
        while(len(total) % 3 != 0):
            total += "0"
        pass
    total = total[::-1]
    return total


def OctDeci(dato):
    if dato == "":
        total = "0"
        return total
    dato = OctBin(dato)
    dato = BinDec(dato)
    return str(dato)


def OctHexa(dato):
    if dato == "":
        total = "0"
        return total
    dato = OctBin(dato)
    dato = BinHexa(dato)
    return dato


def HexaBin(dato):
    total = ""
    if dato == "":
        total = "0"
        return total
    for i in dato:
        if Hexadecimal2(i):
            total += str(DeciBin(Hexadecimal2(i)))
            while(len(total) % 4 != 0):
                total += "0"
        else:
            total += str(DeciBin(i))
            while(len(total) % 4 != 0):
                total += "0"
            pass
        pass
    total = total[::-1]
    return total


def HexaOct(dato):
    if dato == "":
        total = "0"
        return total
    dato = HexaBin(dato)
    dato = BinOct(dato)
    return dato


def HexaDeci(dato):
    if dato == "":
        total = "0"
        return total
    dato = HexaBin(dato)
    dato = str(BinDec(dato))
    return dato
