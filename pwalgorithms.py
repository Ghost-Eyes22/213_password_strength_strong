# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):    #user input
  words = get_dictionary()     # get[list] from dictionary
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1      #increment number of guesses
    if (w == password):
      return True, guesses
  return False, guesses
