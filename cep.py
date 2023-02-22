import re

endereco = 'Rua Cipriano Pereira, 1192 64.220-000 Centro'

end_re = re.compile("[0-9]{2}[.]{0,1}[0-9]{3}[-]{0,1}[0-9]{3}")
end_comp = end_re.search(endereco)
if end_comp:
    cep = end_comp.group()
print(cep)