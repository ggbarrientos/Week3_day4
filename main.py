#names     German B , Ignacio E



# String Methods Practice #1
#slieds 12 -16
# Print the following text in uppercase, using the specific string method:
# "Especially in electronic communications, writing in all caps is equivalent to yelling."
# sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
print(sentence.upper())
# String Methods Practice #2
# Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.
# word_list = ["Simple","is","better","than","complex."]
word_list = "Simple","is","better","than","complex."
print(" ".join(word_list))
# String Methods Practice #3
# Replace in the following sentence:
# "If the implementation is hard to explain, it might be a bad idea."
# the following pairs of words:
# "hard" --> "easy"
# "bad" --> "good"
# and display the sentence with both words modified.
sentence = "If the implementation is hard to explain, it might be a bad idea."
print(sentence.replace("hard" , "easy"))
print(sentence.replace("bad" , "good"))
#################################string properties################################

# String Properties Practice #1
# Concatenate the text "Repetition" 15 times and display the result on the screen.
# Luckily, you know that strings are multipliable and you can do this activity in a simple and elegant way.
text= "Repetition"
print(text *15 )
# String Properties Practice #2
# Check if the word "beach" is not found in the following haiku. You should print the boolean.
# "Whitecaps on the bay:
# A broken signboard banging
# In the April wind."
# — Richard Wright, collected in Haiku: This Other World, 1998
haiku = "Whitecaps on the bay:A broken signboard banging In the April wind."
print(haiku.find("beach"))
# String Properties Practice #3
# Check the Python Documentation to find the description of the len() function. Then, display on the screen the length (in number of characters) of the word electroencephalographist.
W="electroencephalographist"
print(len(W))
#######