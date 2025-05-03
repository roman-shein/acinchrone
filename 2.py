import os
import time
import asyncio


async def do_task(name, time_for_prep_1, time_for_def_1, time_for_prep_2, time_for_def_2):
    print(f"{name} started the 1 task.")
    await asyncio.sleep(0.01)
    print(f"{name} started the 2 task.")
    await asyncio.sleep(time_for_prep_1 / 100)
    print(f"{name} moved on to the defense of the 1 task.")
    await asyncio.sleep(time_for_def_1 / 100)
    print(f"{name} completed the 1 task.")
    await asyncio.sleep(time_for_prep_2 / 100)
    print(f"{name} moved on to the defense of the 2 task.")
    await asyncio.sleep(time_for_def_2 / 100)
    print(f"{name} completed the 2 task.")


async def interviews_2(*peoples):
    tasks = []
    for people in peoples:
        tasks.append(do_task(*people))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
    t0 = time.time()
    asyncio.run(interviews_2(*data))
    print(time.time() - t0)
