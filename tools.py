from langchain.tools import Tool
import datetime
import socket
import os

# Función 1: Hora local
def get_local_time(location: str = "Colombia") -> str:
    now = datetime.datetime.now()
    return f"La hora actual en {location} es {now.strftime('%Y-%m-%d %H:%M:%S')}"

# Función 2: IP local
def get_local_ip(_: str = "") -> str:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return f"La IP local es: {ip_address}"

# Función 3: Archivos en el directorio actual
def list_project_files(_: str = "") -> str:
    files = os.listdir()
    return "\n".join(files)

# Lista de herramientas (bien definidas)
tools = [
    Tool(
        name="get_local_time",
        func=get_local_time,
        description="Devuelve la hora actual en una ubicación (por defecto Colombia). Entrada: ubicación como texto."
    ),
    Tool(
        name="get_local_ip",
        func=get_local_ip,
        description="Devuelve la dirección IP local. No necesita entrada."
    ),
    Tool(
        name="list_project_files",
        func=list_project_files,
        description="Lista los archivos en el directorio actual del proyecto. No necesita entrada."
    )
]
