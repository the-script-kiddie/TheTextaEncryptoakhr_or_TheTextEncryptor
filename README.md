so this is a basic text encryptor and decryptor i made in python (warning: it does NOT use real encryption like base64, base32, hexadecimal etc) and it does not use real caesar cipher either<br>
if you want to test it make sure you have python installed (if you don't have python installed go to <a href="https://www.python.org">the official python site</a>)<br>
if you've heard of ascii values... you know what this does basically<br>
what this does is that it takes a string, breaks it into individual characters, takes the character's ascii value (A = 65, B = 66, C = 67 and so on) and increments/decrements the ascii value of the character by 16 and turns the ascii value back to character for each character, makes an empty string, and puts these "encrypted" characters into the new string
