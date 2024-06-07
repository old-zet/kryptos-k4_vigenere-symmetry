#!/usr/bin/env python3
#coding: utf-8
#!python3

"""
KRYPTOS' K4 functional controller.
"""

import random
import string
import argparse


def compute_alphabet_distances(input_str_1: str, input_str_2: str):
    """Given two strings of the same length, compute the distance
    between each letter and the direction (F: forward | B:backwards) 
    in the alphabet to yield the delta from K1_TO_K3_DECIPHERED to K1_TO_K3_CIPHER_CORRECTED.
    HELPER FUNCTION

    Args:
        input_str_1 (str): the reference string (e.g. K1_TO_K3_DECIPHERED).
        input_str_2 (str): the string of comparison (e.g. K1_TO_K3_CIPHER_CORRECTED).
    """
    K1_TO_K3_DECIPHERED = "BETWEENSUBTLESHADINGANDTHEABSENCEOFLIGHTLIESTHENUANCEOFIQLUSIONITWASTOTALLYINVISIBLEHOWSTHATPOSSIBLE?THEYUSEDTHEEARTHSMAGNETICFIELDXTHEINFORMATIONWASGATHEREDANDTRANSMITTEDUNDERGRUUNDTOANUNKNOWNLOCATIONXDOESLANGLEYKNOWABOUTTHIS?THEYSHOULDITSBURIEDOUTTHERESOMEWHEREXWHOKNOWSTHEEXACTLOCATION?ONLYWWTHISWASHISLASTMESSAGEXTHIRTYEIGHTDEGREESFIFTYSEVENMINUTESSIXPOINTFIVESECONDSNORTHSEVENTYSEVENDEGREESEIGHTMINUTESFORTYFOURSECONDSWESTXLAYERTWOSLOWLYDESPARATLYSLOWLYTHEREMAINSOFPASSAGEDEBRISTHATENCUMBEREDTHELOWERPARTOFTHEDOORWAYWASREMOVEDWITHTREMBLINGHANDSIMADEATINYBREACHINTHEUPPERLEFTHANDCORNERANDTHENWIDENINGTHEHOLEALITTLEIINSERTEDTHECANDLEANDPEEREDINTHEHOTAIRESCAPINGFROMTHECHAMBERCAUSEDTHEFLAMETOFLICKERBUTPRESENTLYDETAILSOFTHEROOMWITHINEMERGEDFROMTHEMISTXCANYOUSEEANYTHINGQ"
    K1_TO_K3_CIPHER_CORRECTED = "EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFDVFPJUDEEHZWETZYVGWHKKQETGFQJNCEGGWHKK?DQMCPFQZDQMMIAGPFXHQRLGTIMVMZJANQLVKQEDAGDVFRPJUNGEUNAQZGZLECGYUXUEENJTBJLBQCRTBJDFHRRYIZETKZEMVDUFKSJHKFWHKUWQLSZFTIHHDDDUVH?DWKBFUFPWNTDFIYCUQZEREEVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDXFLGGTEZ?FKZBSFDQVGOGIPUFXHHDRKFFHQNTGPUAECNUVPDJMQCLQUMUNEDFQELZZVRRGKFFVOEEXBDMVPNFQXEZLGREDNQFMPNZGLFLPMRJQYALMGNUVPDXVKPDQUMEBEDMHDAFMJGZNUPLGESWJLLAETGENDYAHROHNLSRHEOCPTEOIBIDYSHNAIACHTNREYULDSLLSLLNOHSNOSMRWXMNETPRNGATIHNRARPESLNNELEBLPIIACAEWMTWNDITEENRAHCTENEUDRETNHAEOETFOLSEDTIWENHAEIOYTEYQHEENCTAYCREIFTBRSPAMHHEWENATAMATEGYEERLBTEEFOASFIOTUETUAEOTOARMAEERTNRTIBSEDDNIAAHTTMSTEWPIEROAGRIEWFEBAECTDDHILCEIHSITEGOEAOSDDRYDLORITRKLMLEHAGTDHARDPNEOHMGFMFEUHEECDMRIPFEIMEHNLSSTTRTVDOHW"

    result = []
    
    for char1, char2 in zip(input_str_1, input_str_2):
        distance = abs(ord(char2) - ord(char1))
        if char2>char1:
            result.append(f"{distance}F")
        else:
            result.append(f"{distance}B")
    
    for i in range(0, len(result), 5):
        print(' '.join(result[i:i+5]))

def generate_matrices() -> tuple:
    """Generate two 5x5 matrices using a shuffled alphabet 
    where one pair of letters is merged, thus making up to 26;
    the second matrix is the mirror reflection of the first one.

    Returns:
        tuple: two 5x5 matrices (lists of lists).
    """
    alphabet = list(string.ascii_uppercase)
    merged_pair = random.sample(alphabet, 2)
    merged_value = merged_pair[0] + '/' + merged_pair[1]
    alphabet = [char for char in alphabet if char not in merged_pair]
    alphabet.append(merged_value)
    random.shuffle(alphabet)
    
    source_matrix = [alphabet[i*5:(i+1)*5] for i in range(5)]
    target_matrix = [list(reversed(row)) for row in source_matrix]
    
    merged_value_position = [(i, row.index(merged_value)) for i, row in enumerate(source_matrix) if merged_value in row][0]
    new_row = merged_value_position[0]
    new_col = len(source_matrix[0]) - 1 - merged_value_position[1]
    target_matrix[new_row][new_col] = merged_value

    return source_matrix, target_matrix

def print_matrix(matrix: list, name: str):
    """Print a given matrix with a specified name.

    Args:
        matrix (list): a list of lists representing the matrix to be printed.
        name (str): the name of the matrix to be displayed in the header.
    """
    print(f"{name} Matrix:")
    for row in matrix:
        print(" ".join(row))
    print()

def translate_char(char: str, source_matrix: list, target_matrix: list) -> str:
    """Translate a character from the source matrix 
    to the corresponding character in the target matrix via their index.

    Args:
        char (str): the character to be translated.
        source_matrix (list): the source matrix for reference.
        target_matrix (list): the target matrix for translation.

    Returns:
        str: the translated character from the target matrix, or the original character if not found.
    """
    for i, row in enumerate(source_matrix):
        if char in row:
            return target_matrix[i][row.index(char)]
    return char

def translate_string(input_string: str, source_matrix: list, target_matrix: list) -> str:
    """Translate a string using the source and target matrices.

    Args:
        input_string (str): the string to be translated.
        source_matrix (list): the source matrix for reference.
        target_matrix (list): the target matrix for translation.

    Returns:
        str: the translated string.
    """
    return "".join(translate_char(char, source_matrix, target_matrix) for char in input_string)

def process_string(input_string: str) -> list:
    """Recursively process a given string and 
    generate all possible variations of its characters.

    Args:
        input_string (str): the string to be processed.

    Returns:
        list: list of unique strings with all possible variations of split/merged characters.
    """
    result = []
    i = 0
    while '/' in input_string[i:]:
        index = input_string.index('/', i)
        if index>0:
            first_string = input_string[:index-1] + input_string[index+1:]
            result.append(first_string)
        if index+1<len(input_string):
            second_string = input_string[:index] + input_string[index+2:]
            result.append(second_string)
        i = index + 1
    final_result = []
    for string in result:
        if '/' in string:
            final_result.extend(process_string(string))
        else:
            final_result.append(string)
    if '/' not in input_string:
        final_result = [input_string]
    return list(set(final_result))

def find_matching_matrices(input_string: str, output_string: str, admitted_n_of_mismatches: int=2) -> tuple:
    """Find then print source and target matrices 
    such that the translated input string matches the output string, 
    even if a partial match is found, it prints the matrices (see check_partial_match()).

    Args:
        input_string (str): the string to be translated.
        output_string (str): the target string to match.
        admitted_n_of_mismatches (int, optional): maximum number of allowed mismatches. Default is 2.

    Returns:
        tuple: tuple containing the source and target matrices.
    """
    while True:
        source_matrix, target_matrix = generate_matrices()
        translated_string = translate_string(input_string, source_matrix, target_matrix)
        if translated_string==output_string:
            return source_matrix, target_matrix
        if check_partial_match(translated_string, output_string, admitted_n_of_mismatches):
            print("Partial Match Found:")
            print_matrix(source_matrix, "Source")
            print_matrix(target_matrix, "Target")
            return source_matrix, target_matrix

def check_partial_match(translated_string: str, input_string: str, admitted_n_of_mismatches: int) -> bool:
    """Check if the translated string partially 
    matches the input string within an admitted number of mismatches.

    Args:
        translated_string (str): the translated string to check.
        input_string (str): the target string to match against.
        admitted_n_of_mismatches (int, optional): maximum number of allowed mismatches.

    Returns:
        bool: True if a partial match is found within the allowed mismatches, False otherwise.
    """
    for s in process_string(translated_string):
        if len(s)!=len(input_string):
            continue
        mismatch_count = sum(1 for char1, char2 in zip(s, input_string) if char1!=char2)
        if mismatch_count<=admitted_n_of_mismatches:
            return True
    return False
    
def build_vigenere_grid(keyword: str) -> tuple:
    """Given an input string, create the the Vigenère table.

    Args:
        keyword (str): the keyword used to generate the grid.

    Returns:
        tuple: tuple containing the grid and the original alphabet.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    remaining_letters = ''.join([letter for letter in alphabet if letter not in keyword])
    final_alphabet = remaining_letters + keyword
    grid = [final_alphabet[i:] + final_alphabet[:i] for i in range(len(final_alphabet))]
    return grid, alphabet

def translate_via_vigenere(input_string: str, start_pos: str, grid: list, ordinary_alphabet: str) -> str:
    """Transposes an input string using 
    the Vigenère table and a starting position (in the English alphabet).

    Args:
        input_string (str): the string to be transposed.
        start_pos (str): the starting letter in the English alphabet.
        grid (list): the Vigenère table used for transposition.
        ordinary_alphabet (str): the standard English alphabet.

    Returns:
        str: the transposed string.
    """
    translated_string = ""
    start_index = ordinary_alphabet.index(start_pos)
    
    for i, char in enumerate(input_string):
        row_index = (start_index + i) % len(grid)
        if char in grid[row_index]:
            col_index = grid[row_index].index(char)
            translated_string+=ordinary_alphabet[col_index]
        else:
            translated_string+=char
    return translated_string

def main():
    """Process command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="""
        Attempt at solving K4 via the 'KRYPTOS' Vigenère's 
        table with pre-selected initial position and symmetrical 
        matrix transposition. The end result is a pair of matrices 
        that binds the cipher with the plaintext."""
    )
    parser.add_argument('keyword', type=str, help="The keyword for the Vigenère's table (here 'KRYPTOS')")
    parser.add_argument('start_pos', type=str, help="The starting letter in the Vigenère's table (e.g. 'A')")
    parser.add_argument('input_string', type=str, help="The known cipher string (e.g. 'FLRVQQPRNGKSS')")
    parser.add_argument('output_string', type=str, help="The known plaintext string (e.g. 'EASTNORTHEAST')")
    parser.add_argument('admitted_n_mismatches', type=int, help="The allowed number of mismatches between the cipher and plaintext strings (e.g. 2)")
    args = parser.parse_args()

    start_pos = args.start_pos
    input_string = args.input_string
    output_string = args.output_string
    keyword = args.keyword
    admitted_n_mismatches = args.admitted_n_mismatches

    print("Searching for matching matrices...")
    grid, ordinary_alphabet = build_vigenere_grid(keyword)
    translated_string = translate_via_vigenere(input_string, start_pos, grid, ordinary_alphabet)
    source_matrix, target_matrix = find_matching_matrices(translated_string, output_string, admitted_n_mismatches)
    print("Input string:", input_string)
    print("Phase 1 transformation:", translated_string)
    deciphered_string = translate_string(translated_string, source_matrix, target_matrix)
    print("Phase 2 transformation:", deciphered_string)


if __name__=='__main__':
    # For reference.
    k4_cipher_no_interrogation = "OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR"
    k4_deciphered_seq = "EASTNORTHEASTBERLINCLOCK"
    k4_cipher_seq = "FLRVQQPRNGKSSNYPVTTMZFPK"
    # Residual variables.
    keyword = "KRYPTOS"
    start_pos = 'A'
    input_string = "FLRVQQPRNGKSS"
    output_string = "EASTNORTHEAST"
    admitted_n_mismatches = 2

    main()
