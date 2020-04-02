import mysql.connector as mariadb
from datetime import datetime
from datetime import date
#import pytz

DB_DATABASE = "ChallanMasterDatabase"



def connect_databse():
    
    '''This will create the connection to database''' 

    try:
        connection = mariadb.connect(user = "root" , host = " localhost", password= "")
        cursor = connection.cursor()
        
    except Exception as err:

        cursor = connection = None
        print("error while connecting the database : {0}".format(err))


def create_database():
    connection = None
    cursor = None

    try:
        status = True
        connection = mariadb.connect(user = "root" , host = " localhost", password= "") 
        cursor = connection.cursor()

        ''' Create database Challan '''

        sql_command = "CREATE DATABASE IF NOT EXISTS {0}".format(DB_DATABASE)

        cursor.execute(sql_command)

    except Exception as err:    
        print("ERROR {0}".format(err))
        status = False
    finally:
        if connection is not None:
            cursor.close()
            connection.close()
        return status


def init_db():

    ''' This function will initilize the database i.e will create the tables '''

    connection = None
    try:
        # Create the database
        database_status = create_database()

        if database_status:
            cursor, connection = connect_databse()

            cursor.execute(''' CREATE TABLE IF NOT EXISTS Challans(
                               Ticket_Number INTEGER PRIMARY KEY AUTO_INCREMENT, 
                               Date TEXT NOT_NULL,
                               Time TEXT NOT_NULL,
                               Vehicle_Number TEXT NOT_NULL)

                           ''')

            connection.commit()
    except Exception as err:
        print("DB error {0}".format(err))   


    finally:
        if connection is not None:
            cursor.close()
            connection.close()
    return                 

def addChallan(Date, Time, Vehicle_Number):


    ''' This function will add challan's information '''


    status = message = " Success"

    try:
        sql_query = "INSERT INTO Challans (Date, Time, Vehicle_Number) VALUES ('{0}', '{1}', '{2}',)".format(Date, 
        Time, Vehicle_Number)

        cursor, connection = connect_databse()

        cursor.execute(sql_query)
        connection.commit()
    except Exception as err:
        print("database error {0}".format(err))    
    finally:

        if cursor is not None:
            cursor.close()
            connection.close()
    return status, message


def updateChallans(Ticket_Number, Date, Time, Vehicle_Number):

    ''' This function will update the subnet information '''

    status = message = "success"

    try:

        sql_query = " UPDATE Challans SET Date = '{0}', Time = '{1}', Vehicle_number = '{2} WHERE Ticket_Number =  '{3}'".format(Date,Time, Vehicle_Number, Ticket_Number)
        cursor, connection = connect_databse()
        cursor.execute(sql_query)
        connection.commit()
    except Exception as err:
        print("database error {0}".format(err))
        status = "Fail"
        message = "Database update error {0}".format(err)
    finally:
        if connection is not None:
            cursor.close()
            connection.close()

    return status,  message  


'''
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)


tz_ND = pytz.timezone('India/Kolkata')

newDelhi = datetime.now(tz_ND)
print("New Delhi Time: ", datetime_Kolkata.strftime("%H:%M:%S"))

'''

#datetime_object = datetime.datetime.now()  # To print current date and time





# To capture current date

date = date.today()

# dd-Month-YY 
d1 = date.strftime("%d-%B-%Y")
print("Today's date:", d1)


# current time 

now = datetime.now()

time = now.strftime("%I:%M:%p")

print("Current time is:", time)

