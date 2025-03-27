# MISW4304 - Lambda Squad

## Integrantes

## Configurar ambiente

### Crear ambiente virtual
Crear ambiente virtual (venv)

```bash
python3 -m venv venv
```

### Activar ambiente virtual
Activar el ambiente virtual

```bash
source venv/bin/activate
```
### Instalar dependencias
Instalar dependencias necesarias

```bash
pip3 install -r requirements.txt
```

## Ejecutar

Correr el siguiente comando

```bash
uvicorn app.main:app --reload
```
Ir al endpoint de ejemplo: http://127.0.0.1:8000/api/v1/example/

## Ver documentación

Ver la documentación de OpenAPI: http://127.0.0.1:8000/docs



