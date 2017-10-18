#function to convert decimal degrees to dms

import math

def dd2dms(dd):
    
    #find the whole degrees and assign them to d
    d = int(math.floor(dd))
    
    #single out the remainder of the dd and convert to whole minutes
    remainder = dd-d
    m = int(math.floor(remainder*60.0))
    
    #find the remainder of the minutes and convert to seconds
    s = ((remainder*60)-m)*60
    
    #return the concatenated values
    return d, m, s

print(dd2dms(23.45))
