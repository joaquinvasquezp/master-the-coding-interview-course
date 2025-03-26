# ¿Qué es una Data Structure?

Collection of values, estos valores pueden tener relaciones entre ellos o funciones aplicada a ellos, cada una es distinta, bueno y es especial para su enfoque específico.

Pensarlo como un compartimiento, un cajón, mochila, etc. Cada uno de estos compartimientos son buenos para su respectiva cosa por ejemplo no pondré mi comida en una caja cuando es mejor un refrigerador como contenedor, cada uno es usado para una cosa específica.

Data Structure nos permite ordenar los datos para luego recuperar esos datos fácilmente, podemos quitar y agregar datos a nuestras data structures.

*Bitcoin → blockchain es una Data Structure.*

*Array and objects for example are a form of Data Structure.*

**Es importante conocerlas y saber en que situación nos conviene más usar una en específico.**

# ¿Como los computadores almacenan datos?

En nuestros códigos, definimos variables, las cuales guardan datos, estas variables se almacenan en **RAM** (Random Access Memory) (Space Complexity). Si se apaga el pc se pierde la memoria.

Además de esto tenemos **Storage**, donde almacenan videos, musica, documentos, etc. Puede ser un disco duro, SSD, flash drive (USB), esta **data** es **permanente/persistente**, estará siempre guardado incluso cuando se apaga el pc.

Porque entonces no ocupamos siempre el Storage y no la Memoria, si se va a almacenar siempre? Debido a que Persistent Storage es lento.

Acá entra la **CPU**, el computador corre gracias a la CPU, pensarlo como un pequeño trabajador que hace todo el trabajo dentro del pc, necesita acceso a la RAM y a Storage, puede ingresar a RAM mucho mas rápido.

Puedes imaginarte la RAM como un compartimiento grande que almacena datos, así como una Data Structure. Este compartimiento tiene “cajones” que son números, llamados address, los cuales guardan 8bits (numbers, 0 o 1, un bit), un switch que está “on” or “off”.

8bits ⇒ Byte. Cada “cajon” tiene 1 Byte de almacenamiento.

La CPU está conectada a una Memory Controller el cual se encarga de la lectura/escritura en memoria. Esta conexión tiene via directa a cada compartimiento, si se quiere ver el “cajon” 700 no es necesario pasar por todos los anteriores para ver su valor, por eso su nombre Random Access Memory. Aún así al entrar a “cajon” cercanos entre si, es mucho más rápido, el pc está optimizado para funcionar de esa manera, tiene lo llamado CPU Cache, una memoria muy pequeña que guarda los valores de los “cajones” visitados recientemente. ***Un cache común LRU.***

## Referencias

https://www.youtube.com/watch?v=fpnE6UAfbtU

https://statmath.wu.ac.at/courses/data-analysis/itdtHTML/node55.html

### Capacidades máximas

8-bit → 255

16-bit → 65.536

32-bit → 2.147.483.647 (4 “cajones”)

Cuando ya no se puede almacenar el valor en RAM, se tiene que representar ese valor de alguna manera, por ejemplo en Javascript:

```jsx
Math.pow(6, 1000000); // da como resultado: Infinity
```

<aside>

Las Data Structure funcionan de la misma manera, cada una de ellas tiene un número de bits asociado a ella y necesitan almacenarse en nuestro sistema (RAM).

Nuestro objetivo es minimizar la cantidad de operaciones que realiza nuestra CPU para escribir/obtener estos datos desde la memoria.

</aside>

### La mayoría de los lenguajes de programación vienen con Data Structures ya “listas”, pero no por eso tenemos que utilizar esas, podemos crearlas nosotros.

# Tipos de operaciones sobre Data Structures

- Insertion → añadir un nuevo elemento
- Deletion → eliminar un elemento existente
- Traversal → acceder a cada uno de los elementos 1 vez para ser procesados
- Searching → encontrar la localidad de un elemento en la collection si es que existe
- Sorting → ordenar los datos
- Access → acceder a nuestros datos

![image](https://www.miguelfarrajota.com/images/post/data_structures/common_data_structures_operations.png)