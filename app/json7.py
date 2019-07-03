p = {
'l' : ['A function is a set of statements that take inputs, do some specific computation and produces output.','The idea is to put some commonly or repeatedly done task together and make a function, so that instead of writing the same code again and again for different inputs, we can call the function.',
'Function Declaration',
'Function declaration tells compiler about number of parameters function takes, data-types of parameters and return type of function. Putting parameter names in function declaration is optional in function declaration, but it is necessary to put them in definition.',
'In C, we can do both declaration and definition at same place, like done in above example program. ',
'C also allows to declare and define functions separately, this is specially needed in case of library functions. The library functions are declared in header files and defined in library files.',
'Parameter Passing to functions',
'The parameters passed to function are called actual parameters. For example, in the above program 10 and 20 are actual parameters.',
'The parameters received by function are called formal parameters. For example, in the above program x and y are formal parameters.',
'There are two most popular ways to pass parameters.',
'Pass by Value:',
'In this parameter passing method, values of actual parameters are copied to function&#8217;s formal parameters and the two types of parameters are stored in different memory locations.  So any changes made inside functions are not reflected in actual parameters of caller.',
'Pass by Reference',
'Both actual and formal parameters refer to same locations, so any changes made inside the function are actually reflected in actual parameters of caller.',
'In C, parameters are always passed by value. Parameters are always passed by value in C. For example. in the below code, value of x is not modified using the function fun().',
'However, in C, we can use pointers to get the effect of pass by reference.  For example, consider the below program. The function fun() expects a pointer ptr to an integer (or an address of an integer). It modifies the value at the address ptr. The dereference operator * is used to access the value at an address. In the statement ‘*ptr = 30’, value at address ptr is changed to 30. The address operator &amp; is used to get the address of a variable of any data type. In the function call statement ‘fun(&amp;x)’, the address of x is passed so that x can be modified using its address.',
'Following are some important points about functions in C.',
'Every C program has a function called main() that is called by operating system when a user runs the program.',
'Every function has a return type.  If a function doesn/t return any value, then void is used as return type.',
'In C, functions can return any type except arrays and functions. We can get around this limitation by returning pointer to array or pointer to function.',
'Empty parameter list in C mean that the parameter list is not specified and function can be called with any parameters.']

}


import json
s = json.dumps(p)
with open ("Z://my project//json_files//book7.txt","w") as f:
 f.write(s)