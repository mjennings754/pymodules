import random
import time
import sys
random_code = ["_def_CODE(x)_cls_print(e3f)", "print(test_case_complete)", "progress=x100", "def_call_number_to_backend(32019)"]
cols = 40
rows = 20
delay = 0.1

def clear_screen():
    sys.stdout.write("\033[2J\033[H]")
    sys.stdout.flush()

try:
    while True:
        clear_screen()
        for _ in range(rows):
            line = " ".join(random.choice(random_code) for _ in range(cols))
            print(line)
        time.sleep(delay)

except KeyboardInterrupt:
    print("Stopped")