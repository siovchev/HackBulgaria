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

def groupby(func, seq):
    grouped_by = {}

    for element in seq:
        if func(element) not in grouped_by:
            grouped_by[func(element)] = []
        if func(element) in grouped_by:
            grouped_by[func(element)].append(element)

    return grouped_by



print(groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))
{0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}
print(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
{'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]}
print(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))
{0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]}

def reduce_file_path(path):
    import re
    pattern = "/(\w+)/../"
    while re.search(pattern, path) != None or "//" in path or "/./" in path:
        if re.search(pattern, path) != None:
            str_match = re.search(pattern, path)
            path = path.replace(str_match.group(), "/")
        path = path.replace("//", "/")
        path = path.replace("/./", "/")
    if "/../" in path:
        path = path.replace("/../", "/")
    if len(path) >= 2 and path[len(path) - 1] == "/":
        return path[:len(path) - 1]
    return path


print(reduce_file_path("/"))
"/"
print(reduce_file_path("/srv/../"))
"/"
print(reduce_file_path("/srv/www/htdocs/wtf/"))
"/srv/www/htdocs/wtf"
print(reduce_file_path("/srv/www/htdocs/wtf"))
"/srv/www/htdocs/wtf"
print(reduce_file_path("/srv/./././././"))
"/srv"
print(reduce_file_path("/etc//wtf/"))
"/etc/wtf"
print(reduce_file_path("/etc/../etc/../etc/../"))
"/"
print(reduce_file_path("//////////////"))
"/"
print(reduce_file_path("/../"))
"/"
print(reduce_file_path("/home/rex/Destop/././python/home/.././tasks/./"))
"/"

def is_an_bn(word):
    word_length = len(word)

    if word_length == 0:
        return True

    if word_length == 1:
        return True

    compare_str = "a" * (word_length // 2) + "b" * (word_length // 2)
    if compare_str == word:
        return True

    return False



print(is_an_bn(""))
True
print(is_an_bn("rado"))
False
print(is_an_bn("aaabb"))
False
print(is_an_bn("aaabbb"))
True
print(is_an_bn("aabbaabb"))
False
print(is_an_bn("bbbaaa"))
False
print(is_an_bn("aaaaabbbbb"))
True

def simplify_fraction(fraction):
    bigger_number = max(fraction)
    nominator = fraction[0]
    denominator = fraction[1]

    for divisor in range(1, bigger_number):
        if nominator % divisor == 0 and denominator % divisor == 0:
            nominator //= divisor
            denominator //= divisor

    return (nominator, denominator)

print(simplify_fraction((3,9)))
(1,3)
print(simplify_fraction((1,7)))
(1,7)
print(simplify_fraction((4,10)))
(2,5)
print(simplify_fraction((63,462)))
(3,22)

