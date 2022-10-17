import statistics
import pandas as pd

print(statistics.mean([5, 3, 6, 8, 9, 12, 5]))
print(statistics.median([5, 3, 6, 8, 9, 12, 5]))
print(statistics.mode([5, 3, 6, 8, 9, 12, 5]))

#Example 1
#Find the mean, median and mode ages of medical practitioners in New Jersey
#https://towardsdatascience.com/how-to-read-csv-file-using-pandas-ab1f5e7e7b58
df = pd.read_csv ('data/ndb_practitioner_in_new_jersey.csv', usecols=['FST_NM', 'LST_NM', 'DOB'])
print(df)





