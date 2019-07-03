p = {
'l' : ['An array is collection of items stored at continuous memory locations.',
'Why do we need arrays?',
'We can use normal variables (v1, v2, v3,..) when we have small number of objects, but if we want to store large number of instances, it becomes difficult to manage them with normal variables. The idea of array is to represent many instances in one variable.',
'Array declaration in C/C++:',
'We can declare an array by specifying its type and size or by initializing it or by both.',
'Accessing Array Elements:',
'Array elements are accessed by using an integer index. Array index starts with 0 and goes till size of array minus 1. Following are few examples.',
'No Index Out of bound Checking:',
'There is no index out of bound checking in C, for example the following program compiles fine but may produce unexpected output when run.',
'Also, In C, it is not compiler error to initialize an array with more elements than specified size. For example the below program compiles fine.',
'The program won’t compile in C++.',
'If we save the above program as a .cpp, the program generates compiler error “error: too many initializers for ‘int [2]”',
'An Example to show that array elements are stored at contiguous locations',
' C program to demonstrate that array elements are stored contiguous locations',
'Array vs Pointers',
' Arrays and pointer are two different things (we can check by applying sizeof). The confusion happens because array name indicates address of first element and arrays are always passed as pointers (even if we use square bracket). ',
'What is vector in C++?',
'Vector in C++ is a class in STL that represents an array. The advantages of vector over normal arrays are,',
'We do not need pass size as an extra parameter when we pass vector.',
'Vectors have many in-built function like, erasing an element, etc.',
'>Vectors support dynamic sizes, we do not have to initially specify size of a vector. We can also resize a vector.',
'>There are many other functionalities vector provide, please refer vector in C++ for more details.']

}

import json
s = json.dumps(p)
with open ("Z://my project//json_files//book6.txt","w") as f:
 f.write(s)
