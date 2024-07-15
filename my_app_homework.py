import pandas as pd
import seaborn as sns
import streamlit as st
import time
import matplotlib.pyplot as plt


df = pd.read_csv("brazil.csv")

st.write("# First Homework in Streamlit")

st.dataframe(df.head(6))



with st.sidebar:
    option = st.selectbox(
        "Which ones you want to see?",
        ("Pix", "TED", "TEC", "BrazilianBoletoPayment"))
    st.write("You selected:", option)

if option =="Pix":
    option1 = st.selectbox(
        "Which ones you want to see?",
        ("Bar_chart", "Line_chart", "Scatter"))
    st.write("You selected:", option1)
    st.header("")
    if option1 == "Bar_chart":
        st.bar_chart(data= df, x="quantityPix", y="valuePix")
    elif option1 == "Line_chart":
        st.line_chart(data= df, x="quantityPix", y="valuePix")
    else:
        st.vega_lite_chart(data= df, x="quantityPix", y="valuePix")


elif option =="TED":
    option1 = st.selectbox(
        "Which ones you want to see?",
        ("Bar_chart", "Line_chart", "Scatter"))
    st.write("You selected:", option1)
    if option1 == "Bar_chart":
        st.bar_chart(data= df, x="quantityTED", y="valueTED")
    elif option1 == "Line_chart":
        st.line_chart(data= df, x="quantityTED", y="valueTED")
    else:
        st.vega_lite_chart(data= df, x="quantityTED", y="valueTED")


elif option =="TEC":
    option1 = st.selectbox(
        "Which ones you want to see?",
        ("Bar_chart", "Line_chart", "Scatter"))
    st.write("You selected:", option1)
    if option1 == "Bar_chart":
        st.bar_chart(data= df, x="quantityTEC", y="valueTEC")
    elif option1 == "Line_chart":
        st.line_chart(data= df, x="quantityTEC", y="valueTEC")
    else:
        st.vega_lite_chart(data= df, x="quantityTEC", y="valueTEC")


else:
    option1 = st.selectbox(
        "Which ones you want to see?",
        ("Bar_chart", "Line_chart", "Scatter"))
    st.write("You selected:", option1)
    if option1 == "Bar_chart":
        st.bar_chart(data= df, x="quantityBrazilianBoletoPayment", y="valueBrazilianBoletoPayment")
    elif option1 == "Line_chart":
        st.line_chart(data= df, x="quantityBrazilianBoletoPayment", y="valueBrazilianBoletoPayment")
    else:
        st.vega_lite_chart(data= df, x="quantityBrazilianBoletoPayment", y="valueBrazilianBoletoPayment")

      

