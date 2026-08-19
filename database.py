import mysql.connector


# ==========================================
# DATABASE CONNECTION
# ==========================================

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="qr_safety_checker"
    )

    print("Database connected successfully!")

except mysql.connector.Error as error:
    print("Database connection failed!")
    print(error)


# ==========================================
# SAVE SCAN
# ==========================================

def save_scan(url, score, status):
    try:
        cursor = db.cursor()

        query = """
        INSERT INTO scans (url, score, status)
        VALUES (%s, %s, %s)
        """

        values = (url, score, status)

        cursor.execute(query, values)
        db.commit()

        print("Scan saved successfully!")

        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to save scan!")
        print(error)


# ==========================================
# GET SCAN HISTORY
# ==========================================

def get_scan_history():
    try:
        cursor = db.cursor()

        query = """
        SELECT id, url, score, status, scan_date
        FROM scans
        ORDER BY scan_date DESC
        """

        cursor.execute(query)

        records = cursor.fetchall()

        print("\n--- SCAN HISTORY ---")

        for record in records:
            print(record)

        cursor.close()

        return records

    except mysql.connector.Error as error:
        print("Failed to retrieve scan history!")
        print(error)
        return []


# ==========================================
# GET BLACKLIST
# ==========================================

def get_blacklist():
    try:
        cursor = db.cursor()

        query = """
        SELECT domain, reason
        FROM blacklist
        """

        cursor.execute(query)

        records = cursor.fetchall()

        print("\n--- BLACKLIST ---")

        for record in records:
            print(record)

        cursor.close()

        return records

    except mysql.connector.Error as error:
        print("Failed to retrieve blacklist!")
        print(error)
        return []


# ==========================================
# GET WHITELIST
# ==========================================

def get_whitelist():
    try:
        cursor = db.cursor()

        query = """
        SELECT domain
        FROM whitelist
        """

        cursor.execute(query)

        records = cursor.fetchall()

        print("\n--- WHITELIST ---")

        for record in records:
            print(record)

        cursor.close()

        return records

    except mysql.connector.Error as error:
        print("Failed to retrieve whitelist!")
        print(error)
        return []


# ==========================================
# ADD USER
# ==========================================

def add_user(name, email):
    try:
        cursor = db.cursor()

        query = """
        INSERT INTO users (name, email)
        VALUES (%s, %s)
        """

        values = (name, email)

        cursor.execute(query, values)
        db.commit()

        print("User added successfully!")

        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to add user!")
        print(error)


# ==========================================
# GET USERS
# ==========================================

def get_users():
    try:
        cursor = db.cursor()

        query = """
        SELECT id, name, email
        FROM users
        """

        cursor.execute(query)

        records = cursor.fetchall()

        print("\n--- USERS ---")

        for record in records:
            print(record)

        cursor.close()

        return records

    except mysql.connector.Error as error:
        print("Failed to retrieve users!")
        print(error)
        return []


# ==========================================
# TEST USER FUNCTIONS
# ==========================================

