def get_book_text(path_to_file):
    #1. Takes Filepath as Input
    with open (path_to_file) as f:
    #2. Returns Contents of File as a String
        return f.read()

def main():
    path="books/frankenstein.txt"
    text = get_book_text(path)
    result = num_words(text)
    print (result)

def num_words(text):
    words = text.split()
    word_count = len(words)
    return f"{word_count} words found in the document"

main()


