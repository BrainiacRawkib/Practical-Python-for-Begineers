# voltage program

Vc = float(input('Enter the value of Vc : '))
Ic = float(input('Enter the value of Ic : '))
Rc = float(input('Enter the value of Rc : '))

Vcc = Vc + (Ic * Rc)

print('The value of Vcc is : ', Vcc)
