import math

tol=1.e-3
max_iter=100

expr = input("Ingrese la funcion: ")
x_n = float(input("Ingrese xi: "))

x0=10
i=0
while abs(x_n-x0)>tol and i<max_iter :
	i+=1
	
	x0=x_n
	
	libres=dict(x=x0)#evalua en x1
	func=vars(math)
	x1=eval(expr,func,libres)

	libres=dict(x=x1)#evalua en x2
	x2=eval(expr,func,libres)

	x_n=x0-(((x1-x0)**2)/(x2-2*x1+x0))

	print(i," ",x_n)
