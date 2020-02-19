import random

def doubleColor():
    red = random.sample(range(1,34), 6)
    blue = random.choice(range(1, 17))
    return str(red)+'-'+str(blue)

print(doubleColor())
