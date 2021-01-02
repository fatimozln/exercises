import time

key = "mohsen"


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))


C = 0
while True:
    C += 1
    start_time = time.time()
    name = input("Please type {} as soon as possible =\n".format(key))
    low_name = name.lower()
    if low_name == key:
        print("You succeeded in attempt :", C)
        end_time = time.time()
        break
    else:
        print("Does not match the input text")

end_time = time.time()
time_lapsed = int(end_time - start_time)
time_convert(time_lapsed)
