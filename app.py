import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=f2a8d3cfa09e52e461c79918f079392c&language=en-US".format(
        movie_id)
    response=requests.get(url)
    data=response.json()
    print(movie_id)

    poster_path=data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path



def recommend(movie):
    movie_index = movies[movies['Title'] == movie].index.values

    distances = similarity[movie_index]

    distances = (list(*distances))

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recomended_movies = []
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recomended_movies.append(movies.iloc[i[0]].Title)
        recommended_movies_poster.append(fetch_poster(i[0]))
    return recomended_movies




movies_list=pickle.load(open('movies.pkl','rb'))
movies_list=movies_list['title'].values
movies=pd.DataFrame(movies_list)
movies.columns=['Title']

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Choose a Movie',movies_list)

if st.button('Recommend_movie'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])



