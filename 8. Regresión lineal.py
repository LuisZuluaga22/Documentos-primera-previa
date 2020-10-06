# Se importan las libreria a numpy y las funciones de preprocesamiento
import numpy as np
from sklearn import preprocessing
# Datos de prueba
input_data = np.array([[5.1, -2.9, 3.3],
[-1.2, 7.8, -6.1],
[3.9, 0.4, 2.1],
[7.3, -9.9, -4.5]])
print(input_data)
[[ 5.1 -2.9 3.3]
[-1.2 7.8 -6.1]
[ 3.9 0.4 2.1]
[ 7.3 -9.9 -4.5]]

In [2]: # Binarizar los datos

data_binarized = preprocessing.Binarizer(threshold=2.1).transform(input_data)
print("\nDatos binarizados:\n", data_binarized)

In [3]: # Imprimir la media y la desviacion estandar

print("\nANTES:")
print("Media =", input_data.mean(axis=0))
print("Desviacionn estandar =", input_data.std(axis=0))

In [4]: # Remover la media

data_scaled = preprocessing.scale(input_data)
print("\nDESPUES:")
print("Media =", data_scaled.mean(axis=0))
print("Desviacion estandar =", data_scaled.std(axis=0))
Datos binarizados:
[[1. 0. 1.]
[0. 1. 0.]
[1. 0. 0.]
[1. 0. 0.]]

ANTES:
Media = [ 3.775 -1.15 -1.3 ]
Desviacion estandar = [3.12039661 6.36651396 4.0620192 ]

DESPUES:
Media = [1.11022302e-16 0.00000000e+00 2.77555756e-17]
Desviaciรณn estรกndar = [1. 1. 1.]

In [5]: # Escalamiento Min Max

data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0,
1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print("\nMin max escalamiento de datos:\n", data_scaled_minmax)
Min max escalamiento de datos:
[[0.74117647 0.39548023 1. ]
[0. 1. 0. ]
[0.6 0.5819209 0.87234043]
[1. 0. 0.17021277]]

In [6]: # Normalizacion de datos

data_normalized_l1 = preprocessing.normalize(input_data,
norm='l1')
data_normalized_l2 = preprocessing.normalize(input_data,
norm='l2')
print("\nL1 dato normalizado:\n", data_normalized_l1)
print("\nL2 dato normalizado:\n", data_normalized_l2)
L1 dato normalizado:
[[ 0.45132743 -0.25663717 0.2920354 ]
[-0.0794702 0.51655629 -0.40397351]
[ 0.609375 0.0625 0.328125 ]
[ 0.33640553 -0.4562212 -0.20737327]]
L2 dato normalizado:
[[ 0.75765788 -0.43082507 0.49024922]
[-0.12030718 0.78199664 -0.61156148]
[ 0.87690281 0.08993875 0.47217844]
[ 0.55734935 -0.75585734 -0.34357152]]

In [10]: # Manejo de etiquetas
import numpy as np
from sklearn import preprocessing
# Se definen algunas etiquetas simples
input_labels = ['rojo', 'negro', 'rojo', 'verde', 'negro', 'amarillo',
'blanco']
# Se crea un codificador de etiquetas y se ajustan las etiquetas
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)
# Se imprime el mapeo entre palabras y numeros
print("\nMapeo de etiquetas:")
for i, item in enumerate(encoder.classes_):
print(item, '-->', i)
# Codificar un conjunto de etiquetas con el codificador
test_labels = ['verde', 'rojo', 'negro']
encoded_values = encoder.transform(test_labels)
print("\nEtiquetas =", test_labels)
print("Valores codificados =", list(encoded_values))
# Decodificar un conjunto de valores usando el codificador
encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\nValores codificados =", encoded_values)
print("Etiquetas decodificadas =", list(decoded_list))

Mapeo de etiquetas:
black --> 0
green --> 1
red --> 2
white --> 3
yellow --> 4
Labels = ['verde', 'rojo', 'negro']
Encoded values = [1, 2, 0]
Encoded values = [3, 0, 4, 1]
Decoded labels = ['blanco', 'negro', 'amarillo', 'verde']
