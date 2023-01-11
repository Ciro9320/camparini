import string

expected_freqs = {
    "a": 8.4966,
    "b": 2.0720,
    "c": 4.5388,
    "d": 3.3844,
    "e": 11.1607,
    "f": 1.8121,
    "g": 2.4705,
    "h": 3.0034,
    "i": 7.5448,
    "j": 0.1965,
    "k": 0.2902,
    "l": 5.4893,
    "m": 3.0129,
    "n": 6.6544,
    "o": 7.1635,
    "p": 3.1671,
    "q": 0.1962,
    "r": 7.5809,
    "s": 5.7351,
    "t": 6.9509,
    "u": 3.6308,
    "v": 1.0074,
    "w": 1.2899,
    "x": 0.2902,
    "y": 1.7779,
    "z": 0.2722,
}

ciphertext_file = open("/Users/riccardofavaron/Desktop/UNI/Secondo anno/Cybersecurity/Ex/21_11_2021_FirstPartial/Exercise1/ciphertext.txt", "r")
ciphertext = ciphertext_file.read()

actual_freqs = {}
for c in ciphertext:
    if c in string.ascii_letters:
        if c in actual_freqs:
            actual_freqs[c] += 1
        else:
            actual_freqs[c] = 1

count = 0
for c in actual_freqs:
    count += actual_freqs[c]

for c in actual_freqs:
    actual_freqs[c] = actual_freqs[c] / count * 100
#print(sorted(actual_freqs.items(), key = lambda kv: (kv[1], kv[0]), reverse = True))

key = {}
for af in actual_freqs.items():
    error = 100
    min_err_value = ("", 0)
    for ef in expected_freqs.items():
        cur_error = abs(af[1] - ef[1])
        if cur_error < error:
            error = cur_error
            min_err_value = ef
    key[af[0]] = min_err_value[0]
    expected_freqs.pop(min_err_value[0])
#print(key)

plaintext = ""
for c in ciphertext:
    if c not in string.ascii_letters:
        plaintext += c
    else:
        plaintext += key[c]
#print(plaintext)

#now we can guess some letters
voc = {'n': 's',
       'v': 'p',
       'd': 'r',
       'e': 'i',
       'a': 't',
       'k': 'z',
}
flagtext = ''.join(c if c not in voc else voc[c] for c in plaintext)
voc['g'] = 'f'
voc['o'] = 'a'
voc['c'] = 'l'
voc['y'] = 'c'
voc['i'] = 'n'
voc['l'] = 'm'
voc['m'] = 'g'
voc['s'] = 'o'
voc['r'] = 'e'
voc['h'] = 'y'
#at this point we reach the key
flagtext = ''.join(c if c not in voc else voc[c] for c in plaintext)
print(flagtext)
