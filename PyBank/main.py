import os
import csv

from numpy import maximum

#Refernce File
PyBank_csv = os.path.join('Resources', 'budget_data.csv').replace("\\", "/")


#Variables
Months = []

Ttl_ProfitLosses = 0

Profit_Change = []
Last_ProfitLoss = 0

Date = []


#Open File
with open(PyBank_csv, 'r') as bankfile:
    csv_reader = csv.reader(bankfile, delimiter=',')
    
    #Skip the First Line
    header = next(csv_reader)


    #For Loop to Extract Data
    for row in csv_reader:

        
        #Month Count
        Months.append(row[0])
        

        #Calculate Total Profits/Losses
        Present_ProfitLoss = int(row[1])
        Ttl_ProfitLosses = Ttl_ProfitLosses + Present_ProfitLoss


        #Row to Row Change
        Present_Change = Present_ProfitLoss - Last_ProfitLoss
        Profit_Change.append(Present_Change)

        Last_ProfitLoss = Present_ProfitLoss



#Max and Min
Maximum = max(Profit_Change)
Max_Index = Profit_Change.index(Maximum)

Max_Date = Months[Max_Index]

    

Minimum = min(Profit_Change)
Min_Index = Profit_Change.index(Minimum)               

Min_Date = Months[Min_Index]
       



#Finding the Average Change
Profit_Change.pop(0)
Average = round(int(sum(Profit_Change)) / int(len(Profit_Change)), 2)
        
        
#Print Statements
print('Finanacial Analysis')
print('---------------------------------------------')
print(f'Total Months: {len(Months)}')
print(f'Total: ${Ttl_ProfitLosses}')
print(f'Average Change: ${Average}')
print(f'Greatest Increase in Profits: {Max_Date} (${Maximum})')
print(f'Greatest Increase in Profits: {Min_Date} (${Minimum})')

Total = len(Months)

#Write into File
output_bankfile = os.path.join("bankfile.csv")
with open(output_bankfile, 'w') as final_bankfile:
    writer = csv.writer(final_bankfile)

    writer.writerow(['Finanacial Analysis'])
    writer.writerow(['---------------------------------------------'])
    writer.writerow([f'Total Months: {Total}'])
    writer.writerow([f'Total: ${Ttl_ProfitLosses}'])
    writer.writerow([f'Average Change: ${Average}'])
    writer.writerow([f'Greatest Increase in Profits: {Max_Date} (${Maximum})'])
    writer.writerow([f'Greatest Increase in Profits: {Min_Date} (${Minimum})'])

