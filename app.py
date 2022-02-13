import streamlit as st
col1,col2=st.beta_columns(2)
with col1:
    st.title("App para prevención de cancer")
with col2:
    st.image("WAPP.png",None,350)
edad=st.slider("Edad",1,130,None)