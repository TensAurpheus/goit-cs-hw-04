from threading import Thread, Semaphore
from pathlib import Path
from collections import defaultdict
from time import time

def search_in_file(file_path, keywords, results, semaphore):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    with semaphore:
                        results[keyword].append(file_path.as_posix())
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")

if __name__ == '__main__':
    start_time = time()
    file_paths = list(Path("./text").rglob("*.txt"))
    keywords = ["man", "both"]
    results = defaultdict(list)
    semaphore = Semaphore(5)  # Specify the number of allowed concurrent threads

    threads = []
    for file_path in file_paths:
        thread = Thread(target=search_in_file, args=(file_path, keywords, results, semaphore))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    final_results = dict(results)
    print(final_results)
    print(f"Time taken: {time() - start_time} seconds")