# 🎬 Akıllı Film Öneri Sistemi

Bu proje, Streamlit arayüzüne sahip bir film öneri sistemidir. Bir film başlığı girdiğinizde, kosinüs benzerliği kullanarak en benzer filmleri bulur ve TMDb API aracılığıyla onların afişlerini gösterir.

## 📌 Proje Özeti

- Proje Google Colab üzerinde geliştirildi.
- Film açıklamaları sayısal vektörlere dönüştürüldü (**TF-IDF**).
- Filmler arası benzerlikler **Cosine Similarity** ile hesaplandı.
- Kullanıcı bir film ismi girince, en yüksek benzerliğe sahip 5 film gösteriliyor.
- Önerilen filmlerin **afiş görselleri**, **TMDb API** üzerinden otomatik olarak çekiliyor.
- Arayüz, **Streamlit** ile oluşturuldu.


📁 Klasör Yapısı

Smart Movie Recommendation Model/
│
├── System/
│   ├── app.py                        # Streamlit arayüzü
│   └── Smart_Movie_Recom.ipynb       # Google Colab geliştirme dosyası
│
└── Veriler ve Gereksinimler/
    ├── movies.csv                    # Film bilgileri (filmId, title, genres)
    ├── credits.csv                   # Film ekibi bilgileri (movie_id, title, cast, crew)
    ├── movie_dict.pkl                # Film verisi sözlüğü (pickle formatında)
    ├── similarity.pkl                # Film benzerlik matrisi (Cosine Similarity)
    └── requirements.txt              # Projenin çalışması için gerekli Python kütüphanelerinin listesi
-
-
-   ## 🚀 Nasıl Çalıştırılır?

```bash
# 1. Projeyi klonla
git clone https://github.com/AliBrn/Smart-Movie-Recommendation-ML.git
cd Smart-Movie-Recommendation-ML

# 2. Gerekli kütüphaneleri yükle
pip install -r requirements.txt

# 3. Uygulamayı başlat
streamlit run app.py
