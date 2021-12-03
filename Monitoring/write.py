import time

with open('pipe.txt', 'w', encoding='utf-8') as f:
    i = 0
    while True:
        try:
            f.write(f'{i}')
            f.flush()
            print(f'I wrote {i}')
            time.sleep(2)
            i += 1
        except KeyboardInterrupt:
            break
