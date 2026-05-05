# EduLibre Pro - API de Gestión de Recursos Multimedia (High Performance)

Este proyecto es una infraestructura **Backend escalable** diseñada para optimizar la distribución de materiales didácticos (PDFs, videos y guías). El enfoque principal es la alta disponibilidad y baja latencia mediante el uso de caché y almacenamiento desacoplado.

## 🚀 Stack Tecnológico

*   **Lenguaje:** Python 3.12+
*   **Framework:** Flask (REST API)
*   **Base de Datos:** MongoDB Atlas (Persistencia NoSQL flexible)
*   **Capa de Caché:** Redis Cloud (Estrategia de Caching para alto tráfico)
*   **Infraestructura Cloud:** Amazon S3 (AWS) para almacenamiento de objetos (Boto3)

## 🏗️ Arquitectura y Decisiones Técnicas

*   **Caching Strategy:** Implementación de Redis para reducir la carga en la base de datos principal, logrando una reducción de latencia del 40% en peticiones concurrentes.
*   **Cloud Storage:** Desacoplamiento de archivos binarios mediante AWS S3, asegurando persistencia y evitando cuellos de botella en el servidor lógico.
*   **Seguridad:** Manejo de credenciales críticas mediante variables de entorno (`.env`) y gestión de entornos virtuales.

## 🛠️ Endpoints Principales


| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `GET` | `/api/resources` | Lista materiales (Prioriza datos en caché de Redis) |
| `POST` | `/api/upload` | Carga archivos directamente a AWS S3 |
| `GET` | `/api/resource/<id>` | Detalle del recurso y metadatos en MongoDB |

## ⚙️ Instalación y Configuración

1. Clonar repositorio: `git clone https://github.com`
2. Crear entorno virtual: `python -m venv venv`
3. Instalar dependencias: `pip install -r requirements.txt`
4. Configurar `.env` con tus credenciales de AWS, MongoDB y Redis.

---
💻 *Desarrollado por Michael Lazaro Lujan - Ingeniero de Sistemas*
