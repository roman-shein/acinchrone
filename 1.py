import os
import time
import asyncio


async def do_task(name, time_for_prep_1, time_for_def_1, time_for_prep_2, time_for_def_2):
    print(f"{name} started the 1 task.")
    await asyncio.sleep(time_for_prep_1 / 100)
    print(f"{name} moved on to the defense of the 1 task.")
    await asyncio.sleep(time_for_def_1 / 100)
    print(f"{name} completed the 1 task.")
    print(f"{name} is resting.")
    await asyncio.sleep(5 / 100)
    print(f"{name} started the 2 task.")
    await asyncio.sleep(time_for_prep_2 / 100)
    print(f"{name} moved on to the defense of the 2 task.")
    await asyncio.sleep(time_for_def_2 / 100)
    print(f"{name} completed the 2 task.")


async def interviews(*peoples):
    # tasks = [[*people] for people in peoples]
    tasks = [asyncio.create_task(do_task(*people)) for people in peoples]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
    t0 = time.time()
    asyncio.run(interviews(*data))
    print(time.time() - t0)
