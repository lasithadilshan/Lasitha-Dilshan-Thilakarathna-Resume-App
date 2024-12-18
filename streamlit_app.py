import streamlit as st
from PIL import Image

# Load custom styles
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Lasitha Dilshan Thilakarathna, B.Eng.
##### *Resume*
''')

image = Image.open('dp.png')
st.image(image, width=150)

#####################
# Summary
st.markdown('## Summary')
st.info('''
- Software Engineer with over 4 years of experience in IT industry.
- Expertise in Generative AI, Backend, Frontend, and Data Engineering tasks.
- Strong skills in web technologies, mobile development, and AI application development.
- Passionate about leveraging knowledge for organizational benefits and career growth.
''')

#####################
# Objective
st.markdown('## Objective')
st.write('''
Looking for opportunities in career growth and stability. Confident in working within dynamic and challenging environments, utilizing my skills for the benefit of the organization while enhancing my professional capabilities.
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
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certifications">Certifications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Education
st.markdown('## Education')
st.write('''
**M.Sc. in Information Technology**, SLIIT Malabe (Reading)  
**B.Eng. in Software Engineering**, IIC University of Technology, Cambodia (GPA: 3.56/4)
''')

#####################
# Work Experience
st.markdown('## Work Experience')
st.write('''
**Associate Software Engineer**, Virtusa, Colombo (2022 - Present)  
- Developed multiple applications, including Generative AI solutions, internal portals, and frontend applications.  
- Technologies used: Python, Java, Angular, React, OpenAI, LangChain, FastAPI.

**Intern Engineer**, Surrey Tech Consulting Sri Lanka (2021 - 2022)  
- Contributed to Lak Health and Email API projects for the Sri Lankan government.  
- Technologies used: Angular, Spring Boot, HTML, CSS.
''')

#####################
# Projects
st.markdown('## Projects')
st.write('''
- **AI-Powered CV Extractor**: An AI-based application to extract and structure resume data (Python, LangChain).  
- **BRD to User Story Generation**: Generative AI tool for software documentation automation.  
- **SDLC Automation**: Automated software development lifecycle processes using Generative AI.  
- **After-Hour Transport & Food Management System**: Employee management app using Microsoft Power Apps.
''')

#####################
# Skills
st.markdown('## Skills')
st.write('''
- **Programming Languages**: Java, Python, JavaScript, TypeScript, SQL, HTML5, CSS5.  
- **Technologies**: Generative AI, Spring Boot, FastAPI, Node.js.  
- **Databases**: MySQL, PostgreSQL, Firebase, SQLite.  
- **Web Development**: Angular, React, REST APIs, JSON.  
- **Version Control**: Git, GitHub, GitLab.
''')

#####################
# Certifications
st.markdown('## Certifications')
st.write('''
- Career Essentials in Generative AI (Microsoft and LinkedIn, 2023).  
- Gen AI Hackathon Certificate of Participation (Virtusa, 2024).  
- Virtusa Certified GenAI Assisted Engineer (2024).
''')

#####################
# Social Media
st.markdown('## Social Media')
st.write('''
- [Portfolio](https://lasithadilshan.github.io/)  
- [GitHub](https://github.com/lasithadilshan)  
- [LinkedIn](https://linkedin.com/in/lasitha-thilakarathna-3027ab120)  
- [Google Play Store](https://play.google.com/store/apps/dev?id=8598412061020641933)
''')
