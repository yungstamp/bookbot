def main():
    book_path = "books/frankenstein.txt"
    word_count_result = word_count(book_path)
    sorted_alpha_counts = count_report(book_path)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count_result} words found in the document\n")

    for char, count in sorted_alpha_counts:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

def get_text(book_path):
    with open (book_path) as f:
        return f.read()
    
def word_count(book_path):
    text = get_text(book_path)
    words = text.split()
    return len(words)

def char_count(book_path):
    text = get_text(book_path)
    text_lower = text.lower()
    char_storage = {}
    for char in text_lower:
        if char in char_storage:
            char_storage[char] +=1
        else:
            char_storage[char] = 1
    return char_storage

def count_report(book_path):
    char_count_results = char_count(book_path)
    alpha_counts = []
    for char in char_count_results:
        if char.isalpha():
            alpha_counts.append((char, char_count_results[char]))
        else:
            pass
    sorted_alpha_counts = sorted(alpha_counts, key=lambda x: x[1], reverse=True)
    return sorted_alpha_counts
    
        

if __name__ == "__main__":
    main()