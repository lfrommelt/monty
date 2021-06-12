
2. What will be displayed in your terminal if you run these lines of code?
   ```python
   print(2 + 2)
   print('2' + '2')
   ```
   ::: solution
   ```python
   4   # type: int
   22  # type: str
   ```
   :::

2. What is the function of the `+` sign in each case?

:::solution
First line: the `+` sign is used as an operator to add two integers.

Second line: the `+` sign is used to concatenate strings.
:::

## Common operators: Division

1. What is the difference between `/` and `//`?

   :::solution
      - `/` is used to divide the left side before the `/` operator by the right side after the `/` operator.
          The result of this division always results in a float.

      - `//` is used as a floor division operator in Python.
           This means that the result of the division is rounded down to the next integer value.
   :::

2. What would be an application example for each one of the operations?

   :::solution
   ```{ .python .exec}
   # Dividend / Divisor = Quotient

   # set the values of the variables
   dividend = 5
   divisor = 2

   # dividing with /
   quotient_1 = dividend / divisor
   print(
       'The result of the division of 5 by 2 using the "/" operand, results in',
       quotient_1, '.')
   print('The result is of the type ', type(quotient_1), '.')

   # dividing with //
   quotient_2 = dividend // divisor
   print('The result of the division of 5 by 2 using the "//" operand, results in',
         quotient_2, '.')
   print('The result is of the type ', type(quotient_2), '.')
   ```

   !!!!!! add applictaionnnn examples in form of sentences
   Text Zeilen Zeichen; Wie viele volle Zeilen?
   Gläser mit 0,2. Ich habe 3,5 l wasser. We viele kann ich ganz voll machen?

   :::
