# Tarea 21: Calculo de Fracción Irreducible

## Eunciado
Crea un programa que dado un número entre 0,0001 y 0,9999 (y de no más de 4 cifras decimales), obtenga y muestre la correspondiente fracción irreducible.

Por ejemplo, el número 0,25 se puede obtener a partir de 25/100, o de 2/8, o de 1/4, entre otros. La fracción irreducible es 1/4, que está formada por un numerador y un denominador que son primos entre sí.

## Contexto

Dado un número de la forma <img src="https://render.githubusercontent.com/render/math?math=0.abcd">, es decir, <img src="https://render.githubusercontent.com/render/math?math=\frac{abcd}{10000}"> hayar su fracción irreducible.
Una fracción irreducible es una fracción en la que el numerador y el denominador no comparten factores en común, de forma que no existe otra fracción equivalente que se pueda escribir en términos más sencillos.
La solución pasa por hallar los factores primos en común de un numerador, en este caso <img src="https://render.githubusercontent.com/render/math?math=abcd"> de 4 cifras y el número 10000
Por lo tanto, obtener la fracción irreducible correspondiente a un numero dado se reduce a dividir el numerador y el denominador entre su máximo común divisor.
El número 10000 será siempre nuestro denominador, por lo tanto tiene sentido utilizar un conocimiento *a priori* de sus factores primos:
<img src="https://render.githubusercontent.com/render/math?math=10000 = 5^4 \cdot 2^4 = 5 \cdot 5 \cdot 5 \cdot 5 \cdot 2 \cdot 2 \cdot 2 \cdot 2">

## Notación Big-O: O(1)

## Solución

1. **Convertir la fracción en entero.** Como la fracción tendrá como mucho 4 decimales, esto se consigue multiplicando la fraccion po 10.000. A este número le llamaremos el entero.

2. **Encontrar el Máximo Común Divisor (MCD) entre el entero y 10.000.** Empezar desde el entero que se ha conseguido multiplicando la fracción e ir restando 1 hasta encontrar el primer número cuyo remanente con el entero y 10.000 sea 0.

3. **Dividir el entero y 10.000 con el MCD para conseguir el numerador y denominador respectivamente**.

![Diagrama de Flujo](tarea21_diagramaFlujo.png)
![diagrama de flujo](https://drive.google.com/uc?export=view&id=1g76tF9j2ljuqHCZH9eKPB8ssEx1AKeU7)
![ ](https://raw.githubusercontent.com/dmaestrow/theegg_ai/master/tarea_21/flowchart_%2321.png)

## Programas

| Programa              | Lenguaje | Observaciones                                                                       |
|-----------------------|----------|-------------------------------------------------------------------------------------|
| tarea_21.py           | Python   | Calculamos los factores de 10000 y reducimos *abcd* todo lo que se pueda con ellos. |
| tarea_21_numpy_gcd.py | Python   | Halla el máximo común divisor con la función gcd de ``numpy``.                      | 
| tarea_21_simple.py    | Python   | Damos los factores primos de 10000 como conocidos                                   | 
| tarea_21.jl           | Julia    | Calculamos los factores de 10000 y reducimos *abcd* todo lo que se pueda con ellos. |
| tarea_21_gcd.jl       | Julia    | Halla el máximo común divisor con la función gcd de Julia.                          |


El programa está escrito en Python. Se divide en 3 partes:

1. Función para calcular el Máximo Común Divisor.

2. Función principal que:

   Recibe el número como argumento, que esta dentro del rango aceptado [0.0001, 0.9999] y lo convierte en entero.

   LLama a la función para conseguir el MCD y recibe el resultado.

   Divide el entero y 10.000 para conseguir la fracción irreducible e imprime el resultado.

3. Bucle infinito para ir pidiento los números al usuario e imprimir el resultado.

## Ejecución



El programa está desarrollado con Python 3.6.4

Ejecutar comando `python app.py` en la terminal.

A continuación te pedirá que escribas un número decimal. Escribe un número y dale a Enter.

Nota: El separador de decimales debe ser un punto

```console
╰─$ python3 app.py
Mete un número entre [0.0001, 0.9999]: (1 para salir)
0.376
Fraccion minima de 0.3760: 47/125
Mete un número entre [0.0001, 0.9999]: (1 para salir)
1
```

## Referencias
[1] http://www.nachocabanes.com/retos/reto.php?n=013

#########################################################################################################################################################################






## Ejecución

El programa esta escrito usando el compilador de **Python 3.8.3** por lo que se aconseja usar esa versión para ejecutarla. Para eso es suficiente ir a la carpeta de la tarea en una ventana de terminal y teclear `python3 app.py`.

El prompt empezará a imprimir el mensaje para pedir un número para hacer el calculo. Introduciendo 1 pararemos el programa.



###################################################################################################################################################################



## Solución propuesta

Se ha implementado una función en python (`get_irreducible_fraction(x,num_digits=4)`) que calcula la fracción irreducible de un numero x a partir del algoritmo explicado en [1].

Esta función toma un número x y lo convierte a una representación en forma de fracción usando 10^num_digits como denominador.
Nótese que esta primera representación es valida para todos los números con num_digits cifras decimales (por defecto 4).
A continuación, la correspondiente fracción irreducible se halla explotando el hecho de que el 2 y el 5 son los únicos números primos divisores del denominador.
Esto permite hallar la solución simultaneamente dividiendo numerador y denominador entre cada uno de estos números (2 y 5) tantas veces como sea posible. La siguiente figura muestra el diagrama de flujo correspondiente:


![ ](https://raw.githubusercontent.com/dmaestrow/theegg_ai/master/tarea_21/flowchart_%2321.png)


### Ejecución   

La función se ha implementado en un script en python que toma como argumento un numero de entrada y visualiza el resultado (`main_tarea21.py`). 
En caso de no pasarle ningún número, el script llama a la función con un numero aleatorio dentro del rango estipulado. 

Para ejecutarlo basta con llamarlo desde línea de consola:

```
cd ~/EGG/repo/theegg_ai/tarea_21/
```

```
python main_tarea21.py 0.1995
```

Obteniendo a la salida el número aleatorio empleado y su correspondiente fracción irreducible, como por ejemplo:


```
x = 0.1995
```

```
399/2000
```
### Requisitos
Python, probado en 2.7.12 o 3.5.2 (Ubuntu).




############################################################################################################################################################################