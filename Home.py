import streamlit as st
import pandas as pd
from app.db import get_connection 
from app.users import set_user, get_user
from app.users import hash_password
conn = get_connection()
st.title ("Welcome to the Home Page")
st.write ("This is the home page of the Cyber Incidents Dashboard Application.")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'username' not in st.session_state:
    st.session_state['username'] = ""

tab_log_in, tab_registration = st.tabs (["Log In", "Registration"])
with tab_log_in:
    st.header ("Log In")

    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")
    id, name_db, hash_db = get_user(conn, login_username)
    if st.button("Log In"):
    if login_username == name_db and is_valid_hash(login_password, hash_db):


    if st.button("Log In"):
        st.session_state['logged_in'] = True
        st.success("You have successfully logged in.")
        st.session_state['username'] = login_username
    st.session_state


with tab_registration:
    st.header("User Registration")
    register_user = st.text_input("Choose a Username", key="register_username")
    register_password = st.text_input("Choose a Password", type="password", key="register_password")
    
    if st.button("Register"):
        hashed_password = hash_password(register_password)
        set_user(conn, register_user, hashed_password)
        st.success("You have successfully registered. Please log in.")


