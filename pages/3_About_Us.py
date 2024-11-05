import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Pet Ownership & Quarantine Chatbot"
)
# endregion <--------- Streamlit App Configuration --------->

# Title
st.markdown("#About Us")

st.write("This is a Pet Ownership & Quarantine Chatbot that powered by a large language model (LLM) to provide real-time, \
         personlised support to pet owners, offering guidance on pet care, health protocols, and welfare activities tailored to individual circumstances.")

# Project Scope 
with st.expander("Project Scope"):
    # Problem statement 
    st.markdown("### Problem Statement")
    st.markdown("""
                In the wake of increasing pet ownership and heightened need for public health and quarantine measures, \
                **pet owners** often face significant challenges in **managing their pets'needs** while **adhering to \
                local pet ownership laws**. The current situation is marked by lack of reliable, accessible, and \
                real-time information tailored to pet care during **ownership** and **quarantine** settings, \
                leading to uncertainty on best practices for pet health, safety, and mental engagement.
                """)
    # Proposed Solution
    st.markdown("### Proposed Solution")
    st.markdown("""
                We propose to implement a **Pet Ownership and Quarantine Chatbot** powered by a **Large Language Model (LLM)**. \
                This chatbot will provide real-time, personalised support to pet owners, offering guidance on pet care, \
                health protocols, and mental wellness activities tailored to individual circumstances.

                LLMs will enhance the chatbot's functionality in several ways: \
                - **Natural Language Understanding**: The LLM will enable the chatbot to understand and respond to \
                user inquiries in a conversational manner, making it accessible for users of all ages and backgrounds. 
                - **Personalisation**: By analyzing user input, the LLM can provide tailored advice based on the \
                type of pet and specific need or challenge faced by the owner.
                - **Real-Time Updates**: The LLM can be continuously updated with the latest guidelines from the \
                organisation, ensuring the pet owners receive accurate and timely information.
                - **Resource Aggregation**: The chatbot will serve as a centralised hub, aggregating diverse resources \
                such as veterinary advice, emergency contacts, and activity suggestions, reducing the need for \
                users to search on multiple platforms or documents.
                """)
    # Impact
    st.markdown("### Impact")
    st.markdown("""
                The main aim of the chatbot is to **streamline resource access by centralising pet ownership and quarantine information** \
                which is otherwise scattered across various platforms. This provides a **one-stop platform** for pet owners to have \
                **immediate access to reliable information** tailored to their specific needs and scenarios, and to \
                **enhance knowledge and confidence in pet ownership**. \
                With this platform, we expect up to 50% time saved in information seeking behaviour and significant \
                reduction in workload by up to 50%, for NParks'operations and call center. 
                """)
    

# Data Sources
with st.expander("Data Sources"):
    st.markdown("""
                - **Available Data Sources**: All data used in our chatbot are published documents from https://www.nparks.gov.sg/avs/resources/ .
                - **Data Classification**: Official Open.
                """)

# Features

with st.expander("Features"):
    st.markdown("""
                ### What you can expect: 
                - Tailored advice based on your specific query. 
                - Real-time updates and quick response. 
                - Save time by reducing need to search for information on multiple platforms. 
                
                ### How to use this Chatbot:
                1. Enter your **prompt** in the text area.
                2. Click the **'Submit'** button.
                3. The chatbot will generate a **response** based on your prompt.
                """)
