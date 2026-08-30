from database import db


def is_whitelisted(domain):
    cursor = db.cursor()

    query = "SELECT domain FROM whitelist WHERE domain = %s"
    cursor.execute(query, (domain,))

    result = cursor.fetchone()

    cursor.close()

    if result:
        return {
            "whitelisted": True,
            "domain": result[0]
        }

    return {
        "whitelisted": False,
        "domain": domain
    }


if __name__ == "__main__":
    domain = input("Enter domain to check: ")

    result = is_whitelisted(domain)

    print(result)