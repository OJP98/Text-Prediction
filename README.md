# Text-Prediction
Text prediction model using deep learning techniques.

## Limpieza de los datos

La limpieza de los datos se lleva a cabo en el archivo `script.py` o bien, puede ser ejecutado paso por paso en `script.ipynb` con ayuda de un jupyter notebook. Los datos utilizados no se encuentran en este repositorio, por lo que deben de ser descargados [aquí](https://www.kaggle.com/crmercado/tweets-blogs-news-swiftkey-dataset-4million/). 

**NOTA:** Los archivos de texto deben ser almacenados dentro de este repositorio, en una carpeta llamada *files/* para que el script de python los pueda reconocer fácilmente. 

## Modelos Implementados

El archivo `training.csv` contiene 10 mil oraciones las cuales fueron usadas para el entrenamiento de los modelos. 

* Modelo simple basado en N-gramas
  Para entrenar y testear este modelo es necesario correr el script `modeloPre.py`

* Modelo Neuronal
  Para entrenar este modelo es necesario correr el script `TrainDeepModel.py`,dentro del Script encontraremos una variable en donde podemos especificar el nombre del modelo.
  
  Para testear el modelo es necesario correr el script `TestDeepModel.py`, dentro del script podemos especificar el nombre del modelo que queremos cargar. Dentro del repositorio se encuentra el modelo llamado `Deep1` el cual esta listo para ser testeado. 


## Requerimientos de python
* **numpy** tipos de datos y procedimientos útiles.U
* **keras** creación del modelo de dl.
* **nltk** para interpretación del lenguaje natural.
* **tensorflow +2.3.0** creación del modelo con redes neuronales
* **pandas** lectura y escritura de .csv
* **random** para aleatorizar los datos
* **matplotlib** para creación de gráficos
* **re** para expresiones regulares
