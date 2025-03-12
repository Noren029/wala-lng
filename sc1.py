import sqlite3
import pandas as pd

DB_FILE = "bond_movies.db"

def create_database():
    """Creates the SQLite database and movies table if it doesn't exist."""
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()
    
    create_bond_table_query = """ 
    CREATE TABLE IF NOT EXISTS movies (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Year INTEGER NOT NULL,
        Movie TEXT NOT NULL UNIQUE,
        Bond TEXT NOT NULL,
        Bond_Car_MFG TEXT,
        Depicted_Film_Loc TEXT,
        Shooting_Loc TEXT,
        BJB INTEGER CHECK(BJB IN (0, 1, 2)),
        Video_Game INTEGER CHECK(Video_Game IN (0, 1)),
        Avg_User_IMDB REAL CHECK(Avg_User_IMDB BETWEEN 0 AND 10)
    );
    """
    
    cur.execute(create_bond_table_query)
    con.commit()
    con.close()

def populate_database():
    """Populates the database with data from jamesbond.csv if empty."""
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()

    cur.execute("SELECT COUNT(*) FROM movies")
    if cur.fetchone()[0] == 0:
        bond_df = pd.read_csv('jamesbond.csv')

        for row in bond_df.itertuples(index=False):
            cur.execute("""
                INSERT INTO movies (Year, Movie, Bond, Bond_Car_MFG, Depicted_Film_Loc, Shooting_Loc, BJB, Video_Game, Avg_User_IMDB)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (row.Year, row.Movie, row.Bond, row.Bond_Car_MFG, row.Depicted_Film_Loc, row.Shooting_Loc, row.BJB, row.Video_Game, row.Avg_User_IMDB))

        con.commit()
    
    con.close()

def insert_no_time_to_die():
    """Inserts 'No Time to Die' into the database."""
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()

    no_time_to_die = (2021, "No Time to Die", "Daniel Craig", "Aston Martin", "Norway", "Italy", 1, 1, 7.3)

    try:
        cur.execute("""
            INSERT INTO movies (Year, Movie, Bond, Bond_Car_MFG, Depicted_Film_Loc, Shooting_Loc, BJB, Video_Game, Avg_User_IMDB)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, no_time_to_die)
        con.commit()
        print("No Time to Die was successfully added to the database.")
    except sqlite3.IntegrityError:
        print("No Time to Die is already in the database.")

    con.close()

def fetch_movies_formatted():
    """Fetches and displays all movies from the database in the required format."""
    con = sqlite3.connect(DB_FILE)
    df = pd.read_sql_query('SELECT * FROM movies', con)
    con.close()

    print(df.to_string(index=False))  # Print without the default Pandas index

def main():
    """Main function to execute the database operations."""
    create_database()
    populate_database()
    insert_no_time_to_die()
    fetch_movies_formatted()

if __name__ == "__main__":
    main()
