import movieRequests as mr

ratings = []
with open("ratingsOutput.txt", "r") as file:
    for line in file:
        positionList = 0
        (k, v) = line.split()
        tempArr = [k, v]
        ratings.append(tempArr)
    file.close()
print(ratings)
