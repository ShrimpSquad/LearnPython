# Define a function which reverses the word order of a sentence:
# e.g. Hello there my friend --> friend my there Hello

def reverse_sentence(sentence):
    list_of_sentence = sentence.split(" ")
    list_of_sentence.reverse()
    reversed_sentence = " ".join(list_of_sentence)
    return reversed_sentence

print(reverse_sentence("Hello there my friend"))