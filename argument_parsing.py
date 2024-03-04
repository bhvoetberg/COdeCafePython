import sys
import getopt

for x in range(0, len(sys.argv)):
    print(sys.argv[x])

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])
print("--")


# console: python3 argument_parsing.py -f t.txt -m "hello"
for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg
with open(filename, 'w+') as f:
    f.write(message)

print(opts)
print(args)
