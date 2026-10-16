#no outside resources used
#defines heights for later use
heights = []

#defines the function that calculates when the next slope is lower than the current, and returns the number of times that happens
def airtime(length,heights):
    #defines variables
    roc = 0
    previous_roc = 0
    airtime = 0
    #for the length of the entire list, loop
    for i in range(length-1):
        #the rate of change is the next value minus the current
        roc = heights[i+1]-heights[i]
        #if its the first iteration, make previous_roc equal to roc
        if i==0:
            previous_roc = roc
        #if previous_roc is equal to roc, airtime counts up by one
        if previous_roc > roc:
            airtime += 1
        #at the end of the loop, make previous_roc equal to roc
        previous_roc = roc
    #after the loop, return the final value of airtime
    return airtime

#for the given length in the first input, take every remaining input and add it to a list
if __name__ == "__main__":
    length = int(input())
    for _ in range(length):
        heights.append(int(input()))

    #print the value given by the function airtime when given the list heights
    print(airtime(length,heights))