import flet as ft
from SQLite import DataBase

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(ft.Text(f"Initial route: {page.route}"))
    # Начало
    page.title = "flight service"
    first_name = ft.TextField(label="Ім'я", autofocus=True, width=300)
    last_name = ft.TextField(label="Прізвище", width=300)
    Password = ft.TextField(label="Пароль", width=300, password= True)
    Email = ft.TextField(label="Email", width=300)
    Codeworkers = ft.TextField(label="Код доступу", width=300, password= True)
    Code = "369852"

    Visitor = ft.Dropdown(
        label="Роль",
        width=300,
        options=[
            ft.dropdown.Option("Працівник"),
            ft.dropdown.Option("Кліент", ),
        ], )
    greetings = ft.Column()
    # Працівник
    idairline = ft.TextField(label="ID Рейсу", autofocus=True)

    # Рейсы
    flight_id = ft.TextField(label="Номер рейсу", width=300)
    airline = ft.TextField(label="Авіакомпанія",width=300)
    airline.value = ""
    departure_airport = ft.TextField(label="Аеропорт вильоту",width=350)
    arrival_airport = ft.TextField(label="Аеропорт прибуття",width=350)
    departure_date = ft.TextField(label="Дата вильоту", width=300)
    arrival_date = ft.TextField(label="Дата прибуття", width=300)
    duration = ft.TextField(label="Тривалість", width=300)
    available_seats = ft.TextField(label="Вільних місць", width=300)
    ticket_price = ft.TextField(label="Ціна за квиток", width=300)


    # бронирование
    passport_number  = ft.TextField(label="Номер паспорта", width=300)
    first_name = ft.TextField(label="Ім'я", width=300,)
    last_name = ft.TextField(label="Прізвище", width=300)

    date_of_birth = ft.TextField(label="Дата народження",width=300)
    gender = ft.Dropdown(
        label="Стать",
        width=300,
        options=[
            ft.dropdown.Option("Чоловік"),
            ft.dropdown.Option("Жінка"),
            ft.dropdown.Option("Небінарна"),
        ], )
    contact_information = ft.TextField(label="Контактная информация", width=300)

    booking_date = ft.TextField(label="Дата бронювання", width=300)
    seat_number = ft.TextField(label="Місце")
    textf = ft.Text("Рейс зареєстрований")
    textseat = ft.Text("Зайняті місця (Введіть номер рейсу та натисніть оновити)")


    UpdateFlightstext = ft.Text(value="")
    def UpdateFlights(e):
        flight_id_value = flight_id.value
        airline_value = airline.value
        departure_airport_value = departure_airport.value
        arrival_airport_value = arrival_airport.value
        departure_date_value = departure_date.value
        arrival_date_value = arrival_date.value
        duration_value = duration.value
        available_seats_value = available_seats.value
        ticket_price_value = ticket_price.value
        Email_value = Email.value
        page.update()
        DataBase().sql_update_flight_info(flight_id_value, airline_value, departure_airport_value,
                                                arrival_airport_value,
                                                departure_date_value, arrival_date_value, duration_value,
                                                available_seats_value, ticket_price_value, Email_value)
        UpdateFlightstext.value = "Рейс редаговано"
        flight_id.value = ""
        airline.value = ""
        departure_airport.value = ""
        arrival_airport.value = ""
        departure_date.value = ""
        arrival_date.value = ""
        duration.value = ""
        available_seats.value = ""
        ticket_price.value = ""
        page.update()



    #лист рейсов
    lv = ft.ListView(expand=1, spacing=10, item_extent=50)
    page.add(lv)
    for row in DataBase().select_flights_info():
        lv.controls.append(ft.Text("Номер рейсу {}, Компанія {}, Аеропорт вильоту {}, Аеропорт прильоту {},"
                                       "Дата вильоту {}, Дата прильоту {}, Тривалість {} годин, "
                                   "Місткість пасажирів місць {}, Ціна за квиток {}".format(
            *row)))
        if len(lv.controls) % 500 == 0:
            page.update()


    uf = ft.Text(value="")
    page.add(uf)
    def lvUpdateFlights(e):
        uf.value = ""
        flight_id_value = flight_id.value
        formatted_rows = DataBase().select_flights_info_id(flight_id_value)
        for formatted_row in formatted_rows:
            uf.value = "Номер рейсу {}, Компанія {}, Аеропорт вильоту {}, Аеропорт прильоту {},"\
                       " Дата вильоту {}, Дата прильоту {}, Тривалість {} годин," \
                       " Місткість пасажирів місць {}, Ціна за квиток {}".format(*formatted_row)

        page.update()

    def rebut(e):
        lv.controls.clear()
        for row in DataBase().select_flights_info():
            lv.controls.append(ft.Text("Номер рейсу {}, Компанія {}, Аеропорт вильоту {}, Аеропорт прильоту {},"
                                       "Дата вильоту {}, Дата прильоту {}, Тривалість {} годин,"
                                       " Місткість пасажирів місць {}, Ціна за квиток {}".format(
                *row)))
            if len(lv.controls) % 500 == 0:

                page.update()
        page.update()


    # Видалення рейсів
    Deleteflights = ft.TextField(label="Номер рейсу")
    Deleteflightstext = ft.Text(value=" ")
    def Deleteflights_butten(e):
        Deleteflights_value = Deleteflights.value
        if Deleteflights_value:
            print(Deleteflights_value)
            DataBase().delete_flights_info(Deleteflights_value)
            Deleteflightstext.value = "Рейс видалено, натисніть оновити"
        else:
            Deleteflightstext.value = f"Рейсу не існує"
            page.update()
            return
        Deleteflights.value = ""
        page.update()


    flighttext = ft.Text(value="")
    def add_to_database_fli(e):
        if all(value is not None and value != "" for value in
               [flight_id.value, airline.value, departure_airport.value, arrival_airport.value, departure_date.value,
                arrival_date.value, duration.value, available_seats.value, ticket_price.value]):
            flight_id_value = flight_id.value
            airline_value = airline.value
            departure_airport_value = departure_airport.value
            arrival_airport_value = arrival_airport.value
            departure_date_value = departure_date.value
            arrival_date_value = arrival_date.value
            duration_value = duration.value
            available_seats_value = available_seats.value
            ticket_price_value = ticket_price.value
            Email_value = Email.value
            print(Email_value)
            try:
                DataBase().add_to_database_flights_info(flight_id_value, airline_value, departure_airport_value,
                                                        arrival_airport_value,
                                                        departure_date_value, arrival_date_value, duration_value,
                                                        available_seats_value, ticket_price_value, Email_value)
            except Exception as e:
                flighttext.value = f"Номер рейсу зайнятий {e}"
                page.update()
                return

            flighttext.value = "Рейс створено"
            flight_id.value = ""
            airline.value = ""
            departure_airport.value = ""
            arrival_airport.value = ""
            departure_date.value = ""
            arrival_date.value = ""
            duration.value = ""
            available_seats.value = ""
            ticket_price.value = ""
            page.update()
        else:
            flighttext.value = f"Хоча б одне значення порожнє "
            page.update()





    def add_to_database_booking(e):
        # Перевірка, чи всі інші значення не є порожніми
        if all(value is not None and value != "" for value in
               [booking_date.value, flight_id.value, passport_number.value, first_name.value, last_name.value,
                date_of_birth.value, gender.value, contact_information.value, Email.value]):
            seat_number_value = seat_number.value
            booking_date_value = booking_date.value
            flight_id_value = flight_id.value
            passport_number_value = passport_number.value
            first_name_value = first_name.value
            last_name_value = last_name.value
            date_of_birth_value = date_of_birth.value
            gender_value = gender.value
            contact_information_value = contact_information.value
            Email_value = Email.value
            txt = 'Confirmed'

            try:
                DataBase().add_to_database_passenger_info(first_name_value, last_name_value,
                                                          date_of_birth_value, gender_value, contact_information_value,
                                                          passport_number_value)

            except Exception as e:
                text.value = f"Error adding passenger to the database: {e}"
                page.update()
                return

            flight_id_value_price = flight_id.value

            try:
                DataBase().add_to_database_tickets_info(flight_id_value, Email_value, passport_number_value,
                                                        seat_number_value,
                                                        flight_id_value_price)
                print(Email_value)
            except Exception as e:
                text.value = ""
                text.value = f"Це місце вже зайняте "
                print(f"Error adding tickets to the database: {e}")
                page.update()
                return

            try:
                DataBase().add_to_database_booking_info(flight_id_value, seat_number_value, passport_number_value, booking_date_value, txt)

            except Exception as e:
                text.value = f"Номер рейсу не існує: {e}"
                page.update()
                return



            page.update(page.go("/client/Booking/Ticket"))
            booking_date.value = ""
            flight_id.value = ""
            passport_number.value = ""
            first_name.value = ""
            last_name.value = ""
            date_of_birth.value = ""
            gender.value = ""
            contact_information.value = ""
            Email.value = ""
            page.update()


        else:
            text.value ="Хоча б одне значення порожнє."
            page.update()



    Ticket = ft.ListView(expand=1, spacing=10, item_extent=50)

    def text_seat(e):
        flight_id_value = flight_id.value
        textseat.value = " "
        formatted_row = DataBase().select_text_seat(flight_id_value).replace(' ', '').split(',')


        sorted_row_int = sorted([int(item) for item in formatted_row])
        sorted_row_str = ', '.join([str(item) for item in sorted_row_int])
        if ValueError:
            textseat.value = f"Зайнятих місць немає"
            page.update()
        textseat.value = f"Зайняті місця: {sorted_row_str}\n"
        page.update()


    def ticketview(e):
        passport_number_value = passport_number.value
        Ticket.controls.clear()
        formatted_rows = DataBase().select_ticket_and_passenger_info_by_passport(passport_number_value)

        for formatted_row in formatted_rows:
            formatted_values = [str(value) if value is not None else 'Невідомо' for value in formatted_row]
            Ticket.controls.append(ft.Text("ID Квитка {}, Ім'я {}, Прізвище {}, Стать {}, Контактна інформація {}, "
                                           "Дата народження {}, номер паспорту {}, Номер рейсу {} , "
                                           "Номер місця {}, Ціна за квиток {}, Авіакомпанія {}, Аеропорт вильоту {},"
                                           " Аеропорт прибуття {}, Дата відправлення {}, "
                                           "Дата прибуття {}, Час польоту {}, Дата бронювання {}, Статус {}".format(*formatted_values)))
        page.update()
    ticket_id_delete = ft.TextField(label="Ведіть номер квитка")
    DeleteTiketstext = ft.Text(value="")

    def DeleteTikets(e):
        if passport_number.value:
            ticket_id_delete_value = ticket_id_delete.value
            # passport_number_value = passport_number.value
            DataBase().delete_tickets_booking(ticket_id_delete_value)
            DeleteTiketstext.value = "Останнє бронювання скасовано"
            if ValueError:
                DeleteTiketstext.value = "Бронювань немає"
            page.update()
        else:
            DeleteTiketstext.value = "Бронювань немає"
            passport_number.value = ""
            page.update()



    # Booking
    seat_number = ft.TextField(label="Номер місця",width=300)

    def btn_click(e):
        first_name_value = first_name.value
        last_name_value = last_name.value
        Password_value = Password.value
        Email_value = Email.value
        Personal = None
        if Visitor.value == "Працівник":
            result = DataBase().select_authentication_employees_info(first_name_value, last_name_value, Password_value,
                                                            Email_value)
            if result:
                Personal = "/workers"
                first_name.value = ""
                last_name.value = ""
                Password.value = ""
                # Email.value = ""
        if Visitor.value == "Кліент":
            result = DataBase().select_authentication_clients_info(first_name_value, last_name_value, Password_value,
                                                                     Email_value)
            if result:
                Personal = "/client"
                first_name.value = ""
                last_name.value = ""
                Password.value = ""


        if Personal == None:
            regtext.value =""
            regtext.value = "Помилка при вводі даних"
        else:
            regtext.value =""
            page.update(page.go(Personal))


        page.update()

    clientx = ft.Text(value="Якщо ви клієнт, код доступу вводити не потрібно")
    def Regpeople(e):
        if all(value is not None and value != "" for value in
               [first_name.value, last_name.value, Password.value, Email.value]):

            first_name_value = first_name.value
            last_name_value = last_name.value
            Password_value = Password.value
            Email_value = Email.value
            Codeworkers_value = Codeworkers.value

            if Visitor.value:
                if Visitor.value == "Працівник":
                    if Codeworkers_value == Code:
                        try:
                            DataBase().add_to_database_employees_info(first_name_value, last_name_value, Password_value,
                                                                      Email_value)
                            regtext.value = " "
                            regtext.value = "Ви зареєструвалися"
                            Codeworkers.value = " "
                            page.update()
                        except Exception as e:
                            regtext.value = " "
                            regtext.value = f"Цей Email вже зареєстрований"
                            page.update()
                    if Codeworkers_value != Code:
                        regtext.value = " "
                        regtext.value = f"Код доступу недійсний"
                        page.update()
                if Visitor.value == "Клієнт":
                    try:
                        DataBase().add_to_database_clients_info(first_name_value, last_name_value, Password_value,
                                                                Email_value)
                        regtext.value = " "
                        regtext.value = "Ви зареєструвалися"
                        page.update()
                    except Exception as e:
                        regtext.value = " "
                        regtext.value = f"Цей Email вже зареєстрований "
                        page.update()
            else:
                regtext.value = "Виберіть роль натиснувши на спадний список"
                page.update()

            page.update()
        else:
            regtext.value = "Хоча б одне значення порожнє."
            page.update()



    def Checkbooking(e):
        flight_id_value = flight_id.value
        formatted_rows = DataBase().find_booking_seats(flight_id_value)
        Ticket.controls.clear()
        for formatted_row in formatted_rows:
            formatted_values = [str(value) if value is not None else 'Невідомо' for value in formatted_row]
            Ticket.controls.append(ft.Text("Номер місця {}, Ім'я {}, Прізвище {}, Стать {}, Контактна інформація {}, "
                                           "Дата народження {}, Номер паспорту {}, "
                                           "Ціна за квиток {}, Авіакомпанія {}, Аеропорт вильоту {}, "
                                           " Аеропорт прибуття {}, Дата відправлення {}, "
                                           "Дата прибуття {}, Час польоту {},".format(*formatted_values)))
        page.update()

    regtext = ft.Text(value="")
    text = ft.Text(value="", color="red")

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",

                [
                    ft.AppBar(title=ft.Text("Авторизація"), bgcolor=ft.colors.BLACK, color=ft.colors.WHITE,center_title=True),
                    first_name,
                    last_name,
                    Password,
                    Email,
                    Visitor,
                    ft.ElevatedButton("Авторизуватися", on_click=btn_click, bgcolor=ft.colors.ON_BACKGROUND, color=ft.colors.WHITE,width=300,height=40),
                    ft.ElevatedButton("Зареєструватися", on_click=lambda _: page.go("/reg"), bgcolor=ft.colors.AMBER_300,width=300,height=40),
                    greetings,
                    regtext,

                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                vertical_alignment=ft.MainAxisAlignment.CENTER,
            )
        )
        page.update()


        if page.route == "/reg":
            page.views.clear()
            page.views.append(
                ft.View(
                    "/reg",
                    [

                        ft.AppBar(title=ft.Text("Реєстрація"), bgcolor=ft.colors.BLACK, color=ft.colors.WHITE,center_title=True),
                        Visitor,
                        first_name,
                        last_name,
                        Password,
                        Email,
                        clientx,
                        Codeworkers,
                        ft.ElevatedButton("Зареєструватися", on_click=Regpeople, bgcolor=ft.colors.ON_BACKGROUND, color=ft.colors.WHITE, width=300,height=40),
                        ft.ElevatedButton("Увійти в акаунт", on_click=lambda _: page.go("/"), bgcolor=ft.colors.AMBER_300,width=300,height=40),
                        regtext,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/workers":
            page.views.clear()
            page.views.append(
                ft.View(
                    "/workers",
                    [
                        ft.AppBar(title=ft.Text("Рейси"), bgcolor=ft.colors.BLACK, color=ft.colors.WHITE),
                        ft.ElevatedButton("Вихід", on_click=lambda _: page.go("/"),bgcolor=ft.colors.BLACK, color=ft.colors.WHITE),
                        ft.ElevatedButton("Оновити", on_click=rebut, bgcolor=ft.colors.BLUE_ACCENT_200, color=ft.colors.BLACK),
                        lv,
                        ft.OutlinedButton("Створити рейс", on_click=lambda _: page.go("/workers/Flights"),width=300,height=40),
                        ft.OutlinedButton("Редагувати рейс", on_click=lambda _: page.go("/workers/UpdateFlights"),width=300,height=40),
                        ft.OutlinedButton("Переглянути заброньовані місця", on_click=lambda _: page.go("/workers/Checkbooking"),width=300,height=40),
                        ft.OutlinedButton("Видалити рейс", on_click=lambda _: page.go("/workers/Delete"),width=300,height=40),

                    ],

                )
            )
        if page.route == "/workers/Flights":
            page.views.clear()
            page.views.append(
                ft.View(
                    "/workers/Flights",
                    [
                        ft.AppBar(title=ft.Text("Створення рейсу"), bgcolor=ft.colors.BLACK, color=ft.colors.WHITE),
                        ft.ElevatedButton("Назад", on_click=lambda _: page.go("/workers"),bgcolor=ft.colors.BLACK, color=ft.colors.WHITE,width=300,height=40),
                        flight_id,
                        airline,
                        departure_airport,
                        arrival_airport,
                        departure_date,
                        arrival_date,
                        duration,
                        available_seats,
                        ticket_price,
                        ft.OutlinedButton("Зберегти", on_click=add_to_database_fli,width=300,height=40),
                        flighttext,
                    ],
                    scroll=ft.ScrollMode.ALWAYS,
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                )
            )

        if page.route == "/workers/Checkbooking":
            page.views.clear()
            page.views.append(
                ft.View(
                    "/workers/Checkbooking",
                    [
                        ft.AppBar(title=ft.Text("Заброньовані місця"), bgcolor=ft.colors.BLACK, color=ft.colors.WHITE),
                        ft.ElevatedButton("Назад", on_click=lambda _: page.go("/workers"),bgcolor=ft.colors.BLACK, color=ft.colors.WHITE),
                        ft.ElevatedButton("Оновити", on_click=rebut, bgcolor=ft.colors.BLUE_ACCENT_200, color=ft.colors.BLACK),
                        lv,
                        flight_id,
                        Ticket,
                        ft.OutlinedButton("Переглянути", on_click=Checkbooking),

                    ],
                )
            )
        if page.route == "/workers/Delete":
            page.views.clear()
            page.views.append(
                ft.View(
                    "/workers/Delete",
                    [
                        ft.AppBar(title=ft.Text("Видалення рейсу"), bgcolor=ft.colors.BLACK, color=ft.colors.WHITE),
                        ft.ElevatedButton("Назад", on_click=lambda _: page.go("/workers"),bgcolor=ft.colors.BLACK, color=ft.colors.WHITE),
                        ft.ElevatedButton("Оновити", on_click=rebut, bgcolor=ft.colors.BLUE_ACCENT_200, color=ft.colors.BLACK),
                        lv,
                        Deleteflights,
                        ft.OutlinedButton("Видалити", on_click=Deleteflights_butten, icon=ft.icons.DELETE_FOREVER_ROUNDED,
                                          icon_color="pink600"),
                        Deleteflightstext,
                    ],
                )
            )
        if page.route == "/workers/UpdateFlights":
            page.views.clear()
            page.views.append(
                ft.View(
                    "/workers/UpdateFlights",
                    [
                        ft.AppBar(title=ft.Text("Редагування рейсу"), bgcolor=ft.colors.BLACK, color=ft.colors.WHITE),
                        ft.ElevatedButton("Назад", on_click=lambda _: page.go("/workers"),bgcolor=ft.colors.BLACK, color=ft.colors.WHITE,width=300,height=40),
                        uf,
                        flight_id,
                        ft.OutlinedButton("Інформація про рейс", on_click=lvUpdateFlights,width=300,height=40),
                        airline,
                        departure_airport,
                        arrival_airport,
                        departure_date,
                        arrival_date,
                        duration,
                        available_seats,
                        ticket_price,
                        ft.OutlinedButton("Редагувати", on_click=UpdateFlights,width=300,height=40),
                        UpdateFlightstext,

                    ],
                    scroll = ft.ScrollMode.ALWAYS,
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                )
            )

        if page.route == "/client":
            page.views.clear()
            page.views.append(
                ft.View(
                    "/client",
                    [
                        ft.AppBar(title=ft.Text("Рейси"), bgcolor=ft.colors.BLACK, color=ft.colors.WHITE),
                        ft.ElevatedButton("Вийти", on_click=lambda _: page.go("/"),bgcolor=ft.colors.BLACK, color=ft.colors.WHITE),
                        ft.ElevatedButton("Оновити", on_click=rebut, bgcolor=ft.colors.BLUE_ACCENT_200, color=ft.colors.BLACK),
                        lv,
                        ft.OutlinedButton("Забронювати квиток", on_click=lambda _: page.go("/client/Booking"),width=300,height=40),
                        ft.OutlinedButton("Квиток", on_click=lambda _: page.go("/client/Booking/Ticket"),width=300,height=40),


                    ],
                )
            )
        if page.route == "/client/Booking":
            page.views.clear()
            page.views.append(
                ft.View(
                    "/client/Booking",
                    [

                        ft.AppBar(title=ft.Text("Бронювання"), bgcolor=ft.colors.BLACK, color=ft.colors.WHITE),
                        ft.ElevatedButton("Повернутися", on_click=lambda _: page.go("/client"),bgcolor=ft.colors.BLACK, color=ft.colors.WHITE,width=300, height=40),
                        flight_id,
                        seat_number,
                        textseat,
                        ft.ElevatedButton("Оновити", on_click=text_seat, bgcolor=ft.colors.BLUE_ACCENT_200, color=ft.colors.BLACK,width=300, height=40),
                        text,
                        passport_number,
                        first_name,
                        last_name,
                        date_of_birth,
                        gender,
                        contact_information,
                        booking_date,
                        Email,
                        ft.OutlinedButton("Забронювати", on_click=add_to_database_booking, width=300, height=40),
                    ],
                    scroll=ft.ScrollMode.ALWAYS,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/client/Booking/Ticket":
            page.views.clear()
            page.views.append(
                ft.View(
                    "/client/Booking/Ticket",
                    [

                        ft.AppBar(title=ft.Text("Ваш квиток"), bgcolor=ft.colors.BLACK, color=ft.colors.WHITE),
                        ft.ElevatedButton("Повернутися", on_click=lambda _: page.go("/client"),bgcolor=ft.colors.BLACK, color=ft.colors.WHITE),
                        ft.ElevatedButton("Оновити", on_click=ticketview, bgcolor=ft.colors.BLUE_ACCENT_200, color=ft.colors.BLACK),
                        passport_number,
                        Ticket,
                        ticket_id_delete,
                        ft.OutlinedButton("Відмінити бронювання", on_click=DeleteTikets, icon=ft.icons.DELETE_FOREVER_ROUNDED,
                                          icon_color="pink600",height=40),
                        DeleteTiketstext,
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main,)
