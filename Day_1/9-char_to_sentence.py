data = [['c','a','m','p','u','x'], ['i','s'],['b','e','s','t'],['c','h','a','n','n','e','l']]

words = []

for sublist in data:
    word = ''.join(sublist)   
    words.append(word)

result = ' '.join(words)    

print(result)