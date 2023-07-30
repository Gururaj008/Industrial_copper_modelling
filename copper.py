import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import gzip
import numpy as np
import pandas as pd
import numpy as np
import datetime
from sklearn.preprocessing import OneHotEncoder
import scipy.stats as stats
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import PowerTransformer
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,classification_report,f1_score,plot_confusion_matrix,roc_auc_score,roc_curve,ConfusionMatrixDisplay
from sklearn.metrics import plot_roc_curve
import pickle5 as pkl
import warnings
warnings.filterwarnings("ignore")

def country_code(country):
    list1 = [25,26,27,28,30,32,38,39,40,77,78,79,80,84,89,107,113]
    new_list = []
    for i in list1:
        if i == country:
            new_list.append(np.log1p(1))
        else:
            new_list.append(0)
    return new_list

def item_code(item):
    list2 = ['item_type_IPL','item_type_Others', 'item_type_PL', 'item_type_S', 'item_type_SLAWR','item_type_W', 'item_type_WI']
    new_list_2 = []
    for i in list2:
        if i == item:
            new_list_2.append(np.log1p(1))
        else:
            new_list_2.append(0)
    return new_list_2































if __name__ == '__main__':
    st.set_page_config(layout="wide")
    col101, col102, col103 = st.columns([60,180,60])
    with col102:
        st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text { font-family: 'Agdasima', sans-serif; font-size: 70px;color:cyan }
                    </style>
                    <p class="custom-text">Industrial Copper Modeling</p>
                    """, unsafe_allow_html=True)
    st.write('')
    st.write('')
    selected = option_menu(None, ["About the project","Classification","Regression", "Developer contact details"], 
    icons=['pencil-square', "plus-slash-minus", "123", 'file-person-fill'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

    if selected == 'About the project':
        
        st.write('')
        st.write('')
        st.markdown('<div style="text-align: justify">The copper industry deals with data related to sales and pricing. However, this data may suffer from issues such as skewness and noisy data, which can affect the accuracy of manual predictions. Dealing with these challenges manually can be time-consuming and may not result in optimal pricing decisions. A machine learning regression model can address these issues by utilizing advanced techniques such as data normalization, feature scaling, and outlier detection, and leveraging algorithms that are robust to skewed and noisy data.    </div>', unsafe_allow_html=True)
        st.write('')
        st.markdown('<div style="text-align: justify">The steps involves the project are,   </div>', unsafe_allow_html=True)
        st.write('')
        st.markdown('<div style="text-align: justify">1.	Explored skewness and fix the outliers in the dataset   </div>', unsafe_allow_html=True)
        st.write('')
        st.markdown('<div style="text-align: justify">2.	Transformed the data and performed necessary cleaning and pre-processing steps   </div>', unsafe_allow_html=True)
        st.write('')
        st.markdown('<div style="text-align: justify">3.	Built the ML Classification model which predicts Status: WON or LOST   </div>', unsafe_allow_html=True)
        st.write('')
        st.markdown('<div style="text-align: justify">4.	Built the ML Regression model which predicts continuous variable ‘Selling_Price’   </div>', unsafe_allow_html=True)
        st.write('')
        st.markdown('<div style="text-align: justify">5.	Created a streamlit page where you can insert each column value and you will get the Selling_Price predicted value or Status(Won/Lost)   </div>', unsafe_allow_html=True)
        st.write('')
        # st.markdown('<div style="text-align: justify">   </div>', unsafe_allow_html=True)
        # st.write('')
        st.divider()
        col1001, col1002, col1003,col1004, col1005 = st.columns([10,10,10,10,15])
        with col1005:
            st.markdown("""
                                <style>
                                @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                                .custom-text-10 { font-family: 'Agdasima', sans-serif; font-size: 28px;color:#66FFCC }
                                </style>
                                <p class="custom-text-10">An Effort by : MAVERICK_GR</p>
                                """, unsafe_allow_html=True)  
        

    if selected == 'Classification':
        
        st.divider()
        st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-2 { font-family: 'Optima', sans-serif; font-size: 20px;color:GreenYellow }
                    </style>
                    <p class="custom-text-2">Please provide the input to the following fields in order to predict whether the offer is won or lost </p>
                    """, unsafe_allow_html=True)
        st.write('')
        st.write('')

        col104, col105 = st.columns([20,20])
        with col104:
            st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-3 { font-family: 'Geneva', sans-serif; font-size: 20px;color:Gold }
                    </style>
                    <p class="custom-text-3"> Enter the customer ID </p>
                    """, unsafe_allow_html=True)
            st.write('')
            st.write('')
        with col105:
            cust1 = st.text_input('Range: 30072488 to 30404216', '', key=2)
            if cust1:
                try:
                    cust = int(cust1)
                except ValueError:
                    st.warning("Invalid input. Please enter a valid integer.")
            else:
                st.warning("Please enter an integer.")

            st.write('')
            st.write('')

        col104, col105 = st.columns([20,20])
        with col104:
            st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-3 { font-family: 'Geneva', sans-serif; font-size: 20px;color:Gold }
                    </style>
                    <p class="custom-text-3"> Enter the application ID </p>
                    """, unsafe_allow_html=True)
            st.write('')
            st.write('')
        with col105:
            app1 = st.text_input('Range: 10 to 68', '', key=3)
            if app1:
                try:
                    app = int(app1)
                except ValueError:
                    st.warning("Invalid input. Please enter a valid integer.")
            else:
                st.warning("Please enter an integer.")
            st.write('')
            st.write('')

        col104, col105 = st.columns([20,20])
        with col104:
            st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-3 { font-family: 'Geneva', sans-serif; font-size: 20px;color:Gold }
                    </style>
                    <p class="custom-text-3"> Enter the thickness in cm </p>
                    """, unsafe_allow_html=True)
            st.write('')
            st.write('')
        with col105:
            thick1 = st.text_input('Range: 0.18 to 6.39', '', key=4)
            if thick1:
                try:
                    thick = float(thick1)
                except ValueError:
                    st.warning("Invalid input. Please enter a valid floating point number.")
            else:
                st.warning(" Please enter a floating point number.")
            st.write('')
            st.write('')

        col104, col105 = st.columns([20,20])
        with col104:
            st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-3 { font-family: 'Geneva', sans-serif; font-size: 20px;color:Gold }
                    </style>
                    <p class="custom-text-3"> Enter the width in cm </p>
                    """, unsafe_allow_html=True)
            st.write('')
            st.write('')
        with col105:
            width1 = st.text_input('Range: 691.25 to 1985.25', '', key=5)
            if width1:
                try:
                    width = float(width1)
                except ValueError:
                    st.warning("Invalid input. Please enter a valid floating point number.")
            else:
                st.warning(" Please enter a floating point number.")
            st.write('')
            st.write('')

        col104, col105 = st.columns([20,20])
        with col104:
            st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-3 { font-family: 'Geneva', sans-serif; font-size: 20px;color:Gold }
                    </style>
                    <p class="custom-text-3"> Enter the quantity in tons </p>
                    """, unsafe_allow_html=True)
            st.write('')
            st.write('')
        with col105:
            quantity1 = st.text_input('Range: 0.00001 to 146.13', '', key=6)
            if quantity1:
                try:
                    quantity = float(quantity1)
                except ValueError:
                    st.warning("Invalid input. Please enter a valid floating point number.")
            else:
                st.warning(" Please enter a floating point number.")
            st.write('')
            st.write('')

        col104, col105 = st.columns([20,20])
        with col104:
            st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-3 { font-family: 'Geneva', sans-serif; font-size: 20px;color:Gold }
                    </style>
                    <p class="custom-text-3"> Enter the selling price in $ </p>
                    """, unsafe_allow_html=True)
            st.write('')
            st.write('')
        with col105:
            price1 = st.text_input('Range: 0.0 to 81236.14', '', key=7)
            if price1:
                try:
                    price = float(price1)
                except ValueError:
                    st.warning("Invalid input. Please enter a valid floating point number.")
            else:
                st.warning(" Please enter a floating point number.")
            st.write('')
            st.write('')

        col104, col105 = st.columns([20,20])
        with col104:
            st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-3 { font-family: 'Geneva', sans-serif; font-size: 20px;color:Gold }
                    </style>
                    <p class="custom-text-3"> Enter the country code </p>
                    """, unsafe_allow_html=True)
            st.write('')
            st.write('')
        with col105:
            cntry = st.selectbox('Select the country code from drop-down menu',('25','26','27','28','30','32','38','39','40','77','78','79','80','84','89','107','113'),key=10)
            country = int(cntry)
            st.write('')
            st.write('')

        col104, col105 = st.columns([20,20])
        with col104:
            st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-3 { font-family: 'Geneva', sans-serif; font-size: 20px;color:Gold }
                    </style>
                    <p class="custom-text-3"> Enter the item type </p>
                    """, unsafe_allow_html=True)
            st.write('')
            st.write('')
        with col105:
            item = st.selectbox('Select the item type from drop-down menu',('item_type_IPL','item_type_Others','item_type_PL','item_type_S','item_type_SLAWR','item_type_W','item_type_WI'),key=11)
            st.write('')
            st.write('')
        
        if st.button('Predict the outcome of the offer',use_container_width=True):
            list1 = [cust,app,thick, width, quantity, price]
            list_1 = [np.log1p(x) for x in list1]
            list2 = country_code(country)
            list3 = item_code(item)
            final_list = list_1+list2+list3
            with gzip.open('compressed_model_bag.pkl.gz', 'rb') as f:
                model = pkl.load(f)
                res = model.predict([final_list])
            if res == 1:
                col106, col107,col108 = st.columns([50,120,50])
                with col107:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-5 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:Aquamarine }
                        </style>
                        <p class="custom-text-5"> Congratulations! You have won the offer.... </p>
                        """, unsafe_allow_html=True)
                col106, col107,col108 = st.columns([60,100,60])
                with col107:
                    st.image('celeb.gif')             
                    
            else:
                col106, col107,col108 = st.columns([50,120,50])
                with col107:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-6 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:Salmon }
                        </style>
                        <p class="custom-text-6"> Sorry...! you have not won the offer.. </p>
                        """, unsafe_allow_html=True)
                col106, col107,col108 = st.columns([100,75,100])
                with col107:    
                    st.image('sad.gif')
                
        st.divider()
        col1001, col1002, col1003,col1004, col1005 = st.columns([10,10,10,10,15])
        with col1005:
            st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-11 { font-family: 'Agdasima', sans-serif; font-size: 28px;color:#CCFF00 }
                        </style>
                        <p class="custom-text-11">An Effort by : MAVERICK_GR</p>
                        """, unsafe_allow_html=True)           

    if selected == 'Regression':
            
            st.divider()
            st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-2 { font-family: 'Optima', sans-serif; font-size: 20px;color:GreenYellow }
                        </style>
                        <p class="custom-text-2">Please provide the input to the following fields in order to predict the selling price </p>
                        """, unsafe_allow_html=True)
            st.write('')
            st.write('')

            col104, col105 = st.columns([20,20])
            with col104:
                st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-3 { font-family: 'Geneva', sans-serif; font-size: 20px;color:Gold }
                        </style>
                        <p class="custom-text-3"> Enter the customer ID </p>
                        """, unsafe_allow_html=True)
                st.write('')
                st.write('')
            with col105:
                cust1 = st.text_input('Range: 30072488 to 30404216', '', key=2)
                if cust1:
                    try:
                        cust = int(cust1)
                    except ValueError:
                        st.warning("Invalid input. Please enter a valid integer.")
                else:
                    st.warning("Please enter an integer.")

                st.write('')
                st.write('')

            col104, col105 = st.columns([20,20])
            with col104:
                st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-3 { font-family: 'Geneva', sans-serif; font-size: 20px;color:Gold }
                        </style>
                        <p class="custom-text-3"> Enter the application ID </p>
                        """, unsafe_allow_html=True)
                st.write('')
                st.write('')
            with col105:
                app1 = st.text_input('Range: 10 to 68', '', key=3)
                if app1:
                    try:
                        app = int(app1)
                    except ValueError:
                        st.warning("Invalid input. Please enter a valid integer.")
                else:
                    st.warning("Please enter an integer.")
                st.write('')
                st.write('')

            col104, col105 = st.columns([20,20])
            with col104:
                st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-3 { font-family: 'Geneva', sans-serif; font-size: 20px;color:Gold }
                        </style>
                        <p class="custom-text-3"> Enter the thickness in cm</p>
                        """, unsafe_allow_html=True)
                st.write('')
                st.write('')
            with col105:
                thick1 = st.text_input('Range: 0.18 to 6.39', '', key=4)
                if thick1:
                    try:
                        thick = float(thick1)
                    except ValueError:
                        st.warning("Invalid input. Please enter a valid floating point number.")
                else:
                    st.warning(" Please enter a floating point number.")
                st.write('')
                st.write('')

            col104, col105 = st.columns([20,20])
            with col104:
                st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-3 { font-family: 'Geneva', sans-serif; font-size: 20px;color:Gold }
                        </style>
                        <p class="custom-text-3"> Enter the width in cm </p>
                        """, unsafe_allow_html=True)
                st.write('')
                st.write('')
            with col105:
                width1 = st.text_input('Range: 691.25 to 1985.25', '', key=5)
                if width1:
                    try:
                        width = float(width1)
                    except ValueError:
                        st.warning("Invalid input. Please enter a valid floating point number.")
                else:
                    st.warning(" Please enter a floating point number.")
                st.write('')
                st.write('')

            col104, col105 = st.columns([20,20])
            with col104:
                st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-3 { font-family: 'Geneva', sans-serif; font-size: 20px;color:Gold }
                        </style>
                        <p class="custom-text-3"> Enter the quantity in tons </p>
                        """, unsafe_allow_html=True)
                st.write('')
                st.write('')
            with col105:
                quantity1 = st.text_input('Range: 0.00001 to 146.13', '', key=6)
                if quantity1:
                    try:
                        quantity = float(quantity1)
                    except ValueError:
                        st.warning("Invalid input. Please enter a valid floating point number.")
                else:
                    st.warning(" Please enter a floating point number.")
                st.write('')
                st.write('')

            col104, col105 = st.columns([20,20])
            with col104:
                st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-3 { font-family: 'Geneva', sans-serif; font-size: 20px;color:Gold }
                        </style>
                        <p class="custom-text-3"> Enter the country code </p>
                        """, unsafe_allow_html=True)
                st.write('')
                st.write('')
            with col105:
                cntry = st.selectbox('Select the country code from drop-down menu',('25','26','27','28','30','32','38','39','40','77','78','79','80','84','89','107','113'),key=10)
                country = int(cntry)
                st.write('')
                st.write('')

            col104, col105 = st.columns([20,20])
            with col104:
                st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-3 { font-family: 'Geneva', sans-serif; font-size: 20px;color:Gold }
                        </style>
                        <p class="custom-text-3"> Enter the item type </p>
                        """, unsafe_allow_html=True)
                st.write('')
                st.write('')
            with col105:
                item = st.selectbox('Select the item type from drop-down menu',('item_type_IPL','item_type_Others','item_type_PL','item_type_S','item_type_SLAWR','item_type_W','item_type_WI'),key=11)
                st.write('')
                st.write('')
            
            if st.button('Predict the selling price',use_container_width=True):
                list1 = [cust,app,thick, width, quantity]
                list_1 = [np.log1p(x) for x in list1]
                list2 = country_code(country)
                list3 = item_code(item)
                final_list = list_1+list2+list3
                with open("model_hist.pkl", "rb") as file:
                    model = pkl.load(file)
                res = model.predict([final_list])
                res2 = round(res[0],2)
                msg = f'The predicted price is: {res2} $'
                col106, col107, col108 = st.columns([35,80,35])
                with col107:
                    st.markdown(f'<h1 style="font-family: Agdasima,sans-serif; color: #FF7F50;",font-size: 32px;>{msg}</h1>', unsafe_allow_html=True)

            st.divider()
            col1001, col1002, col1003,col1004, col1005 = st.columns([10,10,10,10,15])
            with col1005:
                st.markdown("""
                                <style>
                                @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                                .custom-text-10 { font-family: 'Agdasima', sans-serif; font-size: 28px;color:Salmon }
                                </style>
                                <p class="custom-text-10">An Effort by : MAVERICK_GR</p>
                                """, unsafe_allow_html=True)                  
                
    if selected == 'Developer contact details':
            st.divider()
            col301, col302 = st.columns([10,20])
            with col301:
                st.markdown(":orange[email id:]")
                st.write('')
            with col302:
                st.markdown(":yellow[gururaj008@gmail.com]")
                st.write('')

            col301, col302 = st.columns([10,20])
            with col301:
                st.markdown(":orange[Personal webpage hosting other Datascience projects :]")
                st.write('')
            with col302:
                st.markdown(":yellow[http://gururaj008.pythonanywhere.com/]")
                st.write('')

            col301, col302 = st.columns([10,20])
            with col301:
                st.markdown(":orange[LinkedIn profile :]")
                st.write('')
            with col302:
                st.markdown(":yellow[https://www.linkedin.com/in/gururaj-hc-data-science-enthusiast/]")
                st.write('')


            col301, col302 = st.columns([10,20])
            with col301:
                st.markdown(":orange[Github link:]")
                st.write('')
            with col302:
                st.markdown(":yellow[https://github.com/Gururaj008]")
                st.write('')

            
            
            st.divider()
            col1001, col1002, col1003,col1004, col1005 = st.columns([10,10,10,10,15])
            with col1005:
                st.markdown("""
                                <style>
                                @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                                .custom-text-10 { font-family: 'Agdasima', sans-serif; font-size: 28px;color:#FF99FF }
                                </style>
                                <p class="custom-text-10">An Effort by : MAVERICK_GR</p>
                                """, unsafe_allow_html=True)        