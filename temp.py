import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('railway.db')
cursor = conn.cursor()

# Create table to store train details
cursor.execute('''
    CREATE TABLE IF NOT EXISTS trains (
        train_id INTEGER PRIMARY KEY,
        train_name TEXT NOT NULL,
        source TEXT NOT NULL,
        destination TEXT NOT NULL,
        departure_time TEXT NOT NULL,
        arrival_time TEXT NOT NULL
    )
''')

# Function to add a new train
def add_train(train_name, source, destination, departure_time, arrival_time):
    cursor.execute('''
        INSERT INTO trains (train_name, source, destination, departure_time, arrival_time)
        VALUES (?, ?, ?, ?, ?)
    ''', (train_name, source, destination, departure_time, arrival_time))
    conn.commit()
    print("Train added successfully!")

# Function to display all trains
def display_trains():
    cursor.execute('''SELECT * FROM trains''')
    trains = cursor.fetchall()
    if len(trains) > 0:
        for train in trains:
            print(train)
    else:
        print("No trains available.")

# Main function
if __name__ == "__main__":
    while True:
        print("\nRailway Management System")
        print("1. Add Train")
        print("2. Display Trains")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            train_name = input("Enter train name: ")
            source = input("Enter source: ")
            destination = input("Enter destination: ")
            departure_time = input("Enter departure time: ")
            arrival_time = input("Enter arrival time: ")
            add_train(train_name, source, destination, departure_time, arrival_time)
        elif choice == 2:
            display_trains()
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
