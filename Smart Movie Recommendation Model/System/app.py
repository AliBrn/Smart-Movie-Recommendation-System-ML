import pickle        
import pandas as pd
import streamlit as st 
import requests        

#  ! API ile film afişi çekme fonksiyonu
def fetch_poster(movie_id): 
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id) # * Api key giriş anahtarı /movie/ istediğim film
    data = requests.get(url)  
    data = data.json()
    poster_path = data['poster_path'] # !JSON verisinin içinde "poster_path" anahtarı var. "/kqjL17yufvn9OVLyXYpvtyrFfak.jpg" bu var. Bu sadece dosya yoludur, tam adres değil.
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path # ?poster_path'in başına TMDB'nin resmi görsel adresi (https://image.tmdb.org/t/p/w500/) eklenir.
                                                                 #?  Tam adres ==>https://image.tmdb.org/t/p/w500/kqjL17yufvn9OVLyXYpvtyrFfak.jpg
    return full_path 

# !Film öneri fonksiyonu

def recommend(movie): 
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

#  *  Uygulama başlığı

st.header('Movie Recommender System')

# * Model ve veri yükleme
movies_dict=pickle.load(open(r"C:\Users\msi\Desktop\Smart Movie Recommendation Model\Veriler ve Gereksinimler\movie_dict.pkl","rb"))
similarity=pickle.load(open(r"C:\Users\msi\Desktop\Smart Movie Recommendation Model\Veriler ve Gereksinimler\similarity.pkl","rb"))

movies=pd.DataFrame(movies_dict)

# ? Film seçimi

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)



# ! Öneri butonu ve sonuçların gösterimi

if st.button('Show Recommendation',icon="😃",): 
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    columns = [col1, col2, col3, col4, col5]
    num_recommendations = min(len(recommended_movie_names), len(recommended_movie_posters), 5)

   
    text_area_min_height = "80px" 

    for i in range(num_recommendations):
        with columns[i]: 
           
            st.markdown(
                f"""
                <div style="height: {text_area_min_height}; min-height: {text_area_min_height}; text-align: center; display: flex; flex-direction: column; justify-content: center; margin-bottom: 10px;">
                    <p style="margin: 0; word-wrap: break-word;">{recommended_movie_names[i]}</p>
                </div>
                """,
                unsafe_allow_html=True
            ) 
            
            
            image_width = 150 
            st.image(recommended_movie_posters[i], width=image_width)
            
# * Buton tasarımı (CSS)

st.markdown("""    
    <style>
    .stButton>button {
        background-color: #F5DEB3;  
        color: white;               
        font-size: 16px;           
        padding: 10px 24px;        
        border-radius: 8px;         
        border: none;               
    }

   
    .stButton>button:active {
        background-color: #E0C085;  
    }

    .stButton>button:hover {
        background-color: #E0C085;  
    }

    </style>
    """, unsafe_allow_html=True) 