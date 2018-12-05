### PyBank Script:
### Analyzing financial records
### Tomoko Takita
### December 2018

import csv

# initialize variables
totalMonths = 0
total = 0
avgChng = 0
grtInc = 0
grtDec = 0

# Open de CSV file in read-only mode
with open("budget_data.csv", "r") as data:

    # Parse de CSV file
    reader = csv.reader(data)

    # Read the Header from the Data in order to exclude it from the analysis
    data.readline()

    # Loop through the lines/rows in the data
    for row in reader:
        # Accumulate the P/L in the variable 'total'
        total += float(row[1])
        ## Analyze Monthly changes
        # The conditional makes sure it starts on the second month of the data
        if totalMonths > 0 :
            # Calculates the monthly changes
            chng = float(row[1]) - prevMonthPL
            # Accumulate the monthly changes in order the calculate the average
            avgChng += chng
            # Find the greatest increase and save it in a variable
            if chng > grtInc :
                grtInc = chng
                grtIncDt = row[0]
            # Find the greatest decrease and save it in a variable
            elif chng < grtDec :
                grtDec = chng
                grtDecDt = row[0]
        # Update the counter for the number of months
        totalMonths += 1
        # Keep data from the previous month in order to calculate changes
        prevMonthPL = float(row[1])

    # Final calculation for the average
    avgChng /= (totalMonths-1)

    # Print results in Terminal
    print ("Total Months:  " + str(totalMonths))
    print ("Total:  " + "${:,.2f}".format(total))
    print ("Average Change:  " + "${:,.2f}".format(avgChng))
    print ("Greatest Increase in Profits:  " + grtIncDt + "   (" + "${:,.2f}".format(grtInc) + ")")
    print ("Greatest Decrease in Profits:  " + grtDecDt + "   (" + "${:,.2f}".format(grtDec) + ")")

    # Create/fill/Close the Results file
    results = open("results.txt", "w")
    results.write("Total Months:  " + str(totalMonths) + "\n")
    results.write("Total:  " + "${:,.2f}".format(total) + "\n")
    results.write("Average Change:  " + "${:,.2f}".format(avgChng) + "\n")
    results.write("Greatest Increase in Profits:  " + grtIncDt + "   (" + "${:,.2f}".format(grtInc) + ")" + "\n")
    results.write("Greatest Decrease in Profits:  " + grtDecDt + "   (" + "${:,.2f}".format(grtDec) + ")" + "\n")
    results.close()

# Close the data file
data.close()