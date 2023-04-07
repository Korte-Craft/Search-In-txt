def search_word(filename, keyword):
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if keyword in line:
                print(f'Keyword {i+1}. line: {line.strip()}')


filename = input("Filename: ")
keyword = input("Keyword: ")

search_word(filename, keyword)
