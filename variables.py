
authentication_employees = """SELECT "Correct" AS Result 
FROM `employees` 
WHERE first_name = ? 
AND last_name = ? AND password = ? AND email = ?; """

authentication_clients = """SELECT "Correct" AS Result FROM `clients` WHERE first_name = ? 
AND last_name = ? AND password = ? AND email = ?; """

sql_add_information_of_employees = """
INSERT INTO employees (first_name, last_name, password, email)
VALUES (?, ?, ?, ?);
"""

sql_add_information_of_clients = """
INSERT INTO clients (first_name, last_name, password, email)
VALUES (?, ?, ?, ?);
"""

# Визначення SQL-запиту для додавання інформації про рейс
sql_add_information_of_flights = """
INSERT INTO `flights` (flight_id, airline, departure_airport, arrival_airport, departure_date, 
arrival_date, duration, available_seats, ticket_price, employee_id)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, (SELECT employee_id FROM employees WHERE email = ?))
"""

# Визначення SQL-запиту для додавання інформації пасажира
sql_add_information_of_passenger = """
INSERT INTO `passengers` ( first_name, last_name, date_of_birth, gender, contact_information, passport_number)
VALUES (?, ?, ?, ?, ?, ?)
"""

sql_add_information_of_booking = """
INSERT INTO `booking` (flight_id, ticket_id, passenger_id, booking_date, status)
VALUES (?, (SELECT ticket_id FROM tickets WHERE seat_number = ?), (SELECT passenger_id FROM passengers WHERE passport_number = ?), ?, ?)
"""

# Запит для вставки інформації про квитки
sql_add_information_of_tickets = """
INSERT INTO `tickets` (flight_id, client_id, passenger_id, seat_number, ticket_price)
SELECT ?, (SELECT client_id FROM clients WHERE email = ?),
 (SELECT passenger_id FROM passengers WHERE passport_number = ?), ?, ticket_price
FROM flights
WHERE flight_id = ?
"""

# удаление рейсов
sql_delete_flight = """
DELETE FROM `flights` WHERE flight_id = ?
"""
sql_delete_tickets = """
USE flight_service;
START TRANSACTION;
SET @passenger_id = (SELECT MAX(passenger_id) FROM passengers WHERE passport_number = ?);
DELETE FROM booking WHERE passenger_id = @passenger_id;
DELETE FROM tickets WHERE passenger_id = @passenger_id;
DELETE FROM passengers WHERE passport_number = ? AND passenger_id = @passenger_id;
COMMIT;
"""

# редагування
sql_update_flight = """
UPDATE `flights`
SET airline = ?,
    departure_airport = ?,
    arrival_airport = ?,
    departure_date = ?,
    arrival_date = ?,
    duration = ?,
    available_seats = ?,
    ticket_price = ?,
    employee_id = (SELECT employee_id FROM employees WHERE email = ?)
WHERE flight_id = ?
"""

find_client_id_query = """
        SELECT email
        FROM clients
        WHERE first_name = ?
          AND last_name = ?
          AND password = ?
        """

# sql_query = """
#         SELECT passengers.*, tickets.*
#         FROM passengers
#         LEFT JOIN tickets ON passengers.passenger_id = tickets.passenger_id
#         WHERE passengers.contact_information = %s;
#         """
