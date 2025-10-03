# Calculadora Estadística (Media y Desviación Estándar)

Proyecto Flask simple que calcula la media y la desviación estándar de un conjunto de números.

## Requisitos
- Python 3.8+ instalado
- (Opcional pero recomendado) Entorno virtual

## Pasos rápidos (PowerShell)
1. Abrir PowerShell y situarse en la carpeta del proyecto:

```powershell
Set-Location -Path 'C:\xampp\htdocs\CALCULADORA'
```

2. (Recomendado) Crear y activar un entorno virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

3. Actualizar pip e instalar dependencias (Flask):

```powershell
pip install --upgrade pip
pip install flask
```

4. Ejecutar la aplicación con el CLI de Flask (modo desarrollo):

```powershell
$env:FLASK_APP = 'app.py'
$env:FLASK_ENV = 'development'
flask run
```

- Alternativamente (usa el Python activo):

```powershell
python -m flask run
```

- O ejecutando directamente el archivo con el Python del virtualenv:

```powershell
.\venv\Scripts\python.exe app.py
```

5. Abrir en el navegador:

http://127.0.0.1:5000/

> Importante: no abras `templates/index.html` haciendo doble clic (file://). Debes acceder a la app mediante `http://` mientras Flask esté corriendo.

## Contenido del proyecto
- `app.py` — aplicación Flask y rutas.
- `templates/index.html` — formulario de entrada (usa Bootstrap para estilos).
- `templates/resultado.html` — plantilla que muestra la media y desviación.

## Diagnóstico rápido si obtienes 404 al enviar el formulario
- Asegúrate de que el servidor Flask esté corriendo (mira la salida de `flask run` en la consola).
- Confirma que accedes a la app por `http://127.0.0.1:5000/` (no `file://`).
- Revisa la consola de Flask: al enviar el formulario verás una entrada con `POST /calcular` si la petición llegó al servidor.
- Si el puerto 5000 está ocupado, ejecuta con `flask run --port 5001` u otro puerto.

## Ejemplo opcional: script de ejecución (PowerShell)
Puedes crear un script `run.ps1` con este contenido para arrancar rápidamente la app desde PowerShell:

```powershell
Set-Location -Path 'C:\xampp\htdocs\CALCULADORA'
.\venv\Scripts\Activate
$env:FLASK_APP='app.py'
$env:FLASK_ENV='development'
flask run
```

Guarda `run.ps1` y ejecútalo con `.
un.ps1` (si tu política de ejecución lo permite). Si PowerShell te bloquea la ejecución, puedes ejecutarlo temporalmente con `powershell -ExecutionPolicy Bypass -File .\run.ps1`.

## Notas
- Si quieres que añada un `requirements.txt` o un `run.ps1` real en el proyecto, lo hago ahora.
- Si deseas exponer la app a la red local (para probar desde otro dispositivo), puedo ayudarte a configurar `flask run --host=0.0.0.0` y explicar cómo abrir el puerto en Windows Firewall.

---

Si quieres, creo también:
- `requirements.txt` con `flask` (rápido), y/o
- `run.ps1` en el proyecto para arrancar con doble clic.

¿Lo agrego ahora?