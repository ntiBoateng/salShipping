weight = 1.5
#Ground Shipping
if weight <=2:
  cost_ground = weight*1.5+20
elif weight >2 and weight <=6:
  cost_ground = weight * 3+20
elif weight >6 and weight <=10:
  cost_ground = weight * 4+20
else:
  cost_ground = weight * 4.75+20

print(cost_ground)

cost_ground_premium = 125.00
print(cost_ground_premium)

#Drone shipping
if weight <=2:
  cost = weight*4.5
elif weight >2 and weight <=6:
  cost = weight * 9
elif weight >6 and weight <=10:
  cost = weight * 12
else:
  cost = weight * 14.25



print(cost)