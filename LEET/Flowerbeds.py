def canPlaceFlowers(flowerbed, n):
    count = 0 
    for i in range(len(flowerbed)): #range and len so we can go all over every element and find.
        if flowerbed[i] == 0: # check if selected flowerbed is zero or not if it is zero then check right and left flwoerbeds to see if they are zero.
            empty_right_plot = (i == len(flowerbed) -1) or (flowerbed[i+1] == 0) #check if current plot is the last plot in flowerbed if not then right plot next to curret will be zero
                               #i == flowerbed[-1] is wrong because it gives the value of the last plot in flowerbed not the index 
            empty_left_plot = (i == 0) or (flowerbed[i-1] == 0) #the current postition is zero or a position left to current is zero
            if empty_right_plot and empty_left_plot: # if right and left flowerbeds are zero then put a flower in the selected plot.
                flowerbed[i] = 1 #putting flower on the empty plot.
                count += 1 #then count increased by 1 because a flower is now added to the bed.
    return count >= n #check and return true or false if count is bigger or equal to amount of flowers can be added 

print(canPlaceFlowers([1,0,0,0,1,0,0], 1))