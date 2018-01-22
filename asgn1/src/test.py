from lex import *
import collections

data = "2+6*85+1"

# Give the lexer some input
lexer.input(data)

lexer.sort(key=lambda x: x.lexpos, reverse=False)
#counter=collections.Counter(lexer.type)
#print(counter)

# Tokenize
print("{0:^16} {1:^16} {2:^8}".format("Token", "Occurrences", "Lexemes"))
print("{0:^16} {1:^16} {2:^8}".format("-----", "-----------", "-------"))
for tok in lexer:
    print("{0:^16} {1:^16} {2:^8}".format(tok.type, tok.lexpos, tok.value))