from fastapi import FastAPI
import mook

app = FastAPI()

@app.get("/")
def root():
    return {
        "Servicio": "Estructuras de datos"
    }

@app.post("/indices-invertidos")
def indices_invertidos(palabra: dict):

    cache = {}
    for index, documents in enumerate(mook.my_documents):
        sentences = documents.split()
        for sentence in sentences:
            words = sentence.lower().split()
            for word in words:
                if word in cache:
                   cache[word].append(documents)
                else:
                    cache[word] = [documents]

    return cache.get(palabra["palabra"], "No se encontro")