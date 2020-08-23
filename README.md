# Text-Prediction
Text prediction model using deep learning techniques.


## Modelos Implementados

El archivo `training.csv` contiene 10 mil oraciones las cuales fueron usadas para el entrenamiento de los modelos. 

* Modelo simple basado en N-gramas
  Para entrenar y testear este modelo es necesario correr el script `modeloPre.py`

* Modelo Neuronal
  Para entrenar este modelo es necesario correr el script `TrainDeepModel.py`,dentro del Script encontraremos una variable en donde podemos especificar el nombre del modelo.
  
  Para testear el modelo es necesario correr el script `TestDeepModel.py`, dentro del script podemos especificar el nombre del modelo que queremos cargar. Dentro del repositorio se encuentra el modelo llamado `Deep1` el cual esta listo para ser testeado. 


## Requerimientos 
* numpy
* keras
* nltk
* tensorflow +2.3.0
