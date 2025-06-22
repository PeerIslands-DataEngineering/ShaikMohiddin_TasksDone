import numpy as np 

genarr = np.random.randint(10, 50 ,(5,10))
print(genarr)

print("Average points per game:")
avgli = []
for i in range(5):
    sum = 0
    for j in range(10):
        sum += genarr[i][j]
        
    avgli.append(np.round(sum/5, 2).tolist())
print(avgli)

print("Games with scores above 30: ")
for i in range(5):
    li = []
    for j in range(10):
        if genarr[i][j] > 30:
            li.append(j+1)
        
    if(len(li) > 0):
        print(f"Player {i+1}: Games [{', '.join(map(str, li))}]")
        
print("Sorted players by Total Points:")
sorted_indices = np.argsort(genarr.sum(axis=1))[::-1]
for index in sorted_indices:
    print(f"Player {index + 1} - {genarr[index].sum()} points")