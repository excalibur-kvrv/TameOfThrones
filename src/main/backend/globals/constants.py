import os

"""
The below constants are used in cryptographic algorithms
:constant TOTAL_CHARS -> This is used to specify the range of characters, what should be considered which
                         encrypting or decrypting a cipher.
:constant FIRST_CHAR_ASCII_VALUE -> This is used to specify the starting value of the range(inclusive).
:constant LAST_CHAR_ASCII_VALUE -> This is used to specify the ending value of the range(exclusive). 

char range = [FIRST_CHAR_ASCII_VALUE, LAST_CHAR_ASCII_VALUE)

:constant STRATEGY -> used to indicate the cryptographic algorithm to be used.
"""

TOTAL_CHARS = 26
FIRST_CHAR_UNICODE_VALUE = ord("A")
LAST_CHAR_UNICODE_VALUE = FIRST_CHAR_UNICODE_VALUE + TOTAL_CHARS
STRATEGY = "seaser"

"""
The below constant is used for pointing to the file containing the kingdom data, it should be in a json file,
of the format:-

{
    "rulers": {
        "kingdom_name1": "emblem_name",
        .
        .
        . 
        "kingdom_nameN": "emblem_name",
    }, 
    "allies": {
        "kingdom_name1": "emblem_name",
        .
        .
        . 
        "kingdom_nameN": "emblem_name",
    }
}

"""

KINGDOM_DATA = os.path.join("src", "main", "resources", "kingdoms.json")

"""
The below constants are used for output generation type
:constant OUTPUT_TYPE -> Used to imply whether the output should be printed to console or to a file

values taken by OUTPUT_TYPE = "console", "file"

:constant SAVE_PATH -> Used to indicate the directory of where to save the output

output will be stored as "actual-'input-file-name'"
"""

OUTPUT_TYPE = "console"
SAVE_PATH = os.path.join("src", "tests", "resources")

"""
The below constants is used to indicate the pattern to be used to validate the input file

:constant FILE_PATTERN -> used to check if the input file follows the below pattern.
:constant RUN_VALIDATION -> used to run validation of input file.

"""

FILE_PATTERN = r"^\s*[a-z]+ .+$"
RUN_VALIDATION = True
