def ackermann(m,n):
    if m < 0 or n < 0:
        return (f"The numbers must be positive.")
    if m==0:
      
        return n+1
    elif m>0 and n==0:
                                              
        return ackermann(m-1,1)
    elif m>0 and n>0:
                     
        return ackermann(m-1,ackermann(m,n-1)) 

ackermann(3 , 0)