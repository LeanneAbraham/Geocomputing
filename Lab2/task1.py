#create a function which returns inputed degrees, minutes,
#and seconds as decimal degrees
def dms2dd(d,m,s):
    #convert dms to dd
    
    #convert inputed values and add them together
    #to complete the converstion to a single value
    
    d = float(d)
    
    #ensure that if a negative degree is
    #used the other inputs are also negative
    if (d<0):
        m = float((m/60.0)*-1)
        s = float((s/3600.0)*-1)
    else:
        m = float(m/60.0)
        s = float(s/3600.0)
    
    #combine the converted values
    dd = s+m+d
    
    return dd

print(dms2dd(23,45,12))
