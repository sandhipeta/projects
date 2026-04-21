data = ["CampusX is a channel", "for data-science", "aspirants"]
result = []
for i in range(len(data)):
    sentence = data[i]
    words = sentence.split(" ")
    result.extend(words)

print(result)
    
    