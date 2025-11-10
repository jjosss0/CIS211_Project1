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
st.markdown('''
                  <style>
                    .main-header {font-size: 42px; font-weight: bold; text-align:center;}
                    .sub-header {font_size: 24px; text-align:center; color: #666;}
                 </style>
            ''', unsafe_allow_html = True)
#sidebar
st.sidebar.title('📍navigation')
page = st.sidebar.radio('Go to',
                        ['🏡Home','🤠About', '💼Project','🔩Skills','📝resume','📧Contact'])
# Home page
if page == '🏡Home':
   st.markdown('<p class= "main-header">josmalli Olivero</p>', unsafe_allow_html=True)
   st.markdown('<p class="sub-header">Aspiring Tech Professional | Medgar Evers College</p>', unsafe_allow_html=True)

   #three columns for stats
   col1, col2, col3 = st.columns(3)
   
   with col1:
      st.metric('GPA', '3.8','📚')
   with col2:
      st.metric('project','5','💻')
   with col3:
      st.metric('skills','10','🚀')
   
st.write('---')
   
#Introduction with columns
col1, col2 = st.columns([2,1])
with col1:
   st.subheader('Welcome to my digital space!👋')
   st.write('''
      
             I am a Computer Information Systems student passionate about web development and emerging technologies. Currently learning
             HTML, CSS, JavaScript, and Python to build innovative solutions.
         
             🎯 **Current Focus:** Building interactive web applications with Streamlit
         
             📚 **Currently Learning:** Internet and Emergin Technologies (CIS 211)
         
             🌱 **Fun Fact:** I can solve a Rubik's cube in under 2 minutes!
         ''')    
with col2:
       # Placeholder for image
       st.image('https://github.com/jjosss0/CIS211_Project1/blob/bc25b2d3ff67041bde71e5a816270b8acd9d2ca9/brown-chihuahua-standing-in-grass-071723.jpg?raw=true', use_column_width=True)
   
# About Page
elif page == '🤠About':
     st.title('About Me')

  # Timeline of my Professional Journey
  st.subheader('My Journey 🗺️')

   with st.expander('2025 - Present: Medgar Evers College'):
    st.write('''
                - Major: Computer Information Systems
                - Relevant Coursework: Internet & Emerging Technologies, Programming, Database Systems, AI
                - Activities: Track Team, Volleyball Team, Hackathon participant
            ''')

   with st.expander('2023 - 2025: NYC Museum School'):
    st.write('''
                - Graduated with honors
                - AP Computer Science A (Score: 5)
                - Founded Coding Club
            ''')

  st.subheader('Interests & Hobbies 🏀')
  interests = ['Web Development', 'AI/Machine Learning', 'Photography', 'Basketball', 'Travel', 'Baseball']

  # Display the interests in columns
  cols = st.columns(3)
for i, interest in enumerate(interests):
   with cols[i % 3]:
      st.info(f'🔷 {interest}')
  
