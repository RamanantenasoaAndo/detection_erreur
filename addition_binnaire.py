a = int(input("premier binaire : "))
b = int(input("deuxième binaire : "))
 
retenue = 0
resultat = 0
position = 0
 
while a > 0 or b > 0 or retenue > 0:
    chiffre_a = a % 10
    chiffre_b = b % 10
    a = a // 10
    b = b // 10
    somme = chiffre_a + chiffre_b + retenue
    retenue = somme // 2
    resultat += (somme % 2) * 10**position
    position += 1
 
print(resultat)

