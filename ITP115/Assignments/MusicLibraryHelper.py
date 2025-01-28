"""
Music Library Helper file: provides two functions that:
    1) allows you to load a dictionary from a specified binary file
    2) allows you to save a dictionary to a specified binary file
"""
import pickle


# Input: the name of the file containing the music library dictionary
# Return value: a dictionary representing the music library, where each key is an
#     artist and each value is a list of albums by that artist
# Loads a dictionary from the specified binary file
def loadLibrary(libraryFileName):
    fin = open(libraryFileName, "rb")  # read binary
    library_dct = pickle.load(fin)
    fin.close()
    return library_dct


# Input: the name of the file that the music library will be saved to;
#     the dictionary representing the music library
# Return value: none
# Writes a dictionary to the specified output file
def saveLibrary(libraryFileName, musicLibDct):
    fin = open(libraryFileName, "wb")  # write binary file
    pickle.dump(musicLibDct, fin)
    fin.close()
