#include <Python.h>

static PyObject* calculator_add(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }
    return PyLong_FromLong(a + b);
}

static PyObject* calculator_sub(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }
    return PyLong_FromLong(a - b);
}

static PyObject* calculator_mul(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }
    return PyLong_FromLong(a * b);
}

static PyObject* calculator_div(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }
    if (b == 0) {
        PyErr_SetString(PyExc_ZeroDivisionError, "Cannot divide by zero");
        return NULL;
    }
    return PyLong_FromLong(a / b);
}

static PyMethodDef CalculatorMethods[] = {
    {"add", calculator_add, METH_VARARGS, "Add two integers"},
    {"sub", calculator_sub, METH_VARARGS, "Subtract two integers"},
    {"mul", calculator_mul, METH_VARARGS, "Multiply two integers"},
    {"div", calculator_div, METH_VARARGS, "Divide two integers"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef calculator_module = {
    PyModuleDef_HEAD_INIT,
    "calculator",
    "A simple calculator module",
    -1,
    CalculatorMethods
};

PyMODINIT_FUNC PyInit_calculator(void) {
    return PyModule_Create(&calculator_module);
}
