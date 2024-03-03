def main():
    report_file("books/frankestein.txt")

def report_file(file_name: str):
    content = read_from_file(file_name)
    words = count_words(content)
    characters_count = count_characters(content)

    print(f"--- Begin of report of {file_name} ---")
    print(f"{words} words found in the document")
    print()
    for char in characters_count:
        print(f"The '{char["char"]}' character was found {char["count"]} times")
    print("---End of report ---")


def read_from_file(file_name: str):
    with open(file_name) as f:
        return f.read()

def count_words(content: str):
    words = content.split()
    return len(words)

def count_characters(content: str):
    characters_count = dict()
    words = content.split()
    for word in words:
        for char in word:
            if char.lower() < 'a' or char.lower() > 'z':
                continue
            if char.lower() not in characters_count:
                characters_count[char.lower()] = 0
            characters_count[char.lower()] += 1

    sorted = []
    for char in characters_count:
        sorted.append({"char": char, "count": characters_count[char]})

    sorted.sort(reverse=True, key=sort_on)

    return sorted

def sort_on(dict):
    return dict["count"]

main()
