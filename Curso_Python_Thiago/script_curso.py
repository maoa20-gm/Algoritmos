print([x for x in range (0,10)])
print([c for c in "Oe que te pasa" if c == " " ])

print([chr(n) for n in range(30,100)])

print([n for n in range(1,100) if n%7 == 0])

def ehSeparadorAlternativa(c:str , separador:str) -> bool:
    return [x for x in separador if x == c] != []

codigos = {'BR':55, 'US':1, 'JP':81,'UK':44, 'VU':678, 'UY':598} 

codigos['TO'] = 676

print(codigos)
