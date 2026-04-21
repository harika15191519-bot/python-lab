import CSV


with open(''filebook.CSV'', ''w'', newline='''') as file:
     writer = CSV. writer(file)

     writer.writerow([''Name'', ''Age'',''city'']) # Header
     writer.writerow([''sri'', 20, ''Hyderabad''])
     writer.writerow([''Ravi'', 22, ''Chennai''])
