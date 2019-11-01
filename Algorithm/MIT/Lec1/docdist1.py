import sys
import string

##################################
# Operation 1: read a text file ##
##################################


def read_file(filename):
    """
    Read the text file with the given filename;
    return: L  #a list of the lines of text in the file.
    """
    try:
        fp = open(filename)
        # readlines(): will read the text line by line & return L as a list of lines
        # read(): will read the text as a full string
        L = fp.readlines()
    except IOError:
        print("Error opening or reading input file: ", filename)

    return L
#################################################
# Operation 2: split the text lines into words ##
#################################################


def get_words_from_line_list(L):
    """
    Parse the given list L of text lines into words.
    Return list of all words found.
    """

    word_list = []
    for line in L:
        words_in_line = get_words_from_string(line)
        word_list = word_list + words_in_line
        print(word_list)
        break
    return word_list


def get_words_from_string(line):
    """
    Return a list of the words in the given input string,
    converting each word to lower-case.

    Input:  line (a string)
    Output: a list of strings
              (each string is a sequence of alphanumeric characters)
    """
    word_list = []          # accumulates words in line
    character_list = []     # accumulates characters in word
    for c in line:
        if c.isalnum():
            character_list.append(c)
        elif len(character_list) > 0:
            word = "".join(character_list)
            word = word.lower()
            word_list.append(word)
            character_list = []
    if len(character_list) > 0:
        word = "".join(character_list)
        word = word.lower()
        word_list.append(word)
    return word_list


def main():
    if len(sys.argv) != 3:
        print("Usage: docdist1.py filename_1 filename_2")
    else:
        filename_1 = sys.argv[1]
        filename_2 = sys.argv[2]
        # print(filename_1, filename_2)
        L1 = read_file(filename_1)
        print(get_words_from_line_list(L1))


if __name__ == "__main__":
    # pre-assign sys.argv
    sys.argv = ["docdist1.py", "/Users/quannguyen/Code/Data_Algo/Algorithm/MIT/Lec1/t1.verne.txt",
                "/Users/quannguyen/Code/Data_Algo/Algorithm/MIT/Lec1/t2.bobsey.txt"]
    main()
