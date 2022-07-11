string = input("please type something that has ten letters")
length = len(string)

if length < 10:
    string = input('please type something that has ten letters')
elif length > 10:
    string = input('please type something that has ten letters')
else:
 for character in string:
    output_string += character
    print(output_string)