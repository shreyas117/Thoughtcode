p = {
#datatype definition
'l' : ['All variables use data-type during declaration to restrict the type of data to be stored. Therefore, we can say that data types are used to tell the variables the type of data it can store.Whenever a variable is defined in C++, the compiler allocates some memory for that variable based on the data-type with which it is declared. Every data type requires different amount of memory.',
'Data types in C++ is mainly divided into two types:',
#types of datatype-- (1)
'Primitive Data Types:',
'These data types are built-in or predefined data types and can be used directly by the user to declare variables. example: int, char , float, bool etc. Primitive data types available in C++ are:',
#under primitive datatype
'Integer',
'Character',
'Boolean',
'Floating Point',
'Double Floating Point',
'Valueless or Void',
'Wide Character',
#types of datatype-- (2)
'Abstract or user defined data type:',
'These data types are defined by user itself. Like, defining a class in C++ or a structure',
'This article discusses primitive data types available in C++.',
#discussing primitive datatypes 
'Integer:','Keyword used for integer data types is int. Integers typically requires 4 bytes of memory space and ranges from -2147483648 to 2147483647. ',
'Character:','Character data type is used for storing characters. Keyword used for character data type is char. Characters typically requires 1 byte of memory space and ranges from -128 to 127 or 0 to 255',
'Boolean:','Boolean data type is used for storing boolean or logical values. A boolean variable can store either true or false. Keyword used for boolean data type is bool.',
'Floating Point:','Floating Point data type is used for storing single precision floating point values or decimal values. Keyword used for floating point data type is float. Float variables typically requires 4 byte of memory space. ',
'Double Floating Point:','Double Floating Point data type is used for storing double precision floating point values or decimal values. Keyword used for double floating point data type is double. Double variables typically requires 8 byte of memory space. ',
'void:','Void means without any value. void datatype represents a valueless entity. Void data type is used for those function which does not returns a value. ',
'Wide Character:','Wide character data type is also a character data type but this data type has size greater than the normal 8-bit datatype. Represented by wchar_t. It is generally 2 or 4 bytes long. ',

'Datatype Modifiers:','As the name implies, datatype modifiers are used with the built-in data types to modify the length of data that a particular data type can hold. Data type modifiers available in C++ are',
'Signed',
'Unsigned',
'Short',
'Long']


}







import json
s = json.dumps(p)
with open ("C://Users//dell//Desktop//Thoughtcode//Thoughtcode//json_filesbook.txt","w") as f:
    f.write(s)
