def combiner(data):
    sum = 0
    word = []
    for item in data:
        if isinstance(item, str):
            word.append(item)
        else:
            sum += item
    return ''.join(word) + str(sum)
