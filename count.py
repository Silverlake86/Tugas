import sys


string = " "
alphabets = 0
digits = 0
specials = 0

for line in sys.stdin:
    string = line
    for i in range(len(string)):
        if((string[i] >= 'a' and string[i] <= 'z') or (string[i] >= 'A' and string[i] <= 'Z')): 
            alphabets = alphabets + 1 
        elif(string[i] >= '0' and string[i] <= '9'):
            digits = digits + 1
        else:
            specials = specials + 1

sys.stdout.write("Jumlah Angka: " + str(digits))
sys.stdout.write('\n')
sys.stdout.write("Jumlah Huruf: " + str(alphabets))
sys.stdout.write('\n')
sys.stdout.write("Jumlah Simbol: " + str(specials))
sys.stdout.write('\n')

