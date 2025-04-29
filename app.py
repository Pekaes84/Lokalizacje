
import pandas as pd
import streamlit as st

# Wczytanie danych
@st.cache_data
def zaladuj_dane():
    return pd.read_excel("lokalizacje - JS.xlsx", sheet_name="Arkusz1")

def wyszukaj_po_symbolu(df, symbol):
    wynik = df[df['Symbol'].str.upper() == symbol.upper()]
    if wynik.empty:
        return None
    else:
        rekord = wynik.iloc[0]
        return {
            'Symbol': rekord['Symbol'],
            'Nazwa': rekord['Nazwa'],
            'Kontener': rekord['1. Kontener'] if pd.notna(rekord['1. Kontener']) else 'brak danych',
            'Regał': rekord['2. Regał'] if pd.notna(rekord['2. Regał']) else 'brak danych',
            'Półka': rekord['3. Półka'] if pd.notna(rekord['3. Półka']) else 'brak danych'
        }

# UI aplikacji Streamlit
st.title("Wyszukiwarka Produktów po Symbolu")
dane = zaladuj_dane()

symbol = st.text_input("Wpisz symbol produktu:")

if symbol:
    wynik = wyszukaj_po_symbolu(dane, symbol)
    if wynik:
        st.write(f"**Symbol:** {wynik['Symbol']}")
        st.write(f"**Nazwa:** {wynik['Nazwa']}")
        st.write(f"**Kontener:** {wynik['Kontener']}")
        st.write(f"**Regał:** {wynik['Regał']}")
        st.write(f"**Półka:** {wynik['Półka']}")
    else:
        st.error("Brak produktu o podanym symbolu.")
