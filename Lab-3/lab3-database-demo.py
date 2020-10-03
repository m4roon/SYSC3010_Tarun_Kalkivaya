import sqlite3

conn = sqlite3.connect("lab4.db") # connection object

c = conn.cursor() # cursor object

# All sensors in kitchen
print 'All sensors in kitchen:'
for row in c.execute('SELECT * FROM sensors WHERE zone="kitchen"'):
	print row

print

# All door sensors
print 'All door sensors:'
for row in c.execute('SELECT * FROM sensors WHERE type="door"'):
	print row
