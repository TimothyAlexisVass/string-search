# Class representing a node in the Trie data structure used in the Aho-Corasick algorithm.
class TrieNode:
    def __init__(self):
        """
        Initializes a TrieNode with the following attributes:
            - children: A dictionary to store child nodes (next characters in the trie).
            - is_end_of_word: A flag to indicate if the current node marks the end of a keyword.
            - output: A set to store the output (keywords) associated with the current node.
            - fail: A pointer to the fail node for Aho-Corasick algorithm.
        """

        self.children = {}
        self.is_end_of_word = False
        self.output = set()
        self.fail = None

# Function to build a Trie data structure from a list of keywords.
def build_trie(keywords):
    # Create the root node for the trie.
    root = TrieNode()

    # Iterate through each keyword and build the trie.
    for keyword in keywords:
        node = root
        # Traverse the trie, creating nodes for each character in the keyword.
        for char in keyword:
            node = node.children.setdefault(char, TrieNode())

        node.is_end_of_word = True
        node.output.add(keyword)

    return root

# Function to build failure links in the Trie for the Aho-Corasick algorithm.
def build_failure_links(root):
    queue = []

    for node in root.children.values():
        queue.append(node)
        node.fail = root

    # Process each node in the trie using breadth-first traversal.
    while queue:
        current_node = queue.pop(0)
        # Traverse each child of the current node.
        for char, child_node in current_node.children.items():
            queue.append(child_node)
            failure_node = current_node.fail

            # Traverse the fail link until a match is found or reach the root.
            while failure_node is not None and char not in failure_node.children:
                failure_node = failure_node.fail

            # Set the fail link of the child node.
            child_node.fail = failure_node.children[char] if failure_node else root
            # Update the output set of the child node with the output of the fail node.
            child_node.output.update(child_node.fail.output)

    return root

# Function to search for occurrences of keywords in a given text using the Aho-Corasick algorithm.
def search_occurrences(database, root, queries):
    current_node = root
    occurrences = {query: 0 for query in queries}

    # Traverse the database using the Aho-Corasick algorithm.
    for char in database:
        while current_node is not None and char not in current_node.children:
            current_node = current_node.fail

        if current_node is None:
            current_node = root
            continue

        current_node = current_node.children[char]

        # Update occurrences for each keyword associated with the current node.
        for query in current_node.output:
            occurrences[query] = occurrences.get(query, 0) + 1

    return occurrences

# Function to count occurrences of keywords in a database and save results to an output file.
def count_occurrences(database_file, query_file, output_file):
    with open(database_file, 'r') as file:
        database = file.read()

    with open(query_file, 'r') as file:
        queries = file.read().splitlines()

    # Build the trie and set failure links for the Aho-Corasick algorithm.
    root = build_trie(queries)
    root = build_failure_links(root)

    # Search for occurrences in the database using the Aho-Corasick algorithm.
    occurrences = search_occurrences(database, root, queries)

    with open(output_file, 'w') as file:
        for query, count in occurrences.items():
            file.write(f"{query} {count}\n")

# Main entry point of the script.
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
