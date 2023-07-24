import asyncio
import aiohttp
import time
import decimal


# Корутина для піднесення у степінь
async def power(base, exponent):
    return decimal.Decimal(base) ** exponent


async def calculate_power(number, exponent):
    start_time = time.time()
    result = await power(number, exponent)
    end_time = time.time()
    print(f"Number: {number}, Execution Time: {end_time - start_time} seconds")


async def main():
    numbers = [2, 3, 5]
    exponent = 1000000

    start_time = time.time()
    tasks = [calculate_power(number, exponent) for number in numbers]
    await asyncio.gather(*tasks)
    end_time = time.time()

    print(f"Async Total Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    decimal.getcontext().prec = 4300
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


# Асинхронна функція для отримання відповіді з URL
async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response


# Корутина для синхронних запитів
async def synchronous_request(url, num_requests):
    for _ in range(num_requests):
        response = await fetch_url(url)
        print(f"Synchronous - URL: {url}, Status Code: {response.status}")


# Корутина для багатопоточних запитів
async def threaded_request(url, num_requests):
    tasks = [fetch_url(url) for _ in range(num_requests)]
    responses = await asyncio.gather(*tasks)
    for response in responses:
        print(f"Threaded - URL: {url}, Status Code: {response.status}")


# Корутина для багатопроцесорних запитів
async def process_request(url, num_requests):
    tasks = [fetch_url(url) for _ in range(num_requests)]
    responses = await asyncio.gather(*tasks)
    for response in responses:
        print(f"Multiprocessing - URL: {url}, Status Code: {response.status}")


if __name__ == "__main__":
    urls = ["https://google.com", "https://amazon.com", "https://microsoft.com"]
    num_requests_per_site = 5

    # асинхронні запити
    async def main():
        start_time = time.time()
        await asyncio.gather(
            synchronous_request(urls[0], num_requests_per_site),
            threaded_request(urls[1], num_requests_per_site),
            process_request(urls[2], num_requests_per_site)
        )
        end_time = time.time()
        print(f"Async execution time: {end_time - start_time} seconds")

    asyncio.run(main())
