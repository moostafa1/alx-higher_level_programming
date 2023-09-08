>>> text_indentation = __import__('5-text_indentation').text_indentation


>>> text_indentation("Holberton School")
Holberton School>>>


>>> text_indentation("Holberton.School")
Holberton

School>>>


>>> text_indentation("Holberton. School? How are you: John")
Holberton

School

How are you

John>>>


>>> text_indentation(12)
Traceback (most recent call last):
TypeError: text must be a string


>>> text_indentation("             ")
             >>>


>>> text_indentation("\n")

>>>


>>> text_indentation()
Traceback (most recent call last):
TypeError: text_indentation() missing 1 required positional argument: 'text'
