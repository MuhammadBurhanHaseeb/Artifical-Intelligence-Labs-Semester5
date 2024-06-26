def balance_brackets_sequence(input_sequence):
    openBrackets  = 0 
    closeBrackets = 0
    for char in input_sequence:
        if char == '(':
             closeBrackets = closeBrackets + 1
        elif char == ')':
            if closeBrackets > 0:
                closeBrackets = closeBrackets -1
            else:
                openBrackets = openBrackets + 1
    s1 = '(' * openBrackets 
    s2 =  ')' * closeBrackets
    return s1 + input_sequence + s2
sequence_string = 'a+(b(c))'
balanced_sequence = balance_brackets_sequence(sequence_string)
print("your balanced string is :",balanced_sequence)
