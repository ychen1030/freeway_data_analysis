import xlrd
import numpy as np
import matplotlib.pyplot as plt

# To open Workbook 
wb = xlrd.open_workbook("./pems_output.xlsx") 
sheet = wb.sheet_by_index(0) 
 

times = []
for i in range(1, sheet.nrows):
	times.append(sheet.cell_value(i, 1))

# print(times)
average = sum(times)/len(times)
print(average)

times = np.array(times)
values, base = np.histogram(times, bins=40)
# print(base, values)
total = float(np.sum(values))
cumulative = np.cumsum(values)/total
print(base[:-1], cumulative)
plt.plot(base[:-1], cumulative, c='blue')
plt.xlabel("Travel Time (min)")
plt.ylabel("Probability")
plt.show()
