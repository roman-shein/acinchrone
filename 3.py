import os
import asyncio
import time

COEFF = 100


async def buy_gifts(name_gift, time_for_choice, time_for_buy, wait_next_gift):
    await asyncio.sleep(wait_next_gift / COEFF)
    print(f"Buy {name_gift}")
    await asyncio.sleep((time_for_choice + time_for_buy) / COEFF)
    print(f"Got {name_gift}")


async def main():
    for num, times in stops:
        tasks = []
        rem_time = times[0]
        wait_next_gift = 0
        time_for_all = 0
        while rem_time != 0:
            for name, times_for_gift in gifts:
                if sum(times_for_gift) <= rem_time:
                    # print(num, name, *times_for_gift, wait_next_gift)
                    tasks.append(buy_gifts(name, times_for_gift[0], times_for_gift[1], wait_next_gift))
                    time_for_all = max(time_for_all, times_for_gift[0] + times_for_gift[1] + wait_next_gift)
                    wait_next_gift += times_for_gift[0]
                    rem_time -= times_for_gift[0]
                    gifts.remove((name, times_for_gift))
                    break
            else:
                break
        print(f"Buying gifts at {num} stop")
        await asyncio.gather(*tasks)
        time.sleep((times[0] - time_for_all) / COEFF)
        print(f"Arrive from {num} stop")
        time.sleep(times[1] / COEFF)
    tasks = []
    wait_next_gift = 0
    for name, times_for_gift in gifts:
        tasks.append(buy_gifts(name, times_for_gift[0], times_for_gift[1], wait_next_gift))
        wait_next_gift += times_for_gift[0]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    stops = []
    stop = input()
    c = 1
    while stop != "":
        stops.append((c, list(map(int, stop.split()))))
        c += 1
        stop = input()
    gifts = []
    gift = input()
    while gift != "":
        name, time_for_choice, time_for_buy = gift.split()
        gifts.append((name, [int(time_for_choice), int(time_for_buy)]))
        gift = input()
    gifts = sorted(gifts, key=lambda x: -sum(x[1]))
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    t0 = time.time()

    asyncio.run(main())
