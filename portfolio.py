import streamlit as st
from PIL import Image

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "About", "Projects", "Resume", "Contact"))

# --- Home Page ---
if page == "Home":
    st.title("Welcome to Anas Fareedi's Portfolio")
    st.write("AI & ML Developer | Python Enthusiast")

    profile_image = Image.open(r"C:\Users\Anas\OneDrive\Desktop\WhatsApp Image 2024-09-20 at 21.24.59_2029a7d7.jpg") 
    st.image(profile_image, caption="Anas Fareedi", width=150)

    st.write("""
    Hello! I'm Anas Fareedi, an aspiring AI & ML developer with a passion for creating 
    impactful solutions through technology. I enjoy working with Python and have a strong 
    foundation in Machine Learning.
    """)

# --- About Page ---
elif page == "About":
    st.title("About Me")
    st.write("""
    I am a second-year BTech student in AI and Machine Learning at COER University. I have
    a passion for developing AI-driven applications, solving real-world problems, and 
    continuously learning new skills in the field of Data Science and Machine Learning.
    """)

    st.title("Skills")
    st.write("**Python**")
    st.write("**Frameworks (Streamlit , fastAPI)**")
    st.write("**Libraries (NumPy , Pnadas , OpenCV)**")
    st.write("**JAVA**")
    st.write("**C / C++**")
    st.write("**Machine Learning**")
    st.write("**Data Visualization**")


    st.header("My Journey")
    st.write("""
    I've been working with various ML algorithms, including classification, regression, 
    and clustering. I'm also proficient in libraries like Pandas, NumPy, Matplotlib, 
    and Scikit-learn.
    """)

# --- Projects Page ---
elif page == "Projects":
    st.title("Projects")
    
    # Project 1
    st.subheader("Expirify - Expiry Date Management System")
    st.write("An AI-powered system that tracks product expiration dates and sends timely reminders.")
    # project_image = Image.open(r"C:/path_to_project_image1.jpg") 
    # st.image(project_image, width=400)
    st.markdown("[View on GitHub](https://github.com/anas-fareedi/jarvis.git)")

    # Project 2
    st.subheader("Eduneoxys - E-learning Platform")
    st.write("An e-learning platform that provides interactive and skill-enhancing courses.")
    # project_image2 = Image.open(r"C:/path_to_project_image2.jpg") 
    # st.image(project_image2, width=400)
    # st.markdown("[View on GitHub](https://github.com/your-repo-link2)")

# --- Resume Page ---
elif page == "Resume":
    st.title("My Resume")
    st.write(""" Below is my resume for download:""")

    st.download_button(
        label="Download My Resume",
        data=open("C:/Users/Anas/OneDrive/Desktop/resume/anas_Resume_3.pdf", "rb").read(),  # Replace with your resume file path
        file_name="Anas_Fareedi_Resume.pdf",
        mime="application/pdf"
    )

# --- Contact Page ---
elif page == "Contact":
    st.title("Get in Touch")
    
    # Contact Form
    name = st.text_input("Name")
    email = st.text_input("Email")
    mobile_number = st.text_input("Mobile Number")
    message = st.text_area("Message")
    
    if st.button("Send Message"):
        if name and email and mobile_number and message:
            st.success("Thank you for reaching out! I'll get back to you soon.")
        else:
            st.error("Please fill in all fields.")
    
    # Footer with Social Links
    st.markdown("---")
    st.write("Connect with me on [LinkedIn](https://www.linkedin.com/in/anas-fareedi/) | [GitHub](https://github.com/anasfareedi)")

