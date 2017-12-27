from Connection import Connection
from RipLib import User, Hotel, Booking

con = Connection("dbuser", "123", "rip_course_db")

with con:
    users = User.load_users(con)
    for user in users:
        print(user.first_name, user.last_name, user.phone)

#with con:
    #user = User(con, 'Иван', 'Иванов')
    #user.save()
