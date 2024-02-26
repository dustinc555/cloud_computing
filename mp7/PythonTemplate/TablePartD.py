import happybase as hb

# Define the HBase connection
connection = hb.Connection()

# Open the "powers" table
powers_table = connection.table('powers')

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

def read_powers_row(row_key):
    data = powers_table.row(row_key)
    
    # Extract values from the retrieved data
    hero = data.get(b'personal:hero', b'')
    power = data.get(b'personal:power', b'')
    name = data.get(b'professional:name', b'')
    xp = data.get(b'professional:xp', b'')
    color = data.get(b'custom:color', b'')
    
    # Print the formatted output
    return (hero,power,name,xp,color)

hero,power,name,xp,color = read_powers_row('row1')
print('hero: {}, power: {}, name: {}, xp: {}, color: {}'.format(hero, power, name, xp, color))

hero,power,name,xp,color = read_powers_row('row19')
print('hero: {}, color: {}'.format(hero, color))

hero,power,name,xp,color = read_powers_row('row1')
print('hero: {}, name: {}, color: {}'.format(hero, name, color))