"""Problema 1:

Dada una cadena de texto, escribe una función que devuelva un 
valor booleano que indique si es un palíndromo o no. Se dice 
que una cadena es un palíndromo si el reverso de la cadena es 
el mismo que la cadena. Por ejemplo, "malayalam" es un palíndromo, 
"geek" no lo es.
"""

def is_palindrome(word: str) -> bool:
    """Check if a word or sentence is palindrome
    
    This function cleans the input by keeping only the alphabetic 
    characters and converts them to lowercase. It then checks if 
    the cleaned word is the same as its reversed version.

    Args:
        word: A string to check if it is palindrome.

    Returns:
        bool: True if the input string is a palindrome, otherwise False.

    Raises:
        TypeError: If the input is not a string.
    """

    if not isinstance(word, str):
        raise TypeError(f"Expected a string, but got {type(word).__name__}")

    # Remove non-alphabetic characters and convert the string to lowercase
    cleaned_word = "".join(char.lower() for char in word if char.isalpha())

    # Compare the cleaned word with its inverted version
    return cleaned_word == cleaned_word[::-1]