import streamlit as st
import mysql.connector

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database="afnan"
)
cursor = connection.cursor()

# Home Page
def home_page():
    st.title("KYAAS MARKING PROJECT")
    st.write("Welcome to the Kyaas Marking System!")
    st.write("This system allows you to authenticate users and enter and their information.")
    

    # Add your logo image file path or URL
    logo_path = 'kyLogo1.png'  # Replace with your logo file path or URL

    # Display the logo
    a = st.image(logo_path, width=200)  # Adjust the width as per your preference
# Authenticate Page
def authenticate_page():
    st.title("User Authentication")
    
    # Prompt user for name and password
    name = st.text_input("Enter your name:", key="auth_name_input")
    password = st.text_input("Enter your password:", type="password", key="auth_password_input")
    
    # Button to trigger authentication
    if st.button("Authenticate"):
        # Check if the entered name and password match a record in the database
        select_query = "SELECT * FROM student WHERE name = %s AND password = %s"
        cursor.execute(select_query, (name, password))
        result = cursor.fetchone()
        
        if result:
            # If a matching record is found, authentication is successful
            st.write("Authentication successful!")
            st.write("Welcome, ", result[0])  # Assuming name is stored in the second column (index 1)
            st.write("Your information:")
            # Fetch column names
            column_names = [column[0] for column in cursor.description]

            # Combine column names with the result row
            table_data = [column_names, result]

            # Display the row in a table form
            st.table(table_data)
        else:
            # If no matching record is found, authentication fails
            st.write("Authentication failed. Please try again.")
def del_page():
    st.title("User Authentication")
    
    # Prompt user for name and password
    name = st.text_input("Enter your name:", key="auth_name_input")
    password = st.text_input("Enter your password:", type="password", key="auth_password_input")
    
    # Button to trigger authentication
    if st.button("Authenticate"):
        # Check if the entered name and password match a record in the database
        select_query = "SELECT * FROM student WHERE name = %s AND password = %s"
        cursor.execute(select_query, (name, password))
        result = cursor.fetchone()
        
        if result:
            # Delete the record from the database
                delete_query = "DELETE FROM student WHERE name = %s AND password = %s"
                cursor.execute(delete_query, (name, password))
                connection.commit()
                st.write("Data deleted successfully!")
            # Button to delete data
            
                

        else:
            # If no matching record is found, authentication fails
            st.write("Data deletion failed. Please try again.")

# Data Entry Page
def data_entry_page():
    st.title("Student Information System")
    
    # Get user input
    name = st.text_input("Enter your name:", key="entry_name_input")
    password = st.text_input("Enter your password:", type="password", key="entry_password_input")
    roll = st.number_input("Enter your roll number:", step=1, key="entry_roll_input")
    age = st.number_input("Enter your age:", step=1, key="entry_age_input")
    marks = st.number_input("Enter your marks:", step=1, key="entry_marks_input")
    
    # Button to insert data
    if st.button("Add"):
        # Insert the user input into the database
        insert_query = "INSERT INTO student (name, password, roll, age, marks) VALUES (%s, %s, %s, %s, %s)"
        data_values = (name, password, roll, age, marks)
        cursor.execute(insert_query, data_values)
        connection.commit()
        
        st.write("Data added successfully!")

# Streamlit app
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Home", "Authenticate", "Data Entry","Delete record"))
    
    if page == "Home":
        home_page()
    elif page == "Authenticate":
        authenticate_page()
    elif page == "Data Entry":
    
        data_entry_page()
    elif page == "Delete record":
        del_page()

# Run the Streamlit app
if __name__ == '__main__':
    main()
    
# Close the database connection
cursor.close()
connection.close()
