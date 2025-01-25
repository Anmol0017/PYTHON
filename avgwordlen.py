strr = input("Enter a santance:")

words = strr.split(" ")
sum=0
total_words = len(words)

for word in words:
    temp = word
    sum+=len(temp)
    
print(sum/total_words)