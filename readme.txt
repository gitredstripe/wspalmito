This code creates two REST endpoints, /save_data and /retrieve_data/<table_name>. The /save_data endpoint accepts a POST request with a JSON payload containing the table name and the data to be saved. The /retrieve_data/<table_name> endpoint accepts a GET request with the table name as a parameter and returns the data in the table as a JSON response.

Please replace the dbname, user, password, host, and port with your actual PostgreSQL database credentials.

You can test the endpoints using tools like curl or Postman. For example, to save data, you can use the following curl command:
curl -X POST -H "Content-Type: application/json" -d '{"table_name": "sample_table", "data": [{"name": "John", "age": 25, "city": "New York"}, {"name": "Jane", "age": 30, "city": "Los Angeles"}]}' http://localhost:5000/save_data

And to retrieve data, you can use the following curl command:
curl http://localhost:5000/retrieve_data/

