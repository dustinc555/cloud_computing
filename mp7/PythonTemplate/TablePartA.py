import happybase as hb

# Define the HBase connection
connection = hb.Connection()

# Create a table named "powers" with three column families
powers_table = connection.create_table(
    'powers',
    {
        'personal': dict(),
        'professional': dict(),
        'custom': dict()
    }
)

# Create a table named "food" with two column families
food_table = connection.create_table(
    'food',
    {
        'nutrition': dict(),
        'taste': dict()
    }
)