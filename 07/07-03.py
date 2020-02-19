import string
from random import choice

characters = string.ascii_letters + string.digits
selected = [choice(characters) for i in range(1000)]
ch = choice(selected)
print(ch, ':', selected.count(ch))
