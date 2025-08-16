import streamlit as st
import pandas as pd
import tempfile
from dotenv import load_dotenv
from langchain_experimental.agents import create_csv_agent
from langchain_google_genai import GoogleGenerativeAI

def main():
    load_dotenv()

    st.set_page_config(
        page_title="Ask your CSV",
        page_icon=":chart_with_upwards_trend:",
        layout="centered",
    )   

    # Upload CSV file
    csv_file = st.file_uploader('upload your csv file', type=['csv'])
    if not csv_file or csv_file is None:
        st.info("Please upload a CSV file to continue.")
        return
    else:
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as temp_file:
                temp_file.write(csv_file.getbuffer())
                temp_file_path = temp_file.name
            # Try reading the CSV into a DataFrame
            df = pd.read_csv(temp_file_path)
            st.success("DataFrame loaded successfully!")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Failed to load CSV: {e}")
            return

    # get query from user
    query = st.text_input("Enter your query: ")
    if not query or query.strip() == "":
        st.warning("Please enter a query to proceed.")
        return

    # Initialize the Google Generative AI model
    try:
        model = GoogleGenerativeAI(model="models/gemini-2.5-flash-lite", temperature=0.0)
        # Create the CSV agent
        agent_executor = create_csv_agent(
            llm=model,
            path=temp_file_path,
            verbose=True,
            allow_dangerous_code=True
        )
    except Exception as e:
        st.error(f"Failed to initialize agent: {e}")
        return

    if query.strip():
        try:
            # Run the agent with the user's query
            response = agent_executor.run(input=query)
            st.write("Answer:", response)
        except Exception as e:
            st.error(f"Error running agent: {e}")


if __name__ == '__main__':
    main()

