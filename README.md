# Reto Circles
## Descripcion
Este es un conjunto artificial creado utilizando la funcion `make_circles` de [sklearn.datasets](http://scikit-learn.org/stable/modules/classes.html#samples-generator).

![graph](images/graph.png)

Consiste en 400 datos divididos en 2 grupos.

### Ranking
Ver [ranking](https://github.com/cgarciae/supervised-basico-circles/blob/master/ranking.md).

### Formato Datos
Los datos se encuentran en los siguientes archivos CSV:
* `traning-set.csv`
* `test-set.csv`

### Variables
* Features: Las primeras 2 columnas del csv son las cooredenadas `x` y `ỳ`.
* Lables: La ultima cooredenada es la clase a la cual corresponde el dato.


### Objetivo
Crear un algortimo que tome como input un vector 2D y retone la clase a la que pertenece ese punto. Solo se puede utilizar los datos del `traning-set.csv` para entrenar.

El performance se debe medir con respecto a los datos del `test-set.csv` utilizando la siguiente formula
```python
score = n_aciertos / n_total * 100
```
donde `n_aciertos` es el numero de imagenes clasificadas de forma correcta y `n_total` es el numero total de muestras en el `test-set`.

### Notas Teoricas
* [Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
* [SVM](https://en.wikipedia.org/wiki/Support_vector_machine)
* [Decision Trees](https://en.wikipedia.org/wiki/Decision_tree_learning)

### Solucion
Ver procedimiento de [solucion](https://github.com/colomb-ia/formato-retos#solucion).

##### Requerimientos
*Indica los requerimientos para utilizar el codigo de tu solucion.*

##### Procedimiento
*Indica el procedimiento que se debe seguir para reproducir tu solucion.*

##### Metodo
*Indica el metodo que utilizaste para solucionar el reto.*

##### Resultados
*Indica el metodo que utilizaste para solucionar el reto.*

## Getting Started
Para resolver este reto primero has un [fork](https://help.github.com/articles/fork-a-repo/) de este repositorio y [clona](https://help.github.com/articles/cloning-a-repository/) el fork en tu maquina.

```bash
git clone https://github.com/{username}/supervised-avanzado-mnist
cd supervised-avanzado-mnist
```

*Nota: reemplaza `{username}` con tu nombre de usuario de Github.*

### Requerimientos
Para descargar y visualizar los datos necesitas Python 2 o 3. Las dependencias las puedes encontrar en el archivo `requirements.txt`. Puedes instalarlas fácilmente utilizando el commando

```bash
pip install -r requirements.txt
```
Dependiendo de tu entorno puede que necesites instalar paquetes del sistema adicionales, si tienes problemas revisa la documentación de estas librerías.

# Starter Code Python
Para iniciar con este reto puedes correr el codigo de Python en Jupyter del archivo `python-sample.ipynb`. Este código que ayudará a cargar y visualizar algunas imágenes. Las dependencias son las mismas que se instalaron durante la descarga de los datos, ver [Requerimientos](#requerimientos).

Para iniciar el código solo hay que prender Jupyter en esta carpeta

```bash
jupyter notebook --NotebookApp.iopub_data_rate_limit=10000000000 .
```
y abrir el archivo `python-sample.ipynb`.
