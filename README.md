# TuPrimeraPaginaGaldeano

Sistema de registro de licitaciones mineras desarrollado en Django como parte del curso de Python en Coderhouse (Entrega 3).

## 📌 Descripción general

Este sistema permite registrar empresas licitantes y licitadores interesados en participar de licitaciones mineras, cubriendo todas las fases del ciclo de vida de un proyecto: **proyecto, construcción, operación y cierre**.

Cada licitación puede tener múltiples ofertas asociadas. El sistema está orientado tanto a la gestión administrativa como a la visualización de oportunidades para los licitadores.

## 🧱 Estructura del proyecto

- `EmpresaLicitante`: modelo para gestionar empresas proveedoras de bienes o servicios.
- `Licitador`: modelo para registrar empresas que desean postularse a licitaciones.
- `Licitacion`: modelo central donde se definen las convocatorias abiertas.
- `Oferta`: modelo para registrar la postulación de un licitador a una licitación específica.

## 💡 Funcionalidades implementadas

- Alta de empresas licitantes, licitadores, licitaciones y ofertas mediante formularios.
- Listado y búsqueda de licitaciones disponibles.
- Postulación a licitaciones con vinculación automática entre oferta, licitación y licitador.
- Herencia de plantillas HTML.
- CRUD básico para todas las entidades.

## 🧪 ¿Cómo probar el proyecto?

1. **Clonar el repositorio:**

```bash
git clone https://github.com/fedegaldeano/TuPrimeraPaginaGaldeano.git
cd TuPrimeraPaginaGaldeano
```

2. **Crear y activar entorno virtual (opcional pero recomendado):**

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias:**

```bash
pip install django
```

4. **Ejecutar migraciones:**

```bash
python manage.py migrate
```

5. **Levantar el servidor:**

```bash
python manage.py runserver
```

6. **Abrir en el navegador:**

```
http://127.0.0.1:8000/
```

## 🔍 Funcionalidad de búsqueda

Desde la barra de búsqueda, se pueden encontrar licitaciones por nombre o descripción.

## 📁 Estructura de carpetas

```
TuPrimeraPaginaGaldeano/
│
├── licitaciones/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── templates/
│   ├── base.html
│   ├── licitaciones/
│   │   ├── licitacion_list.html
│   │   ├── licitacion_form.html
│   │   └── ...
│
├── manage.py
└── README.md
```

## ✍️ Autor

Federico Galdeano  
Curso de Python - Coderhouse  
Entrega 3 - Proyecto Web en Django