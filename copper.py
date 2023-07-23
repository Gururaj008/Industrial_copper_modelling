import streamlit as st
from streamlit_option_menu import option_menu

if __name__ == '__main__':
    st.set_page_config(layout="wide")
    col101, col102, col103 = st.columns([20,60,20])
    with col102:
        st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text { font-family: 'Agdasima', sans-serif; font-size: 60px;color:cyan }
                    </style>
                    <p class="custom-text">Industrial Copper Modeling</p>
                    """, unsafe_allow_html=True)
    st.write('')
    st.write('')
    selected = option_menu(None, ["About the project","Classification","Regression", "Developer contact details"], 
    icons=['pencil-square', "plus-slash-minus", "123", 'file-person-fill'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
