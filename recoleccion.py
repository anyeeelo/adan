import feedparser

FUENTES_RSS = [
    "http://feeds.bbci.co.uk/news/rss.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
]

def obtener_rss(url):
    entradas = []
    feed = feedparser.parse(url)
    for entrada in feed.entries[:10]:
        titulo = entrada.get('title', 'Sin título')
        resumen = entrada.get('summary', 'Sin resumen')
        entradas.append({"titulo": titulo, "resumen": resumen})
    return entradas

def obtener_todo_conocimiento():
    todo = []
    for url in FUENTES_RSS:
        todo.extend(obtener_rss(url))
    return todo

if __name__ == "__main__":
    conocimiento = obtener_todo_conocimiento()
    print(f"Obtuvimos {len(conocimiento)} noticias.")

