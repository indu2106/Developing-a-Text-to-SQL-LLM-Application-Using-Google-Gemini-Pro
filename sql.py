import sqlite3
import csv
#Connection to sqlite
connection = sqlite3.connect("student_info.db")

## create a cursor object to insert record, create table , retrieve
cursor = connection.cursor()

##create the table
table_info = """
CREATE TABLE STUDENT_DATA(
    id INTEGER PRIMARY KEY,
    name TEXT,
    nationality TEXT,
    city TEXT,
    latitude REAL,
    longitude REAL,
    gender TEXT,
    ethnic_group TEXT,
    age INTEGER,
    english_grade REAL,
    math_grade REAL,
    sciences_grade REAL,
    language_grade REAL,
    portfolio_rating REAL,
    coverletter_rating REAL,
    refletter_rating REAL
);
"""

cursor.execute(table_info)

# Read data from CSV and insert into SQLite
with open('student-dataset.csv', 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO STUDENT (
                id, name, nationality, city, latitude, longitude, gender, 
                ethnic_group, age, english_grade, math_grade, sciences_grade, 
                language_grade, portfolio_rating, coverletter_rating, refletter_rating
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            row['id'], row['name'], row['nationality'], row['city'], 
            row['latitude'], row['longitude'], row['gender'], row['ethnic.group'], 
            row['age'], row['english.grade'], row['math.grade'], row['sciences.grade'], 
            row['language.grade'], row['portfolio.rating'], row['coverletter.rating'], 
            row['refletter.rating']
        ))

# ##Insert Some more records

# cursor.execute('''Insert into STUDENT values('Monica','Math','A', 90)''')
# cursor.execute('''Insert into STUDENT values('Ross','English','B', 80)''')
# cursor.execute('''Insert into STUDENT values('Joe','Science','C', 70)''')
# cursor.execute('''Insert into STUDENT values('Chandler','Account','B', 85)''')
# cursor.execute('''Insert into STUDENT values('Pheobe','Social Studies','A', 100)''')
# cursor.execute('''Insert into STUDENT values('Rachel','Painting','C', 75)''')

##Display all the records
# print("The inserted records are")
# data = cursor.execute('''Select * from STUDENT''')

# for row in data:
#     print(row)

#Close the Connection
connection.commit()
connection.close()