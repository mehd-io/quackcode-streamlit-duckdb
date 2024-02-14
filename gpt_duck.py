import streamlit as st
from ollama import Client
import duckdb

# Initialize DuckDB and Ollama Client
con = duckdb.connect(database='data/duckdb_stats.db', read_only=False)
ollama_client = Client(host='http://host.docker.internal:11434')

# Function to get the schema description
def get_schema_description(con, table_name):
    schema_query = f"DESCRIBE {table_name};"
    schema_result = con.execute(schema_query).fetchall()
    return f"The table name {table_name} contains the following columns: {schema_result}"

# Streamlit UI
st.title('PyPI Stats Explorer')

# User input for natural language query
user_query = st.text_input("Enter your query in natural language:")

if st.button("Get Data"):
    if user_query:
        # Dynamically get the schema description
        schema_description = get_schema_description(con, "daily_stats")
        
        # Combine schema description with user's query
        full_query = schema_description + " " + user_query
        
        # Convert natural language to SQL using Ollama
        response = ollama_client.chat(model='duckdb-nsql', messages=[
            {
                'role': 'user',
                'content': full_query,
            },
        ])
        sql_query = response['message']['content']
        st.text(f"Generated SQL Query: {sql_query}")
        
        # Execute SQL query on DuckDB
        try:
            result = con.execute(sql_query).df()
            # Display results as a table
            st.write(result)
        except Exception as e:
            st.error(f"Error executing query: {e}")
    else:
        st.error("Please enter a query.")

# Function to update the database with the uploaded CSV
def update_database_with_csv(con, uploaded_file):
    if uploaded_file is not None:
        # Read the uploaded CSV into a DataFrame
        con.execute(f"CREATE OR REPLACE TABLE daily_stats AS SELECT * FROM '{uploaded_file}'")
        st.success("Database updated with uploaded CSV!")
    else:
        st.info("Using existing database data.")
        
