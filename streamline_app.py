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
        🌱 **Fun Fact:** I am proficient in simultaneous interpretation(interpreter speaks at the same time as the original speaker, with only a minimal delay.). 
        ''')
    with col2:
        st.image('https://github.com/jjosss0/CIS211_Project1/blob/bc25b2d3ff67041bde71e5a816270b8acd9d2ca9/brown-chihuahua-standing-in-grass-071723.jpg?raw=true', use_column_width=True)

# About page
elif page == '🤠About':
    st.title('About Me')
    st.subheader('My Journey🏔️')

    with st.expander('2023 - Present: Medgar Evers College'):
        st.write('''
        - Major: Computer Information Systems  
        - Relevant Coursework: Internet & Emerging Technologies, Contemporary Comp Apps, Comp Ghaphics   
        - Activities: Read
        ''')

   # with st.expander('2023 - 2025: NYC Museum School'):
        st.write('''
        - Graduated with honors  
        - AP Computer Science A (Score: 5)  
        - Founded Coding Club
        ''')

    st.subheader('Interests & Hobbies 🏀')
    interests = ['Web Development', 'AI/Machine Learning', 'Reading', 'Runing', 'Travel', ' Trying new food']

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
            st.image('https://code.org/images/tutorials/hoc2023/danceparty_ai.png', use_column_width=True)
        with col2:
            st.subheader('🛒  Building interactive web applications with Streamlit')
            st.write('Python web scraper that monitors Amazon prices and sends alerts.')
            st.caption('**Technologies:** Python, BeautifulSoup, Streamlit')

    # Project 2
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('https://storage.needpix.com/rsynced_images/calculator-1464008_1280.png', use_column_width=True)
        with col2:
            st.subheader('📄It will showcase my résumé and skills for future job opportunities.')
            st.write('Interactive web app for calculating and visualizing grades.')
            st.caption('**Technologies:** Python ')

# Skills page
elif page == '🛠Skills':
    st.title('Skills & Competencies')

    st.subheader('Technical & Professional Skills')
    skills_data = {
        'Python': 30,
        'Microsoft Excel': 80,
        'JavaScript': 5,
        'Interpretation': 100,
        'Technical Writing': 50
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
# resume page 
elif page == '📝Resume':
    st.title( 'My Resume')
    
    # Read PDF from my GitHub repository
    with open('Resume.pdf', 'rb') as pdf_file:
        PDFbyte = pdf_file.read()
      
    st.download_button(
        label ='🔻 Download Full Resume (PDF)',
        data = PDFbyte,
        file_name = 'Resume.pdf',
        mime ='application/pdf'
    )

elif page == '📧Contact':
  st.title("Contact me!")

  col1, = st.columns(1)

  with col1:
    st.subheader('Send me a message.')

    st.write('''
        📧 **Email:** josmalli09@gmail.com

        🏢 **LinkedIn:** [linkedin.com/in/yourname](https://www.linkedin.com/in/josmalli-olivero-0b4b38223/)

        👩‍💻 **Github:** [https:https://github.com/jjosss0](https://github.com)

        📁**Indeed:** [profile.indeed.com](https://profile.indeed.com/?hl=en_US&co=US&from=gnav-homepage)

    ''')

    # Fun interative element
    st.subheader('Current Status')

    status = st.selectbox(
        "I'm currently:",
        [
            '👩‍💻 Coding',
            '📕 Studying',
            '☕ On a coffee break',
            '🎮 Gaming',
            '😴 Sleeping'
        ]
    )


    st.info(f'Status: {status}')

    # Footer
    st.write('---')
    st.markdown(
        f'<center>Made with 💗 using Streamlit | © {datetime.now().year} Josmalli Olivero </center>',
        unsafe_allow_html = True
    )
    

