import sqlite3
from nicegui import ui

con = sqlite3.connect('task.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Tache (id INTEGER PRIMARY KEY, what TEXT)')

columns = [
    {'name': 'id', 'label': 'ID', 'field': 'id', 'required': True, 'align': 'left'},
    {'name': 'task', 'label': 'Task', 'field': 'task', 'sortable': True},
]

selectedtask = None

def load_data():
    rows = [
        {'id': row[0], 'task': row[1]} 
        for row in cur.execute('SELECT id, what FROM Tache')
    ]
    table.rows = rows

def selectiontask(e):
    ui.notify(f'selected: {e.selection}')
    global selectedtask
    selectedtask = e.selection[0]['id'] if e.selection else None
    print(selectedtask)

def deletetask():
    if selectedtask is not None:
        cur.execute("DELETE FROM Tache WHERE id = ?", (selectedtask,))
        con.commit()
        ui.notify("Task deleted successfully")
        print("Task deleted successfully")
        load_data()
    else:
        ui.notify("No task selected")
        print("No task selected")

def addtask():
    global demandenomtask
    global validationnewtask
    demandenomtask = ui.input(label="Veuillez saisir la tache à ajouter : ", on_change=lambda e: print(e.value))
    validationnewtask = ui.button('Valider', on_click=lambda e: addtasktodb(demandenomtask.value), color='green')

def addtasktodb(tasktoadd):
    cur.execute("INSERT INTO Tache (what) VALUES (?)", (tasktoadd,))
    con.commit()
    ui.notify("Task added successfully")
    print("Task added successfully")
    load_data()
    demandenomtask.delete()
    validationnewtask.delete()

table = ui.table(columns=columns, rows=[], row_key='id', on_select=selectiontask, selection='single')
delete_button = ui.button('Delete', on_click=deletetask, color='red')
add_button = ui.button('Add',on_click=addtask,color='green')


load_data()

ui.run()
