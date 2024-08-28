import streamlit as st
from forms.app_form import display_app_form
from forms.info_form import display_info_form

@st.dialog("Loan Prediction by Chris")
def show_content(item):
    if item == "About the model.":
        return display_info_form()
    elif item == "Please fill up the application form.":
        return display_app_form()

if "content" not in st.session_state:
    st.session_state.content = None

st.write("Welcome to the Loan Prediction App")

col1, col2 = st.columns(2)

with col1:
    if st.button("Info"):
        st.session_state.content = {"item": "Info", "reason": None}
        reason = show_content("About the model.")
        if reason is not None:
            st.session_state.content["reason"] = reason

with col2:
    if st.button("Apply"):
        st.session_state.content = {"item": "Apply", "reason": None}
        reason = show_content("Please fill up the application form.")
        if reason is not None:
            st.session_state.content["reason"] = reason

if st.session_state.content:
    st.write(f"You selected {st.session_state.content['item']}")
    if st.session_state.content['reason']:
        st.write(st.session_state.content['reason'])

    
with open("web/styles/app_form.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)