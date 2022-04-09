nota=int(input("Ingrese cantidad de notas de los estudiantes: "))
vec=[]
n=0

for i in range(1,nota+1):
    nota=int(input("nota: "))
    n=n+nota
    vec.append(nota)
    