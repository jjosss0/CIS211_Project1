import streamlit as st
import pandas as pd
from datetime import datetime

# Page config
st.set_page_config(
    page_title='joss | portfolio',
    page_icon='👻',
    layout='wide'
)

# Custom CSS
st.markdown('''
    <style>
        .main-header {font-size: 42px; font-weight: bold; text-align:center;}
        .sub-header {font-size: 24px; text-align:center; color: #666;}
    </style>
''', unsafe_allow_html=True)

# Sidebar
st.sidebar.title('📍Navigation')
page = st.sidebar.radio('Go to',
                        ['🏡Home', '🤠About', '💼Projects', '🛠Skills', '📝Resume', '📧Contact'])

# Home page
if page == '🏡Home':
    st.markdown('<p class="main-header">Josmalli Olivero</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Aspiring Tech Professional | Medgar Evers College</p>', unsafe_allow_html=True)

    # Three columns for stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('GPA', '3.8', '📚')
    with col2:
        st.metric('Projects', '5', '💻')
    with col3:
        st.metric('Skills', '10', '🚀')

    st.write('---')

    # Introduction
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader('Welcome to my digital space! 👋')
        st.write('''
        I am a Computer Information Systems student passionate about web development and emerging technologies. 
        Currently learning HTML, CSS, JavaScript, and Python to build innovative solutions.

        🎯 **Current Focus:** Building interactive web applications with Streamlit  
        📚 **Currently Learning:** Internet and Emerging Technologies (CIS 211)  
        🌱 **Fun Fact:** I can solve a Rubik's cube in under 2 minutes!
        ''')
    with col2:
        st.image('https://github.com/jjosss0/CIS211_Project1/blob/bc25b2d3ff67041bde71e5a816270b8acd9d2ca9/brown-chihuahua-standing-in-grass-071723.jpg?raw=true', use_column_width=True)

# About page
elif page == '🤠About':
    st.title('About Me')
    st.subheader('My Journey🏔️')

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

    cols = st.columns(3)
    for i, interest in enumerate(interests):
        with cols[i % 3]:
            st.info(f'🔷 {interest}')

# Projects page
elif page == '💼Projects':
    st.title('My Projects')
    st.write('Here are some projects I have worked on:')

    # Project 1
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('https://cdn-icons-png.flaticon.com/512/3075/3075977.png', use_column_width=True)
        with col2:
            st.subheader('🛒 E-Commerce Price Tracker')
            st.write('Python web scraper that monitors Amazon prices and sends alerts.')
            st.caption('**Technologies:** Python, BeautifulSoup, Streamlit')

    # Project 2
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('https://cdn-icons-png.flaticon.com/512/3556/3556433.png', use_column_width=True)
        with col2:
            st.subheader('📊 Student Grade Calculator')
            st.write('Interactive web app for calculating and visualizing grades.')
            st.caption('**Technologies:** Python, Pandas, Plotly')

# Skills page
elif page == '🛠Skills':
    st.title('Technical Skills')

    st.subheader('Programming Languages')
    skills_data = {
        'Python': 85,
        'HTML/CSS': 70,
        'JavaScript': 60,
        'SQL': 50,
        'Technical Writing': 40
    }

    for skill, level in skills_data.items():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.write(skill)
        with col2:
            st.progress(level / 100)

    st.subheader('Tools & Technologies')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success('Excel')
        st.info('Word')
    with col2:
        st.warning('Access')
        st.error('PowerPoint')
    with col3:
        st.info('GitHub')
        st.success('Canva')

