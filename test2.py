def compute_grad(x):
    if(x>=90 & x<=100):
        grade = 'A'
    elif (x>=75 & x<90):
        grade = 'B'
    elif (x>=60 & x<75):
        grade = 'C'
    else:
        grade = "D"    
    return(grade)
compute_grad(67)