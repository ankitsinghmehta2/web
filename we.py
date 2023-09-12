import streamlit as st
data1=st.text_input("Enter your name")
fname=st.text_input("Enter your father name")
adrs=st.text_area("Enter your area")
ged=st.selectbox("Enter your Gender :", ("MALE","FEMALE","OTHER"))
happy=st.selectbox("Enter the mode of you :",("happy","sad"))
var=st.button("Sumit Now")
if var:
    st.markdown(f"""
    Name : {data1}
    father name : {fname}
    address : {adrs}
    Gender : {ged}
    mode: {happy}
    """)