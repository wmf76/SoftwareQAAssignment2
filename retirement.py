def savings_per_year(salary,percent_saved):
    return round((salary*percent_saved)*1.35,2)

def num_years_till_goal(savings_goal,savings_per_year):
    return round(savings_goal/savings_per_year,0)

def age_when_goal_met(age,salary,percent_saved,goal):
    spy=savings_per_year(salary,percent_saved)
    nyt=num_years_till_goal(goal,spy)
    age_when_goal_meet= round(age+nyt,0)

    goal_meet=True
    if(age_when_goal_meet>=100):
        goal_meet=False
    return age_when_goal_meet, goal_meet

