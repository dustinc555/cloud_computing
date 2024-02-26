import happybase as hb

# Define the HBase connection
connection = hb.Connection()

# Open the "powers" table
powers_table = connection.table('powers')

# 1. Update the data in a particular cell using the put() method
row_key = b'row7'
update_data = {'custom:color': 'purple'}
powers_table.put(row_key, update_data)

# 2. Retrieve all versions of all columns for the updated row
row = powers_table.row(row_key)

for column_family, _ in row.items():
    cells = powers_table.cells(row_key, column=column_family, include_timestamp=True)
    for value_of_time, timestamp in cells:
        print("row: {}, column family:qualifier: {}, value: {}, timestamp: {}".format(row_key, column_family, value_of_time, timestamp))