import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_movies(filepath, query, top_n=5):
    """Recommends movies based on a user query."""
    df = pd.read_csv(filepath)
    print(df.head())  # Inspect the data

    df["combined_text"] = df["overview"].fillna('') + ' ' + df["genres"].fillna('') + ' ' + df["keywords"].fillna('') + ' ' + df["director"].fillna('')
    print(df["combined_text"].head()) # Inspect combined text

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(df["combined_text"])
    print(vectorizer.get_feature_names_out()) # Inspect vocabulary
    print(tfidf_matrix.shape) # Check TF-IDF matrix shape

    query_vec = vectorizer.transform([query])
    print(query_vec) # Check query vector

    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    print(similarities) # Check similarity scores

    top_indices = similarities.argsort()[-top_n:][::-1]
    top_scores = similarities[top_indices]

    recommendations = df.iloc[top_indices]["title"]

    print(f"\nBased on your interest in '{query}', here are some movie recommendations:")
    for i, (title, score) in enumerate(zip(recommendations, top_scores)):
        print(f"🎬 Rank {i+1} | Similarity: {score:.4f} | {title}")

if __name__ == "__main__":
    filepath = "movie_set.csv"  # Replace with your file path
    user_input = input("Tell me what kind of movies you like: ")
    recommend_movies(filepath, user_input)