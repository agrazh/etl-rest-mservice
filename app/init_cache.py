import sqlite3

def init_cache():
    connection = sqlite3.connect('cache.db')
    cursor = connection.cursor()

    create_table = "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, \
        username TEXT, password TEXT)"
    cursor.execute(create_table)

    query = "INSERT INTO user VALUES (NULL, ?, ?)"
    cursor.execute(query, ("client", "client"))

    create_table = "CREATE TABLE IF NOT EXISTS queue (id INTEGER PRIMARY KEY, \
        name TEXT)"
    cursor.execute(create_table)

    create_table = "CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY, \
        name TEXT, priority INTEGER, queue_id INTEGER, \
        FOREIGN KEY(queue_id) REFERENCES queue(id))"
    cursor.execute(create_table)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    init_cache()
