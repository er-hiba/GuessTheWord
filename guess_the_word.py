def valid(T):
    if 4 <= len(T) <= 25 and T.isupper() == True :
        return True

word = input("Enter a word (with capital letters between 4 and 25): ")

while valid(word) != True :
    word = input("Enter a valid word: ")

word = [char for char in word]

text = [] 
for i in range(len(word)):
    text.append("*")

n_attempts = 0

while word != text :
    letter = input("Enter a letter: ")
    for i in range(len(word)):
        if letter == word[i] :
            text[i] = letter
    if text.count(letter) == 0 :
        n_attempts += 1

    if n_attempts == 5 :
        break

if word == text :
    print("You guessed the word.")
else:
    print("Game Over. You couldn't guess the word.")
