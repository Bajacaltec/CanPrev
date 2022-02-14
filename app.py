from os import link
import streamlit as st
col1,col2=st.beta_columns(2)
with col1:
    st.title("CanPrev App ")
    st.subheader("Prevención de cancer según edad")
with col2:
    st.image("WAPP.png",None,350)
    st.subheader("https://elmedpost.wordpress.com")
edad=st.slider("Edad",1,130,None)