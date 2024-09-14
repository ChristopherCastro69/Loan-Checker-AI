import streamlit as st
import os
from dialogs import content_dialog, submitted_form_dialog, result_dialog, details_dialog
from hooks import set_png_as_page_bg

# Constants
BACKGROUND_IMAGE = 'web/images/bg.png'
CSS_FILE_PATH = "web/styles/styles.css"
INFO_DIALOG = "About the model."
APPLICATION_DIALOG = "Please fill up the application form."

# Set the background image
set_png_as_page_bg(BACKGROUND_IMAGE)

if "content" not in st.session_state:
    st.session_state.content = None

col1, col2 = st.columns(2)

def handle_button_click(item, dialog_message):
    st.session_state.open_results_dialog = False
    st.session_state.open_details_dialog = False
    st.session_state.open_new_application = False
    st.session_state.content = {"item": item, "reason": None}
    reason = content_dialog(dialog_message)
    if reason is not None:
        st.session_state.content["reason"] = reason

with col1:
    if st.button("Info"):
        handle_button_click("Info", INFO_DIALOG)

with col2:
    if st.button("Apply"):
        handle_button_click("Apply", APPLICATION_DIALOG)

if st.session_state.content and st.session_state.content['reason']:
    st.write(st.session_state.content['reason'])

if st.session_state.get("open_new_application", False):
    content_dialog(APPLICATION_DIALOG)

# Display recent submission details if available
if st.session_state.get("form_submitted") and st.session_state.get("open_form_dialog", False):
    submitted_form_dialog()

# Display result if success_modal is True
if st.session_state.get("open_result_dialog", False):
    result_dialog()

# Display the details of the predicted value
if st.session_state.get("open_details_dialog", False):
    details_dialog()

# Check if the CSS file exists before attempting to open it
def load_css(file_path):
    if os.path.exists(file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.error(f"CSS file not found: {file_path}")

load_css(CSS_FILE_PATH)