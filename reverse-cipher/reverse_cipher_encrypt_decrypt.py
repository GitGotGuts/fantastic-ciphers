given_text = input("Put the text to encode/decode:  ")

output_text = ""

for i in given_text:
    output_text = i + output_text

print("The output is: '" + output_text + "'")
