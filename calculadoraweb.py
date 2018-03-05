#!/usr/bin/python3

import webapp
import calculadora

#GET /1/suma/2 ...

class calculadoraweb(webapp.webApp):

    def parse(self,request):
        return request.split()[1].split('/')[1:] #['','1','suma','2']

    def process(self,parsedRequest):
        op1, operacion, op2 = parsedRequest

        resultado = calculadora.funciones[operacion](int(op1),int(op2))

        return ("200 OK", "<html><body><h1>" + "Resultado: " +
                str(resultado) + "</h1></body></html>")

if __name__ == "__main__":
    testWebApp = calculadoraweb("localhost", 1234)

