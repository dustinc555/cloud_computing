import happybase as hb

# Define the HBase connection
connection = hb.Connection()

# Open the "powers" table
powers_table = connection.table('powers')

# Scan the data in the "powers" table
data_list = [(key, data) for key, data in powers_table.scan()]

# Create sets to store unique combinations of color and name
color_name_set = set()


# Iterate over the data to achieve the equivalent of the SQL query
for key, data in data_list:
    color = data.get(b'custom:color', b'')
    name = data.get(b'professional:name', b'')
    power = data.get(b'personal:power', b'')

    # Check if the combination of color and name already exists in the set
    if (color, name) in color_name_set:
        continue

    # Find matching entries with the same color and different names
    matching_entries = [(k, d) for k, d in data_list if k != key and d.get(b'custom:color', b'') == color]

    # Print the combinations
    for entry in matching_entries:
        name2 = entry[1].get(b'professional:name', b'')
        power2 = entry[1].get(b'personal:power', b'')
        print('{}, {}, {}, {}, {}'.format(name, power, name2, power2, color))

    # Add the current combination to the set
    color_name_set.add((color, name))