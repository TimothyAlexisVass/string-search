import subprocess
import shutil
import time
import sys
import os

# Function to run a given script multiple times and calculate the average runtime
def run_script(script_name, input_file, query_file, output_file, number_of_tests=100):
    runtimes = []

    python_command = 'python3' if shutil.which('python3') else 'python'

    for _ in range(number_of_tests):
        start_time = time.time()
        subprocess.run([python_command, script_name, input_file, query_file, output_file])
        runtimes.append(time.time() - start_time)

    return sum(runtimes) / number_of_tests

# Main entry point of the script
if __name__ == "__main__":
    this_file = os.path.basename(__file__)

    if len(sys.argv) != 4:
        print(f"Usage: python3 {this_file} <number_of_tests> <input_file> <query_file>")
        sys.exit(1)

    number_of_tests = int(sys.argv[1])
    input_file = sys.argv[2]
    query_file = sys.argv[3]

    # Get a list of all .py files in the current folder except for this one
    py_files = [os.path.splitext(f)[0] for f in os.listdir() if f.endswith(".py") and f != this_file]

    print(f"Running {number_of_tests} tests each for comparing runtimes.")

    result_dict = {}

    # Loop through each script file and run the test
    for script_name in py_files:
        output_file = f"{script_name.replace('count_with', 'output')}.txt"

        # Run the script and store the average runtime in the dictionary
        result_dict[script_name] = run_script(
            f"{script_name}.py",
            input_file,
            query_file,
            output_file,
            number_of_tests
        )

    # Print the results in sorted order
    print(f"Average runtime for {number_of_tests} tests")
    for file, avg_runtime in sorted(result_dict.items(), key=lambda item: item[1]):
        print(f"{file}: {round(avg_runtime * 1000, 1)} ms")
