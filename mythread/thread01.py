import threading
from time import sleep


def work(total_repos):
    print("run--{}---{}".format(threading.currentThread().getName(), total_repos))


def main():
    global total_repos
    total_repos = []
    # 循环所有的project id
    for i in range(1000):
        # 获取所有tag超过30的repos
        repos = "1"
        total_repos.extend(repos)

    threads = [threading.Thread(target=work, args=[total_repos],name="work-{}".format(i)) for i in range(10)]
    [x.start() for x in threads]
    for y in threads:
        y.join()


if __name__== "__main__":
    print("thread test work")
    main()
