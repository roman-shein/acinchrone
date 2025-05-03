import asyncio
from PIL import Image

roman_num = {1: "I", 2: "II", 3: "III", 4: "IV"}


async def processing_image(filename):
    print(f"Start {filename}")
    im = Image.open(filename)
    pixels = im.load()
    x, y = im.size
    summa = 0
    for i in range(x):
        for j in range(y):
            summa += sum(pixels[i, j])
    av = summa / x / y
    d = {}
    for i in range(x):
        for j in range(y):
            if sum(pixels[i, j]) > av:
                d[pixels[i, j]] = d.get(pixels[i, j], 0) + 1
    percent = int(max(d.values()) / x / y * 100000)
    print(f"Done {filename}, percent {int(percent)}")
    # print(int(percent))
    amount = int(sum(list(d.values())) / x / y * 100)
    print(f"Done {filename}, amount {int(amount)}")
    # print(int(amount))
    arr = [(range(x // 2, x), range(y // 2)),
           (range(x // 2), range(y // 2)),
           (range(x // 2), range(y // 2, y)),
           (range(x // 2, x), range(y // 2, y))]
    res = {}
    for index, spans in enumerate(arr):
        for i in spans[0]:
            for j in spans[1]:
                if sum(pixels[i, j]) > av:
                    res[index + 1] = res.get(index + 1, 0) + 1
    max_c = 0
    ans = 0
    for key, val in res.items():
        if val > max_c:
            max_c = val
            ans = key
    print(f"Done {filename}, quarter {roman_num[ans]}")
    print(f"Ready {filename}")
    # print(roman_num[ans])
    return filename, percent, amount, roman_num[ans]


async def asteroids(*names_of_files):
    tasks = []
    res = []
    for el in names_of_files:
        tasks.append(processing_image(el))
    for future in asyncio.as_completed(tasks):
        ans = await future
        res.append(ans)
    return res


if __name__ == "__main__":
    data = ['1.jpg']
    print(asyncio.run(asteroids(*data)))
