from os import path


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


class Test:
    _test_path = "tests"
    _file_name = "test"

    def __init__(self, run) -> None:
        self.__run = run

    def run(self) -> None:
        iter = 0

        while True:
            file_in = path.join(
                self._test_path,
                f"{self._file_name}.{iter}.in",
            )
            file_out = path.join(
                self._test_path,
                f"{self._file_name}.{iter}.out",
            )
            if not path.exists(file_in) or not path.exists(file_out):
                return

            with open(file_in, "r") as f:
                in_ = f.read().strip()
            with open(file_out, "r") as f:
                out_ = f.read().strip()

            result = self.__run(in_)

            if result == out_:
                print(f"Тест {iter} ОК: {result}")
            else:
                print(f"Тест {iter} ошибка: {result} ожидалось: {out_}")

            iter += 1


Test(Solver().run).run()
