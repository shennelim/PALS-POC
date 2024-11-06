import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Pet Ownership & Quarantine Chatbot"
)
# endregion <--------- Streamlit App Configuration --------->

#Disclaimer
with st.expander("DISCLAIMER"):
    st.markdown("""
                **IMPORTANT NOTICE**: 
                
                This web application is developed as a proof-of-concept prototype. \
                The information provided here is **NOT intended for actual usage** and should not be relied upon \
                for making any decisions, especially those related to financial, legal, or healthcare matters. \

                
                **Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. \
                You assume full responsibility for how you use any generated output.** \

                
                Always consult with qualified professionals for accurate and personalized advice.
                """)

# Title
st.markdown("# Methodology")

# Body 

with st.expander("Data Integration"):
    st.markdown("""
                Multiple documents from https://nparks.gov.sg/avs/resources/ have been integrated to support the LLM in processing \
                user queries and provide factual updates based on the organisation's policies.
                """)


with st.expander("Flow Chart"):
    st.markdown(""" 
                Below is a generic flowchart containing our information ranging from our data collection process, to \
                integration of the chatbot into a Streamlit application, to \
                ensuring it handles context well and iterating based on feedback.
                """)
    st.image("./data/Methodology.jpg", caption="Flowchart")
