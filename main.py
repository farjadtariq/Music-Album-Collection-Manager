#main.py
#
#Author:        Farjad Tariq
#Version:       2023/08/13
#
#Purpose:       The purpose of this is to write a complete Python 
#               program that reads a file containing a collection of music 
#               albums and build a dictionary.

from time import ctime

def displayTerminationMessage():
    print(f"""
Programmed by Farjad Tariq
Date: {ctime()}
End of processing.\n""")

def readFile(filename):
    # fileName = Name of the file that you want to read.
    # infile = the file descriptor.
    # lines = A list containing all the data in the file.
    # infos = information for the albums
    # item = specific items in album

    infile = open(filename, 'r')
    lines = infile.readlines()
    infile.close()
    albums = {}
    for line in lines:
        infos = line.strip()[2:-2].split('] [')
        for info in infos:
            item = info.split(';')
            if item[0] in albums:
                albums[item[0]].append((item[1],item[2]))
            else:
                albums[item[0]] = [(item[1],item[2])]
    return albums

def displayAlbums(collection):
    # key = name of artist
    # collection = album
    # item = specific items in album

    for key in collection:
        print('\n'+key)
        for item in collection[key]:
            print('    %s, %s' % (item[0], item[1]))

def main():
    print('\n' + '-' * 80)
    # fileName = Name of the file that you want to read
    # albums = dictionary

    fileName = input('Enter the name of the file: ')
    albums = readFile(fileName)
    displayAlbums(albums)
    displayTerminationMessage()

main()