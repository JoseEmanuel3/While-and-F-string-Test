frase = input("Digita uma frase: ")
range_nome = len(frase)
i = 0
completed_frase = ''

while i < range_nome:

    new_frase = (f'{frase[i]:*^2}')
    completed_frase += new_frase

    i += 1
print(completed_frase)