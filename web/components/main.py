import streamlit as st
import base64
import os
from content_display import show_content, display_submission_details, display_result, display_details

def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        st.error(f"File not found: {bin_file}")
        return None

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    if bin_str:
        page_bg_img = f'''
        <style>
        .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
    
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)



# Set the background image
set_png_as_page_bg('web/images/bg.png')

if "content" not in st.session_state:
    st.session_state.content = None



col1, col2 = st.columns(2)

with col1:
    if st.button("Info"):
        st.session_state.content = {"item": "Info", "reason": None}
        reason = show_content("About the model.")
        if reason is not None:
            st.session_state.content["reason"] = reason

with col2:
    if st.button("Apply"):
        st.session_state.open_result_modal = False
        st.session_state.open_details_modal = False
        st.session_state.content = {"item": "Apply", "reason": None}
        reason = show_content("Please fill up the application form.")
        if reason is not None:
            st.session_state.content["reason"] = reason

if st.session_state.content:
    # st.write(f"You selected {st.session_state.content['item']}")
    if st.session_state.content['reason']:
        st.write(st.session_state.content['reason'])

# Display recent submission details if available
if st.session_state.get("form_submitted"):
    # display_scaled_details()
    if st.session_state.get("applicant_modal", False):
        display_submission_details()

# Display result if success_modal is True
if st.session_state.get("open_result_modal", False):
    display_result()

if st.session_state.get("open_new_application", False):
    show_content("Please fill up the application form.")

if st.session_state.get("open_details_modal", False):
     display_details()

# Check if the CSS file exists before attempting to open it
css_file_path = "web/styles/app_form.css"
if os.path.exists(css_file_path):
    with open(css_file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.error(f"CSS file not found: {css_file_path}")