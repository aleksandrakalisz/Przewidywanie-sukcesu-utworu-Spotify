import streamlit as st
import pandas as pd
from sklearn import linear_model
import time


st.title(":violet[Przewidywanie popularności utworu na Spotify]")
st.set_page_config(page_title="Przewidywanie popularności Spotify", page_icon="ikona.png")
st.markdown("Model przewiduje wynik utworu platformie Spotify w skali 0-100, gdzie 100 to najlepszy możliwy wynik. Prognoza jest wyliczana na podstawie wprowadzonych danych, dotyczących wyników artysty w mediach społecznościowych.")
st.logo("ikona.png")
st.image("nutki.jpg")
dane=pd.read_excel("dane.xlsx")
x=dane.drop(columns=["Tytuł", "Wykonawca", "Popularność utworu Spotify"])
y= dane["Popularność utworu Spotify"]

regresja=linear_model.LinearRegression()
regresja.fit(x,y)

st.subheader("Wprowadź dane")

lewa, prawa= st.columns(2, border=True)

with lewa:
    miesieczni_sluchacze_spotify= st.number_input("Liczba miesięcznych słuchaczy Spotify", min_value=0)
    obs_spotify=st.number_input("Liczba obserwujących Spotify", min_value=0)
    subskrybcje_yt=st.number_input("Liczba subskrybcji YouTube", min_value=0)
with prawa:
    obs_insta=st.number_input("Obserwujący Instagram", min_value=0)
    nowi_obs_insta=st.number_input("Liczba nowych obserwujących instagram(14 dni)", min_value=0)
    wszystkie_polubienia_tiktok=st.number_input("Polubienia TikTok (wszystkie fimy na profilu)", min_value=0)

if st.button("Oblicz"):
    wprowadzone_dane= [[
        miesieczni_sluchacze_spotify,
        obs_spotify,
        subskrybcje_yt,
        obs_insta,
        nowi_obs_insta,
        wszystkie_polubienia_tiktok
    ]]
    with st.spinner("Jeszcze chwila...", show_time=True):
        time.sleep(5)
        st.success("Gotowe!")
        st.balloons()
        st.button("Powrót")
    przewidywany_wynik_utworu = regresja.predict(wprowadzone_dane)[0]
    przewidywany_wynik_utworu=max(0, min(100, przewidywany_wynik_utworu))

    st.metric("Przewidywany wynik utworu na Spotify:", round(przewidywany_wynik_utworu,0))
    if przewidywany_wynik_utworu <=20:
        opis="Bardzo słaby wynik"
        zdjecie= "bardzoslabo.gif"
    elif przewidywany_wynik_utworu <=40:
        opis="Słaby wynik"
        zdjecie= "slabo.gif"
    elif przewidywany_wynik_utworu <=60:
        opis="Satysfakcjonujący wynik"
        zdjecie= "ok.gif"
    elif przewidywany_wynik_utworu <=80:
        opis="Dobry wynik"
        zdjecie= "dobrze.gif"
    else:
        opis="Świetny wynik"
        zdjecie="super.gif"
    st.subheader(opis)
    st.image(zdjecie, width=400)

