import ctypes
import os


class CalcModelMVP:
    class CalcModel(ctypes.Structure):
        pass

    def __init__(self):
        # Загрузка динамической библиотеки
        if os.getcwd() == "/":
            os.chdir("/Applications/CalculatorApp")
        self.lib = ctypes.CDLL("libcalc.dylib")
        self.lib = os.path.join(os.path.dirname(__file__), "libcalc.dylib")
        lib_path = os.path.join(os.path.dirname(__file__), "libcalc.dylib")
        self.lib = ctypes.CDLL(lib_path)

        # Определение аргументов и возвращаемых типов для функций библиотеки
        self.lib.CalcModel_new.restype = ctypes.POINTER(self.CalcModel)
        self.lib.CalcModel_delete.argtypes = [ctypes.POINTER(self.CalcModel)]
        self.lib.CalcModel_SetInfix.argtypes = [ctypes.POINTER(self.CalcModel), ctypes.c_char_p]
        self.lib.CalcModel_SetX.argtypes = [ctypes.POINTER(self.CalcModel), ctypes.c_longdouble]
        self.lib.CalcModel_GetStatus.argtypes = [ctypes.POINTER(self.CalcModel)]
        self.lib.CalcModel_GetStatus.restype = ctypes.c_int
        self.lib.CalcModel_GetResult.argtypes = [ctypes.POINTER(self.CalcModel)]
        self.lib.CalcModel_GetResult.restype = ctypes.c_longdouble
        self.lib.CalcModel_EvalExpression.argtypes = [ctypes.POINTER(self.CalcModel)]

        # Создание экземпляра CalcModel
        self.calc_model = self.lib.CalcModel_new()

    def __del__(self):
        # Удаление экземпляра CalcModel при удалении объекта CalcModelMVP
        if self.calc_model:
            self.lib.CalcModel_delete(self.calc_model)

    def set_expression(self, infix: str, x: float) -> None:
        """Установить выражение и значение x."""
        infix_bytes = infix.encode('utf-8')
        self.lib.CalcModel_SetInfix(self.calc_model, infix_bytes)
        self.lib.CalcModel_SetX(self.calc_model, ctypes.c_longdouble(x))

    def calculate(self) -> None:
        """Выполнить вычисление выражения."""
        self.lib.CalcModel_EvalExpression(self.calc_model)

    def get_result(self) -> float:
        """Получить результат вычисления."""
        return float(self.lib.CalcModel_GetResult(self.calc_model))

    def get_status(self) -> str:
        """Получить статус вычисления."""
        status = self.lib.CalcModel_GetStatus(self.calc_model)
        return "ok" if status == 0 else "err"
