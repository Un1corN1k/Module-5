import requests
import time
import threading
import multiprocessing


# Завдання 1
def synchronous_request(url, num_requests):
    for _ in range(num_requests):
        response = requests.get(url)
        print(f"Synchronous - URL: {url}, Status Code: {response.status_code}")


def threaded_request(url, num_requests):
    for _ in range(num_requests):
        response = requests.get(url)
        print(f"Threaded - URL: {url}, Status Code: {response.status_code}")


def process_request(url, num_requests):
    for _ in range(num_requests):
        response = requests.get(url)
        print(f"Multiprocessing - URL: {url}, Status Code: {response.status_code}")


if __name__ == "__main__":
    urls = ["https://google.com", "https://amazon.com", "https://microsoft.com"]
    num_requests_per_site = 5

    # синхронні
    start_time = time.time()
    for url in urls:
        synchronous_request(url, num_requests_per_site)
    end_time = time.time()
    print(f"Synchronous execution time: {end_time - start_time} seconds")

    # багатопоточні
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=threaded_request, args=(url, num_requests_per_site))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Threaded execution time: {end_time - start_time} seconds")

    # багатопроцесорні
    start_time = time.time()
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=process_request, args=(url, num_requests_per_site))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    end_time = time.time()
    print(f"Multiprocessing execution time: {end_time - start_time} seconds")


# Завдання 2
def power(base, exponent):
    return base ** exponent


if __name__ == "__main__":
    numbers = [2, 3, 5]
    exponent = 1000000

    # синхронні
    start_time = time.time()
    for number in numbers:
        result = power(number, exponent)
    end_time = time.time()
    print(f"Synchronous execution time: {end_time - start_time} seconds")

    # багатопоточні
    start_time = time.time()
    threads = []
    for number in numbers:
        thread = threading.Thread(target=power, args=(number, exponent))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Threaded execution time: {end_time - start_time} seconds")

    # багатопроцесорні
    start_time = time.time()
    processes = []
    for number in numbers:
        process = multiprocessing.Process(target=power, args=(number, exponent))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    end_time = time.time()
    print(f"Multiprocessing execution time: {end_time - start_time} seconds")
