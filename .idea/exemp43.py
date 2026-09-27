#encryption program
import random
import string
from pickletools import string1

#personagens = string.punctuation + string.digits + string.ascii_letters
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

#personagens = string.whitespace + string.punctuation + string.digits + string.ascii_letters
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

personagens = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
#!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

print(personagens)

personagens = list(personagens)
print(personagens)

#-------------------------------
personagens = list(personagens)
chave =personagens.copy()
print(f"personagens: {personagens}")
print(f"chave: {chave}")

#---------------------------------
print("--//--")
random.shuffle(chave)
print(f"personagens: {personagens}")
print(f"chave: {chave}")

#---------------------------------
print("-------------------")
# CRIPTOGRAFIA
texto_plano= input("inserir uma mensagem para criptografar: ")
Criptografar_texto = ""

for letra in texto_plano:
    indice = personagens.index(letra)
    Criptografar_texto += chave[indice]

print(f"mensagem original: {texto_plano}")
print(f"mensagem CRIPTOGRAFada: {Criptografar_texto}")

#---------------------------------
print("-------------------")
# DECRIPTOGRAFIA
Criptografar_texto= input("inserir uma mensagem para decriptografar: ")
texto_plano = ""

for letra in Criptografar_texto:
    indice = chave.index(letra)
    texto_plano += personagens[indice]

print(f"mensagem CRIPTOGRAFada: {Criptografar_texto}")
print(f"mensagem original: {texto_plano}")

"""
#---------------------------------------
print("-------------------")
#não vai dar
import random
import string

personagens = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
personagens = list(personagens)
chave =personagens.copy()
"""
print(f"personagens: {personagens}")
print(f"chave: {chave}")

#---------------------------------
print("--//--")
random.shuffle(chave)
print(f"personagens: {personagens}")
print(f"chave: {chave}")

#---------------------------------
print("-------------------")
"""
# CRIPTOGRAFIA
texto_plano= input("inserir uma mensagem para criptografar: ")
Criptografar_texto = ""

for letra in texto_plano:
    indice = personagens.index(letra)
    Criptografar_texto += chave[indice]

print(f"mensagem original: {texto_plano}")
print(f"mensagem CRIPTOGRAFada: {Criptografar_texto}")
"""