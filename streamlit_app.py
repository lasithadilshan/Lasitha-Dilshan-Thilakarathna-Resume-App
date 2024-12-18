import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Lasitha Dilshan Thilakarathna
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Software Engineer with 4 years of experience in IT Industry.
- Strong expertise in Generative AI, Backend, Frontend, and Data Engineering tasks.
- Passionate about leveraging knowledge for organizational benefits and career growth.
''')

#####################
# Objective
st.markdown('## Objective')
st.write('''
I am looking for opportunities in career growth and stability and look forward to working with confidence in a dynamic and challenging environment, utilizing my knowledge for the benefit of the organization and enhancing my skills.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://lasithadilshan.github.io/" target="_blank">Portfolio</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#experience">Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#achievements">Achievements</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Experience
st.markdown('## Experience')
txt('**Associate Software Engineer**, Virtusa, Colombo', '2022 - Present')
st.write('''
- Performed Frontend, Backend, and Data Engineering tasks, including work on Generative AI projects.
''')

txt('**Intern Engineer**, Surreytech Consulting Sri Lanka', '2021 - 2022')
st.write('''
- Full Stack Engineer for a one-year internship.
''')

#####################
# Education
st.markdown('## Education')
txt('**MSc in Information Technology** (Reading), SLIIT, Sri Lanka', '2023 - Present')
txt('**B.Eng in Software Engineering**, IIC University of Technology, Cambodia', '2018 - 2021')
st.write('''
- Degree with Second Upper (GPA: `3.56`).
''')

txt('**Professional Higher National Diploma in Software Engineering**, Scottish Qualifications Authority, Scotland', '2019 - 2020')

#####################
# Projects
st.markdown('## Projects')
txt4('**AI-Powered CV Extractor**', 'Virtusa', 'Python, Generative AI, OpenAI, LangChain, LLM')
st.write('''
- An AI application that extracts information from various CV formats and exports results in Word/PDF.
''')

txt4('**BRD to User Story Generation**', 'Virtusa - Generative AI Hackathon', 'Python, Generative AI, OpenAI, LangChain')
st.write('''
- Transformed Business Requirement Documents into user stories using Generative AI.
''')

txt4('**SDLC Automation**', 'MSc Final Year Project', 'Python, Generative AI, OpenAI, LangChain')
st.write('''
- Automated Software Development Life Cycle processes using Generative AI.
''')

txt4('**After-Hour Transport & Food Management System**', 'Virtusa', 'Microsoft Power Apps, SharePoint, React')
st.write('''
- Managed food and transport facilities for employees working after hours.
''')

#####################
# Skills
st.markdown('## Skills')
txt3('Programming', '`Java`, `Python`, `JavaScript`, `CSS`, `HTML`, `SCSS`')
txt3('Generative AI', '`OpenAI`, `LangChain`, `LLM`, `Hugging Face`, `FastAPI`')
txt3('Web Development', '`Java Spring Boot`, `Angular`, `React`')
txt3('Database', '`MySQL`, `PostgreSQL`, `Firebase`')
txt3('API Management', '`Spring Boot`, `FastAPI`')
txt3('Mobile Development', '`Native Android`, `Google Play Store`')

#####################
# Achievements
st.markdown('## Achievements')
st.write('''
- Arctic Code Vault Contributor (2020 GitHub Archive Program).
- Virtusa Certified GenAI Assisted Engineer (2024).
- Gen AI Hackathon Certificate of Participation, Virtusa (2024).
''')

#####################
# Social Media
st.markdown('## Social Media')
txt2('Portfolio', 'https://lasithadilshan.github.io/')
txt2('LinkedIn', 'https://www.linkedin.com/in/lasitha-thilakarathna-3027ab120/')
txt2('GitHub', 'https://github.com/lasithadilshan')