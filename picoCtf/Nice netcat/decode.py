res = ""
with open('file.txt', 'r') as f:
    for line in f:
        ascii_num = int(line.strip())  # convert the string to an integer
        char = chr(ascii_num)    # convert the ASCII number to a character
        res += char
        
print(res)
