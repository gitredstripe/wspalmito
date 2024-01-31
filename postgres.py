import psycopg2
from flask import Flask, request, jsonify
from psycopg2.extras import RealDictCursor
from typing import List

app = Flask(__name__)

class PostgreSQLClient:
    def __init__(self, dbname: str, user: str, password: str, host: str, port: int):
        self.dbname = "delpalmito"
        self.user = "postgres"
        self.password = "admin"
        self.host = "localhost"
        self.port = 5432
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Connected to PostgreSQL database")
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL database: {e}")

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print("Disconnected from PostgreSQL database")

    def save_data(self, table_name: str, data: List[dict]):
        cursor = self.conn.cursor()
        for item in data:
            keys = ', '.join(item.keys())
            values = ', '.join(f"'{v}'" for v in item.values())
            insert_query = f"INSERT INTO {table_name} ({keys}) VALUES ({values})"
            cursor.execute(insert_query)
        self.conn.commit()
        cursor.close()

    def retrieve_data(self, table_name: str):
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        select_query = f"SELECT * FROM {table_name}"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

client = PostgreSQLClient(dbname="mydatabase", user="myuser", password="mypassword", host="localhost", port=5432)
client.connect()

@app.route('/save_data', methods=['POST'])
def save_data_rest():
    data = request.get_json()
    table_name = data.get('table_name')
    sample_data = data.get('data')
    client.save_data(table_name, sample_data)
    return jsonify({'message': 'Data saved successfully'})

@app.route('/retrieve_data/<string:table_name>', methods=['GET'])
def retrieve_data_rest(table_name):
    data = client.retrieve_data(table_name)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)