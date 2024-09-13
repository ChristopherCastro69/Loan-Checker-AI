import streamlit as st
import os
from dialogs import content_dialog, submitted_form_dialog, result_dialog, details_dialog
from hooks import set_png_as_page_bg


# Set the background image
set_png_as_page_bg('web/images/bg.png')

if "content" not in st.session_state:
    st.session_state.content = None

col1, col2 = st.columns(2)

with col1:
    if st.button("Info"):
        st.session_state.open_results_dialog = False
        st.session_state.open_details_dialog = False
        st.session_state.open_new_application = False
        
        st.session_state.content = {"item": "Info", "reason": None}
        reason = content_dialog("About the model.")
        if reason is not None:
            st.session_state.content["reason"] = reason

with col2:
    if st.button("Apply"):
        st.session_state.open_result_dialog = False
        st.session_state.open_details_dialog = False
        st.session_state.content = {"item": "Apply", "reason": None}
        reason = content_dialog("Please fill up the application form.")
        if reason is not None:
            st.session_state.content["reason"] = reason

if st.session_state.content:
    if st.session_state.content['reason']:
        st.write(st.session_state.content['reason'])
        

if st.session_state.get("open_new_application", False):
    content_dialog("Please fill up the application form.")

# Display recent submission details if available
if st.session_state.get("form_submitted"):
    if st.session_state.get("open_form_dialog", False):
        submitted_form_dialog()

# Display result if success_modal is True
if st.session_state.get("open_result_dialog", False):
    result_dialog()

# Display the details of the predicted value
if st.session_state.get("open_details_dialog", False):
     details_dialog()

# Check if the CSS file exists before attempting to open it
css_file_path = "web/styles/styles.css"
if os.path.exists(css_file_path):
    with open(css_file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.error(f"CSS file not found: {css_file_path}")