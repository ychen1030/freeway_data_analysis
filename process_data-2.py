import xlrd
import numpy as np
import matplotlib.pyplot as plt

# To open Workbook 
wb = xlrd.open_workbook("./pems_output.xlsx") 
sheet = wb.sheet_by_index(0)
 
flows, density= [], []
for i in range(1, sheet.nrows):
	flow = [sheet.cell_value(i, 1), sheet.cell_value(i, 3), 
			sheet.cell_value(i, 5), sheet.cell_value(i, 7)]
	spd = [sheet.cell_value(i, 2), sheet.cell_value(i, 4), 
			sheet.cell_value(i, 6), sheet.cell_value(i, 8)]
	flows.append(sum(flow) * (60/5))
	density.append(sum([flow[i]/spd[i] for i in range(len(flow))] * (60/5)))


plt.scatter(density, flows, c='blue', s=1)
plt.xlabel("Density (Veh/Mile)")
plt.ylabel("Flow (Veh/Hour)")
plt.show()
