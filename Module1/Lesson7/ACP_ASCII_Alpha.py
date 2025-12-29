ch = input("Enter an alphabet: ")

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

if len(ch) == 1 and ch in uppercase:
    ascii_value = int(uppercase.index(ch)) + 65
    print("ASCII value of", ch, "is", ascii_value)

elif len(ch) == 1 and ch in lowercase:
    ascii_value = int(lowercase.index(ch)) + 97
    print("ASCII value of", ch, "is", ascii_value)

else:
    print("Please enter a single alphabet only.")