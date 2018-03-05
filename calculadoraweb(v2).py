#!/usr/bin/python3

#Solo sumador, sin reutilizar el código de calculadora.py

import webapp

class Calc(webapp.webApp):

    def parse(self, request):
        return request.split()[1].split('/')[1:]

    def process(self, parsedRequest):
        op1, operacion, op2 = parsedRequest
        resultado = self.suma(int(op1), int(op2))
        return ("200 OK", "<html><body><h1>Calculadora suma: " + 
                str(resultado) + "</h1></body></html>")

    def suma(self, op1, op2):
        return op1 + op2

if __name__ == "__main__":
    testCalc = Calc("localhost", 1234)
