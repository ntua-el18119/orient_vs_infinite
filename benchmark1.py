import pyorient
import time
import matplotlib.pyplot as plt
import numpy as np
# Function to connect to the OrientDB server
def connect_to_orientdb(database_name):
    client = pyorient.OrientDB("localhost",2424)  # Modify the host and port as needed
    
    client.set_session_token( True )  # set true to enable the token based
    client.connect("root", "4g34gf")
    #database_name = "GratefulDeadConcerts"  # Replace with the name of your database
    #print("Session Token: ")
    client.db_open(database_name, "root", "4g34gf")  # Specify the database name
    
  
    
    #print("Session ID:")
    return (client)

# Function to disconnect from the OrientDB server
def disconnect_from_orientdb(client):
    client.db_close()
    client.close()

# Function to execute a query and measure execution time
def execute_query_and_measure_time(client, query):
    start_time = time.time()
    result = client.command(query)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Main function
if __name__ == "__main__":
    try:
        database_name="Whisky"
        client = connect_to_orientdb(database_name)
        
        #database_name = "GratefulDeadConcerts"  # Replace with the name of your database
        #client.db_open(database_name, "root", "4g34gf")  # Specify the database name
        
        # Example CRUD operations and time measurement
        insert_query = "INSERT INTO V SET followed_by = 'Johhhhhn', age = 30"
        select_query = "SELECT * FROM V WHERE followed_by = 'John'"
        update_query = "UPDATE V SET age = 31 WHERE followed_by = 'John'"
        delete_query = "DELETE FROM V WHERE followed_by = 'John'"
        # Execute and measure the time for each query
        
        min_time_insert = 100000
        max_time_insert = 0
        med_time_insert = 0

        min_time_select = 100000
        max_time_select = 0
        med_time_select = 0

        min_time_update = 100000
        max_time_update = 0
        med_time_update = 0
        
        #min_time_delete = 100000
       # max_time_delete = 0
       # med_time_delete = 0

        for i in range(0,100):
            insert_result, insert_time = execute_query_and_measure_time(client, insert_query)
       
            select_result, select_time = execute_query_and_measure_time(client, select_query)
        
            update_result, update_time = execute_query_and_measure_time(client, update_query)
        
            #delete_result, delete_time = execute_query_and_measure_time(client, delete_query)
           
            if insert_time<min_time_insert :  min_time_insert = insert_time
            if insert_time > max_time_insert :  max_time_insert = insert_time
            med_time_insert = insert_time + med_time_insert

            if select_time<min_time_select :  min_time_select = select_time
            if select_time>max_time_select :  max_time_select = select_time
            med_time_select = select_time + med_time_select

            if update_time<min_time_update :  min_time_update = update_time
            if update_time>max_time_update :  max_time_update = update_time
            med_time_update = update_time+ med_time_update

           # if delete_time<min_time_delete :  min_time_delete = delete_time
            #if delete_time>max_time_delete :  max_time_delete = delete_time
            #med_time_delete = update_time+ med_time_delete
        
        
        #med_time_delete = med_time_delete/100 
        med_time_update = med_time_update/100    
        med_time_insert = med_time_insert/100 
        med_time_select = med_time_select/100 
       
        
        query_types = ["Insert", "Select", "Update"]
        min_times = [min_time_insert, min_time_select, min_time_update]
        max_times = [max_time_insert, max_time_select, max_time_update]
        med_times = [med_time_insert, med_time_select, med_time_update]

# Plotting the data
        fig, ax = plt.subplots(figsize=(10, 6))

# Bar width
        bar_width = 0.2

# Bar positions
        index = range(len(query_types))

# Plot minimum times
        plt.bar(index, min_times, bar_width, label="Minimum", color="blue")
# Plot maximum times
        plt.bar([i + bar_width for i in index], max_times, bar_width, label="Maximum", color="red")
# Plot median times
        plt.bar([i + 2 * bar_width for i in index], med_times, bar_width, label="Median", color="green")

# X-axis labels and title
        plt.xlabel("Query Types")
        plt.ylabel("Execution Time (seconds)")
        plt.title("Minimum, Maximum, and Median Query Runtimes")
        plt.xticks([i + bar_width for i in index], query_types)

# Legend
        plt.legend()

# Show the plot
        plt.tight_layout()
        plt.show()
        
        
        
        database_name="MovieRatings"
        client = connect_to_orientdb(database_name)
        
        #database_name = "GratefulDeadConcerts"  # Replace with the name of your database
        #client.db_open(database_name, "root", "4g34gf")  # Specify the database name
        
        # Example CRUD operations and time measurement
        insert_query = "INSERT INTO V SET followed_by = 'Johhhhhn', age = 30"
        select_query = "SELECT * FROM V WHERE followed_by = 'John'"
        update_query = "UPDATE V SET age = 31 WHERE followed_by = 'John'"
        delete_query = "DELETE FROM V WHERE followed_by = 'John'"
        # Execute and measure the time for each query
        
        min_time_insert = 100000
        max_time_insert = 0
        med_time_insert = 0

        min_time_select = 100000
        max_time_select = 0
        med_time_select = 0

        min_time_update = 100000
        max_time_update = 0
        med_time_update = 0
        
        #min_time_delete = 100000
       # max_time_delete = 0
       # med_time_delete = 0

        for i in range(0,100):
            insert_result, insert_time = execute_query_and_measure_time(client, insert_query)
       
            select_result, select_time = execute_query_and_measure_time(client, select_query)
        
            update_result, update_time = execute_query_and_measure_time(client, update_query)
        
            #delete_result, delete_time = execute_query_and_measure_time(client, delete_query)
           
            if insert_time<min_time_insert :  min_time_insert = insert_time
            if insert_time > max_time_insert :  max_time_insert = insert_time
            med_time_insert = insert_time + med_time_insert

            if select_time<min_time_select :  min_time_select = select_time
            if select_time>max_time_select :  max_time_select = select_time
            med_time_select = select_time + med_time_select

            if update_time<min_time_update :  min_time_update = update_time
            if update_time>max_time_update :  max_time_update = update_time
            med_time_update = update_time+ med_time_update

           # if delete_time<min_time_delete :  min_time_delete = delete_time
            #if delete_time>max_time_delete :  max_time_delete = delete_time
            #med_time_delete = update_time+ med_time_delete
        
        
        #med_time_delete = med_time_delete/100 
        med_time_update = med_time_update/100    
        med_time_insert = med_time_insert/100 
        med_time_select = med_time_select/100 
           
        
        
        query_types = ["Insert", "Select", "Update"]
        min_times = [min_time_insert, min_time_select, min_time_update]
        max_times = [max_time_insert, max_time_select, max_time_update]
        med_times = [med_time_insert, med_time_select, med_time_update]

# Plotting the data
        fig, ax = plt.subplots(figsize=(10, 6))

# Bar width
        bar_width = 0.2

# Bar positions
        index = range(len(query_types))

# Plot minimum times
        plt.bar(index, min_times, bar_width, label="Minimum", color="blue")
# Plot maximum times
        plt.bar([i + bar_width for i in index], max_times, bar_width, label="Maximum", color="red")
# Plot median times
        plt.bar([i + 2 * bar_width for i in index], med_times, bar_width, label="Median", color="green")

# X-axis labels and title
        plt.xlabel("Query Types")
        plt.ylabel("Execution Time (seconds)")
        plt.title("Minimum, Maximum, and Median Query Runtimes")
        plt.xticks([i + bar_width for i in index], query_types)

# Legend
        plt.legend()

# Show the plot
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print("An error occurred:", str(e))

    
