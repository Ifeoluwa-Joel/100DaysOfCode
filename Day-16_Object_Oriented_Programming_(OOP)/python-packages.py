# import prettytable

from prettytable import PrettyTable

table = PrettyTable()
col1 = ['Pikachu', 'Squirtle', 'Charmander']
col2 = ['Electric', 'Water', 'Fire']
table.add_column(fieldname='Pokemon Name', column=col1)
table.add_column(fieldname='Type', column=col2)
table.align = 'l'
print(table)


cgpa_table = PrettyTable()
col = [1, 2, 3, 4]
col2 = ['Afonja', 'Ifeoluwa', 'Shang', 'Joshua']
col3 = [3.9, 3.79, 3.65, 3.6]
cgpa_table.add_column(fieldname='S/N', column=col, align='c')
cgpa_table.add_column(fieldname='Name', column=col2, align='l')
cgpa_table.add_column(fieldname='CGPA', column=col3, align='l')
row6 = [5, 'Peter', 3.59]
cgpa_table.add_row(row6)
print(cgpa_table)
