# write a program to convert lower case to upper or uppercase to lower

in_ltr = input('Enter the letter : ')
if 'A'<=in_ltr<='Z':
    ch_in_ltr = chr(ord(in_ltr)+32)
    print(in_ltr," in lower case is ",ch_in_ltr)

elif 'a'<=in_ltr<="z":
    ch_in_ltr = chr(ord(in_ltr)-32)
    print(in_ltr, "in upper case is ", ch_in_ltr)

else:
    print(in_ltr)