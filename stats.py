def get_word_count(text):
    """
    Counts the number of words in a given text.
    Args: text (str): The text to count words in.
    Returns: int: The number of words in the text.
    """
    words = text.split()
    return len(words)

def character_type_count(text):
    convert_lower = text.lower()
    char_count_dict = {}    
    for char in convert_lower:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict