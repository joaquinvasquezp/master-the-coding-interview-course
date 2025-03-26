# Arrays

En algunos casos también es llamado "List".

Organiza elementos de manera secuencial, esto quiere decir 1 y después el otro, en memoria.

Pensar que estos son los “cajones” en memoria:

[0] → Juice
[1] → Apple
[2] → Cheese
…

Tienen la menor cantidad de reglas, los mas sencillos de usar.

Si solo necesitas almacenar datos e iterar sobre ellos (1 a 1) esta es la mejor opción, especialmente si conocemos el index de los elementos.

# Operaciones

Time complexity

- Access (lookup) → O(1)
- Push → O(1) *constant time*
- Insert → O(n) *linear time*
- Delete → O(n)

En JavaScript por ejemplo:

- *Si es un pop(), por ejemplo en JavaScript, sería O(1)*
- Unshift() → añade un elemento al principio del array, O(n) ya que mueve todo lo existente “1 espacio” en memoria para añadir el nuevo al principio
- Splice() → O(n)

# Static arrays vs Dynamic arrays

Arrays estáticos tienes que definir la cantidad de elementos que almacenará el array.

Dynamic array funciona de la siguiente manera:

- Si a un array estático se le quiere añadir un elemento más fuera de la cantidad definida
- Entra acá el array dinámico, se copia el estático en un nuevo array y se añade el nuevo elemento
- Para este caso de array estáticos en insert (push, al final del array) tendría un time complexity O(n)
- Esto en Python y JavaScript no ocurre, en lenguaje como C++ puede ocurrir.