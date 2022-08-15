"""Count words in file."""


def get_word_count(text_file):
    text = open(text_file)
    word_count = {}

    for line in text:
        line = line.rstrip()
        line = line.split(' ')

        for word in line:
            word = word.lower()
            if word.isalpha() == False:
                word = list(word)
                word = word[:-1]
                word = ''.join(word)
                word_count[word] = word_count.get(word, 0) + 1
            else:
                word_count[word] = word_count.get(word, 0) + 1

    return word_count


print(get_word_count('twain.txt'))

# import sys
# text = open(sys.argv[1])

# word_count = {}

# for line in text:
#     line = line.rstrip()
#     line = line.split(' ')

#     for word in line:
#         word_count[word] = word_count.get(word, 0) + 1
# for word, count in word_count.items():
#     print(word, count)


# def tokenize(filename):
#     words = []
#     text = open(filename)
#     for line in text:
#         line = line.rstrip()
#         line = line.split(' ')
#         for word in line:
#             words.append(word)
#     return words


# # print(tokenize("test.txt"))


# def count_words(words):

#     word_counts = {}

#     for word in words:
#         word_counts[word] = word_counts.get(word, 0) + 1

#     return word_counts


# # print(count_words(["apple", "berry", "cherry", "apple"]))

# def print_word_counts(word_counts):
#     for word, count in word_counts.items():
#         print(f'{word} {count}')


# # print_word_counts({'apple': 2, 'berry': 1, 'cherry': 1})
