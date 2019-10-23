# Working with Files
## Open files
you can use the ```open()``` function, which takes two parameters: the name of the target file and the mode. Three modes are available:

* r - read mode (the file is opened for reading)
* w - write mode (the file is opened for writing, and if a file having the same name exists, it will be erased)
* a - append mode (the file is opened for appending, which means that data is only to be added to the existing data in the file)
```
f = open('input.txt', 'r')
```

## Reading files
* ```f.read(n)``` returns n bytes of data from the file as a string. When the size parameter is omitted, the entire contents of the file will be read and returned.

* ```f.readline()``` takes a single line from the file.

* ```f.readlines()``` returns a list containing every line in the file.

* An alternative way to read lines is to loop over the file object.
```
for line in f: print(line)
```

## Splitting data
* The command ```line.split()``` uses whitespace in addition to \n as delimeters by default
```
'Beautiful is better than ugly.\n'.split()

returns

['Beautiful', 'is', 'better', 'than', 'ugly.']
```
* The  command for file parsing is ```f.splitlines()```. It returns a list of the lines in the string, breaking at line boundaries. Line breaks are not included.

```
'Simple is\nbetter than\ncomplex.\n'.splitlines()

returns

['Simple is', 'better than', 'complex.']
```

## Writing to files
* To save a file, output the desired file in write mode:
```
f = open('output.txt', 'w')

f.write('Any data you want to write into file')
```
* You must first convert data to a string by using the function str().

```
inscription = ['Rosalind Elsie Franklin ', 1920, 1958] 
s = str(inscription)
f.write(s)
```
* Adding ```\n``` to ```str(i)``` means that every item will start with a new line.
```
output.write(str(i) + '\n')
```
