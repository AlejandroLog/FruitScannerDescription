import cv2
import numpy as np
import os
from skimage.feature import local_binary_pattern
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Definir rutas para las imágenes
ruta = {
    'platano2': r'C:\Users\samue\Downloads\platano2',
    'mango': r'C:\Users\samue\Downloads\mango',
    'manzna': r'C:\Users\samue\Downloads\manzna'
}


# Función para cargar imágenes con preprocesamiento
def cargar_imagenes(ruta):
    imagenes = []
    for nombre_archivo in os.listdir(ruta):
        ruta_imagen = os.path.join(ruta, nombre_archivo)
        imagen = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
        if imagen is not None:
            imagen = cv2.resize(imagen, (128, 128))  # Redimensionar
            imagen = cv2.GaussianBlur(imagen, (3, 3), 0)  # Reducción de ruido
            imagen = cv2.equalizeHist(imagen)  # Mejora del contraste
            imagenes.append(imagen)
    return imagenes


# Función para extraer características LBP y estadísticas de textura
def procesar_y_extraer_caracteristicas(imagenes):
    caracteristicas = []
    for imagen in imagenes:
        lbp = local_binary_pattern(imagen, 8, 1, method="uniform")
        hist, _ = np.histogram(lbp.ravel(), bins=np.arange(0, 11), range=(0, 10))
        hist = hist / (hist.sum() + 1e-6)  # Normalizar evitando división por cero
        mean = np.mean(imagen)
        std = np.std(imagen) + 1e-6  # Evitar división por cero
        skewness = np.mean((imagen - mean) ** 3) / (std ** 3 + 1e-6)
        kurtosis = np.mean((imagen - mean) ** 4) / (std ** 4 + 1e-6)  # Nueva característica
        caracteristicas.append(np.hstack([hist, mean, std, skewness, kurtosis]))
    caracteristicas = np.nan_to_num(np.array(caracteristicas))  # Reemplazar NaN o Inf por 0
    return caracteristicas


# Cargar datos y etiquetas
datos, etiquetas = [], []
for etiqueta, dir_ruta in ruta.items():
    imagenes = cargar_imagenes(dir_ruta)
    datos.extend(imagenes)
    etiquetas.extend([etiqueta] * len(imagenes))

# Balancear las clases
distribucion = Counter(etiquetas)
minimo = min(distribucion.values())
datos_balanceados, etiquetas_balanceadas = [], []
for etiqueta in ruta.keys():
    indices = [i for i, e in enumerate(etiquetas) if e == etiqueta]
    indices_muestreados = np.random.choice(indices, minimo, replace=False)
    datos_balanceados.extend([datos[i] for i in indices_muestreados])
    etiquetas_balanceadas.extend([etiquetas[i] for i in indices_muestreados])

# Extraer características
caracteristicas_lbp = procesar_y_extraer_caracteristicas(datos_balanceados)

# Dividir en entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
    caracteristicas_lbp, etiquetas_balanceadas, test_size=0.3, random_state=42, stratify=etiquetas_balanceadas
)

# Optimizar número de vecinos
param_grid = {'n_neighbors': [1, 3, 5, 7, 9, 11]}
modelo_knn = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)
modelo_knn.fit(X_entrenamiento, y_entrenamiento)
mejor_knn = modelo_knn.best_estimator_

# Conectar con la cámara
camara = cv2.VideoCapture(1)
if not camara.isOpened():
    print("Error al acceder a la cámara.")
    exit()

print("Presiona 'a' para capturar una imagen y analizarla. Presiona 'q' para salir.")

while True:
    ret, cuadro = camara.read()
    if not ret:
        print("Error al capturar imagen.")
        break

    cv2.imshow('Vista previa - Presiona "a" para capturar', cuadro)

    if cv2.waitKey(1) & 0xFF == ord('a'):
        imagen_gris = cv2.cvtColor(cuadro, cv2.COLOR_BGR2GRAY)
        imagen_redimensionada = cv2.resize(imagen_gris, (128, 128))
        imagen_redimensionada = cv2.GaussianBlur(imagen_redimensionada, (3, 3), 0)
        imagen_redimensionada = cv2.equalizeHist(imagen_redimensionada)

        caracteristicas = procesar_y_extraer_caracteristicas([imagen_redimensionada])
        caracteristicas = np.nan_to_num(np.array(caracteristicas).reshape(1, -1))
        prediccion = mejor_knn.predict(caracteristicas)

        resultado = f'Predicción: {prediccion[0]}'
        cv2.putText(cuadro, resultado, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Resultado', cuadro)
        cv2.waitKey(2000)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()

# Evaluar modelo
y_pred = mejor_knn.predict(X_prueba)
print(f'Precisión del modelo: {accuracy_score(y_prueba, y_pred):.2f}')
print("Reporte de clasificación:\n", classification_report(y_prueba, y_pred))

# Mostrar matriz de confusión
cm = confusion_matrix(y_prueba, y_pred)
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=mejor_knn.classes_, yticklabels=mejor_knn.classes_)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()