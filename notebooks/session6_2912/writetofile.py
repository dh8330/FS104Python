file_string = str(input("Enter text here;"))

def write(text):
    file_object = open("textfile","w")
    file_object.write(text)
    file_object.close
write(file_string)
