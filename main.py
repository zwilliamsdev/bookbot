def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    letter_counts = get_letter_counts(text)
    create_report(book_path, num_words, letter_counts)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_counts(text):
    letter_counts = {}
    text = text.lower()
    for letter in text:
        if letter.isalpha() and not letter in letter_counts:
            letter_counts[letter] = 1
        elif letter.isalpha():
            letter_counts[letter] += 1
    return letter_counts

def sort_on(dict):
    return dict["count"]

def create_report(book_path, word_count, letter_count):
    letter_list = [{'letter':key, 'count':value} for key, value in letter_count.items()]
    letter_list.sort(reverse=True, key=sort_on)

    # Print report
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for letter in letter_list:
        print(f"The '{letter['letter']}' was found {letter['count']} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()

