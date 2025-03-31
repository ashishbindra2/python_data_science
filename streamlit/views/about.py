import streamlit as st
from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()
# Hero section

col1, col2 = st.columns(2,gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/ASHISH_BINDRA.jpeg",width=230,)

with col2:
    st.title("Ashish Bindra", anchor=False)
    st.write("Data Analyst, Assisting enterprises by supporting data friven decisio-making")
    
    if st.button(" 💌 Contact Me"):
        show_contact_form()
        
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write("""
         - 3 Years experience extracting actionable insight from data
         - Strong hand-on experience and knowlage in Python
         - Good understanding of statical principles and their respective applications
         - Excellent team-player and displaying a strong sense of intative on tasks
         """)


# skills
st.write("\n")
st.subheader("Hard skills", anchor=False)
st.write("""
        - Python Programming: Python(Pandas), SQL
        - Data Visualization: PowerBi
        - Modeling: liner regression
        - Databases: MongoDb,Mysql, Postgres
        """)
