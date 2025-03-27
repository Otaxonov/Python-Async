from time import perf_counter, sleep

def write():
    print('Hey')
    sleep(1)
    print('there')

def main():
    for _ in range(5):
        write()

if __name__ == '__main__':

    start = perf_counter()
    main()
    end = perf_counter()

    elapsed = end - start
    print(f'Executed in {elapsed:.2f} seconds.')
