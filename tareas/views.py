from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .utils import obtener_tareas_usuario, agregar_tarea, obtener_tarea, eliminar_tarea as eliminar_tarea_db
from .forms import TareaForm

# VISTA 1: Lista de tareas
@login_required
def lista_tareas(request):
    username = request.user.username
    tareas = obtener_tareas_usuario(username)
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

# VISTA 2: Crear nueva tarea
@login_required
def crear_tarea(request):
    username = request.user.username
    
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            descripcion = form.cleaned_data['descripcion']
            agregar_tarea(username, titulo, descripcion)
            return redirect('tareas:lista')
    else:
        form = TareaForm()
    
    return render(request, 'tareas/crear_tarea.html', {'form': form})

# VISTA 3: Ver detalle de una tarea específica
@login_required
def detalle_tarea(request, tarea_id):
    username = request.user.username
    tarea = obtener_tarea(tarea_id, username)
    
    if tarea is None:
        return render(request, 'tareas/error.html', {
            'mensaje': 'Tarea no encontrada'
        })
    
    return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea})

# VISTA 4: Eliminar una tarea
@login_required
def eliminar_tarea(request, tarea_id):
    username = request.user.username
    eliminar_tarea_db(tarea_id, username)
    return redirect('tareas:lista')

# VISTA 5: Registro de nuevos usuarios
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tareas:lista')
    else:
        form = UserCreationForm()
    
    return render(request, 'tareas/registro.html', {'form': form})

# VISTA 6: Inicio de sesión
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tareas:lista')
    else:
        form = AuthenticationForm()
    
    return render(request, 'tareas/login.html', {'form': form})

# VISTA 7: Cerrar sesión
def logout_view(request):
    logout(request)
    return redirect('tareas:login')