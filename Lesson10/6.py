def getPercent(sal,per,costs):
    total = sal*per-costs
    return total

salary=1000
percent = 0.3
costs = 100
total_salary=salary+getPercent(salary,percent,costs)
print(total_salary)