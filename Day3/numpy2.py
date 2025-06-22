import numpy as np

genArr = np.random.randint(10, 99 ,(6,3))

sumo = 0
sumw = 0
sumf = 0
for i in range(6):
    for j in range(3):
        if j == 0:
            sumo += genArr[i][j]
        elif j == 1:
            sumw += genArr[i][j]
        elif j == 2:
            sumf += genArr[i][j]
            
print(f"Total resources needed (tons): Oxygen: {sumo}, Water: {sumw}, Food: {sumf}")

maxi = genArr.max()
for i in range(6):
    for j in range(3):
        if genArr[i][j] == maxi:
            if j == 0:
                print(f"Highest consumption in a month: Water ({genArr[i][j]} tons in month {i+1})")
            elif j == 1:
                print(f"Highest consumption in a month: Oxygen ({genArr[i][j]} tons in month {i+1})")
            else:
                print(f"Highest consumption in a month: Food ({genArr[i][j]} tons in month {i+1})")
        break

oxygen_std = np.std(genArr[:, 0], ddof=0)
water_std = np.std(genArr[:, 1], ddof=0)
food_std = np.std(genArr[:, 2], ddof=0)

# Print result
print("Standard deviation of consumption:")
print(f"Oxygen: {oxygen_std:.1f}, Water: {water_std:.1f}, Food: {food_std:.1f}")

print("Transposed matrix: ")
print(genArr.T)