import mysql.connector
# from variabls import *

passagers_list = []

class DataBase:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            port=3306,
            host='localhost',
            user='root',
            password='192837465',
            database='flight_service',

        )


    # def create_table(self, sql: str):
    #     self.mydb.cursor().execute(sql)

    def add_to_database_employees_info(self, first_name_value, last_name_value, Password_value, Email_value,):
        val = (first_name_value, last_name_value, Password_value, Email_value,)
        self.mydb.cursor().execute(sql_add_information_of_employees, val)
        self.mydb.commit()

    def add_to_database_clients_info(self, first_name_value, last_name_value, Password_value, Email_value,):
        val = (first_name_value, last_name_value, Password_value, Email_value,)
        self.mydb.cursor().execute(sql_add_information_of_clients, val)
        self.mydb.commit()


    def add_to_database_passenger_info(self, first_name_value, last_name_value,
                                                date_of_birth_value, gender_value, contact_information_value, passport_number_value):
        val = (first_name_value, last_name_value, date_of_birth_value, gender_value,
               contact_information_value, passport_number_value)
        self.mydb.cursor().execute(sql_add_information_of_passenger, val)
        self.mydb.commit()


    def add_to_database_booking_info(self, flight_id_value, passenger_id_value, booking_date_value, txt):
        val = (flight_id_value, passenger_id_value, booking_date_value, txt)

        self.mydb.cursor().execute(sql_add_information_of_booking, val)
        self.mydb.commit()

    def add_to_database_flights_info(self, flight_id_value, airline_value, departure_airport_value, arrival_airport_value, departure_date_value,
                                     arrival_date_value, duration_value, available_seats_value, ticket_price_value):
        val = (flight_id_value, airline_value, departure_airport_value, arrival_airport_value, departure_date_value,
               arrival_date_value, duration_value, available_seats_value, ticket_price_value)
        self.mydb.cursor().execute(sql_add_information_of_flights, val)
        self.mydb.commit()

    def add_to_database_tickets_info(self, flight_id_value, Email_value, passenger_id_value, seat_number_value,
                                     flight_id_value_price):
        val = (flight_id_value, Email_value, passenger_id_value, seat_number_value, flight_id_value_price,)
        self.mydb.cursor().execute(sql_add_information_of_tickets, val)
        self.mydb.commit()

    def select_passenger_info(self):
        with self.mydb.cursor(buffered=True) as cursor:
            cursor.execute('SELECT * FROM `passengers`;')
            row = cursor.fetchone()
            while row is not None:
                print(row)
                row = cursor.fetchone()

    def select_booking_info(self):
        with self.mydb.cursor(buffered=True) as cursor:
            cursor.execute('SELECT * FROM `booking`;')
            row = cursor.fetchone()
            while row is not None:
                print(row)
                row = cursor.fetchone()

    def select_authentication_employees_info(self, first_name_value, last_name_value, Password_value, Email_value):
        with self.mydb.cursor(buffered=True) as cursor:
            val= (first_name_value, last_name_value, Password_value, Email_value)
            cursor.execute(authentication_employees, val)
            result = cursor.fetchone()
            return result

    def select_authentication_clients_info(self, first_name_value, last_name_value, Password_value, Email_value):
        with self.mydb.cursor(buffered=True) as cursor:
            val= (first_name_value, last_name_value, Password_value, Email_value)
            cursor.execute(authentication_clients, val)
            result = cursor.fetchone()
            return result

    # def find_client_id(self, first_name_value, last_name_value, Password_value, Email_value):
    #     with self.mydb.cursor(buffered=True) as cursor:
    #         sql = 'SELECT client_id FROM clients WHERE first_name = %s AND last_name = %s AND password = %s AND email = %s;'
    #         val = (first_name_value, last_name_value, Password_value, Email_value)
    #         cursor.execute(sql, val)
    #         result = cursor.fetchone()
    #         return result

    # def select_free_seats_for_flight(self,):
    #     with self.mydb.cursor(buffered=True) as cursor:
    #         all_seats = cursor.execute('SELECT available_seats FROM `flights` WHERE flight_id = %s;', (flight_id,))
    #         all_seats = cursor.fetchone()
    #         print(all_seats[0])

            # sold_seats = cursor.execute('SELECT booking_id FROM `booking` WHERE flight_id = %s};', (flight_id,))
            # sold_seats = cursor.fetchone()
            # # free_seats = all_seats[0] - sold_seats[0]
            #
            # print(sold_seats)








            # row = cursor.fetchone()
            # while row is not None:
            #     print(row)
            #     row = cursor.fetchone()

    def select_flights_info(self):
        with self.mydb.cursor(buffered=True) as cursor:
            cursor.execute('SELECT * FROM `flights`')
            row = cursor.fetchone()

            while row is not None:
                yield row
                row = cursor.fetchone()


    def select_tickets_info(self):
        with self.mydb.cursor(buffered=True) as cursor:
            cursor.execute('SELECT * FROM `tickets`')
            row = cursor.fetchone()
            while row is not None:
                row = cursor.fetchone()
                print(row)

    def select_ticket_and_passenger_info_by_passport(self, passport_number):
        formatted_rows = []
        with self.mydb.cursor(buffered=True) as cursor:
            cursor.execute('''
                    SELECT 
                        p.first_name AS passenger_first_name,
                        p.last_name AS passenger_last_name,
                        p.gender,
                        p.contact_information,
                        p.date_of_birth,
                        p.passport_number,
                        t.flight_id,
                        t.seat_number,
                        t.ticket_price,
                        f.airline,
                        f.departure_airport,
                        f.arrival_airport,
                        f.departure_date,
                        f.arrival_date,
                        f.duration
                    FROM clients AS c
                    JOIN tickets AS t ON c.client_id = t.client_id
                    JOIN passengers AS p ON t.passenger_id = p.passenger_id
                    JOIN flights AS f ON t.flight_id = f.flight_id
                    WHERE p.passport_number = %s
                ''', (passport_number,))
            row = cursor.fetchone()
            while row is not None:
                formatted_row = tuple(row)
                formatted_rows.append(formatted_row)
                row = cursor.fetchone()
        return formatted_rows

    def select_text_seat(self, flight_id_value):
        with self.mydb.cursor(buffered=True) as cursor:
            cursor.execute('''
                SELECT t.seat_number
                FROM tickets AS t
                WHERE t.flight_id = %s
            ''', (flight_id_value,))
            rows = cursor.fetchall()

        # Об'єднати номери місць в один рядок
        seat_numbers = ', '.join(str(row[0]) for row in rows)

        return seat_numbers

    def delete_tickets_booking(self, passport_number):
        with self.mydb.cursor() as cursor:
            cursor.execute("SELECT MAX(passenger_id) FROM passengers WHERE passport_number = %s", (passport_number,))
            passenger_id = cursor.fetchone()[0]

        if passenger_id is not None:
            # Видаліть записи в таблиці booking за відповідним passenger_id
            with self.mydb.cursor() as cursor:
                cursor.execute("DELETE FROM booking WHERE passenger_id = %s", (passenger_id,))

            # Видаліть записи в таблиці tickets за відповідним passenger_id
            with self.mydb.cursor() as cursor:
                cursor.execute("DELETE FROM tickets WHERE passenger_id = %s", (passenger_id,))

            # Видаліть записи в таблиці passengers за номером паспорта та passenger_id
            with self.mydb.cursor() as cursor:
                cursor.execute("DELETE FROM passengers WHERE passport_number = %s AND passenger_id = %s",
                               (passport_number, passenger_id))

            # Закриття транзакції
            self.mydb.commit()

    def delete_flights_info(self, Deleteflights_value):
        flight_id_to_delete = Deleteflights_value
        self.mydb.cursor().execute(sql_delete_flight, (flight_id_to_delete,))
        self.mydb.commit()

    def sql_update_flight_info(self,flight_id_value, airline_value, departure_airport_value, arrival_airport_value, departure_date_value, arrival_date_value, duration_value, available_seats_value):
        val = (airline_value, departure_airport_value, arrival_airport_value, departure_date_value, arrival_date_value, duration_value, available_seats_value, flight_id_value)
        self.mydb.cursor().execute(sql_update_flight,  val)
        self.mydb.commit()

    def select_flights_info_id(self, flight_id_value):
        formatted_rows = []
        with self.mydb.cursor(buffered=True) as cursor:
            # Вивести інформацію про рейс за його ідентифікатором
            cursor.execute('SELECT * FROM `flights` WHERE flight_id = %s', (flight_id_value,))
            row = cursor.fetchone()
            while row is not None:
                formatted_row = tuple(row)
                formatted_rows.append(formatted_row)
                row = cursor.fetchone()
        return formatted_rows

    def select_ticket_info(self, flight_id_value):
        with self.mydb.cursor(buffered=True) as cursor:
            # Вивести інформацію про рейс за його ідентифікатором
            cursor.execute('SELECT ticket_price FROM `flights` WHERE flight_id = %s', (flight_id_value,))
            row = cursor.fetchone()
            while row is not None:
                print(row)
                row = cursor.fetchone()

    def find_booking_seats(self, flight_id):
        formatted_rows = []
        with self.mydb.cursor(buffered=True) as cursor:
            cursor.execute('''
                SELECT 
                t.seat_number,
                    p.first_name AS passenger_first_name,
                    p.last_name AS passenger_last_name,
                    p.gender,
                    p.contact_information,
                    p.date_of_birth,
                    p.passport_number,
                    t.ticket_price,
                    f.airline,
                    f.departure_airport,
                    f.arrival_airport,
                    f.departure_date,
                    f.arrival_date,
                    f.duration
                FROM passengers AS p
                JOIN tickets AS t ON p.passenger_id = t.passenger_id
                JOIN flights AS f ON t.flight_id = f.flight_id
                WHERE t.flight_id = %s
            ''', (flight_id,))
            row = cursor.fetchone()
            while row is not None:
                formatted_row = tuple(row)
                formatted_rows.append(formatted_row)
                row = cursor.fetchone()
        return formatted_rows

    # def find_client_id(self, first_name_value, last_name_value, Password_value):
    #     with self.mydb.cursor(buffered=True) as cursor:
    #         val = (first_name_value, last_name_value, Password_value)
    #         cursor.execute(find_client_id_query, val)
    #         row = cursor.fetchone()
    #         while row is not None:
    #             print(row)
    #             row = cursor.fetchone()



A = DataBase()
#A.add_to_database_flights_info()
#A.add_to_database_passenger_info()
#A.add_to_database_booking_info()
#A.add_to_database_tickets_info()
#A.select_passenger_info()
#A.select_flights_info()
#A.select_booking_info()
#A.select_tickets_info()
# DataBase().delete_flights_info()
# A.select_free_seats_for_flight(654)
