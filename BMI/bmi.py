def bmi(weight,heightft,heightin):
    
    ht=(heightft*12+heightin)*0.025
    bmi= round((weight*0.45)/(ht*ht),1)
    
    return bmi

