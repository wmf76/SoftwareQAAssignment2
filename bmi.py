def bmi(weight,heightft,heightin):
    
    ht=(heightft*12+heightin)*0.025
    bmi= round((weight*0.45)/(ht*ht),1)

    classification="None"

    if(bmi<= 18.5):
        classification="Under weight"
    elif(bmi>18.5 and bmi<25):
        classification="Normal weight"
    elif(bmi>=25 and bmi<30):
        classification="Over weight"
    else:
        classification="Obese"
    return bmi , classification

