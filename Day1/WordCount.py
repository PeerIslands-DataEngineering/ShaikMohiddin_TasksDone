

def find_cnt(li):
    dic = {}
    for i in li:
        for j in i:
            if j.lower() == 'stop':
                break
            elif j in dic and len(j) > 3:
                dic[j] += 1
            elif len(j) > 3:
                dic[j.lower()] = 1
        if j == 'stop':
            break
                
    return dic

paragraph = [
    ["Hello", "world", "hello"],
    ["this", "is", "a", "test"],
    ["STOP", "ignore", "this", "line"],
    ["should", "not", "be", "processed"]
]

print(find_cnt(paragraph))