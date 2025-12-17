from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import sqlite3  
import google.generativeai as genai 
genai.configure(api_key=os.getenv("GENAI_API_KEY"))
#function to load google model and sql query response
def get_gemini_response(question,prompt):
    model = genai.GenerativeModel("gemini-2.5-flash",)
    response = model.generate_content([prompt[0], question])
    return response.text
#FUNCTION TO RETRIEVE QUERY FROM DB
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows

prompt=["YOu are an expert data analyst. Analyze the following SQL query result and provide insights. "
"The SQL data base  is named *students*and contains following columns:"
"*name*(VARCHAR),*CLASS*(VARCHAR),*SECTION*(VARCHAR),*MARKS*(INTEGER)."
"Following these guidelines when generating sql queries:"
"1.Ensure the output contains only the SQL quey do-not include any explanations, formatting marks or additional text."
"2.Use proper SQL syntax while maintaining accuracy and efficeincy."
"3.If the query involves filtering , apply appropriate conditions using WHERE clause."
"4.If an aggregation is required(e.g; counting records, averaging values), use suitable aggregate functions like COUNT(), AVG(), SUM() etc."
"*Examples*"
"*question:Retrieve the names of all students in Data Science class.*"
"*SQL Query:SELECT name FROM students WHERE CLASS='Data Science';*"
"*question:How many names are present?*"
"*SQL Query:SELECT COUNT(*) FROM students;*"
"*question:What is the average marks of students ?*"
"*SQL Query:SELECT AVG(MARKS) FROM students;*"
"Now, generate SQL query for the given questions."

        ]
#Stream lit APP
st.set_page_config(page_title="SQL QUERY GENERATOR",page_icon="🟩")
st.title("SQL QUERY GENERATOR USING GEMINI 1.5 PRO")
st.markdown("This app generates SQL queries based on user questions using Google's Gemini 1.5 Pro model and retrieves data from a SQLite database.")
st.markdown("Ask any questions , and it will generate the SQL query and fetch the results from the database.")
#user input for the question
question=st.text_input("Enter your question in the plain english:",key="input")
#submit button
submit=st.button("Generate SQL Query and Fetch Data")
if submit:
    sql_query = get_gemini_response(question, prompt)
    result = read_sql_query(sql_query, "students.db")
    print(sql_query)
    st.subheader("Query Result")
    for row in result:
        st.header(row[0])

        