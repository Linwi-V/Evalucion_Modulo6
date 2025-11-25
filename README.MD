# Gestor de Tareas - Aplicación Web Django

Sistema de gestión de tareas desarrollado con Django que permite a los usuarios registrarse, autenticarse y administrar sus tareas personales.

## Características

- Sistema de autenticación completo (registro, login, logout)
- Crear, ver y eliminar tareas
- Cada usuario solo puede ver sus propias tareas
- Interfaz responsiva con Bootstrap
- Almacenamiento de tareas en memoria

## Tecnologías Utilizadas

- Python 3.12
- Django 5.2.7
- Bootstrap 5.3
- SQLite (base de datos para usuarios y sesiones)

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/Linwi-V/Evalucion_Modulo6.git
cd Evalucion_Modulo6
```

### 2. Crear y activar entorno virtual

En Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

En Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar migraciones

```bash
python manage.py migrate
```

### 5. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

### 6. Acceder a la aplicación

Abrir el navegador en http://127.0.0.1:8000/

## Estructura del Proyecto

```
gestor_tareas/
├── manage.py
├── requirements.txt
├── README.md
├── gestor_tareas/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── tareas/
    ├── views.py
    ├── urls.py
    ├── forms.py
    ├── utils.py
    └── templates/
        └── tareas/
            ├── base.html
            ├── lista_tareas.html
            ├── crear_tarea.html
            ├── detalle_tarea.html
            ├── login.html
            └── registro.html
```

## Funcionalidades Principales

### Autenticación de Usuarios

- Registro de nuevos usuarios
- Inicio de sesión con usuario y contraseña
- Cierre de sesión seguro
- Solo usuarios autenticados pueden acceder a las funcionalidades

### Gestión de Tareas

- Listar todas las tareas del usuario autenticado
- Crear nuevas tareas con título y descripción
- Ver detalle completo de cada tarea
- Eliminar tareas con confirmación

## Seguridad

- Decorador login_required para proteger vistas
- Tokens CSRF en todos los formularios
- Cada usuario solo puede acceder a sus propias tareas
- Contraseñas hasheadas por Django

## Notas

- Las tareas se almacenan en memoria y se pierden al reiniciar el servidor
- Para uso en producción se recomienda implementar persistencia en base de datos
- DEBUG está configurado como True solo para desarrollo

## Autor

Linwi Vargas - Proyecto desarrollado para la evaluación del Módulo 6 - Bootcamp Full Stack Python

## Repositorio

https://github.com/Linwi-V/Evalucion_Modulo6
