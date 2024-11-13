def ComparisonCountingSort(unsortedarray):
    sortedarray = [0] * len(unsortedarray)
    count = [0] * len(unsortedarray)
    for i in range(0, len(unsortedarray)-1):
        for j in range(i+1, len(unsortedarray)):
            if unsortedarray[i] < unsortedarray[j]: 
                count[j] += 1
            else:
                count[i] += 1
    for i in range(0, len(unsortedarray)):
        sortedarray[count[i]] = unsortedarray[i]
    return sortedarray