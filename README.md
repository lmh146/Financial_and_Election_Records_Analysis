# Python_Challenge

## Background

This project looks at two data sets, one on the financial records of a company and another on the voting outcome of a small town. The first part uses the financial data collected from the company to analyze changes in profits and losses over given periods of time. The second part creates a script to more efficiently count and total votes to conclude who won the election.

## PyBank

This script reads in a CSV file for which it then utilizes a for-loop to run through the profit data to append a list and obtain the count of how many months are in the data set. The script then calculates the total profits/losses and appends another list with the month to month change. Using the list of profit changes, it calculates the greatest increase and decrease in profit. The script concludes by writing to a new file the final financial analysis totaling the months and profits in addition to information on profit changes as pictured below.

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

## PyPoll

This script reads in its respective CSV file on the voting information by county for a recent election then using a for-loop begins the process of analyzing the voting data. By appending a list with each voter in the data, it is able to calculate the total number of votes. The script then uses conditionals within the for-loop to calculate the number of votes each candidate accumulated. The percentage of the vote each candidate received is then calculated utilizing both the total votes and the per candidate votes. Following this another conditional is implemented to print out the winner of the election based on the percentage of the vote they received. The script finishes by writing the election results including the total votes, percentage each candidate received, and the final winner as seen below to a separate file.

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```


