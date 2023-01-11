import random
import string

#la prima lettera dell'input la sposta nell'ultima posizione
def transformation(input):
    input = list(input)
    input.append(input[0])
    input.pop(0)
    return "".join(input)

def encrypt(input, seed):
    input = transformation(input)
    input = list(input)
    random.seed(seed)
    input = [chr(ord(x) ^ random.randint(80, 120)) for x in input]
    input = "".join(input)
    return input

def reverse_transformation(input):
    input = list(input)
    c = input[len(input) - 1]
    input.pop()
    input.insert(0, c)
    return "".join(input)

def decrypt(input, seed):
    random.seed(seed)
    out = ""
    for c in input:
        out += chr(ord(c) ^ random.randint(80, 120))
    out = reverse_transformation(out)
    return out

file = open("/Users/riccardofavaron/Desktop/UNI/Secondo anno/Cybersecurity/Ex/21_11_2021_FirstPartial/Exercise3/secret.txt", "r")
cipher = file.read()

out = dict()
for seed in range(1000):
    dec = decrypt(cipher, seed)
    if set(dec).issubset(set(string.ascii_letters + string.digits + "}{_")) and "spritz" in dec:
        print(dec)
        out[seed] = dec