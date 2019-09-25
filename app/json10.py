p={

	'l':['Pointers in C++',
		'Pointers store address of variables or a memory location.',
		'datatype *var_name; ',
		'int *ptr;',
		'Using a Pointer:',
		'To use pointers in C, we must understand below two operators.',
		'To access address of a variable to a pointer, we use the unary operator & (ampersand) that returns the address of that variable. For example &x gives us address of variable x.',
		'One more operator is unary * (Asterisk) which is used for two things :',
		'To declare a pointer variable: When a pointer variable is declared in C/C++, there must a * before its name.',
		'To access the value stored in the address we use the unary operator (*) that returns the value of the variable located at the address specified by its operand.',
		'Output :',
		'Value of Var = 10 Address of Var = 0x7fffa057dd4 After doing *ptr = 20, *ptr is 20',
		'Pointer Expressions and Pointer Arithmetic',
		'A limited set of arithmetic operations can be performed on pointers. A pointer may be:',
		'incremented ( ++ )',
		'decremented ( — )',
		'an integer may be added to a pointer ( + or += )',
		'an integer may be added to a pointer ( + or += )',
		'Array Name as Pointers ',
		'An array name acts like a pointer constant. The value of this pointer constant is the address of the first element.',
		'Output:',
		'Elements of the array are: 5 10 20'
		]
}		

import json
s = json.dumps(p)
with open ("C://Users//dell//Desktop//Thoughtcode//Thoughtcode//json_filesbook10.txt","w") as f:
 f.write(s)