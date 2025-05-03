import asyncio

COEFF = 1


async def sowing(*vegetables):
    for vegetable in vegetables:
        pass


if __name__ == "__main__":
    data = [('carrot', 7, 18, 2), ('cabbage', 2, 6, 10), ('onion', 5, 12, 7)]
    asyncio.run(sowing(*data))
