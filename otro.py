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






