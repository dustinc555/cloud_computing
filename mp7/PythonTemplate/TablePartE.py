import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

# Define the HBase connection
connection = hb.Connection()

# Open the "powers" table
powers_table = connection.table('powers')

# Scan and print every item in the "powers" table
for key, data in powers_table.scan(include_timestamp=True):
    print('Found: {}, {}'.format(key, data))