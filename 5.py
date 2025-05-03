import asyncio

COEFF = 1000


async def growing(name, time_for_soaking, time_for_germinate, time):
    print(f"0 Beginning of sowing the {name} plant")
    print(f"1 Soaking of the {name} started")
    await asyncio.sleep(time_for_soaking / COEFF)
    print(f"2 Soaking of the {name} is finished")
    print(f"7 Application of fertilizers for {name}")
    await asyncio.sleep(3 / COEFF)
    print(f"7 Fertilizers for the {name} have been introduced")
    print(f"8 Treatment of {name} from pests")
    await asyncio.sleep(5 / COEFF)
    print(f"8 The {name} is treated from pests")
    print(f"3 Shelter of the {name} is supplied")
    await asyncio.sleep(time_for_germinate / COEFF)
    print(f"4 Shelter of the {name} is removed")
    print(f"5 The {name} has been transplanted")
    await asyncio.sleep(time / COEFF)
    print(f"6 The {name} has taken root")
    print(f"9 The seedlings of the {name} are ready")


async def sowing(*vegetables):
    tasks = []
    for vegetable in vegetables:
        tasks.append(asyncio.create_task(growing(*vegetable)))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    data = [('carrot', 7, 18, 2), ('cabbage', 2, 6, 10), ('onion', 5, 12, 7)]
    asyncio.run(sowing(*data))
