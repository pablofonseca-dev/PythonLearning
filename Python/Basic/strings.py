book_title = "albert einstein"

#Simple python methods 

print(book_title.lower())
print(book_title.upper())
print(book_title.title())


#Combining or Concatening Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name #This is called concatenation

print(full_name) 

#Adding WhiteSpace to Strings with Tabs or Newlines

print("Languages:\n\tPython\n\tC\n\tJavaScript")

#To ensure that no whitespace exist at the right end of a string, use rstrip() method

print('Pablo Fonseca Moncada                            '.rstrip())

#To ensure that no whitespace exist at the left end of a string, use lstrip() method
print('                                               Pablo Fonseca Moncada'.lstrip())

#To ensure that no whitespace exist in both sides use strip() method 
print('         Pablo Fonseca Moncada          '.strip())

print("Hello, I'm Pablo")
