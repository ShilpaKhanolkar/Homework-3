import os
import csv

#read the 2 budget csv files
file_no=['1','2']
for num in file_no:
    print()
    print("For Paragraph" + str(num))

    csv_path=os.path.join("raw_data","budget_data_"+num+".csv")
    newoutput=os.path.join("raw_data","output"+num+".txt")

    with open(csv_path, mode='r', newline="", encoding="utf-8") as csv_file:
        csvReader=csv.DictReader(csv_file, delimiter=',')

        # The total number of months included in the dataset
        data = list(csvReader)
        row_count = len(data)
        print("Total months: " + str(row_count))

    #Write to a txt file    
    with open(newoutput, mode='w') as txt_file:
        txt_file.write("Total months: " + str(row_count) + '\n')

    #The total amount of revenue gained over the entire period
    with open(csv_path, mode='r', newline="", encoding="utf-8") as csv_file:  
        csvReader=csv.reader(csv_file, delimiter=',')  
        next(csvReader,None)
        total_revenue=0
        change_in_revenue_list=[]
        change=0
        old_revenue=0
        no_of_months=0
        month_list=[]

        for row in csvReader:

            #calculate total revenue
            total_revenue=total_revenue+int(int(row[1]))

            #calculate change in revenue
            change=int(row[1])-old_revenue
            old_revenue=int(row[1])
            change_in_revenue_list.append(change)
            no_of_months=no_of_months+1
            month_list.append(str(row[0]))

        print("Total revenue: $"+str(total_revenue))

        #remove the first value from change_in_revenue_list and month_list since it is the actual revenue value and not the change
        change_in_revenue_list.pop(0)
        month_list.pop(0)

        #Calculate average change in revenue
        average_change_in_revenue=int(sum(change_in_revenue_list)/(row_count-1))
    
        print("Average revenue change: $" + str(average_change_in_revenue))

        print("Greatest Increase in revenue: " + \
        str(month_list[change_in_revenue_list.index(max(change_in_revenue_list))]) + \
        " ($" + str(max(change_in_revenue_list)) + ")")
        
        print("Greatest Decrease in revenue: " + \
        str(month_list[change_in_revenue_list.index(min(change_in_revenue_list))]) +\
        " ($" + str(min(change_in_revenue_list)) + ")")
        

    #write to a txt file
    with open(newoutput, mode='a',newline='') as txt_file:
        txt_file.write("Total revenue: $"+str(total_revenue) + '\n')

        txt_file.write("Average revenue change: $" + str(average_change_in_revenue) + '\n')

        txt_file.write("Greatest Increase in revenue: " + \
        str(month_list[change_in_revenue_list.index(max(change_in_revenue_list))]) + \
        " ($" + str(max(change_in_revenue_list)) + ")" + '\n')
        
        txt_file.write("Greatest Decrease in revenue: " + \
        str(month_list[change_in_revenue_list.index(min(change_in_revenue_list))]) +\
        " ($" + str(min(change_in_revenue_list)) + ")" + '\n')
            
