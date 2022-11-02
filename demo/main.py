import streamlit as st
import numpy as np

def load_model():
    model = np.array([0.88502653, 1.57509821])
    return model

def predict(amount):
    predict = model[0] * amount + model[1]
    predict_time = [int(predict), round((predict - int(predict))*60)]
    return predict_time

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

model = load_model()
st.title('Время сборки заказа')
number = st.slider('Количество товаров в заказе', 1, 60)
result = st.button("Рассчитать время")

if result:
    st.write("Расчетное время сборки составляет ~", predict(number)[0], "мин.", predict(number)[1], "сек.")

