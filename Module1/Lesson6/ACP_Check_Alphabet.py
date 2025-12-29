ch = input("Enter a character: ")


if len(ch) >1:
    print(f"Please enter only ONE character." ,{int(ch, base=0)})
    exit(0)

 

if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
    print("The entered character is an Alphabet.")
else:
    print("The entered character is NOT an Alphabet.")

   