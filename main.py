# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
# from helper_functions import llm
from logics.customer_query_handler import process_user_message
from helper_functions.llm import get_embedding
from helper_functions.utility import check_password
from helper_functions.loaddata import load_files
#from helper_functions.preretrieval import semantic_chunking


# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Pet Ownership and Quarantine Chatbot"
 )

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()

documents_loaded = load_files()

#semantic_chunking(documents_loaded)
    
# endregion <--------- Streamlit App Configuration --------->

#Disclaimer
with st.expander("DISCLAIMER"):
    st.markdown("""
                **IMPORTANT NOTICE**: This web application is developed as a proof-of-concept prototype. \
                The information provided here is **NOT intended for actual usage** and should not be relied upon \
                for making any decisions, especially those related to financial, legal, or healthcare matters. \
                
                **Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. \
                You assume full responsibility for how you use any generated output.** \
                
                Always consult with qualified professionals for accurate and personalized advice.
                """)

st.title("Pet Ownership and Quarantine Chatbot")

form = st.form(key="form")
form.subheader("How can we help you today?")

user_prompt = form.text_area("Type your message here", height=150)

if form.form_submit_button("Submit"):
    
    st.toast(f"User Input Submitted - {user_prompt}")

    st.divider()

    response, course_details = process_user_message(user_prompt)
    st.write(response)

    st.divider()

    #print(course_details)
    #df = pd.DataFrame(course_details)
    #df 
