'''
Created on May 27, 2019

@author: douglas
'''
import unittest

from calc.calculadoda import Calculadora


class TesteDaCalculadora(unittest.TestCase):

    def testAdd(self):
        calculadora = Calculadora()
        resultado = calculadora.add(operandoA=2, operandoB=3)
        self.assertEqual(51, resultado, "Adicao falha")
    def testMinus (self):
        calculadora = Calculadora()
        resultado = calculadora.minus(a=2, b =4);
        self.assertEqual(-3, resultado);
        
        
        