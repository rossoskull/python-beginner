
def intPolSearch(values,x ):
    idx0 = 0
    idxn = (len(values) - 1)

    while idx0 <= idxn and x >= values[idx0] and x <= values[idxn]:


	mid = idx0 +\
               int(((float(idxn - idx0)/( values[idxn] - values[idx0]))
                    * ( x - values[idx0])))


        if values[mid] == x:
            return "Found "+str(x)+" at index "+str(mid)

        if values[mid] < x:
            idx0 = mid + 1
    return "NOT PRESENT"


l = [1, 2, 45, 64, 244, 23, 54, 12]
print(intPolSearch(l, 2))