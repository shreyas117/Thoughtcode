
p = {

'1' : 'Loops in programming comes into use when we need to repeatedly execute a block of statements.',
'2' : 'Using Loops',
'3' : 'In Loop, the statement needs to be written only once and the loop will be executed 10 times as shown below.In computer programming, a loop is a sequence of instructions that is repeated until a certain condition is reached.',
'4' : 'An operation is done, such as getting an item of data and changing it, and then some condition is checked such as whether a counter has reached a prescribed number.',
'5' :'Counter not Reached: If the counter has not reached the desired number, the next instruction in the sequence returns to the first instruction in the sequence and repeat it.',
'6' : 'Counter reached: If the condition has been reached, the next instruction “falls through” to the next sequential instruction or branches outside the loop.',
'7' : 'There are mainly two types of loops:',
'8' : 'Entry Controlled loops: In this type of loops the test condition is tested before entering the loop body. For Loop and While Loop are entry controlled loops.',
'9' : 'Exit Controlled Loops: In this type of loops the test condition is tested or evaluated at the end of loop body. Therefore, the loop body will execute atleast once, irrespective of whether the test condition is true or false. do – while loop is exit controlled loop.',
'10' : 'for Loop',
'11' : 'A for loop is a repetition control structure which allows us to write a loop that is executed specific number of times. The loop enables us to perform n number of steps together in one line.',
'12' : 'Syntax:',
'13' : 'for (initialization expr; test expr; update expr){',
'14' : '// body of the loop',
'15' : '// statements we want to execute}',
'16' : 'In for loop, a loop variable is used to control the loop. First initialize this loop variable to some value, then check whether this variable is less than or greater than counter value. If  statement is true, then loop body is executed and loop variable gets updated . Steps are repeated till  exit condition comes.',
'17' : 'Initialization Expression: In this expression we have to initialize the loop counter to some value. for example: int i=1;',
'18' : 'Test Expression: In this expression we have to test the condition. If the condition evaluates to true then we will execute the body of loop and go to update expression otherwise we will exit from the for loop. For example: i <= 10;',
'19' : ' Update Expression: After executing loop body this expression increments/decrements the loop variable by some value. for example: i++;',
'20' : '// C++ program to illustrate ',
'21' : 'for Loop',
'22' : '#include <iostream>',
'23' : 'using namespace std;',
'24' : 'int main(){',
'25' : 'for (int i = 1; i <= 10; i++){',
'26' : 'cout << "Hello World\n"; }',
'27'  :'return 0; }',
'28' : 'While Loop',
'29' : ' While studying for loop we have seen that the number of iterations is known beforehand, i.e. the number of times the loop body is needed to be executed is known to us.  while loops are used in situations where we do not know the exact number of iterations of loop beforehand. The loop execution is terminated on the basis of test condition.',
'30' : 'Syntax:',
'31' : 'We have already stated that a loop is mainly consisted of three statements – initialization expression, test expression, update expression. The syntax of the three loops – For, while and do while mainly differs on the placement of these three statements.',
'32' : 'initialization expression;',
'33' : 'While',
'34' : '(test_expression){',
'35' :' // statements',
'36' : 'update_expression;}',
'37' : '// C++ program to illustrate While loop',
'38' : '#include <iostream> ',
'39' : 'using namespace std;',
'40' : 'int main(){',
'41' : '// initialization expression ',
'42' : 'int i = 1;',
'43' : ' // test expression ',
'44' : 'While',
'45' : '(i < 6){',
'46' : 'cout << "Hello World\n";',
'47' : '  // update expression',
'48' : ' i++;}',
'49' : 'return 0;}',
'50' : 'Output:',
'51' : 'Hello World',
'52' : 'Hello World',
'53' : 'Hello World',
'54' : 'Hello World',
'55' : 'Hello World',
'56' : 'Do While',
'57' : 'In do while loops also the loop execution is terminated on the basis of test condition. The main difference between do while loop and while loop is in do while loop the condition is tested at the end of loop body, i.e do while loop is exit controlled whereas the other two loops are entry controlled loops.',
'58' : 'Note: In do while loop the loop body will execute at least once irrespective of test condition',
'59' : 'Syntax:',
'60' : 'initialization expression;',
'61' : 'do{',
'62' : '// statements',
'63' : ' update_expression;',
'64' : 'While',
'65' : '(test_expression);',
'66' : '// C++ program to illustrate do-while loop',
'67' : '#include <iostream>',
'68' : 'using namespace std;',
'69' : 'int main(){',
'70' : 'int i = 2; // Initialization expression ',
'71' : 'do{',
'72' : ' // loop body',
'73' : ' cout << "Hello World\n"; ',
'74' : '// update expression ',
'75' : 'i++;',
'76' : 'While',
'77' : ' (i < 1);   // test expression',
'78' : 'return 0;} ',
'79' : 'Output:',
'80' : 'Hello World',
'81' : 'In the above program the test condition (i<1) evaluates to false. But still as the loop is exit – controlled the loop body will execute once.',
'82' : 'Important Points:',
'83' : 'Use for loop when number of iterations is known beforehand, i.e. the number of times the loop body is needed to be executed is known.',
'84' : 'Use while loops where exact number of iterations is not known but the loop termination condition is known.',
'85' : 'Use do while loop if the code needs to be executed at least once like in Menu driven programs'

}















import json
s = json.dumps(p)
with open ("C://Users//dell//Desktop//Thoughtcode//Thoughtcode//json_filesbook4.txt","w") as f:
    f.write(s)
