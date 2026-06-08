from database import engine


try:
    connection = engine.connect()
    print("Databse Connected Succesfully")
    connection.close()
except Exception as e:
    print("Connection failed", e)
