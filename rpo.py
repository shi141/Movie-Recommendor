import streamlit as st
import pickle
import pandas as pd

movie_list=pickle.load(open('movies.pkl','rb'))
movie_list=movie_list['title'].values

movies=pd.DataFrame(movie_list)
st.title('Movie Recommender')

def recommend(movie):
    #find index of the movie in dataset
    m_index=movies[movies['title']==movie].index[0]
    #perform cosine_similarity to find similarity of the movie with other movies
    distance=similarity[m_index]
    m_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    rec_mov=[]
    for i in m_list:
        rec_mov.append(movies.iloc[i[0]].title)
    return rec_mov

similarity=pickle.load(open('similarity.pkl','rb'))
option = st.selectbox(
    "How would you like to be contacted?",
    movie_list,
)

if st.button("Recommend"):
    recommendation=recommend(option)
    for i in recommendation:
        st.write(i)


