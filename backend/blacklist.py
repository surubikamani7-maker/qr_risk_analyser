from database import db


def is_blacklisted(domain):
    cursor = db.cursor(buffered=True)

    query = "SELECT domain, reason FROM blacklist WHERE domain = %s"
    cursor.execute(query, (domain,))

    result = cursor.fetchone()

    cursor.close()

    if result:
        return {
            "blacklisted": True,
            "domain": result[0],
            "reason": result[1]
        }

    return {
        "blacklisted": False,
        "domain": domain,
        "reason": None
    }

if __name__ == "__main__":
    domain = input("Enter domain to check: ")

    result = is_blacklisted(domain)

    print(result)
