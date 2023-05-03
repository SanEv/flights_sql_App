import mysql.connector
from mysql.connector.plugins import caching_sha2_password

class DB:
    def __init__(self):
        #connect to database
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='password',
                database='flights'

            )
            self.mycursor =self.conn.cursor()
            print('connection established')
        except:
            print('connection error')

    def fetch_city_names(self):
        city=[]
        self.mycursor.execute("""
        SELECT DISTINCT (Destination) FROM flights.flight
        UNION
        SELECT DISTINCT (Source) FROM flights.flight
        """)
        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
        return city

    def fetch_all_flights(self,source,destination):
        self.mycursor.execute(
            """
            SELECT Airline,Route,Dep_Time,Duration,Price FROM flights.flight
            WHERE Source='{}' AND Destination ='{}'
            """.format(source,destination)
        )
        data=self.mycursor.fetchall()
        return data

    def fetch_airline_frequency(self):
        airline=[]
        frequency=[]
        self.mycursor.execute("""
        Select Airline,COUNT(*)
        FROM flights.flight
        GROUP BY Airline""")

        data =self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])
        return airline,frequency

    def busy_airport(self):
        city = []
        frequency = []
        self.mycursor.execute("""
        SELECT Source, COUNT(*) FROM (SELECT Source FROM flights.flight
                              UNION ALL
                               SELECT Destination FROM flights.flight) t
                               GROUP BY t.Source
                               ORDER BY COUNT(*) DESC""")
        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            frequency.append(item[1])
        return city, frequency


    def daily_frequency(self):
        date = []
        frequency = []
        self.mycursor.execute("""
        SELECT Date_of_Journey,Count(*) FROM flights.flight
        GROUP BY Date_of_Journey""")
        data = self.mycursor.fetchall()
        for item in data:
            date.append(item[0])
            frequency.append(item[1])
        return date, frequency

