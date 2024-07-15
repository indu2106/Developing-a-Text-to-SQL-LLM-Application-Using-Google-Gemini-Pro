from dotenv import load_dotenv
load_dotenv() ## load all the environment varibales

import streamlit as st
import os
import sqlite3
import pandas  as pd
import google.generativeai as genai

##Configure our API key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#fUNCTION TO LOAD gOOGLE Gemini model and provide sql query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

## Function to retrieve query from sql database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL queries!

The SQL database is named STUDENT and contains the following columns: ID, NAME, NATIONALITY, CITY, LATITUDE, LONGITUDE, GENDER, ETHNIC_GROUP, AGE, ENGLISH_GRADE, MATH_GRADE, SCIENCES_GRADE, LANGUAGE_GRADE, PORTFOLIO_RATING, COVERLETTER_RATING, and REFLETTER_RATING.

For example:

If the question is "How many entries of records are present?", the SQL command will be SELECT COUNT(*) FROM STUDENT;
If the question is "Tell me all the students who have a portfolio rating of 5?", the SQL command will be SELECT * FROM STUDENT WHERE PORTFOLIO_RATING=5;
Remember, the SQL code should not include backticks (`) at the beginning or end, and should not include the word "sql" in the output.

Here are more examples to guide you:

Input: How many students are there in total?
Thought Process:

Identify the key entity: "total students".
Formulate the query to count all students.
Output: SELECT COUNT(*) FROM STUDENT;
Input: List the names of students who are from New York.
Thought Process:

Identify the key entities: "names of students" and "New York".
Formulate the query to select names of students from New York.
Output: SELECT NAME FROM STUDENT WHERE CITY='New York';
Input: Show all students who are 18 years old.
Thought Process:

Identify the key entities: "all students" and "18 years old".
Formulate the query to select all records for students who are 18 years old.
Output: SELECT * FROM STUDENT WHERE AGE=18;
Input: How many students have an English grade greater than 80?
Thought Process:

Identify the key entity: "students with an English grade greater than 80".
Formulate the query to count students with an English grade greater than 80.
Output: SELECT COUNT(*) FROM STUDENT WHERE ENGLISH_GRADE>80;
Input: List all the students' names and their math grades.
Thought Process:

Identify the key entities: "students' names" and "math grades".
Formulate the query to select names and math grades of all students.
Output: SELECT NAME, MATH_GRADE FROM STUDENT;
Now, let's convert the following English question to a SQL query:

Input: [Your English question here]
Thought Process:

Identify the key entities and their relationships.
Formulate the SQL query based on the identified entities.
Output: [Your SQL query here]

The output should only be SQL query which can be directly executed.


    """
]

## Streamlit App
conn = sqlite3.connect('student_info.db')
# df = pd.read_sql('SELECT * FROM STUDENT_DATA', conn)
st.set_page_config(page_title="I can Retrieve Any SQL query")
# st.sidebar.dataframe(df, use_container_width=True)

st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
# if submit:
#     response=get_gemini_response(question,prompt)
#     # print(response)
#     response=read_sql_query(response,"student_info.db")
#     st.subheader("The Response is")
#     for row in response:
#         print(row)
#         st.header(row)

if submit:
    response = get_gemini_response(question, prompt)
    
    # Execute the generated SQL query
    query_result = read_sql_query(response, "student_info.db")
    
    st.subheader("The Response is:")
    
    # Check if there are results
    if query_result:
        if len(query_result[0]) == 1:
            # The query result is a single value (e.g., COUNT(*))
            st.markdown(
                f"""
                <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px; background-color: #f9f9f9;">
                    <pre>{query_result[0][0]}</pre>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            # The query result is a table
            df = pd.DataFrame(query_result, columns=["ID", "Name", "Country", "City", "Latitude", "Longitude", "Gender", "Other Info", "Age", "GPA1", "GPA2", "GPA3", "GPA4", "GPA5", "GPA6", "GPA7"])
            
            st.markdown(
                """
                <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px; background-color: #f9f9f9;">
                """, 
                unsafe_allow_html=True
            )
            st.table(df)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.write("No results found.")

