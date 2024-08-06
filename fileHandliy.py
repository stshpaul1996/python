# from faker import Faker
# import random
# fake = Faker()
# file = open("employees_data.csv", 'w')
# file.write("Name,Department,Salary,Mobile\n")
# for i in range(100):
#     row = f'{fake.name()},{fake.word()},{random.randint(200000, 500000)},{fake.phone_number()}/n'
#     file.write(row)
# file.close()
# print(file)

# f = open("employees_data.csv", "r")
# f = f.readlines()
# #print(f)
# sal = []
# for i in f[1:-1]:
#     item = i.split(",")
#     print(item)


import pymysql
import random

# Connect to your MySQL database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='aja'
)
cursor = conn.cursor()

# Define the number of records to insert
num_records = 2500000  # 25 lakh records

create_table = "CREATE TABLE employees(name CHAR, salary INT)"



# Generate and execute bulk insert statements
insert_query = "INSERT INTO employees (name, salary) VALUES (%s, %s)"
data_to_insert = [(f"Employee {i}", random.randint(50000, 200000)) for i in range(num_records)]
cursor.executemany(insert_query, data_to_insert)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print(f"Inserted {num_records} records into the 'employees' table.")
