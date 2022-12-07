def day_six():
    stream = ""
    print("Day six")

    def setup():
        nonlocal stream
        with open("./6/input.txt", "r") as f:
            stream = f.readlines()[0].strip()
    
    def chunks(lst, n):
        for i in range(0, len(lst)-3):
            yield lst[i:i + n]
    
    def get_answer(chunk_size):
        nonlocal stream
        i = 0
        for chuck in chunks(stream, chunk_size):
            if len(set(chuck)) == chunk_size:
                return i + chunk_size
            i += 1


    setup()
    print(f"\tSolution 1: {get_answer(4)}")
    print(f"\tSolution 2: {get_answer(14)}")

if __name__ == "__main__":
    day_six()

