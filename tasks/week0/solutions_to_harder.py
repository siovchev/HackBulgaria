def count_words(arr):
    word_occurrences = {}
    copy_arr = arr
    while len(copy_arr) != 0:
        first_word = copy_arr[0]
        occurrences = 0
        for word in copy_arr:
            if first_word == word:
                occurrences += 1
        word_occurrences[first_word] = occurrences
        while first_word in copy_arr:
            copy_arr.remove(first_word)
    return word_occurrences

print(count_words(["apple", "banana", "apple", "pie"]))
{'apple': 2, 'pie': 1, 'banana': 1}
print(count_words(["python", "python", "python", "ruby"]))
{'ruby': 1, 'python': 3}

def unique_words_count(arr):
    unique_words = 0
    copy_arr = arr

    while len(copy_arr) != 0:
        first_word = copy_arr[0]
        while first_word in copy_arr:
            copy_arr.remove(first_word)
        unique_words += 1

    return unique_words

print(unique_words_count(["apple", "banana", "apple", "pie"]))
3
print(unique_words_count(["python", "python", "python", "ruby"]))
2
print(unique_words_count(["HELLO!"] * 10))
1