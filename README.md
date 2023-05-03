# clipboardWordsToPythonEnum



https://user-images.githubusercontent.com/20190653/235925917-e07bae3f-a31f-42d7-a58d-2fe2a30bf328.mp4



A simple Python program that takes something like:

```
    Book Sissor Fork Glass='half empty'
```

out of your clipboard and replaces it with:

```py
    Book   = 'Book'
    Sissor = 'Sissor'
    Fork   = 'Fork'
    Glass  = 'half empty'
```

Alternatively if you have:

```py
    Book       = 'Book'
    Sissor =          'Sissor'
  Fork                =           "Fork"
    Glass  =  'half empty'
```

In your clipboard, it will give you:

```py
    Book   = 'Book'
    Sissor = 'Sissor'
    Fork   = 'Fork'
    Glass  = 'half empty'
```

In your clipboard! Note that it also:
* maintains indentation (only spaces are supported for indentation).
* removes duplicate keys
* Aligns the assignment operators (equal signs) by adding extra spaces to there left

### Binaries

You can grab binary versions at https://github.com/ItsCubeTime/clipboardWordsToPythonEnum/releases/

Alternatively compile yourself with: https://pypi.org/project/auto-py-to-exe/ . Just open up the directory with the .py file in a cmd line window and type auto-py-to-exe

You can also run the .py file yourself assuming that you have a working & compatible Python3 interpreter installed. Developed in a Windows 11 environment using Python 3.10.2.
