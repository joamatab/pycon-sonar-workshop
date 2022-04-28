import sqlite3


def main():
    connection = sqlite3.connect("database.db")

    with open("pokedex/schema.sql") as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    with open("pokemon.txt") as file:
        lines = file.readlines()
        for pokemon_number, line in enumerate(lines, start=1):
            name, description = line.split(";")
            cur.execute(
                f"INSERT INTO POKEDEX (id, pokemon_name, image_url, description) VALUES ("
                f"{pokemon_number}, "
                f'"{name}", '
                f'"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_number}.png", '
                f'"{description}")'
            )
    cur.execute('INSERT INTO SUBSCRIBERS (id, email) VALUES (1, "subscriber1@example.com")')
    cur.execute('INSERT INTO SUBSCRIBERS (id, email) VALUES (2, "subscriber2@example.com")')

    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
