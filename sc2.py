import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_FILE = "bond_movies.db"

def get_movie_by_year():
    """Asks the user for a year and retrieves the Bond movie released that year."""
    year = input("Enter a year to search for a Bond movie: ")

    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()
    cur.execute("SELECT Year, Movie, Bond FROM movies WHERE Year = ?", (year,))
    result = cur.fetchone()
    con.close()

    if result:
        print(f"\n In {year} the movie was release and the movie tittle is {result[1]} Starring {result[2]}\n")
    else:
        print(f"\n No Bond movie was released in {year}.\n")

def plot_avg_imdb_by_car():
    """Plots the average IMDb rating for each Bond car manufacturer and prints the result in the table format."""
    con = sqlite3.connect(DB_FILE)
    df = pd.read_sql_query(''' 
        SELECT Bond_Car_MFG, COALESCE(AVG(Avg_User_IMDB), 0) as Bond_AVG
        FROM movies
        GROUP BY Bond_Car_MFG;
    ''', con)
    con.close()

    if df.empty:
        print("\n No data available for plotting.\n")
        return

    # Printing the result in the requested format
    print("-" * 35)
    print(f"{'Bond_Car_MFG':<20}{'Bond_AVG':>10}")
    print("-" * 35)
    for index, row in df.iterrows():
        print(f"{row['Bond_Car_MFG']:<20}{row['Bond_AVG']:>10.2f}")

    # Plot the graph
    df.plot(kind="bar", x="Bond_Car_MFG", y="Bond_AVG", color="pink", legend=False)
    plt.title("Average IMDb Rating by Bond Car Manufacturer")
    plt.xlabel("Bond Car Manufacturer")
    plt.ylabel("Average IMDb Rating")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

def main():
    get_movie_by_year()
    plot_avg_imdb_by_car()

if __name__ == "__main__":
    main()
