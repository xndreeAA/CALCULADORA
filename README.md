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


## Contenido del proyecto
- `app.py` — aplicación Flask y rutas.
- `templates/index.html` — formulario de entrada (usa Bootstrap para estilos).
- `templates/resultado.html` — plantilla que muestra la media y desviación.

## Diagnóstico rápido si obtienes 404 al enviar el formulario
- Asegúrate de que el servidor Flask esté corriendo (mira la salida de `flask run` en la consola).
- Confirma que accedes a la app por `http://127.0.0.1:5000/` (no `file://`).
- Revisa la consola de Flask: al enviar el formulario verás una entrada con `POST /calcular` si la petición llegó al servidor.
- Si el puerto 5000 está ocupado, ejecuta con `flask run --port 5001` u otro puerto.

