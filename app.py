import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6];

        recommended_movies = []

        for i in movies_list:
            movie_id = i[0]
            #fetch the poster of movie

            # print(.iloc[i[0]].title)
            recommended_movies.append(movies.iloc[i[0]].title)

        return recommended_movies


movies_dict = pickle.load(open('MoviesDictonary.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarityValue.pkl','rb'))

st.title('Movie Recommender System');

option = st.selectbox('Select from option Below',movies['title'].values);

if st.button('Recommend'):
    recommendations = recommend(option)
    for i in recommendations:
          st.write(i)