p = {
'1' : 'Operators are the foundation of any programming language. Thus the functionality of C/C++ programming language is incomplete without the use of operators. We can define operators as symbols that helps us to perform specific mathematical and logical computations on operands. In other words we can say that an operator operates the operands.For example, consider the below statement:',
'2' : 'c = a + b;',
'3' : 'Here, ‘+’ is the operator known as addition operator and ‘a’ and ‘b’ are operands. The addition operator tells the compiler to add both of the operands ‘a’ and ‘b’. C/C++ has many built-in operator types and they can be classified as: ',
'4' : 'Arithmetic Operators: These are the operators used to perform arithmetic/mathematical operations on operands. Examples: (+, -, *, /, %,++,–).Arithmetic operator are of two types:',
'5' : 'Unary Operators: Operators that operates or works with a single operand are unary operators.For example: (++ , –)',
'6' : 'Binary Operators: Operators that operates or works with two operands are binary operators.For example: (+ , – , * , /)',
'7' : 'Relational Operators: Relational operators are used for comparison of the values of two operands. For example: checking if one operand is equal to the other operand or not, an operand is greater than the other operand or not etc. Some of the relational operators are (==, >= , <= ).',
'8' : 'Logical Operators:  Logical Operators are used to combine two or more conditions/constraints or to complement the evaluation of the original condition in consideration. The result of the operation of a logical operator is a boolean value either true or false',
'9' : 'Bitwise Operators: The Bitwise operators is used to perform bit-level operations on the operands. The operators are first converted to bit-level and then calculation is performed on the operands. The mathematical operations such as addition , subtraction , multiplication etc. can be performed at bit-level for faster processing.',
'10' : 'Assignment Operators: Assignment operators are used to assign value to a variable. The left side operand of the assignment operator is a variable and right side operand of the assignment operator is a value. The value on the right side must be of the same data-type of variable on the left side otherwise the compiler will raise an error.',
'11' : 'Different types of assignment operators are shown below:',
'12' : '“=”: This is the simplest assignment operator. This operator is used to assign the value on the right to the variable on the left.For example:<br>a = 10;',
'13' : 'b = 20;',
'14' : 'ch = y;',
'15' : '“+=”:This operator is combination of ‘+’ and ‘=’ operators. This operator first adds the current value of the variable on left to the value on right and then assigns the result to the variable on the left.Example:',
'16' : ' (a += b) can be written as (a = a + b)',
'17' : ' If initially value stored in a is 5. Then (a += 6) = 11.',
'18' : '“/=”:This operator is combination of ‘/’ and ‘=’ operators. This operator first divides the current value of the variable on left by the value on right and then assigns the result to the variable on the left.Example:',
'19' : '(a /= b) can be written as (a = a / b)',
'20' : ' If initially value stored in a is 6. Then (a /= 2) = 3.',
'21' : 'Other Operators: Apart from the above operators there are some other operators available in C or C++ used to perform some specific task. Some of them are discussed here:',
'22' : 'sizeof operator: sizeof is a much used in the C/C++ programming language. It is a compile time unary operator which can be used to compute the size of its operand. The result of sizeof is of unsigned integral type which is usually denoted by size_t. Basically, sizeof operator is used to compute the size of the variable.',
'23' : 'Comma Operator: The comma operator (represented by the token ,) is a binary operator that evaluates its first operand and discards the result, it then evaluates the second operand and returns this value (and type). The comma operator has the lowest precedence of any C operator. Comma acts as both operator and separator.',
'24' : 'Conditional Operator: Conditional operator is of the form Expression1 ? Expression2 : Expression3 . Here, Expression1 is the condition to be evaluated. If the condition(Expression1) is True then we will execute and return the result of Expression2 otherwise if the condition(Expression1) is false then we will execute and return the result of Expression3. We may replace the use of if..else statements by conditional operators.'

}
import json
s = json.dumps(p)
with open ("C://Users//dell//Desktop//Thoughtcode//Thoughtcode//json_filesbook3.txt","w") as f:
    f.write(s)

