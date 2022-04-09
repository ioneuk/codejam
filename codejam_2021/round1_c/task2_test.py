import random
import task2_naive as ex
import task2 as act

if __name__ == "__main__":
    while True:
        year = random.randint(1, 100000)
        expected = ex.find_roaring(str(year))
        actual = act.find_roaring(str(year))

        if expected != actual:
            print(f"Initial year: {year}")
            print(f"Expected year: {expected}")
            print(f"Actual year: {actual}")
            raise Exception("ex")