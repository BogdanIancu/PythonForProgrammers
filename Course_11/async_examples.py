import asyncio
import aiohttp
import datetime
import requests


async def greet(name):
    print(f"Hello, {name}!")
    await asyncio.sleep(1)  # Simulating an asynchronous operation
    print(f"Goodbye, {name}!")


async def main():
    print("Starting...")
    await asyncio.gather(
        greet("Alice"),
        greet("Bob"),
        greet("Charlie")
    )
    print("All done!")


asyncio.run(main())


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def scrape_websites():
    start = datetime.datetime.now()
    websites = ["http://google.com", "http://google.ro", "http://google.it", "http://google.fr"]
    tasks = []
    for website in websites:
        tasks.append(asyncio.create_task(fetch(website)))

    responses = await asyncio.gather(*tasks)
    for website, response in zip(websites, responses):
        print(f"Scraped {website}: {len(response)} characters")
    end = datetime.datetime.now()
    result = end-start
    print("Async: ", result)

asyncio.run(scrape_websites())


def scrape_synchronously():
    start = datetime.datetime.now()
    websites = ["http://google.com", "http://google.ro", "http://google.it", "http://google.fr"]
    for w in websites:
        response = requests.get(w)
        print(f"Scraped {w}: {len(response.text)} characters")
    end = datetime.datetime.now()
    result = end - start
    print("Sync: ", result)


scrape_synchronously()
