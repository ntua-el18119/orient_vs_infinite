import pyorient
import time
import matplotlib.pyplot as plt
import numpy as np
# Function to connect to the OrientDB server
def connect_to_orientdb(database_name):
    client = pyorient.OrientDB("localhost",2424)  # Modify the host and port as needed
    
    client.set_session_token( True )  # set true to enable the token based
    client.connect("root", "testpassword")
    #database_name = "GratefulDeadConcerts"  # Replace with the name of your database
    #print("Session Token: ")
    client.db_open(database_name, "root", "testpassword")  # Specify the database name

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
        
        min_time_delete = 100000
        max_time_delete = 0
        med_time_delete = 0

        for i in range(0,100):
            select_query = "SELECT FROM Whisky WHERE out('ProducedIn').name IN ['Aberlour', 'Elgin']"
            update_query = f"UPDATE FlavourGroup SET description = 'TestDescription {10*i+1000}' WHERE dryness = 'Medium'"
            insert_query = f"INSERT INTO Flavour(name) VALUES ({10*i+1000})"
            #delete_query = "DELETE FROM Flavour WHERE name = 'TestName'"

            insert_result, insert_time = execute_query_and_measure_time(client, insert_query)

            select_result, select_time = execute_query_and_measure_time(client, select_query)
            update_result, update_time = execute_query_and_measure_time(client, update_query)
            #print('a')
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

            #if delete_time<min_time_delete :  min_time_delete = delete_time
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
        plt.title("Whisky DB: Minimum, Maximum, and Median Query Runtimes")
        plt.xticks([i + bar_width for i in index], query_types)

# Legend
        plt.legend()

# Show the plot
        plt.tight_layout()
        plt.show()
        database_name = "demodb"
        client = connect_to_orientdb(database_name)
        
        #database_name = "GratefulDeadConcerts"  # Replace with the name of your database
        #client.db_open(database_name, "root", "4g34gf")  # Specify the database name
        
        # Example CRUD operations and time measurement
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
        
        min_time_delete = 100000
        max_time_delete = 0
        med_time_delete = 0

        for i in range(0,100):
            select_query = "SELECT FROM Profiles"
            update_query = "UPDATE PROFILES SET Name = 'Name'"
            insert_query = f"INSERT INTO Theatres(Id) VALUES ({i+10001})"
            #delete_query = "DELETE FROM Movies where id = 10000000"
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

            #if delete_time<min_time_delete :  min_time_delete = delete_time
            #if delete_time>max_time_delete :  max_time_delete = delete_time
           #med_time_delete = update_time+ med_time_delete
        
        
        #med_time_delete = med_time_delete/100 
        med_time_update = med_time_update/100    
        med_time_insert = med_time_insert/100 
        med_time_select = med_time_select/100 
       
        
        query_types = ["Insert", "Select", "Update"]
        min_times = [min_time_insert, min_time_select, min_time_update]
        #print(min_time_insert)
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
        plt.title("DemoDB: Minimum, Maximum, and Median Query Runtimes")
        plt.xticks([i + bar_width for i in index], query_types)

# Legend
        plt.legend()

# Show the plot
        plt.tight_layout()
        plt.show()
database_name = 'Tolkien-Arda'
        client = connect_to_orientdb(database_name)
        
        #database_name = "GratefulDeadConcerts"  # Replace with the name of your database
        #client.db_open(database_name, "root", "4g34gf")  # Specify the database name
        
        # Example CRUD operations and time measurement
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
        
        min_time_delete = 100000
        max_time_delete = 0
        med_time_delete = 0

        for i in range(0,100):
            select_query = "select from Creature where gender = 'male' and race != 'Hobbit'"
            update_query = "update Creature set searchname = 'TestSearchname' where not died is null"
            insert_query = f"INSERT INTO Event(illustrator, description) VALUES ('Illustrator {10*i+1}', 'Description {10*i+1}')"
            #delete_query  = f"DELETE FROM Event WHERE illustrator = 'Illustrator {i}'"

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

            #if delete_time<min_time_delete :  min_time_delete = delete_time
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
        plt.title("Tolkien-Arda DB: Minimum, Maximum, and Median Query Runtimes")
        plt.xticks([i + bar_width for i in index], query_types)

# Legend
        plt.legend()

# Show the plot
        plt.tight_layout()
        plt.show()     
        database_name = 'Reactome'
        client = connect_to_orientdb(database_name)

        #database_name = "GratefulDeadConcerts"  # Replace with the name of your database
        #client.db_open(database_name, "root", "4g34gf")  # Specify the database name
        
        # Example CRUD operations and time measurement
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
        
        min_time_delete = 100000
        max_time_delete = 0
        med_time_delete = 0

        for i in range(0,100):
            insert_id = i + 12312312312
            select_query = "select from vAffiliation where address is null"
            update_query = f"update vAffiliation set displayName = 'displayName' where simpleLabel = 'Affiliation'"
            insert_query = f"INSERT INTO vEvidenceType(dbId) VALUES({insert_id})"
           # delete_query_Reactome f"DELETE FROM vBook where dbId = {insert_id}"

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

            #if delete_time<min_time_delete :  min_time_delete = delete_time
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
        plt.title("Reactome DB: Minimum, Maximum, and Median Query Runtimes")
        plt.xticks([i + bar_width for i in index], query_types)

# Legend
        plt.legend()

# Show the plot
        plt.tight_layout()
        plt.show()
        database_name = 'SmallDB'
        client = connect_to_orientdb(database_name)

        #database_name = "GratefulDeadConcerts"  # Replace with the name of your database
        #client.db_open(database_name, "root", "4g34gf")  # Specify the database name
        
        # Example CRUD operations and time measurement
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
        
        min_time_delete = 100000
        max_time_delete = 0
        med_time_delete = 0

        for i in range(0,100):
            select_query = "select from Customer where rewardPoints >= 100"
            update_query = f"update Customer set rewardPoints = 0 where lastName = 'Wilkinson'"
            insert_query = f"INSERT INTO Customer(firstName, lastName, rewardPoints) VALUES(TestName,TestLastName, 0)"
           # delete_query_Reactome f"DELETE FROM vBook where dbId = {insert_id}"

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

            #if delete_time<min_time_delete :  min_time_delete = delete_time
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
        plt.title("Small DB (self-created): Minimum, Maximum, and Median Query Runtimes")
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
        
        min_time_delete = 100000
        max_time_delete = 0
        med_time_delete = 0

        for i in range(0,100):
            insert_result, insert_time = execute_query_and_measure_time(client, insert_query)
       
            select_result, select_time = execute_query_and_measure_time(client, select_query)
        
            update_result, update_time = execute_query_and_measure_time(client, update_query)
        
            delete_result, delete_time = execute_query_and_measure_time(client, delete_query)
           
            if insert_time<min_time_insert :  min_time_insert = insert_time
            if insert_time > max_time_insert :  max_time_insert = insert_time
            med_time_insert = insert_time + med_time_insert

            if select_time<min_time_select :  min_time_select = select_time
            if select_time>max_time_select :  max_time_select = select_time
            med_time_select = select_time + med_time_select

            if update_time<min_time_update :  min_time_update = update_time
            if update_time>max_time_update :  max_time_update = update_time
            med_time_update = update_time+ med_time_update

            if delete_time<min_time_delete :  min_time_delete = delete_time
            if delete_time>max_time_delete :  max_time_delete = delete_time
            med_time_delete = update_time+ med_time_delete
        
        
        med_time_delete = med_time_delete/100 
        med_time_update = med_time_update/100    
        med_time_insert = med_time_insert/100 
        med_time_select = med_time_select/100 
       
        
        query_types = ["Insert", "Select", "Update", "Delete"]
        min_times = [min_time_insert, min_time_select, min_time_update, min_time_delete]
        max_times = [max_time_insert, max_time_select, max_time_update, max_time_delete]
        med_times = [med_time_insert, med_time_select, med_time_update, med_time_delete]

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
