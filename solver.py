class Solver:
    def run(self, n_str: str) -> str:
        n_ = int(n_str)
        return str(self.tickets(n_))

    def tickets(self, n: int) -> int:
        base_array = [1] * 10

        for n_ in range(2, n + 1):
            current_length = 9 * n_ + 1
            m = [[0 for _ in range(current_length)] for _ in range(10)]

            for y in range(len(m)):
                for x in range(len(base_array)):
                    m[y][y + x] = base_array[x]

            base_array = [0] * current_length
            for x in range(current_length):
                base_array[x] = sum(m[y][x] for y in range(10))

        return sum(x**2 for x in base_array)
