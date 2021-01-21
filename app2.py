import pickle
import streamlit as st
import numpy as np
from PIL import Image
from sklearn.ensemble import RandomForestClassifier

#load the trained model
pickle_in = open("model.pkl","rb")
classifier = pickle.load(pickle_in)

#defining the function wich will make the prediction using the data wich the user inputs

def prediction(Area, Qualidade, AnoConstrucao,Banheiros,Comodos, Lareiras,Garagem):


	yhat = classifier.predict([[Area, Qualidade, AnoConstrucao,Banheiros,Comodos, Lareiras,Garagem]])

	prediction = (yhat)
	
	return prediction

def main():
	# front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Precificando Imóveis</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    st.text("Autor: Jorge Barros - Data Scientist")

    Area = st.slider("Área do imóvel em pés",0,10000,0)

    #menu_options = ["Selecione uma Opção","4","5","6","7","8"]	
    Qualidade = st.slider("Nível de qualidade do acabamento",4,8,1, step = 1)
    AnoConstrucao = st.slider("Ano de Construção do Imóvel",1900,2021,1900, step = 1)
    Banheiros = st.number_input("Quantidade de banheiros", value = 0)
    Comodos = st.number_input("Quantidade de Cômodos do Imóvel", value = 0)
    Lareiras = st.number_input("Quantidade de Lareiras", value = 0)
    Garagem = st.number_input("Quantidade de garagens disponíveis", value = 0)
    result = ""

    if st.button("Predict"):
    	result = prediction(Area, Qualidade, AnoConstrucao,Banheiros,Comodos, Lareiras,Garagem) 
    	st.success("O preço do imóvel será R$ {:.2f} ".format(float(result)))
    	#result

    st.sidebar.title("About Me")
    st.sidebar.title("Autor: Jorge Barros")
    st.sidebar.markdown("Data Scientist")
    st.sidebar.markdown("For more projects, follow me on [Linkedin](https://www.linkedin.com/in/jorge-barros-medeiros/)")
    st.sidebar.markdown("Instagram: [@jorgebarros.ia](https://www.instagram.com/jorgebarros.ia/)")
    st.sidebar.markdown("Repository : [Github](https://github.com/jorgebarrosmedeiros)")

if __name__ == "__main__":
	main()