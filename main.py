# Шифр Цезаря с шагом 3
step = 3
text = input()
new_text = ""
for char in text:
    if 1040 <= ord(char) <= 1071:
        if ord(char) + step >= 1071:
            a = (ord(char) + step) % 1071
            new_text += chr(1040 + a)
        else: new_text += chr(ord(char) + step)
    elif ord(char) == 1025:
        new_text += chr(1045 + step)
    elif 1072 <= ord(char) <= 1103:
        if ord(char) + step >= 1103:
            a = (ord(char) + step) % 1103
            new_text += chr(1072 + a)
        else: new_text += chr(ord(char) + step)
    elif ord(char) == 1105:
        new_text += chr(1077 + step)
    else:
        new_text += char
print(new_text)