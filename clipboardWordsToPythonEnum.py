"""
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
    Glass    =        'half full'
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

valueArea = False
newInputStr = ''
for char in inputStr:
    if char in ['"', "'"]:
        valueArea = not valueArea
        continue
    if valueArea:
        newInputStr += char.replace(' ', '&&_#&space')
    else:
        appendChar = char
        if char == '=':
            appendChar = f' {appendChar} '
        newInputStr += appendChar
inputStr = newInputStr
indentation = ''
for char in inputStr:
    if char == ' ':
        indentation += ' '
    else:
        break
inputStr = inputStr.replace('\n', ' ').replace('\r', ' ').replace('	', ' ') # Replace tabulation (tabs) & new lines with spaces
while '  ' in inputStr:
    inputStr = inputStr.replace('  ', ' ')


inputList = inputStr.split(' ')
while '' in inputList:
    inputList.remove('')


longestWordLen = 1
i = -1
for word in inputList:
    i += 1
    if i > 0:
        if inputList[i-1] == '=':
            continue
    print(word)
    longestWordLen = max(longestWordLen, len(word))
i = -1
numberOfSkips = 0
addedKeys = []
for word in inputList:
    i += 1
    if numberOfSkips > 0:
        numberOfSkips -= 1
        continue
    value = word
    if len(inputList) > i+1:
        if inputList[i+1] == '=':
            value = inputList[i+2].replace('"', '').replace("'", '').replace('&&_#&space', ' ')
            numberOfSkips = 2
    if word in addedKeys:
        continue
    spacingStr = ''
    while len(word + spacingStr) < longestWordLen:
        spacingStr += ' '
    returnVal += f"""{indentation}{word}{spacingStr} = '{value}'\n"""
    addedKeys.append(word)
clipboard.copy(returnVal)