import turtle as t
from random_example import random
#
# forward(200)
# left(120)


for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)