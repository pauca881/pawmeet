# Sistema de Recomendación de Mascotas

Este proyecto implementa un sistema de recomendación de mascotas utilizando el algoritmo K-Nearest Neighbors (KNN) basado en características como tamaño, color, temperamento, nivel de actividad, peso, socialización y estado de vacunación. El modelo encuentra las mascotas más cercanas en función de estas características y calcula la similitud utilizando la distancia euclidiana.

## Descripción

El objetivo del proyecto es encontrar mascotas similares a una nueva mascota, proporcionando un sistema que pueda sugerir animales con características cercanas. El algoritmo usa un **modelo de K-Nearest Neighbors (KNN)** para calcular las distancias entre las mascotas y encontrar las más cercanas en base a sus atributos.

## Tecnologías Utilizadas

- **Python**
- **Pandas**: Manipulación y análisis de datos.
- **Scikit-learn**: Implementación de modelos de aprendizaje automático y procesamiento de datos.
  - **K-Nearest Neighbors (KNN)**
  - **OneHotEncoder** (para codificar variables categóricas)
  - **StandardScaler** (para normalizar características numéricas)
  - **Pipeline** (para crear un flujo de trabajo eficiente)
  - **ColumnTransformer** (para aplicar diferentes transformaciones a columnas específicas)
- **Datetime**: Para trabajar con fechas (aunque no se usa activamente en el código final).
