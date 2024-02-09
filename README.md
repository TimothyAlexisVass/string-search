# Keyword Occurrence Counting Project

This project provides different implementations for counting the occurrences of keywords in a given database using various algorithms. The primary goal is to compare the runtime performance of different approaches.

## Notes

- Ensure that Python 3 is installed on your system.
- Provide the required command-line arguments for each script as mentioned in the usage sections.

Feel free to explore and analyze the differences in runtime performance among the implemented algorithms.

## Quick start

- Clone this project
- Run `python compare_runtimes.py 100 input.txt query.txt`
- You will get 4 output files, one for each string searching method.
- You will also be presented with a comparison of the average runtimes for 100 tests using the specified input and query files.

## Table of Contents

- `compare_runtimes.py`
- `count_with_trie.py`
- `count_with_ahocorasick.py`
- `count_with_pycount.py`
- `count_with_regex.py`

### `compare_runtimes.py`

Compares the runtime performance of the different implementations by running each script multiple times. It calculates the average runtime for a specified number of tests and presents the results in sorted order.

#### Usage

```bash
python compare_runtimes.py <number_of_tests> <input_file> <query_file>
```

### `count_with_trie.py`

Implements the Aho-Corasick algorithm using a Trie data structure. The script builds the Trie, establishes failure links, and then searches for keyword occurrences in a given database.

#### Usage

```bash
python count_with_trie.py <input_file> <query_file> <output_file>
```

### `count_with_ahocorasick.py`

Utilizes the Aho-Corasick algorithm through the `ahocorasick` library. It builds an automaton for keyword matching and counts occurrences in the provided database.

#### Usage

```bash
python count_with_ahocorasick.py <input_file> <query_file> <output_file>
```

### `count_with_pycount.py`

Provides a simple approach using Python's built-in `str.count()` method. It directly counts occurrences of each keyword in the database.

#### Usage

```bash
python count_with_pycount.py <input_file> <query_file> <output_file>
```

### `count_with_regex.py`

Uses regular expressions to count occurrences of keywords in the database.

#### Usage

```bash
python count_with_regex.py <input_file> <query_file> <output_file>
```
