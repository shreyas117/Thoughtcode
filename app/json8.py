p={

 'l' : ['References',
		'When a variable is declared as reference, it becomes an alternative name for an existing variable. A variable can be declared as reference by putting ‘&’ in the declaration.',
        'Output:','x = 20','ref = 30','Following is one more example that uses references to swap two variables.'
		'Output:',
		'3 2 ',
		'References vs Pointers',
		'Both references and pointers can be used to change local variables of one function inside another function. Both of them can also be used to save copying of big objects when passed as arguments to functions or returned from functions, to get efficiency gain.',
		'Despite above similarities, there are following differences between references and pointers.',
		'References are less powerful than pointers',
		'Once a reference is created, it cannot be later made to reference another object; it cannot be reseated. This is often done with pointers.',
		'References cannot be NULL. Pointers are often made NULL to indicate that they are not pointing to any valid thing.',
		'A reference must be initialized when declared. There is no such restriction with pointers',
		'References are safer and easier to use:',
		'Easier to use: References don’t need dereferencing operator to access the value. They can be used like normal variables. ‘&’ operator is needed only at the time of declaration. Also, members of an object reference can be accessed with dot operator (‘.’), unlike pointers where arrow operator (->) is needed to access members.']
	}
       

import json
s = json.dumps(p)
with open ("C://Users//dell//Desktop//Thoughtcode//Thoughtcode//json_filesbook8.txt","w") as f:
 f.write(s)