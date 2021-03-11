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

![ ](tarea21_diagramaFlujo.png)
![ ](https://drive.google.com/uc?export=view&id=1g76tF9j2ljuqHCZH9eKPB8ssEx1AKeU7)
![ ](https://raw.githubusercontent.com/dmaestrow/theegg_ai/master/tarea_21/flowchart_%2321.png)

Se ha implementado una función en python (`get_irreducible_fraction(x,num_digits=4)`) que calcula la fracción irreducible de un numero x a partir del algoritmo explicado en [1].

Esta función toma un número x y lo convierte a una representación en forma de fracción usando 10^num_digits como denominador.
Nótese que esta primera representación es valida para todos los números con num_digits cifras decimales (por defecto 4).
A continuación, la correspondiente fracción irreducible se halla explotando el hecho de que el 2 y el 5 son los únicos números primos divisores del denominador.
Esto permite hallar la solución simultaneamente dividiendo numerador y denominador entre cada uno de estos números (2 y 5) tantas veces como sea posible. La siguiente figura muestra el diagrama de flujo correspondiente:


![ ](https://raw.githubusercontent.com/dmaestrow/theegg_ai/master/tarea_21/flowchart_%2321.png)


## Programas

| Programa              | Lenguaje | Observaciones                                                                       |
|-----------------------|----------|-------------------------------------------------------------------------------------|
| tarea_21.py           | Python   | Calculamos los factores de 10000 y reducimos *abcd* todo lo que se pueda con ellos. |
| tarea_21_numpy_gcd.py | Python   | Halla el máximo común divisor con la función gcd de ``numpy``.                      | 
| tarea_21_simple.py    | Python   | Damos los factores primos de 10000 como conocidos                                   | 
| tarea_21.jl           | Julia    | Calculamos los factores de 10000 y reducimos *abcd* todo lo que se pueda con ellos. |
| tarea_21_gcd.jl       | Julia    | Halla el máximo común divisor con la función gcd de Julia.                          |

## Ejecución

### tarea_21.py

```console
cd ~/repo/theegg_ai/tarea_21/
╰─$ python3 tarea_21.py 0.2340
117 / 500
```
### tarea_21_numpy_gcd.py
Para ejecutar este fichero habría que disponer de ``numpy``.
 
```console
cd ~/repo/theegg_ai/tarea_21/
╰─$ python3 tarea_21_ultra_simple.py 0.2340
117 / 500
```

### tarea_21_simple.py
```console
cd ~/repo/theegg_ai/tarea_21/
╰─$ python3 tarea_21.py 0.2340
117 / 500
```

## Programas en Julia
La programación de las tareas en Julia las realizo por querer familiarizarme con el lenguaje. El evaluador puede centrarse en los programas en Python si así lo desea.
Para ejecutar los programas en Julia es necesario disponer del REPL de Julia (intérprete). Es posible bajarlo desde [aquí](https://julialang.org/downloads).

### tarea_21.jl
```console
cd ~/repo/theegg_ai/tarea_21/
╰─$ julia tarea_21.jl 0.2340
117/500
```

### tarea_21_gcd.jl
```console
cd ~/repo/theegg_ai/tarea_21/
╰─$ julia tarea_21_gcd.jl 0.2340
117/500
```

## Referencias
[1] http://www.nachocabanes.com/retos/reto.php?n=013
