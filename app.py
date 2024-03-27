import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/324a0d39-9c16-4e8d-a4fe-1c9aee5290ad/df941iz-02ca2842-7988-4e52-981c-f7cf4cd764b4.png/v1/fill/w_1013,h_569,q_80,strp/pastel_clouds___aesthetic_wallpaper_by_waterlemonppy_df941iz-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTY5IiwicGF0aCI6IlwvZlwvMzI0YTBkMzktOWMxNi00ZThkLWE0ZmUtMWM5YWVlNTI5MGFkXC9kZjk0MWl6LTAyY2EyODQyLTc5ODgtNGU1Mi05ODFjLWY3Y2Y0Y2Q3NjRiNC5wbmciLCJ3aWR0aCI6Ijw9MTAxMyJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.bibXbbppT1Z-E-XoOsmGvToF1KMOIbE40GZlZcw_0tY");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='color: black;'>Movie Recommender System</h1>", unsafe_allow_html=True)

movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    ":blue[Type or select a movie from the dropdown]",
    movie_list
)

if st.button(':red[Show Recommendation]'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
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
