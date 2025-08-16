import streamlit as st
from  langchain.agents import create_csv_agent
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
    if not csv_file:
        st.warning("Please upload a CSV file to proceed.")
        return
    else:
        st.success("DataFrame loaded successfully!")

    if csv_file is None:
        st.error("No CSV file uploaded.")
    else:
        query= st.text_input("Enter your query: ", key='Question')   

        if not query:
            return
            st.write(f"You asked: {query}")

            
        
            # Here you would typically process the query against the CSV data
            # For example, you could use pandas to read the CSV and answer the query
            # df = pd.read_csv(csv_file)
            # answer = process_query(df, query)
            # st.write(answer)

if __name__ == '__main__':
    main()

