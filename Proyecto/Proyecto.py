import requests
import xml.etree.ElementTree as ET
import os

# Configura tus claves de API
OMDB_API_KEY = 'e7c1bec0'  # Reemplaza con tu clave de API
GOOGLE_BOOKS_API_URL = 'https://www.googleapis.com/books/v1/volumes?q='
GEMINI_API_KEY = 'AIzaSyDGxsfH03G3mmZj0IfYyKuw_gAwkPWg6kI'
GEMINI_API_URL = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}'

# Función para buscar películas
def buscar_pelicula(titulo):
    url = f"http://www.omdbapi.com/?t={titulo}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        print("\n🔍 Resultados de la búsqueda:")
        print(f"🎬 Título: {data.get('Title', 'Desconocido')}")
        print(f"📅 Año: {data.get('Year', 'Desconocido')}")
        print(f"⏳ Duración: {data.get('Runtime', 'Desconocida')}")
        print(f"🎭 Género: {data.get('Genre', 'Desconocido')}")
        print(f"📝 Descripción: {data.get('Plot', 'No disponible')}\n")
    else:
        print("❌ No se encontró la película.")

# Función para buscar libros con formato limpio
def buscar_libro(titulo):
    url = GOOGLE_BOOKS_API_URL + titulo
    response = requests.get(url)
    data = response.json()

    if "items" in data:
        libro = data["items"][0]["volumeInfo"]
        print("\n🔍 Resultados de la búsqueda:")
        print(f"📖 Título: {libro.get('title', 'Desconocido')}")
        print(f"🖊️ Autor(es): {', '.join(libro.get('authors', ['Desconocido']))}")
        print(f"📅 Publicado en: {libro.get('publishedDate', 'Desconocido')}")
        print(f"📖 Páginas: {libro.get('pageCount', 'Desconocido')}")
        print(f"📝 Descripción: {libro.get('description', 'No disponible')}\n")
    else:
        print("❌ No se encontró el libro.")

# Función para registrar en XML
def registrar_en_xml(tipo, titulo):
    archivo = 'biblioteca.xml'
    root = ET.Element('biblioteca')

    if os.path.exists(archivo):
        try:
            tree = ET.parse(archivo)
            root = tree.getroot()
        except ET.ParseError:
            os.remove(archivo)
            root = ET.Element('biblioteca')

    item = ET.SubElement(root, 'item')
    ET.SubElement(item, 'tipo').text = tipo
    ET.SubElement(item, 'titulo').text = titulo

    tree = ET.ElementTree(root)
    tree.write(archivo, encoding="utf-8", xml_declaration=True)


# Función para obtener recomendaciones con la API de Gemini
def obtener_recomendaciones(tipo):
    items = cargar_datos_xml()
    if not items:
        print("No hay libros o películas registrados para obtener recomendaciones.")
        return

    input_text = "Recomiéndame 5 " + ("películas" if tipo == 'pelicula' else "libros") + " similares a: "
    input_text += ", ".join([titulo for t, titulo in items if t == tipo])

    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": input_text}]}]}

    response = requests.post(GEMINI_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        recomendaciones = response.json()
        print("\n📌 Recomendaciones:")
        for recomendacion in recomendaciones.get('candidates', []):
            print(recomendacion['content']['parts'][0]['text'].strip())
    else:
        print("❌ Error al obtener recomendaciones:", response.status_code, response.text)

# Función para cargar datos desde XML
def cargar_datos_xml():
    archivo = 'biblioteca.xml'
    if os.path.exists(archivo):
        try:
            tree = ET.parse(archivo)
            root = tree.getroot()
            return [(item.find('tipo').text, item.find('titulo').text) for item in root.findall('item')]
        except ET.ParseError:
            print("Error: No se pudo leer el archivo XML porque está mal formado.")
    return []

# Función para eliminar un libro o película
def eliminar_item(tipo):
    items = cargar_datos_xml()
    items_filtrados = [t for t in items if t[0] == tipo]

    if not items_filtrados:
        print(f"No tienes {'películas' if tipo == 'pelicula' else 'libros'} en la lista.")
        return

    print(f"\nTus {'películas' if tipo == 'pelicula' else 'libros'}:")
    for i, (t, titulo) in enumerate(items_filtrados, 1):
        print(f"{i}. {titulo}")

    try:
        opcion = int(input("Selecciona el número del que quieres eliminar: ")) - 1
        if 0 <= opcion < len(items_filtrados):
            items.remove(items_filtrados[opcion])

            root = ET.Element('biblioteca')
            for t, titulo in items:
                item = ET.SubElement(root, 'item')
                ET.SubElement(item, 'tipo').text = t
                ET.SubElement(item, 'titulo').text = titulo

            tree = ET.ElementTree(root)
            tree.write('biblioteca.xml', encoding="utf-8", xml_declaration=True)

            print("Elemento eliminado con éxito.")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Error: Debes ingresar un número.")

# Función principal
def main():
    while True:
        print("\n📌 MENÚ PRINCIPAL")
        print("1. 🔍 Buscar")
        print("2. ➕ Añadir")
        print("3. 📜 Ver lista")
        print("4. 🌟 Recomendaciones")
        print("5. ❌ Eliminar libro o película")
        print("6. 🚪 Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':  # Buscar
            print("\n🔍 BÚSQUEDA")
            print("1. Buscar película")
            print("2. Buscar libro")
            subopcion = input("Selecciona una opción: ")
            if subopcion == '1':
                titulo = input("Introduce el título de la película: ")
                buscar_pelicula(titulo)
            elif subopcion == '2':
                titulo = input("Introduce el título del libro: ")
                buscar_libro(titulo)

        elif opcion == '2':  # Añadir
            print("\n➕ AÑADIR")
            print("1. Añadir película")
            print("2. Añadir libro")
            subopcion = input("Selecciona una opción: ")
            if subopcion == '1':
                titulo = input("Introduce el título de la película: ")
                registrar_en_xml('pelicula', titulo)
            elif subopcion == '2':
                titulo = input("Introduce el título del libro: ")
                registrar_en_xml('libro', titulo)

        elif opcion == '3':  # Ver lista
            print("\n📜 VER LISTA")
            print("1. Ver mis películas")
            print("2. Ver mis libros")
            subopcion = input("Selecciona una opción: ")
            if subopcion == '1':
                for t, titulo in cargar_datos_xml():
                    if t == 'pelicula':
                        print(f"🎬 {titulo}")
            elif subopcion == '2':
                for t, titulo in cargar_datos_xml():
                    if t == 'libro':
                        print(f"📖 {titulo}")

        elif opcion == '4':  # Recomendaciones
            print("\n🌟 RECOMENDACIONES")
            print("1. Recomendaciones de películas")
            print("2. Recomendaciones de libros")
            subopcion = input("Selecciona una opción: ")
            if subopcion == '1':
                obtener_recomendaciones('pelicula')
            elif subopcion == '2':
                obtener_recomendaciones('libro')

        elif opcion == '5':  # Eliminar
            print("\n❌ ELIMINAR")
            print("1. Eliminar película")
            print("2. Eliminar libro")
            subopcion = input("Selecciona una opción: ")
            if subopcion == '1':
                eliminar_item('pelicula')
            elif subopcion == '2':
                eliminar_item('libro')

        elif opcion == '6':  # Salir
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
