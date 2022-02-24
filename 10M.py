import random as rd
palabras = ["pollos","cajas","mama","papas","ligas"]
indice=rd.randint(0,len(palabras)-1)# 0 1 2 3 4 
pal=palabras[indice]
print(indice,pal)
palMayus=pal.upper()
letraPri=palMayus[0]
letraUlt=palMayus[-1]
n=len(palMayus)-2
subGuio=n * " _ "
pista= letraPri + subGuio + letraUlt
print(pista)
palUser=input("Adivine la palabra: ").upper()
cond= palUser == palMayus
print("¿Gano? ",cond)