import os
import sys

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '../')
sys.path.append(mymodule_dir)

import unittest
from model import CalcModelMVP


class TestCalcModelMVP(unittest.TestCase):
    def setUp(self):
        self.controller = CalcModelMVP()

    def test_0(self):
        self.controller.set_expression("5+-1)", 0)
        self.controller.calculate()
        self.assertEqual(self.controller.get_status(), "err")

    def test_1(self):
        self.controller.set_expression("sqrt(16)+sin(1)", 0)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), 4.841470984807897, places=6)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_2(self):
        self.controller.set_expression("2^(2^(2^2))", 0)
        self.controller.calculate()
        self.assertEqual(self.controller.get_result(), 65536)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_3(self):
        self.controller.set_expression("log(25)-acos(0.45)", 0)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), 0.293909, places=6)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_4(self):
        self.controller.set_expression("(4*sin(2.9)+3*cos(0.47))/4", 0)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), 0.907926, places=6)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_5(self):
        expressions_results = [
            ("log(50)", 1.69897),
            ("acos(0.35)", 1.213225),
            ("atan(1.1)", 0.832981),
            ("sqrt(64)", 8.0)
        ]
        for exp, result in expressions_results:
            with self.subTest(exp=exp):
                self.controller.set_expression(exp, 0)
                self.controller.calculate()
                self.assertAlmostEqual(self.controller.get_result(), result, places=6)
                self.assertEqual(self.controller.get_status(), "ok")

    def test_6(self):
        self.controller.set_expression("log(50)/acos(0.35)*atan(1.1)*sqrt(64)", 0)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), 9.3318876, places=6)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_7(self):
        expression = "(sin(1.4)*cos(0.85)/tan(0.68))/(asin(0.38)/2*acos(0.45)^3-atan(0.54)*sqrt(49))+ln(5)*log(100)"
        self.controller.set_expression(expression, 0)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), 2.967829, places=6)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_8(self):
        expression = "acos(0.25)^ln(2)-atan(1.5)*sqrt(16)*log(10)*sin(2.5)/(cos(1.1)/tan(1.9)*asin(0.4))"
        self.controller.set_expression(expression, 0)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), 38.104222613215, places=6)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_9(self):
        expression = "((sin(1.7)*acos(0.3)-atan(0.35)*tan(1.5))^2)/sqrt(9)*(ln(7)+log(1000)/acos(0.6))"
        self.controller.set_expression(expression, 0)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), 21.0601731, places=6)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_10(self):
        expression = "atan(0.75)*log(10)+sqrt(64)*sin(2)-cos(0.576)/acos(0.78)/5-2*ln(3)*asin(0.29)*tan(1.05)"
        self.controller.set_expression(expression, 0)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), 6.5427849584, places=6)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_11(self):
        expression = "(cos(2.1)^2*sin(1.2)*atan(0.85)+acos(0.4))/log(250)*sqrt(169)+ln(5)*asin(0.55)*tan(0.5)"
        self.controller.set_expression(expression, 0)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), 7.70412863, places=6)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_12(self):
        expression = "(sin(0.93)+acos(0.71)/atan(1.37)*tan(1.8))/(sqrt(25)*ln(10)*acos(0.3)-asin(0.6)*cos(1.1))"
        self.controller.set_expression(expression, 0)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), -0.193212471, places=6)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_13(self):
        expression = "sin(cos(tan(ln(log(1234)+1)*2)/3)-4)"
        self.controller.set_expression(expression, 0)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), -0.134926396, places=6)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_14(self):
        expression = "(sin(0.93)+acos(0.71)/atan(1.37)*tan(1.8))/(sqrt(25)*ln(10)*acos(0.3)-asin(0.6)*cos(1.1))-sin(cos(tan(ln(log((cos(2.1)^2*sin(1.2)*atan(0.85)+acos(0.4))/log(250)*sqrt(169)+ln(5)*asin(0.55)*tan(0.5))+1)*2)/3)-4)"
        self.controller.set_expression(expression, 0)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), -0.565264615, places=6)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_15(self):
        self.controller.set_expression("1/0", 0)
        self.controller.calculate()
        self.assertEqual(self.controller.get_status(), "err")

    def test_16(self):
        self.controller.set_expression("sqrt(-16)", 0)
        self.controller.calculate()
        self.assertEqual(self.controller.get_status(), "err")

    def test_17(self):
        self.controller.set_expression("654+", 0)
        self.controller.calculate()
        self.assertEqual(self.controller.get_result(), 654)
        self.assertEqual(self.controller.get_status(), "err")

    def test_18(self):
        self.controller.set_expression("(5+", 0)
        self.controller.calculate()
        self.assertEqual(self.controller.get_status(), "err")

    def test_19(self):
        self.controller.set_expression("sin(x)", 1)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), 0.841471, places=6)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_20(self):
        self.controller.set_expression("=1e+06", 0)
        self.controller.calculate()
        self.assertEqual(self.controller.get_status(), "err")

    def test_21(self):
        self.controller.set_expression("-3+1e+06", 0)
        self.controller.calculate()
        self.assertEqual(self.controller.get_result(), 1e+06 - 3)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_22(self):
        self.controller.set_expression("INCORRECT", 0)
        self.controller.calculate()
        self.assertEqual(self.controller.get_status(), "err")

    def test_23(self):
        self.controller.set_expression("1e+999", 0)
        self.controller.calculate()
        self.assertEqual(self.controller.get_status(), "err")

    def test_24(self):
        self.controller.set_expression("1e-900", 0)
        self.controller.calculate()
        self.assertEqual(self.controller.get_status(), "err")

    def test_25(self):
        self.controller.set_expression("-1-(-1-(-1-(-2-1)))", 0)
        self.controller.calculate()
        self.assertEqual(self.controller.get_result(), 2)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_26(self):
        self.controller.set_expression("1--1", 0)
        self.controller.calculate()
        self.assertEqual(self.controller.get_result(), 1)
        self.assertEqual(self.controller.get_status(), "err")

    def test_27(self):
        self.controller.set_expression("1-sin(1)", 0)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), 0.158529, places=6)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_28(self):
        self.controller.set_expression("cos(1)+sin(1)", 0)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), 1.381773, places=6)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_30(self):
        self.controller.set_expression("x*x", 1)
        self.controller.calculate()
        self.assertEqual(self.controller.get_result(), 1)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_31(self):
        self.controller.set_expression("x+5)", 1)
        self.controller.calculate()
        self.assertEqual(self.controller.get_status(), "err")

    def test_32(self):
        self.controller.set_expression("sin(sin(sin(5*5*5*x)))", 1)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), -0.54618912006, places=6)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_33(self):
        self.controller.set_expression("x*x-x", 2)
        self.controller.calculate()
        self.assertEqual(self.controller.get_result(), 2)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_34(self):
        self.controller.set_expression("x*x-x+x*x-x", 1)
        self.controller.calculate()
        self.assertEqual(self.controller.get_result(), 0)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_35(self):
        self.controller.set_expression("0.0000000000010000000", 0)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), 1e-12, places=13)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_37(self):
        self.controller.set_expression("asin(0.5)", 0)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), 0.523599, places=6)
        self.assertEqual(self.controller.get_status(), "ok")

    def test_39(self):
        self.controller.set_expression("log(50)+acos(0.35)", 0)
        self.controller.calculate()
        self.assertAlmostEqual(self.controller.get_result(), 2.912195, places=6)
        self.assertEqual(self.controller.get_status(), "ok")


if __name__ == '__main__':
    unittest.main()
