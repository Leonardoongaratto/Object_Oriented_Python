from pessoa import Pessoa

p1 = Pessoa('Luiz', 24)
p2 = Pessoa('Leonardo', 23)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())


p1.comer('Uva')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.comer('pão')
p1.parar_falar()
