import re

def count_occurrences(database_file, query_file, output_file):
    with open(database_file, 'r') as file:
        database = file.read()

    with open(query_file, 'r') as file:
        queries = file.read().splitlines()

    with open(output_file, 'w') as file:
        for query in queries:
            pattern = re.compile(re.escape(query))
            occurrences = len(pattern.findall(database))
            file.write(f"{query} {occurrences}\n")

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
