# clipboardWordsToPythonEnum
A simple Python program that takes something like:

Book Sissor Fork Glass

out of your clipboard and replaces it with:

Fork   = 'Fork'
Sissor = 'Sissor'
Glass  = 'Glass'
Book   = 'Book'

Alternatively if you have:

    Fork                = 'Fork'
    Sissor =          'Sissor'
    Glass          = 'Glass'
    Book    = 'Book'

In your clipboard, it will give you:

    Fork   = 'Fork'
    Glass  = 'Glass'
    Book   = 'Book'
    Sissor = 'Sissor'

In your clipboard! Note that it also maintains indentation (only spaces are supported for indentation).


Compile with: https://pypi.org/project/auto-py-to-exe/ . Just open up the directory with the .py file in a cmd line window and type auto-py-to-exe
