import binascii

code = "32 69 31 73 34 69 31 73 31 35 64 31 6f 34 39 69 31 6f 34 64 31 6f 33 69 31 6f 31 35 64 31 6f 32 32 64 31 6f 32 30 64 31 6f 31 39 69 31 6f 37 64 31 6f 35 64 31 6f 32 69 31 6f 35 35 69 31 6f 31 64 31 6f 31 39 64 31 6f 31 37 64 31 6f 31 38 64 31 6f 32 39 69 31 6f 31 32 69 31 6f 32 36 69 31 6f 38 64 31 6f 35 39 64 31 6f 32 37 69 31 6f 36 64 31 6f 31 37 69 31 6f 31 32 64 31 6f 37 64 31 6f 35 69 31 6f 31 64 31 6f 32 64 31 6f 31 32 69 31 6f 39 64 31 6f 32 36 64 31 6f"

step1 = ''.join(code.split(" "))

step1 = binascii.unhexlify(step1).decode()
print("\nStep 1: Convertir depuis l'hexadécimal")
print(step1)

step2 = ""

num = ""
for index in range(len(step1)):
    if step1[index] in ['1','2','3','4','5','6','7','8','9']:
        num += step1[index]
    
    try:
        if step1[index + 1] not in ['1','2','3','4','5','6','7','8','9']:
            step2 += step1[index + 1] * int(num)
            num = ""
            index += 1
    except:
        pass

print("\nStep 2: Développer de sorte à ne plus voir de chiffres")
print(step2)
