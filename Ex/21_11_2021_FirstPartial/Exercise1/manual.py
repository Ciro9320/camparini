with open("/Users/riccardofavaron/Desktop/UNI/Secondo anno/Cybersecurity/Ex/21_11_2021_FirstPartial/Exercise1/ciphertext.txt", "r") as ciphertext_file:
    ciphertext = ciphertext_file.read().lower()

trans = str.maketrans(
    "abcdefghijklmnopqrstuvwxyz",
    "IMZOPKSTEBWGNRVL_UJAYHF_DC",
)

print(ciphertext.translate(trans))
