import google.generativeai as genai
import streamlit as st

GOOGLE_API_KEY = "AIzaSyBuCGMy6lE-oC9FIixRp_qyfeoLrAmQMwE"

genai.configure(api_key= GOOGLE_API_KEY)

model= genai.GenerativeModel('gemini-1.5-flash')

def getresponsefrommodel(user_input):
    response = model.generate_content(user_input)
    return response.text
st.set_page_config(page_title="Chatbot Ahsan",layout="centered")
st.title ("Chatbot Ahsan")
st.write ("Powered by Google API Key")

#user_input = input("enter your question =")
#output = getresponsefrommodel(user_input)

#print(output)



with st.form(key="chat_form",clear_on_submit=True):
     user_input = st.text_input("", max_chars=2000)
     submit_button= st.form_submit_button("send")
     if submit_button:
        if user_input:
            response = getresponsefrommodel(user_input)
            st.write(response)
        else:
            st.warning("please enter a question")
