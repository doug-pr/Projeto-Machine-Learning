import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="Minha Primeira Página de Machine Learning",
    page_icon="👋",
)

df = pd.read_csv("Pizzas.csv")

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)

st.title("Prevendo o Valor de Uma Pizza")
st.divider()

diametro = st.number_input("Digite o tamanho do diâmetro da pizza:")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O Valor da pizza com diâmetro de {diametro:.2f} cm é de R$ {preco_previsto:.2f}!")
    st.balloons()

<b>Desenvolvido por Douglas Barcelos</b>