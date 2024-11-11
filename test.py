from os import path


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
