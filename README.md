# EduLibre Pro - Gestión Educativa Escalable
Este proyecto es una API profesional diseñada para optimizar la gestión de materiales didácticos.

## Stack Tecnológico
*   **Backend:** Python con Flask.
*   **Base de Datos:** MongoDB Atlas (Persistencia NoSQL).
*   **Aceleración:** Redis Cloud (Gestión de caché para alta velocidad).
*   **Almacenamiento:** Amazon S3 (AWS) para archivos binarios (PDF/Videos).

## Características Principales
- **Velocidad:** Implementación de caché con Redis para reducir la latencia en consultas frecuentes.
- **Sincronización:** Lógica de invalidación de caché automática al insertar nuevos datos.
- **Escalabilidad:** Integración con AWS para almacenamiento desacoplado.