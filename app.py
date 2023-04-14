import streamlit as st
import pickle
import requests

# API Key: 887f865bdc7afcfc949d7d5272cc5091

api_key = '887f865bdc7afcfc949d7d5272cc5091'

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + api_key + "&language=en-US"
    response = requests.get(url)
    data = response.json()
    print(data['original_title'])
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

similarity = pickle.load(open('similar.pkl','rb'))
movies = pickle.load(open('movies.pkl', 'rb'))

st.title('Movie Recommendor System')

selected_movie_name = st.selectbox(
    'Movie?',
    movies['title']
)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    rec_movies = []
    rec_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        rec_movies.append(movies.iloc[i[0]].title)
        rec_movie_posters.append(fetch_poster(movie_id))

    return rec_movies, rec_movie_posters

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    c1,c2,c3,c4,c5 = st.columns(5)
    with c1:
        st.text(names[0])
        st.image(posters[0])
    with c2:
        st.text(names[1])
        st.image(posters[1])
    with c3:
        st.text(names[2])
        st.image(posters[2])
    with c4:
        st.text(names[3])
        st.image(posters[3])
    with c5:
        st.text(names[4])
        st.image(posters[4])
    
    
        
