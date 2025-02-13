import sqlite3
from nicegui import ui

#connection to the database
con = sqlite3.connect('task.db')
cur = con.cursor()
#GUIs


#creation of the table if she wasn't created
cur.execute('CREATE TABLE IF NOT EXISTS Tache (id INTEGER PRIMARY KEY, what TEXT)')

columns = [
    {'name': 'id', 'label': 'ID', 'field': 'id', 'required': True, 'align': 'left'},
    {'name': 'task', 'label': 'Task', 'field': 'task', 'sortable': True},
]
rows = [
    {'id': row[0], 'task': row[1]} 
    for row in cur.execute('SELECT id, what FROM Tache')
    ]

ui.table(columns=columns, rows=rows, row_key='id')

ui.run()