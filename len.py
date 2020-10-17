
def find_longest_word(words_list):
    max= []
    for n in words_list:
        max.append((len(n), n))
    max.sort()
    return max[-1][1]

print(find_longest_word(['aba','auranbgadsa','hjk']))