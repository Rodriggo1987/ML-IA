import streamlit as st  
import pandas as pd 
from sklearn.linear_model import LinearRegression 


df = pd.read_csv('pizzas.csv')

df.columns = df.columns.str.strip()


modelo = LinearRegression() #  modelo de regressão Linear 
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x,y)   #Treinar modelo 




st.title("Prevendo um Valor de Uma Pizza")
st.divider()    # inserir uma linha 

diametro = st.number_input("Digite o tamanho do diâmentro da Pizza: ")

if diametro: 
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O valor da pizza com diâmetro de {diametro:.2f} cm é de R${preco_previsto:.2f}.")