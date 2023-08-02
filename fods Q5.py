import numpy as np


fuel_efficiency = np.array([25.0, 30.0, 28.0, 35.0, 22.0, 20.0, 18.0, 32.0, 26.0, 24.0])


average_fuel_efficiency = np.mean(fuel_efficiency)


car_model_index1 = 1
car_model_index2 = 4


fuel_efficiency_car1 = fuel_efficiency[car_model_index1]
fuel_efficiency_car2 = fuel_efficiency[car_model_index2]


percentage_improvement = ((fuel_efficiency_car2 - fuel_efficiency_car1) / fuel_efficiency_car1) * 100

print("Average fuel efficiency: {:.2f} miles per gallon".format(average_fuel_efficiency))
print("Percentage improvement in fuel efficiency between Car Model {} and Car Model {}: {:.2f}%".format(
    car_model_index1, car_model_index2, percentage_improvement))
