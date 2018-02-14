
# Import the `employee_data1.csv` and `employee_data2.csv` files, which currently holds employee records like the below:
import os
import csv
import datetime
file_num = ['1', '2']
for num in file_num:
    csv_path = os.path.join("raw_data", "employee_data" + str(num) + ".csv")

    # Then convert and export the data to use the following format instead:
    new_output = os.path.join("raw_data", "new_employee_data" + str(num) + ".csv")

    # In summary, the required conversions are as follows:
    with open (csv_path, mode = 'r', newline = '', encoding = 'utf=8') as csv_file1:
        csvReader = csv.DictReader(csv_file1, delimiter = ',')

    # Read the Employy ID number and add it to a list 
    # The `Name` column should be split into separate `First Name` and `Last Name` columns.
        emp_id = []
        name_split = []
        first_name = []
        last_name = []
        dob_new = []
        ssn = []
        ssn_split = []
        state_new = []
        states = {'Alabama': 'AL', 
        'Alaska': 'AK', 
        'Arizona': 'AZ', 
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'}


        for row in csvReader:

            # Add emp id
            emp_id.append(row["Emp ID"])

            #names split
            name_split = row["Name"].split(" ")
            #print(name_split)
            first_name.append(name_split[0])
            last_name.append(name_split[1])
            #print(first_name[0])
        
            # The `DOB` data should be re-written into `DD/MM/YYYY` format.
            dob_formatted = datetime.datetime.strptime(row["DOB"], '%Y-%m-%d')
            dob_formatted = dob_formatted.strftime('%d/%m/%Y')
            dob_new.append(dob_formatted)
        
            # The `SSN` data should be re-written such that the first five numbers are hidden from view.
            ssn_split = list(row["SSN"])
            ssn_split[0:3] = ("*", "*", "*")
            ssn_split[4:6] = ("*", "*")
            joined_ssn = "".join(ssn_split)
            ssn.append(joined_ssn)
     
            # The `State` data should be re-written as simple two-letter abbreviations.
            state_abv = states[row["State"]]    
            state_new.append(state_abv)

    zip_lists = zip(emp_id, first_name, last_name, dob_new, ssn, state_new)

    with open(new_output, mode='w', newline='') as csv_file2:
        csvWriter = csv.writer(csv_file2, delimiter = ',')   
        csvWriter.writerow(["Emp ID", "First Name","Last Name", "DOB_new", "SSN", "State Abv"])
        csvWriter.writerows(zip_lists)