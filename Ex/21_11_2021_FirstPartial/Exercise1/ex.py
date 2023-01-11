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

def calculate_freq(text):
    dictionary = {}
    for c in text:
        if c not in dictionary:
            dictionary[c] = 1
        else:
            dictionary[c] += 1
    return dictionary

ciphertext_file = open("/Users/riccardofavaron/Desktop/UNI/Secondo anno/Cybersecurity/Ex/21_11_2021_FirstPartial/Exercise1/ciphertext.txt", "r")
ciphertext = ciphertext_file.read()

actual_freqs = calculate_freq(ciphertext)
#print(actual_freqs)

sum_freq = 0
for c in actual_freqs:
    if c in string.ascii_uppercase:
        sum_freq += actual_freqs[c]

for c in actual_freqs:
    actual_freqs[c] = float(actual_freqs[c] / sum_freq * 100)

#actual_freq = sorted(actual_freq.items(), key = lambda kv: (kv[1], kv[0]), reverse = True)

key = {}
for actual_freq in actual_freqs.items():
    error = 100
    min_err_value = ("", 0)
    for expected_freq in expected_freqs.items():
        current_error = abs(float(actual_freq[1] - expected_freq[1]))
        if current_error < error:
            error = current_error
            min_err_value = expected_freq
    key[actual_freq[0]] = min_err_value[0]
    expected_freqs.pop(min_err_value[0])

plaintext = "".join(c if c not in string.ascii_lowercase else key[c] for c in ciphertext)
print(plaintext)