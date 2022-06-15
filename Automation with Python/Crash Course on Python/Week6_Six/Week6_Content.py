class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout" and machines[event.machine] == event.user:
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)


""" Funcion de ayuda para ordenar la lista """
 def get_event_date(event):
    return event_date

""" Funcion para llamar usuarios actuales """
def current_users(events):
    # Ordenar por definicion de clave
    events.sor(key = get_event_date)
    # Creamos el diccionario donde almacenaremos los nombre de los usuario finales de una maquina
    machines ={}
    # Repetimos lista de eventos
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set ()
        if event.type = "login":
            machines[event.machine].add(event.user)
        elif event.type = "logout":
            machines[event.machine].remove(event.user)
    # El diccionario contendra todas las maquinas que hemos visto como claves
    return machines

""" Creamos nueva funcion para generar el reporte """
def generate_report(machines):
    for machine, users in machines.items():
        # Asegúrese de no imprimir ninguna máquina en la que nadie haya iniciado sesión actualmente
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))