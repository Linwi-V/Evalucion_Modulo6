# Lista global para almacenar tareas (simulando una base de datos)
TAREAS_DB = []

def obtener_tareas_usuario(username):
#Devuelve las tareas de un usuario específico
    return [tarea for tarea in TAREAS_DB if tarea['usuario'] == username]

def agregar_tarea(username, titulo, descripcion):
#Agrega una nueva tarea para un usuario
    tarea_id = len(TAREAS_DB) + 1
    tarea = {
        'id': tarea_id,
        'usuario': username,
        'titulo': titulo,
        'descripcion': descripcion
    }
    TAREAS_DB.append(tarea)
    return tarea

def obtener_tarea(tarea_id, username):
#Obtiene una tarea específica del usuario
    for tarea in TAREAS_DB:
        if tarea['id'] == tarea_id and tarea['usuario'] == username:
            return tarea
    return None

def eliminar_tarea(tarea_id, username):
#Elimina una tarea del usuario
    global TAREAS_DB
    TAREAS_DB = [t for t in TAREAS_DB if not (t['id'] == tarea_id and t['usuario'] == username)]