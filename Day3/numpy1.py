
import numpy as np 

genArr = np.random.randint(100, 500, (30, 5))

print('Average stock price: ',end=' ')
print(genArr.mean(axis=0)) 

for i in range(30):
    for j in range(5):
        if genArr[i][j] == genArr.max():
            print(f"Highest Price recorded {genArr[i][j]} at Day {i+1}, company {j+1}")
            break

print("normalized prices: ")
nor = [np.round(((x - genArr.min()) / (genArr.max() - genArr.min())),3).tolist() for x in genArr]
print(nor)

print("Risky Investments Days:")
for i in range(30):
    li = []
    for j in range(5):
        
        if genArr[i][j] < 200:
            li.append(genArr[i][j])
    if(len(li) > 0):
        print(f"day{i+1}: [{', '.join(map(str, li))}]")
            
