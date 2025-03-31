import streamlit_app as st

st.title("registration form")

# prompt = st.chat_input("Asd")

# if prompt:
#     st.text(prompt)

name = st.text_input("Name")
age = st.number_input("age")
dob = st.date_input("DOB")
time = st.time_input("time")
# st.camera_input("access your camera")
age2 = st.slider("age2",25,100,33)
model= st.selectbox("silder",("a","b","c"))

st.write(model)

# Start a form with a unique key
with st.form(key='my_form'):
    text_input = st.text_input(label='Enter some text',)
    submit_button = st.form_submit_button(label='Submit')
    
    if submit_button:
        st.balloons()
