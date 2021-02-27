def savings_per_year(salary,percent_saved):
    return round((salary*percent_saved)*1.35,2)

def num_years_till_goal(savings_goal,savings_per_year):
    return round(savings_goal/savings_per_year,0)

def age_when_goal_met(age, num_years_till_goal):
    return round(age+num_years_till_goal,0)

