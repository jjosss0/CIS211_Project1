import streamlit as st

#st.title('👋🏽welsome to my website')
#st.write("i'm building this live in class!")

import pandas as pd 
from datetime import datetime

#page config
st.set_page_config (
   page_title = 'joss | portfolio',
   page_icon='👻�',
   layout= 'wide'
)

#custom CSS (optional - for style)
     <style>
                    .main-header {font-size: 42px; font-weight: bold; text-align:center;}
                    .sub-header {font_size: 24px; text-align:center; color: #666;}
                </style>
            ''', unsafe_allow_html = True)
#sidebar
st.sidebar.title('📍navigation')
page = st.sidebar.radio('Go to',
                        ['🏡Home','🤠About', '💼Project','🔩Skills','📝resume','📧Contact'])
                        


