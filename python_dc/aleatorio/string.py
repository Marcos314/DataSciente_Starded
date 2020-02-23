# text = 'Python para análise de dados'
#
# print(text[0])
# print(text[1])
# print(text[2])


'''
Manipulando strings
'''
s = 'Data Science Academy'
#slicing

#retorna tudo, exceto a ultima posição
print(s[:-1])

#retorna tudo até a pos 3
print(s[:3])

#tudo menos as duas ultimas
print(s[:-2])


print(s[::-2])

#Buit-in

#s2 = s.upper()
s2 = s.split('a')
print(s2)