# Proyecto Digitalización 2 🎬  

## ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?
1. **Generar**: Cuando buscas un libro o una peli, el programa saca la info de **OMDb** (para pelis) o **Google Books** (para libros).  
2. **Almacenar**: Lo guardo en un **archivo XML** para que puedas verlo después.  
3. **Consultar**: Si quieres ver tu lista, el programa **lee el XML** y te muestra lo que tienes guardado.  
4. **Eliminar**: Si decides borrar algo, el programa **actualiza el archivo** y lo quita.  
5. **Recomendar**: Basándome en lo que tienes guardado, el programa usa **Gemini** para recomendarte algo nuevo.  

##  ¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?
- Compruebo que la peli o el libro existen antes de guardarlos.  
- Mantengo el archivo XML ordenado para que no se dañe.  
- Si pasa algo raro y el archivo se rompe, el programa lo arregla creando uno nuevo.  

---

#  Almacenamiento en la nube  

## ¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual?
- **SQLite o MongoDB**: Son bases de datos buenas, pero para lo que necesito, XML me basta.  
- **JSON**: Es otra opción, pero XML es más claro en este caso.  

## Si no trabajas con datos, ¿cómo podrías incluir una funcionalidad que los gestione de forma eficiente?
- Los datos los guardo en un fichero XML en local pero:

    Podría **subir los datos a Google Drive o Firebase** para acceder desde cualquier lado.

    Usar **una base de datos online** para guardar las listas.  

---

# Seguridad y normas  

## ¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?
- Solo uso **fuentes oficiales** (OMDb y Google Books).  
- Verifico que los datos sean correctos antes de guardarlos.  

## ¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta?
- **Normas de las APIs**: Respeto las reglas de OMDb y Google Books para no abusar de sus servicios.  

---

# ¿Cómo podría usarse en empresas o fábricas?  

## ¿Qué impacto tendría tu software en un entorno de negocio o en una planta industrial? 
- **Librerías o videoclubs** pueden usarlo para llevar el control de sus catálogos.  
- **Plataformas de streaming** podrían usarlo para recomendar contenido a los usuarios.  

## ¿Cómo crees que tu solución podría mejorar procesos operativos o la toma de decisiones?
- **Búsquedas más rápidas**: Encuentras pelis y libros en segundos.  
- **Mejores recomendaciones**: Sugiere cosas que realmente te podrían gustar.  

---

# IT y OT (tecnología en empresas)  

## Si no aplica a IT u OT, ¿cómo podrías adaptarlo para mejorar procesos tecnológicos concretos? 
- Haciendo una **app móvil** para sincronizar las listas. 

---

# Tecnologías Digitales (THD)  

## ¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?
- **APIs**: Para buscar info automáticamente en OMDb y Google Books.  
- **XML**: Para guardar los datos bien organizados.  

## ¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software?
- **No tienes que escribir nada manualmente** porque busca la info solo.  
- **Se puede ampliar fácilmente** si quiero añadir más cosas.  

