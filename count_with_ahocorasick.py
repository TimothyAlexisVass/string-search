import ahocorasick
from collections import Counter

# Function to build an Aho-Corasick automaton with a set of keywords.
def build_automaton(keywords):
    A = ahocorasick.Automaton()

    # Add each keyword to the automaton with its corresponding index and value.
    for idx, key in enumerate(keywords):
        A.add_word(key, (idx, key))

    # Make the automaton ready for matching.
    A.make_automaton()

    return A

# Function to count occurrences of keywords in a database and save results to an output file.
def count_occurrences(database_file, query_file, output_file):
    with open(database_file, "r") as file:
        database = file.read()

    with open(query_file, "r") as file:
        queries = file.read().splitlines()

    # Build an Aho-Corasick automaton using the list of queries.
    automaton = build_automaton(queries)

    query_occurrences = {query: 0 for query in queries}

    # Iterate over matches found by the Aho-Corasick automaton in the database.
    for _, keyword in automaton.iter(database):
        query_occurrences[keyword[1]] += 1

    with open(output_file, "w") as file:
        for query, count in query_occurrences.items():
            file.write(f"{query} {count}\n")

# Entry point of the script.
if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) != 4:
        print(f"Usage: python {os.path.basename(__file__)} <database_file> <query_file> <output_file>")
        sys.exit(1)

    database_file = sys.argv[1]
    query_file = sys.argv[2]
    output_file = sys.argv[3]

    count_occurrences(database_file, query_file, output_file)
