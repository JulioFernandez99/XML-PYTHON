import xml.etree.ElementTree as ET
import pandas as pd

xml_data = open('pr.xml', 'r',).read()  # Read file
root = ET.XML(xml_data,)  # Parse XML

data = []
cols = []
for i, child in enumerate(root):
    data.append([subchild.text for subchild in child])
    cols.append(child.tag)

df = pd.DataFrame(data).T  # Write in DF and transpose it
df.columns = cols  # Update column names
print("")

print("---------------------------Datos archivo XML---------------------------")
print(df)
codigo=list(df["codigo"])
alumnos=list(df["Alumnos"])
promedio=list(df["Promedio"])
print("-----------------------------------------------------------------------")

a=[]
b=[]
c=[]

def burbuja(A,B,C):
    global a,b,c
    for i in range(1,len(A)):
        for j in range(0,len(A)-i):
            if(A[j+1] < A[j]):
                aux=A[j]
                auxA=B[j]
                A[j]=A[j+1]
                A[j+1]=aux

                B[j] = B[j + 1]
                B[j + 1] = auxA

                a=A
                b=B

        for i in range(1, len(C)):
            for j in range(0, len(C) - i):
                if (C[j + 1] < C[j]):
                    aux = C[j];
                    C[j] = C[j + 1];
                    C[j + 1] = aux;
                    c=C


for i in range(len(codigo)):
    codigo[i]=int(codigo[i])

for i in range(len(promedio)):
    promedio[i]=int(promedio[i])

print("")
print("--------------------------Datos Desorndenados--------------------------")
print(f"Codigos: {codigo}")
print(f"Alumnos: {alumnos}")
print(f"Promedios: {promedio}")
print("-----------------------------------------------------------------------")

burbuja(codigo,alumnos,promedio)


print("")
print("----------------------------Datos Orndenados----------------------------")
print(f"Codigos: {a}")
print(f"Alumnos: {b}")
print(f"Promedios: {c}")
print("-----------------------------------------------------------------------")
