from calculator import calc

if __name__ == '__main__':
    while True:
        print(
            calc(input())
        )


"""import time
from multiprocessing import Pool

from calculator import plot, core


def video(c):
    expr, _id = c
    plot.save_plot_video(expr, f"output/{_id}.mp4")
    print(f"{_id} done")


expressions = tuple((core.parse(expression), i) for i, expression in enumerate((
    "x+y",
    "x-y",
    "x*y",
    "x/y",
    "sin xy",
    "x % y",
    "exp(x)*y")))

if __name__ == '__main__':
    starttime = time.time()
    pool = Pool()
    pool.map(video, expressions)
    pool.close()
    endtime = time.time()
    print(f"Time taken {endtime-starttime} seconds")"""
