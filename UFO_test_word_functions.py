
def word_reader(updated_guess_so_far):
    index = 0
    dictionary_of_letters = {}
    for letter in updated_guess_so_far:
        if letter != "_":
            dictionary_of_letters[index] = letter
        index += 1
    return dictionary_of_letters

# here dicitonary_of_letters is represented by secret_word_bits, which is ultimately a dicitonary

def word_searcher(secret_word_bits, excluded_letters):
    f = open('nouns.txt', 'r')
    words_list = f.readlines()
    f.close()
    possible_words_list = []
    for word in words_list:
        if len(secret_word_bits) != len(word.strip('\n')):
           continue
        else:
           #use word_reader to convert the word in words_list into a dictionary that can be compared with a dicitonary from the updated_guess_so_far
           dictionary_of_letters_in_words_list = word_reader(word)
           superset = dictionary_of_letters_in_words_list
           dictionary_of_letters_in_secret_word_bits = word_reader(secret_word_bits)
           subset = dictionary_of_letters_in_secret_word_bits
           if all(item in superset.items() for item in subset.items()):
               possible_words_list.append(word.strip('\n'))
    print(possible_words_list)
    filtered_list = []
    for word in possible_words_list:
        letter_found = False
        print("word high level: " + word)
        for letter in excluded_letters:
            # print("letter high level: " + letter)
            if letter in word:
                letter_found = True
                # print("word: " + word)
                # possible_words_list.remove(word)
                break
        if letter_found == False:
            filtered_list.append(word)

    print(filtered_list)
    return filtered_list

 #TEST

word_searcher("_______un_", "b")
