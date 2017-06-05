"""
Open a file, replace string based on a dictionary and output a new file
"""
import sys
import pdb

def read_dictionaryfile(f):
    '''
    read a file to a dictionary
    filemanager.read_dictionaryfile("..\\test\\dictionary.txt")
    '''
    new_dict = {}
    with open(f, 'rt') as fdict:
        for line in fdict:
            keyword, replacestring = line.split(',')
            if keyword  not in new_dict:
                new_dict[keyword] = replacestring
    return new_dict

def replace_string(inputfile,outputfile,dictfile):
    '''
    repace string
    filemanager.replace_string("..\\test\\input.txt","..\\test\\output.txt","..\\test\\dictionary.txt")
    '''
    pdb.set_trace()
    new_dict = read_dictionaryfile(dictfile)
    with open(inputfile, "rt") as fin:
        with open(outputfile, "wt") as fout:
            for line in fin:
                for key in new_dict:
                    newline = line
                    if key in line:
                        newline = line.replace(key, new_dict[key])
                        line = newline
                    else:
                        line = newline
                fout.write(line)

