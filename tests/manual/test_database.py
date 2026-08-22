from src.db.connection import get_connection


def main():

    with get_connection() as connection:

        with connection.cursor() as cursor:

            cursor.execute("SELECT version();")

            result = cursor.fetchone()

            print("Database connection successful.")
            print(result[0])


if __name__ == "__main__":
    main()
