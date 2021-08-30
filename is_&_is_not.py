if 1 is 1:
    print('1 is 1')
elif 1 is not 1:
    print('1 is not 1')

if 1 is 2:
    print('1 is 1')
elif 1 is not 2:
    print('1 is not 1')

# output:
# c:\Users\Dell\algorithm_python\is_&_is_not.py:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
#   if 1 is 1:
# c:\Users\Dell\algorithm_python\is_&_is_not.py:3: SyntaxWarning: "is not" with a literal. Did you mean "!="?
#   elif 1 is not 1:
# c:\Users\Dell\algorithm_python\is_&_is_not.py:6: SyntaxWarning: "is" with a literal. Did you mean "=="?
#   if 1 is 2:
# c:\Users\Dell\algorithm_python\is_&_is_not.py:8: SyntaxWarning: "is not" with a literal. Did you mean "!="?
#   elif 1 is not 2:
# 1 is 1
# 1 is not 1

# 이런식으로 warning이 나오네? 