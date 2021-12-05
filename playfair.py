import string
import itertools
 
 
def chunker(seq, size):
    it = iter(seq)
    while True:
        chunk = tuple(itertools.islice(it, size))
        if not chunk:
            return
        yield chunk
 
 
def prepare_input(dirty):
 
    dirty = "".join([c.upper() for c in dirty if c in string.ascii_letters])
    clean = ""
 
    if len(dirty) < 2:
        return dirty
 
    for i in range(len(dirty) - 1):
        clean += dirty[i]
 
        if dirty[i] == dirty[i + 1]:
            clean += "X"
 
    clean += dirty[-1]
 
    if len(clean) & 1:
        clean += "X"
 
    return clean
 
 
def generate_table(key):

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table = []
    for char in key.upper():
        if char not in table and char in alphabet:
            table.append(char)
    for char in alphabet:
        if char not in table:
            table.append(char)
 
    return table
 
 
def encode(plaintext, key):
    table = generate_table(key)
    plaintext = prepare_input(plaintext)
    ciphertext = ""
    for char1, char2 in chunker(plaintext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)
 
        if row1 == row2:
            ciphertext += table[row1 * 5 + (col1 + 1) % 5]
            ciphertext += table[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += table[((row1 + 1) % 5) * 5 + col1]
            ciphertext += table[((row2 + 1) % 5) * 5 + col2]
        else:  # rectangle
            ciphertext += table[row1 * 5 + col2]
            ciphertext += table[row2 * 5 + col1]
 
    return ciphertext
 
 
def decode(ciphertext, key):
    table = generate_table(key)
    plaintext = ""
    for char1, char2 in chunker(ciphertext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)
 
        if row1 == row2:
            plaintext += table[row1 * 5 + (col1 - 1) % 5]
            plaintext += table[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += table[((row1 - 1) % 5) * 5 + col1]
            plaintext += table[((row2 - 1) % 5) * 5 + col2]
        else:  
            plaintext += table[row1 * 5 + col2]
            plaintext += table[row2 * 5 + col1]
 
    return plaintext

print(encode("DOGG", "HELL"))
