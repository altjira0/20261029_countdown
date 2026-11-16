# Bomba con cuenta atrás

Programa en Python que simula una bomba con una cuenta atrás de 10 a 0. En cada número par el usuario elige qué cable cortar. Los colores de los cables se leen de un archivo JSON.

## Archivos

Archivo 'bomba.py' contiene el código del programa 
Archovo cables.json contiene los colores que desactivan la bomba y los que no hacen nada

## Cómo ejecutarlo

1. Abrir la carpeta del proyecto en Visual Studio Code
2. Ejecutar en la terminal:

```
python bomba.py
```

## Cómo funciona

1. El programa abre 'cables.json' en modo lectura y lo convierte en un diccionario de Python con 'json.load()'.
2. Empieza una cuenta atrás de 10 a 0 con 'range(10, -1, -1)'.
3. Los números 5, 4 y 3 no se muestran: en su lugar aparece '...'.
4. En cada número que se muestra, el programa pregunta qué cable cortar:
   - Si el color está en "desactivan", la bomba se desactiva y el programa termina.
   - Si el color está en "no_hacen_nada", la cuenta atrás sigue.
   - Si el color no está en el JSON, avisa de que ese cable no existe.
5. Si la cuenta llega a 0, la bomba explota.

## Formato del JSON
Para cambiar qué cables desactivan la bomba solo hay que editar este archivo.