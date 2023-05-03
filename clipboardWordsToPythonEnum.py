"""A simple Python program that takes something like:

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


Compile with:
"""
import subprocess
import sys
try:
    import clipboard
except:
    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    install('clipboard')
    import clipboard

returnVal = ''
inputStr = clipboard.paste()
indentation = ''
for char in inputStr:
    if char == ' ':
        indentation += ' '
    else:
        break
inputStr = inputStr.replace('\n', ' ').replace('\r', ' ').replace('	', ' ') # Replace tabulation (tabs) & new lines with spaces
while '  ' in inputStr:
    inputStr = inputStr.replace('  ', ' ')

inputStr = inputStr.replace("'", '').replace('"','')

inputList = inputStr.split(' ')
while '=' in inputList:
    inputList.remove('=')
while '' in inputList:
    inputList.remove('')
inputList = list(set(inputList))

longestWordLen = 1
for word in inputList:
    longestWordLen = max(longestWordLen, len(word))
for word in inputList:
    spacingStr = ''
    while len(word + spacingStr) < longestWordLen:
        spacingStr += ' '
    returnVal += f"""{indentation}{word}{spacingStr} = '{word}'\n"""
clipboard.copy(returnVal)