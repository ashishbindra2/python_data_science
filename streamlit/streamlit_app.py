import streamlit as st


# ---PAGE SETUO ---
about_page = st.Page(
    page="views/about.py",
    title="About Me",
    icon=":material/account_circle:",
)

sales_page = st.Page(
    page="views/sales.py",
    title="sale Me",
    icon=":material/bar_chart:",
    default=True
)


chat_page = st.Page(
    page="views/chatbot.py",
    title="char Me",
    icon=":material/smart_toy:",
)


#  --- Navigation setup
pg  = st.navigation(
    {
        "Info": [about_page],
        "Projects":[sales_page,chat_page]
    }
)

st.logo("assets/logo.png")
st.sidebar.text("Made with 💛 By Ashish")

pg.run()