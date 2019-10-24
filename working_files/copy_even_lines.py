# Given: A file containing at most 1000 lines.
#
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines. Please copy the content of output file into the text field below.

def cp_even_line(filename, newfile):
    f = open(filename,'r')
    w = open(newfile, 'w+')
    for i in f.read().splitlines()[1::2]:
        w.write(str(i) + '\n')
    return 'Done'

cp_even_line(f1,f2)
