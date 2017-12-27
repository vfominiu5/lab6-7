class User:
    def __init__(self, db_connection, first_name, last_name, phone=None):
        self.db_connection = db_connection.connection
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO users (first_name, last_name, phone) VALUES (%s, %s, %s);",
                  (self.first_name, self.last_name, self.phone))
        self.db_connection.commit()
        c.close()

    @staticmethod
    def load_users(db_connection):
        c = db_connection.connection.cursor()
        c.execute("SELECT * FROM users")
        lines = c.fetchall()
        c.close()
        users = [User(db_connection, l[0], l[1], l[2]) for l in lines]
        return users


class Hotel:
    def __init__(self, db_connection, name, phone,adress,description=None):
        self.db_connection = db_connection.connection
        self.name = name
        self.phone = phone
        self.adress = adress
        self.description = description

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO hotels (name, phone, adress, description) VALUES (%s, %s, %s, %s);",
                  (self.name, self.phone, self.adress, self.description))
        self.db_connection.commit()
        c.close()


class Booking:
    def __init__(self, db_connection, user_id,hotel_id,price,start_date,end_date):
        self.db_connection = db_connection.connection
        self.user_id = user_id
        self.hotel_id = hotel_id
        self.price = price
        self.start_date = start_date
        self.end_date = end_date

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO bookings (user_id, hotel_id, price, start_date, end_date) VALUES (%d, %d, %d, %s, %s);",
                  (self.user_id, self.hotel_id, self.price, self.start_date, self.end_date))
        self.db_connection.commit()
        c.close()
