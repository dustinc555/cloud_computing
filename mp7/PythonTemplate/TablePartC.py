import happybase as hb
import csv

# Define the HBase connection
connection = hb.Connection()

# Open the "powers" table
powers_table = connection.table('powers')

rows_inserted = 0

# Read data from input.csv and insert into the "powers" table
with open('input.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        row_key, is_hero, power, name, xp, color = row
        rows_inserted += 1
        powers_table.put(row_key, {
            'personal:hero': is_hero,
            'personal:power': power,
            'professional:name': name,
            'professional:xp': xp,
            'custom:color': color
        })

# Print a message indicating successful data insertion
print("Data inserted into the 'powers' table.")
print(rows_inserted)