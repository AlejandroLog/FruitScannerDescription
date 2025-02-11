# Scanner Fruit

## Descripción
Descripción:
Fruit Scanner es un sistema que permite identificar frutas a partir de imágenes capturadas en tiempo real. Utiliza técnicas de visión artificial y aprendizaje automático para proporcionar información detallada sobre cada fruta, incluyendo su nombre, características nutricionales y precio.

Principales Características:

Captura y procesamiento de imágenes: Uso de OpenCV/TensorFlow para mejorar la detección de frutas.

Reconocimiento de frutas: Clasificación de piña, papaya, naranja y plátano con un modelo de Machine Learning knn.

Información Nutricional: Datos detallados sobre calorías, vitaminas, proteínas y más.

Recetas personalizadas: Sugerencias de recetas en base a la fruta detectada via youtube.

Base de datos integrada: Almacenamiento y actualización de datos con Firebase o SQL Server.

Metodología de Desarrollo:

Diseño modular con arquitectura escalable.

Implementación de pruebas unitarias y de integración.

Desarrollo iterativo con retroalimentación de usuarios.
## Integrantes del Equipo
Lista de los miembros del equipo junto con sus roles.

- **Samuel Alejandro Vilchis Cisneros** - Rol (Administrador, Desarrollador)
- **Salvador Lozano Galvan** - Rol (Desarrollador)
- **Antonio Perez Cabrera** - Rol (Desarrollador)
- **Jaime Eduardo Zermeño Andrade** - Rol (Desarrollador)
- **Jesus Alejandro Torres Lopez** - Rol (Desarrollador)



## Requerimientos
Una lista de los requerimientos necesarios para ejecutar o desarrollar el proyecto.

Requerimientos No Funcionales 
1. Usabilidad 
La interfaz debe ser intuitiva para usuarios sin conocimientos técnicos. 
Los resultados deben mostrarse de forma clara y rápida. 
2. Rendimiento 
El procesamiento de imágenes no debe excederse por captura. 
La base de datos debe responder lento. 
3. Seguridad 
La base de datos debe contar con autenticación para evitar modificaciones no autorizadas. 
5. Escalabilidad 
Posibilidad de agregar más frutas en el futuro sin modificar la estructura base. 
Permitir la integración con APIs externas para mejorar el reconocimiento. 
7. Precisión del reconocimiento 
El modelo de Machine Learning debe alcanzar al menos un 85% de precisión en la detección de 
frutas. 
Se debe entrenar el modelo con un dataset variado para mejorar la identificación.

Requerimientos Funcionales 
1. Captura y procesamiento de imágenes 
El software debe acceder a la cámara de la laptop para capturar imágenes en tiempo real. 
Permitir activar y desactivar la cámara según la necesidad del usuario. 
Ajustar la resolución de la imagen para optimizar el rendimiento del procesamiento. 
Procesar la imagen para mejorar la detección de frutas (uso de filtros, eliminación de ruido). 
Convertir la imagen a un formato compatible para la clasificación (RGB, escala de grises). 
2. Reconocimiento de frutas 
Identificar si la imagen contiene una fruta entre las siguientes: piña, papaya, naranja o plátano. 
Utilizar algoritmos de visión artificial como OpenCV, TensorFlow o PyTorch para la clasificación. 
Mostrar el nombre, precio, información nutrimental, imagen y recetas de la fruta detectada en 
pantalla. 
3. Información nutricional y detalles de la fruta 
3.1. Mostrar información de la fruta detectada: 
• Nombre 
• Tipo 
• Imagen de referencia 
• Calorías 
• Vitaminas 
• Carbohidratos 
• Proteína 
3.2. Permitir la visualización de información en una interfaz gráfica. 
4. Checador de precio 
4.1. Mostrar el precio estimado de la fruta en distintas tiendas. 
5. Recetas con la fruta detectada 
5.1. Mostrar recetas recomendadas basadas en la fruta detectada dentro de youtube. 
6. Base de datos 
6.1. Conectar con una base de datos para almacenar información de frutas y recetas. 
6.2. Permitir la actualización de la base de datos con nuevos registros. 
7. Interfaz de usuario (UI) 
Diseñar una interfaz gráfica amigable con botones e información estructurada. 
