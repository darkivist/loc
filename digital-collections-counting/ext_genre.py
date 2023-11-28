#written by Paul Kelly 2023, adapted from code by Hilary Shiue 2021
#script to obtain file extensions and corresponding genre terms from LC digital format description XML: https://www.loc.gov/preservation/digital/formats/fdd/fdd_xml_info.shtml
#download zip of xml, extract, copy this script to extracted folder then run

#to do: address records that have no extension tag (e.g. containers and wrappers)?

import xml.etree.ElementTree as ET
from pathlib import Path

# create the function
def get_elements(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    ns = '{http://www.loc.gov/preservation/digital/formats/schemas/fdd/v1}'
    
    genre = []
    extension = []
    
    for gdfrGenreSelection in tree.findall('.//' + ns + 'gdfrGenreSelection'):
        tag = gdfrGenreSelection.find(ns +'tag')
        # finding genres
        genre_list = gdfrGenreSelection.findall('.//' + ns + 'gdfrGenre')
        for gr in genre_list:
                genre.append(gr.text)
        
    for filenameExtension in tree.findall('.//' + ns + 'filenameExtension'):
        tag = filenameExtension.find(ns +'tag')
        # finding extensions
        extension_list = filenameExtension.findall('.//' + ns + 'sigValue')
        
        for ext in extension_list:
                extension.append(ext.text)

    return (genre, extension)

print('file_extension,genre_type')

pathlist = Path('.').rglob('*.xml')

# loops through FDD xml in local folder
for path in pathlist:
    path_str = str(path)
    genre_type,file_extension = get_elements(path_str)
    
    genre_str = ''
    for gt in genre_type:
        genre_str += gt + '; '
    genre_str = '"' + genre_str[:-2] + '"'
    
    extension_str = ''
    for ex in file_extension:
        extension_str += ex + '; '
    extension_str = '"' + extension_str[:-2] + '"'
        
    print('{},{}'.format(extension_str,genre_str))
