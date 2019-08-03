import os
import csv

budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

#Print results
def print_data(TotalMonth, NetTotal, AvgChange, GreatestProfit_M,
                GreatestProfit, GreatestLoss_M, GreatestLoss):
    #Results
    print('Financial Analysis')
    print('______________________________')
    print(f"Total Months: {TotalMonth}")
    print(f"Total:  ${NetTotal}")
    print(f"Averge Change: {round(NetTotal / (TotalMonth)),2}")
    print(f"Greatest increase in profit: {GreatestProfit_M} (${GreatestProfit})")
    print(f"Total Months: {GreatestLoss_M} (${GreatestLoss})")

firstRow=True
TotalMonth=0
NetTotal=0
GreatestProfit=0
GreatestLoss=0
GreatestProfit_M=0
GreatestLoss_M=0
total=0
previoustotal=0
totalChange=0

# Open and read csv
with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

   # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    # print(f"Header: {csv_header}")

    for row in csvreader:
            date = row[0]
            currenttotal = int(row[1])
            gainloss = total - previoustotal

            if firstRow ==True:
                firstRow = False
            else:
                 totalChange += gainloss

            if gainloss > GreatestProfit: 
                GreatestProfit = gainloss
                GreatestProfit_M = date
            elif gainloss < GreatestLoss:
                GreatestLoss = gainloss
                GreatestLoss_M = date

            previoustotal = currenttotal
            TotalMonth += 1
            NetTotal+= currenttotal

with open('Financial_Analysis.txt', 'w') as txtwriter:
    txtwriter.write("inancial Analysis" + "\n")
    txtwriter.write("______________________________" + "\n")
    txtwriter.write(f"Total Months: {TotalMonth}" + "\n")
    txtwriter.write(f"Total:  ${NetTotal}" + "\n")
    txtwriter.write(f"Averge Change: {round(NetTotal / (TotalMonth)),2}" + "\n")
    txtwriter.write(f"Greatest increase in profit: {GreatestProfit_M} (${GreatestProfit})" + "\n")
    txtwriter.write(f"Total Months: {GreatestLoss_M} (${GreatestLoss})")