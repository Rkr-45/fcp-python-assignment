
import sys
import random
filen = sys.argv[1]
lines = open(filen).readlines()
quotes = "".join(lines)
quote = random.choice(quotes.split("%"))
print(quote)
