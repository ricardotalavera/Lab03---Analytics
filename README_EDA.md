![](https://ucsp.edu.pe/wp-content/uploads/2021/05/telecomunicaciones-evoluci%C3%B3n.jpg)


# PI03 - ANALYTICS - CASO TELECOMUNICACIONES - INFORME EDA

### 1.- INTRODUCCION

En este caso de Analytics dentro del sector de telecomunicaciones, se decidió trabajar con python en la fase de extracción de data desde la API, así como en la primera parte de exploración de data.
Los archivos pre-revisados en python fueron dejados en un directorio de trabajo "PowerBI" para luego fueran subidos a PowerBI.

###  2.- EDA

### 2.1.- CONEXION A LA API de ENACOM.
En esta etapa se obtuvo una API-KEY del portal de ENACOM de forma manual, según la documentación de la propia API. Luego se construyeron los modulos **main.py** y **utils.py**, los cuales se encargan de comunicarse con la API y bajarse los 16 archivos disponibles concernientes a acceso a internet de manera automática hacia un directorio de trabajo. EL trabajo se hizo con las librerias **reguests** y **BeautifulSoup4**, las cuales se usaron en el correspondiente webscrapping a la página web de Enacom.

### 2.2.- CARGA DE ARCHIVOS PARA SU EXPLORACION.
En esta fase, ya contando con los archivos dejados por el proceso automático de descarga desde la API, se revisó la data y se determinaron los archivos necesarios para la presentación en POWERBI, por lo cual se construyó un modulo **eda.PY**, el cual se encarga de leer los archivos seleccionados para el análisis, para que solamente esos archivos sean sometidos al proceso de exploración y limpieza.

A través de su carga con la libreria **pandas** se sortea el problema de puntos y comas en lugares indebidos, de tal manera que los campos que deben ser numéricos se cargaron directamente como numéricos. Lo anterior se logró con los comandos **thousands=** y **decimal=** que brinda la citada libreria.

![](https://conceptodefinicion.de/wp-content/uploads/2017/03/Ingenier%C3%ADa_Telecomunicaciones.jpg)

### 2.3.- REVISION DE LA ESTRUCTURA DEL DATASET

Inmediatamente a traves de los comandos **head** e **info**, se observa cada dataset para cerciorarnos que se vea bien la carga y conocer que los tipos de datos sean los correctos. Recordemos que tenemos la facilidad de observar los archivos en el portal como dataviews, lo cual nos ayuda como aduana de revisión.

### 2.4.- PRESENCIA DE NAs O NULLs

Asimismo a través del comando **isna().sum(axis=0)** se revisó que no existan valores perdidos peligrosos. Se encontraron valores perdidos que justificaron intervención solo en un file de los escogidos, el cual contenia la ultima linea con una anotación de asterisco a forma de nota de llamada de alerta. Asimismo este file fue el unico que ameritó efectuar un **replace** con expresiones regulares a fin de desaparecer un asterisco junto al año 2019 y junto a sus trimestres.

También se borraron algunas columnas no necesarias en un archivo y se convirtió un archivo de formato horizontal a formato vertical, ya que se le necesitará de ambas formas.

### 2.5.- MATERIA PRIMA PARA POWER BI

Finalmente el modulo **eda.py** deja los archivos ya procesados en el mismo directorio de trabajo "PowerBI", con la diferencia de que el modulo coloca los nombres de cada archivo con minúsculas esta vez y añade el sufijo **_EDA** a cada archivo.

### 2.6.- POWER QUERY - TRNAFORMACION DE DATOS PARTE -II.

Durante el trabajo de confección de la presentación en POWERBI, los archivos limpios debieron ser manipulados de diversas maneras : crear columnas, crear un calendario, cruzar consultas para añadr algunos campos entre datasets etc. La parte anteriormente mencionada se efectúo en **POWER-QUERY**, a través de crear columnas personalizadas, anular dinamizaciones de columnas etc. Se considera esta la parte de filigrana final en el proceso de EDA.

### CONCLUSIONES DEL EDA

Se pensó en efectuar correlaciones y otros análisis estadísticos, pero no se efectuaron debido a que las tendencias y correlaciones eran muy evidentes y lo anterior no crearia valor para la analítica. Sin embargo este paso debera efectuarse si se desea luego construir modelos de machine learning.

![](https://www.redeszone.net/app/uploads-redeszone.net/2022/05/motivos-conexion-internet-lenta.jpg)

