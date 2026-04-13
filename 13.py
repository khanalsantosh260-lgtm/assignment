from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

DB_CONFIG = {
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'flight_game',
    'user': 'root',
    'password': 'root123'
}

# 1️⃣ Prime number
def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route("/prime_number/<int:number>", methods=["GET"])
def prime_number(number):
    return jsonify({
        "Number": number,
        "isPrime": check_prime(number)
    })


# 2️⃣ Airport
def get_airport_by_icao(icao_code):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)

    sql = """
    SELECT ident, name, municipality
    FROM airport
    WHERE ident = %s
    """
    cursor.execute(sql, (icao_code.upper(),))
    result = cursor.fetchone()

    cursor.close()
    conn.close()
    return result

@app.route("/airport/<icao>", methods=["GET"])
def airport_info(icao):
    airport = get_airport_by_icao(icao)

    if airport:
        return jsonify({
            "ICAO": airport["ident"],
            "Name": airport["name"],
            "Location": airport["municipality"]
        })
    else:
        return jsonify({"error": "Airport not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)