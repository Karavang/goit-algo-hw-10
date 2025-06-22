from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, value


model = LpProblem("Maximize_Production", LpMaximize)
lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")
model += lemonade + fruit_juice, "Total_Production"
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Limit"
model += 1 * lemonade <= 50, "Sugar_Limit"
model += 1 * lemonade <= 30, "Lemon_Juice_Limit"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Limit"

model.solve()

print("Статус:", LpStatus[model.status])
print("Кількість лимонаду:", lemonade.varValue)
print("Кількість фруктового соку:", fruit_juice.varValue)
print("Максимальна кількість продуктів:", value(model.objective))
