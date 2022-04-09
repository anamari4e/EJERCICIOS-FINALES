print("Calcula multiplos digitados por el usuario")
valorn=int(input("Digita numero para sacar el multiplo: "))
valorm=int(input("Digitanumero para la cantidad a sacar del multiplo: "))

def generar_multiplos(valorn,valorm):
    return [valorn * i for i in range(1,valorm + 1)]
print(generar_multiplos(valorn,valorm))
