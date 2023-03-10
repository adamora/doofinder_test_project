# Enunciado

Disponemos de un barco con varias posiciones de almacenaje.

Cada posicion de almacenaje puede tener 0, 1 o varias cajas con provisiones.

Tenemos una grua que es capaz de mover cajas individualmente de una posicion a otra

## Ejemplo

En el ejemplo siguiente, el barco dispone de 3 posiciones de almacenaje.
La posicion 1 tiene las cajas Z y N
La posicion 2 tiene las cajas M, C y D
La posicion 3 tiene la caja P

La caja Z no puede ser movida por la grua, puesto que la caja N esta encima.

Para poder mover la caja Z primero deberia moverse la caja N a la posicion 2 o a la posicion 3.

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

Si recibimos el siguiente fichero con instrucciones:

    move 1 from 2 to 1
    move 3 from 1 to 3
    move 2 from 2 to 1
    move 1 from 1 to 2

Estariamos moviendo una caja de la posicion 2 a la posicion 1

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

Luego moveriamos 3 cajas, de una en una, de la posicion 1 a la posicion 3

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

Luego moveriamos 2 cajas de la posicion 2 a la posicion 1

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3

Y por ultimo una caja de la posicion 1 a la posicion 2

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3

En este ejemplo, despues de realizar todos los movimientos, la solucion seria CMZ, puesto que son las tres cajas que estan en lo mas alto de cada posicion

## Prueba

El barco es el siguiente

                [B] [L]     [J]
            [B] [Q] [R]     [D] [T]
            [G] [H] [H] [M] [N] [F]
        [J] [N] [D] [F] [J] [H] [B]
    [Q] [F] [W] [S] [V] [N] [F] [N]
[W] [N] [H] [M] [L] [B] [R] [T] [Q]
[L] [T] [C] [R] [R] [J] [W] [Z] [L]
[S] [J] [S] [T] [T] [M] [D] [B] [H]
 1   2   3   4   5   6   7   8   9

BOAT = [
    ['S', 'L', 'W'],
    ['J', 'T', 'N', 'Q'],
    ['S', 'C', 'H', 'F', 'J'],
    ['T', 'R', 'M', 'W', 'N', 'G', 'B'],
    ['T', 'R', 'L', 'S', 'D', 'H', 'Q', 'B'],
    ['M', 'J', 'B', 'V', 'F', 'H', 'R', 'L'],
    ['D', 'W', 'R', 'N', 'J', 'M'],
    ['B', 'Z', 'T', 'F', 'H', 'N', 'D', 'J'],
    ['H', 'L', 'Q', 'N', 'B', 'F', 'T'],
]

No es necesario crear una función que parsee estos datos, puedes inicializar a mano tu estructura con estos datos.

Las instrucciones con los movimientos a realizar vienen en un fichero, que sí deberás parsear.

Se valorará no solo encontrar la solución sino que el código sea legible.

Que el código esté optimizado no es importante.
