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
data = {
    "Project": ["Excel Dashboard", "Python App", "Quinceañera Website"],
    "Status": ["Completed", "In Progress", "Published"],
    "Date": [datetime(2024, 10, 20), datetime(2025, 4, 15), datetime(2025, 5, 1)]
}
