from datetime import datetime

number = 12.35
intnumber = 1234
print(f"{number:+.1f}")
print(f"{intnumber:b}")

now = datetime.now()
print(f"{now:%Y-%m-%d}")

# align
name = "Alice"
width = 12
print(f"{name:<{width}}")
print(f"{name:>{width}}")
print(f"{name:^{width}}")

x=15
y=10

print(f"{x = }, {y=}, {x+y=} ")