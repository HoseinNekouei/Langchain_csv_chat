import streamlit as st
from langchain.agents import create_csv_agent
from langchain_google_genai import GoogleGenerativeAI

def main():
    st.set_page_config(
        page_title="Ask your CSV",
        page_icon=":chart_with_upwards_trend:",
        layout="centered",
    )   
    st.title("Ask your CSV")

    csv_file= st.file_uploader('upload your csv file', type=['csv'])
    
    #Upload CSV file
    if not csv_file or csv_file is None:
        st.warning("Please upload a CSV file to proceed.")
        return
    else:
        st.success("DataFrame loaded successfully!")

    # get query from user
    query= st.text_input("Enter your query: ", key='Question')   

    # Initialize the Google Generative AI model
    model = GoogleGenerativeAI(model_name="models/gemini-2.5-flash-lite", tempreature=0)

    # Create the CSV agent
    agent_executor = create_csv_agent(
        model=model,
        csv_file=csv_file,
        verbose=True
    )

    if not query or query.strip() == "":
        st.warning("Please enter a query to proceed.")
        return

    





if __name__ == '__main__':
    main()

