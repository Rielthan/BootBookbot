def get_book_text(filepath):
    """
    Reads the content of a book from a given file path.
    
    Args:
        filepath (str): The path to the book file.
        
    Returns:
        str: The content of the book.
    """
    with open(filepath) as file:
        return file.read()

from stats import get_word_count, character_type_count

def main():
    # Call get_book_text with the path to frankenstein.txt
    book_content = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_content)
    char_counts = character_type_count(book_content)
    # Print the content
    print(f"{word_count} words found in the document")
    print(char_counts)

main()