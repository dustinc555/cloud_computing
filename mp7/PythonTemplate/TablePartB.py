import happybase as hb

# Define the HBase connection
connection = hb.Connection()

# Get a list of all tables
tables = connection.tables()

# Print the list of tables
print(tables)