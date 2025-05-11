# 📚 Project Wiki

Welcome to the Wiki for the Movies & Books Recommender project. Here you'll find technical documentation and a devlog to track the evolution of the project.

---

## 🛠 Developer Documentation

### 🔧 Project Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/jvazlop/ProyectoDigitalizacion2.git
   ```

2. **Install dependencies:**

   * Python 3.8+

3. **Add your API keys:**

   * OMDb API Key: [https://www.omdbapi.com/](https://www.omdbapi.com/)
   * Google Books API: No key needed.
   * Gemini API Key: Requires access to Google AI Studio.

   Update your `main.py` file with the appropriate keys:

   ```python
   OMDB_API_KEY = 'your_key_here'
   GEMINI_API_KEY = 'your_key_here'
   ```

### 🗃 File Structure

```plaintext
movies-books-recommender/
│
├── main.py               # Main logic and CLI
├── biblioteca.xml        # Stored user items
├── README.md             # Overview and usage
├── CONTRIBUTING.md       # Contribution guidelines
└── wiki.md               # Project documentation and devlog
```

### 🔄 Key Functions

* `buscar_pelicula(titulo)`: Search for a movie using OMDb API.
* `buscar_libro(titulo)`: Search for a book using Google Books API.
* `registrar_en_xml(tipo, titulo)`: Save movie/book to an XML file.
* `obtener_recomendaciones(tipo)`: Ask Gemini API for similar items.

### 🚀 Run the Project

```bash
python Proyecto.py
```

## 📓 Devlog

### ✅ Week 1: Project Initialization

* Defined project scope.
* Set up main script and XML storage.
* Integrated OMDb and Google Books API.

### ✅ Week 2: Gemini Integration

* Connected Gemini API for recommendation system.
* Added functionality to request recommendations based on saved items.

### ✅ Week 3: User Interface and Menu

* Implemented CLI with search, add, list, delete, and recommendation features.
* Enhanced error handling for XML and API calls.

---

Feel free to extend this wiki with additional pages or improvements!

