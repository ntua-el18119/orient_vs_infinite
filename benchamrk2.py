

import time
from matplotlib import pyplot as plt
import requests
import json
import subprocess

import json

# Define the JSON schema
json_schema = [
  {
    "className": "FleetData.Customer",
    "isReferenceable": True,
    "superClass": None,
    "attributes": [
      {
        "attributeName": "rewardPoints",
        "logicalType": "integer",
        "encoding": "unsigned",
        "storage": "b32"
      },
      {
        "attributeName": "firstName",
        "logicalType": "string",
        "encoding": "utf8",
        "storage": "variable"
      },
      {
        "attributeName": "lastName",
        "logicalType": "string",
        "encoding": "utf8",
        "storage": "variable"
      },
      {
        "attributeName": "friendships",
        "logicalType": "list",
        "storage": "variable",
        "elementSpecification": {
          "logicalType": "reference",
          "referencedClass": "FleetDataCustomers"
          
        }
      }
    ]
  }
]

# Convert the JSON schema to a string
json_schema_str = json.dumps(json_schema)

# Define the curl command as a list of arguments
curl_command = [
    'curl',
    '-X', 'POST',
    '-H', 'Content-Type: application/json',
    '-d', json_schema_str,
    'localhost:8185/v1/object'
]

try:
    # Execute the curl command
    subprocess.run(curl_command, check=True)
    print("Request successful")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
    

curl_command = [
    'curl',
    '-X', 'POST',
    '-H', 'Content-Type: application/json',
    '-H', 'Accept: application/json',
    '-d', '{"class":"FleetData.Customer","attributes":{"lastName":"Suarez","firstName":"paul","rewardPoints":"150"}}',
    'localhost:8185/v1/object'
]

try:
    # Execute the curl command
    subprocess.run(curl_command, check=True)
    print("Request successful")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

curl_command = [
    'curl',
    '-X', 'POST',
    '-H', 'Content-Type: application/json',
    '-H', 'Accept: application/json',
    '-d', '{"class":"FleetData.Customer","attributes":{"lastName":"Suarez","firstName":"ross","rewardPoints":"45"}}',
    'localhost:8185/v1/object'
]

try:
    # Execute the curl command
    subprocess.run(curl_command, check=True)
    print("Request successful")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

curl_command = [
    'curl',
    '-X', 'POST',
    '-H', 'Content-Type: application/json',
    '-H', 'Accept: application/json',
    '-d', '{"class":"FleetData.Customer","attributes":{"lastName":"Suarez","firstName":"john","rewardPoints":"150"}}',
    'localhost:8185/v1/object'
]

try:
    # Execute the curl command
    subprocess.run(curl_command, check=True)
    print("Request successful")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

curl_command = [
    'curl',
    '-X', 'POST',
    '-H', 'Content-Type: application/json',
    '-H', 'Accept: application/json',
    '-d', '{"class":"FleetData.Customer","attributes":{"lastName":"Trout","firstName":"Mike","rewardPoints":"431"}}',
    'localhost:8185/v1/object'
]

try:
    # Execute the curl command
    subprocess.run(curl_command, check=True)
    print("Request successful")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")


curl_command = [
    'curl',
    '-X', 'POST',
    '-H', 'Content-Type: application/json',
    '-H', 'Accept: application/json',
    '-d', '{"class":"FleetData.Customer","attributes":{"lastName":"Saul","firstName":"Mike","rewardPoints":"12"}}',
    'localhost:8185/v1/object'
]

try:
    # Execute the curl command
    subprocess.run(curl_command, check=True)
    print("Request successful")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

curl_command = [
    'curl',
    '-X', 'POST',
    '-H', 'Content-Type: application/json',
    '-H', 'Accept: application/json',
    '-d', '{"class":"FleetData.Customer","attributes":{"lastName":"Ukno","firstName":"BetterCall","rewardPoints":"0"}}',
    'localhost:8185/v1/object'
]

try:
    # Execute the curl command
    subprocess.run(curl_command, check=True)
    print("Request successful")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")


curl_command = [
    'curl',
    '-X', 'POST',
    '-H', 'Content-Type: application/json',
    '-H', 'Accept: application/json',
    '-d', '{"class":"FleetData.Customer","attributes":{"lastName":"ase","firstName":"Venctura","rewardPoints":"2222"}}',
    'localhost:8185/v1/object'
]

try:
    # Execute the curl command
    subprocess.run(curl_command, check=True)
    print("Request successful")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

curl_command = [
    'curl',
    '-X', 'POST',
    '-H', 'Content-Type: application/json',
    '-H', 'Accept: application/json',
    '-d', '{"class":"FleetData.Customer","attributes":{"lastName":"Suzy","firstName":"Jean","rewardPoints":"1550"}}',
    'localhost:8185/v1/object'
]

try:
    # Execute the curl command
    subprocess.run(curl_command, check=True)
    print("Request successful")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

min_time_insert = 100000
max_time_insert = 0
med_time_insert = 0

min_time_select = 100000
max_time_select = 0
med_time_select = 0

min_time_update = 100000
max_time_update = 0
med_time_update = 0


# Define the API endpoint URL
for i in range(0,10):
    
    api_endpoint = 'http://localhost:8185/v1/query'

# Define the query JSON
    query_json = {
       "query": "UPDATE Customer WHERE lastName == 'White' CLEAR rewardPoints;",
       "language": "do"
    }

# Convert the query JSON to a string
    query_data = json.dumps(query_json)

# Set the headers
    headers = {
     'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    
    # Send the POST request with the query JSON
    start_time = time.time()
    response = requests.post(api_endpoint, headers=headers, data=query_data)
    end_time = time.time()
    execution_time = end_time - start_time
    time.sleep(1)
    
    # Check the response
    if response.status_code == 200:
            print("Request successful")
            print(response.json())  # Print the response content
    else:
        print(f"Request failed with status code {response.status_code}:")
        print(response.text)
                

    if execution_time<min_time_update :  min_time_update =execution_time
    if execution_time>max_time_update :  max_time_update =execution_time
    med_time_update =execution_time+ med_time_update

for i in range(0,10):
    
    api_endpoint = 'http://localhost:8185/v1/query'

# Define the query JSON
    query_json = {
       "query": "FROM FleetData.Customer WHERE firstName = 'Mike' RETURN *;",
       "language": "do"
    }

# Convert the query JSON to a string
    query_data = json.dumps(query_json)

# Set the headers
    headers = {
     'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    
    # Send the POST request with the query JSON
    start_time = time.time()
    response = requests.post(api_endpoint, headers=headers, data=query_data)
    end_time = time.time()
    execution_time = end_time - start_time
    time.sleep(1)
    # Check the response
    if response.status_code == 200:
            print("Request successful")
            print(response.json())  # Print the response content
    else:
        print(f"Request failed with status code {response.status_code}:")
        print(response.text)
    if execution_time<min_time_select :  min_time_select =execution_time
    if execution_time>max_time_select :  max_time_select =execution_time
    med_time_select =execution_time + med_time_select

query_types = [ "Select", "Update"]
min_times = [ min_time_select, min_time_update]
max_times = [max_time_select, max_time_update]
med_times = [ med_time_select, med_time_update]

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

