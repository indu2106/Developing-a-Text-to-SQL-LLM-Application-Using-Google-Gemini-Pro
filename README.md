# Text-to-SQL LLM Application with Google Gemini Pro

## Overview

The Text-to-SQL LLM Application integrates Google Gemini Pro for natural language processing capabilities, enabling users to convert English questions into SQL queries. This README outlines the components, architecture, and setup instructions for the application.

## Components

### User Interface (Streamlit App)

- Provides a user-friendly interface for inputting English questions.
- Displays the converted SQL queries and query results.

### Google Gemini Pro API

- Handles natural language processing (NLP) tasks, including language understanding and query generation.
- Requires an API key for authentication and authorization.

### SQLite Database

- Stores student data used for querying.
- Contains a table (STUDENT_DATA) with fields such as ID, NAME, NATIONALITY, CITY, LATITUDE, LONGITUDE, GENDER, ETHNIC_GROUP, AGE, ENGLISH_GRADE, MATH_GRADE, SCIENCES_GRADE, LANGUAGE_GRADE, PORTFOLIO_RATING, COVERLETTER_RATING, and REFLETTER_RATING.

### Application Logic

#### Streamlit App Backend

- Handles user inputs and button interactions.
- Calls the Google Gemini Pro API to convert user queries into SQL.
- Executes SQL queries against the SQLite database and retrieves results.
- Displays formatted results back to the user interface.

## Flow

### User Interaction

1. User inputs an English question related to student data into the Streamlit app.
2. Clicks on the "Ask the question" button to submit the query.

### Query Processing

1. Streamlit app sends the user's question to the Google Gemini Pro API.
2. Gemini Pro API processes the query to generate an appropriate SQL command based on predefined prompts and its understanding of the question.

### Database Interaction

- The generated SQL query is executed against the SQLite database (STUDENT_DATA table).
- Results (if any) are retrieved from the database.

### Response Presentation

- Streamlit app formats the SQL query results and displays them back to the user.
- Results include student data or confirmation of query execution.

## Scalability

- **Gemini Pro API**: Designed to handle large volumes of natural language queries, scalable based on Google's infrastructure.
- **Database Scalability**: SQLite is suitable for small to medium-sized applications; consider migrating to a more scalable database solution for larger datasets or higher traffic.

## Installation

To run this application locally:

1. Install dependencies:

   ```bash
   pip install -r requirements.txt

2. Set up environment variables:
Create a .env file and add your Google Gemini Pro API key:
   ```bash
   GOOGLE_API_KEY="your_google_api_key_here"

3. Run the Streamlit app:

   ```bash
   streamlit run app.py

4. Access the application in your browser at localhost


