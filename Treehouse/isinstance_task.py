def combiner(list_of_datas):
    sum = 0
    words = []
    for item in list_of_datas:
        if isinstance(item, str):
           words.append(item) 
        else:
            sum += item
    return ''.join(words) + str(sum)  


print(combiner(["apple", 5.2, "dog", 8]))
