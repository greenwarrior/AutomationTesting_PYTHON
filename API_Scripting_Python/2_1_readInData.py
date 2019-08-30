#############################################################################
# import csv  - csv modeule makes it a lot easier to read in and manipulate
#               csv files
# 1. Read the file in using the construct with open ()
# 2. Define the list where we can store the data in, initialized as blank
# 3. Read in the data to the file_reader, calling each row in the file_reader
#    and append it in the timing_data.
#    - CSV reader will split each row at the commas and automatically
#       make this into a list of lists
# 4. Define the list for each of the data sets
#
#
############################################################################


import csv

#final desired format
# - Charts [["Test Name",<diff from avg>]]
# - spreadsheet [["Test Name",<current run time>]]

# 2
timing_data = []

# 1
with open('TestTimingData.csv') as csv_file:
    # 3
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        timing_data.append(row)

# 4
column_chart_data = [["Test Name","Diff from Avg"]]
table_data = [["Test Name","Run Time (s)"]]

for row in timing_data[1:]:
    test_name = row[0]

    #if row is empty go the next
    if not row[1] or not row[2]:
        continue
    # convert the string to float
    current_run_time = float(row[1])
    avg_run_time = float(row[2])
    diff_from_avg = avg_run_time - current_run_time
    column_chart_data.append([test_name,diff_from_avg])
    table_data.append([test_name,current_run_time])

print (column_chart_data)
print (table_data)