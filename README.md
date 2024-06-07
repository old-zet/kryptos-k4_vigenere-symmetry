# kryptos-k4_vigenere-symmetry
Algorithmic implementation of the Avirai's proposition to solve KRYPTOS' K4 via the 'KRYPTOS' Vigenère's table with randomized initial position and symmetry transposition via a pair of inversed matrices (cf. https://www.reddit.com/r/codes/comments/wwqj3m/kryptos_yar_east_north_east_and_muko/)

## DESCRIPTION
Launch decipher_k4 in CMD (no modules required). The positional arguments are:

_keyword_: The keyword for the Vigenère's table (e.g. 'KRYPTOS')
  
_start_pos_: The starting letter in the Vigenère's table (e.g. 'A')

_input_string_: The known cipher string (e.g. 'FLRVQQPRNGKSS')
  
_output_string_: The known plaintext string (e.g. 'EASTNORTHEAST')
  
_admitted_n-mismatches_: The allowed number of mismatches between the cipher and plaintext strings

Thus, 'python decipher_k4.py KRYPTOS A QQPRNGKSS NORTHEAST 2' produces: 

_Source Matrix_  |||  _Target Matrix_ 

K/H B W E I	|||	I E W B K/H 

V L N C X	|||	X C N L V 

F Z J Y G	|||	G Y J Z F 

A M Q O D	|||	D O Q M A 

T P S U R	|||	R U S P T 


__Phase 1 transformation: NMURIBNSR__ 

__Phase 2 transformation: NOPTK/HENST__

Which means that 'NMURIBNSR' is obtained from ciphertext 'QQPRNGKSS' if the process starts at the letter A in the the 'KRYPTOS' Vigenère's table; then 'NOPTK/HENST' is produced via the found pair of matrices, where the source matrix takes every letter in 'NMURIBNSR' then translates them via the target matrix to obtain 'NOPTK/HENST', or simply 'NOPTHENST', where two letters mismatch the plaintext, as defined by the last argument '2'.

## DISCUSSION
More combinations of 'keyword' and 'start_pos' must be tested.

Yet, KRYPTOS' K4 doesn't budge for now over 35 years, despite the efforts of thousands of cryptanalysts, mathematicians, and artists. It is a testament to poor ciphering decisions and the creator's amateurism. 

It will die out with its creator soon enough, he's 75 after all. Such flawed codes should be forgotten.
