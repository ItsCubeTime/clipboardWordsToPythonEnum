# clipboardWordsToPythonEnum

A simple Python program that takes something like:

```
Book Sissor Fork Glass
```

out of your clipboard and replaces it with:

```py
Fork   = 'Fork'
Sissor = 'Sissor'
Glass  = 'Glass'
Book   = 'Book'
```

Alternatively if you have:

```py
    Fork                = 'Fork'
    Sissor =          'Sissor'
    Glass          = 'Glass'
    Book    = 'Book'
```

In your clipboard, it will give you:

```py
    Fork   = 'Fork'
    Glass  = 'Glass'
    Book   = 'Book'
    Sissor = 'Sissor'
```

In your clipboard! Note that it also:
* maintains indentation (only spaces are supported for indentation).
* removes duplicate keys

### Binaries

You can grab binary versions at https://github.com/ItsCubeTime/clipboardWordsToPythonEnum/releases/

Alternatively compile yourself with: https://pypi.org/project/auto-py-to-exe/ . Just open up the directory with the .py file in a cmd line window and type auto-py-to-exe

You can also run the .py file yourself assuming that you have a working & compatible Python3 interpreter installed. Developed in a Windows 11 environment using Python 3.10.2.
