##1.remove duplicates from string

anime_character =input("enter the char_name: ")
result=""
for words in anime_character:
    if words not in result:
        result += words
        
print(result)

##2.remove duplicate words from string

para = input("Enter the sentence: ")
words = para.split()
result = []

for word in words:
    if word not in result:
        result.append(word)

print("Result:", " ".join(result))

##3.sort the letters in a word

word = input("Enter the word: ")
letters = list(word)
for i in range(len(letters)):
    for j in range(i+1, len(letters)):
        if letters[i] > letters[j]:
            letters[i], letters[j] = letters[j], letters[i]

print("".join(letters))


#bubble sort

bubble_sort =["audi","benz","byd","tesla","ferrai","porsche","madza","jaguar","Rmd","rr"]
n = len(bubble_sort)

for i in range(n):
    for j in range(0,n-i-1):
        if bubble_sort[j]>bubble_sort[j+1]:
            bubble_sort[j], bubble_sort[j+1] = bubble_sort[j+1],bubble_sort[j]

print("bubble sorted list: ",bubble_sort)

##bubble sorted list:  ['Rmd', 'audi', 'benz', 'byd', 'ferrai', 'jaguar', 'madza', 'porsche', 'rr', 'tesla']


#selection sort

selection_sort =["audi","benz","byd","tesla","ferrai","porsche","madza","jaguar","rmd","RR"]
n = len(selection_sort)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if selection_sort[j] < selection_sort[min_index]:
            min_index = j

    selection_sort[i], selection_sort[min_index] = selection_sort[min_index], selection_sort[i]

print("selection Sorted list:", selection_sort)

##selection Sorted list: ['RR', 'audi', 'benz', 'byd', 'ferrai', 'jaguar', 'madza', 'porsche', 'rmd', 'tesla']

