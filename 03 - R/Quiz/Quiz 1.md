---
sources:
  - "[[678. Valid Parenthesis String]]"
---
> [!question] Select all valid strings from the following options:
> a) ((*)
> b) (*)*)
> c) (()*)
> d) (*
> e) *)
>> [!success]- Answer
>> a) ((*)
>> c) (()*)
>> d) (*

> [!question] According to the rules, the string `(*` is considered `____` while the string `*(` is considered `____`.
>> [!success]- Answer
>> True, False

> [!question] Match the following strings with their validity status:
>> [!example] Group A
>> a) (*)
>> b) ()
>> c) (*))
>> d) )*
>
>> [!example] Group B
>> n) True
>> o) False
>> p) True
>> q) True
>
>> [!success]- Answer
>> a) -> n)
>> b) -> n)
>> c) -> n)
>> d) -> o)

> [!question] Which of the following strings is considered valid according to the given rules?
> a) (*
> b) (*))
> c) )*
> d) ()
>> [!success]- Answer
>> b) (*))

> [!question] A string containing only '(', ')', and '*' is considered valid if every '(' has a corresponding ')' and every ')' has a corresponding '(', and '(' must come before its corresponding ')'.
>> [!success]- Answer
>> True

> [!question] Explain why the string '(*' is considered valid while '*(' is not, according to the provided rules.
>> [!success]- Answer
>> According to the rules, '*' can be treated as '(', ')' or an empty string. In '(*', '*' can be treated as '(', making the string '((', which is invalid because the opening parenthesis doesn't have a closing one. However, '*' can also be treated as an empty string, resulting in '(', which is also invalid because of the missing closing parenthesis.  But since '*' can represent a ')' as well, the string becomes '()', which is valid. In '*(', '*' cannot be a closing parenthesis, and if it is an empty string or an opening parenthesis, the string would be invalid because a closing parenthesis appears before the opening one.

> [!question] Describe the algorithm you would use to determine whether a given string of '(', ')', and '*' characters is valid according to the rules provided. Explain why your approach correctly handles all cases, including those where '*' is interpreted as an empty string, '(', or ')'. Provide an example to illustrate your algorithm.
>> [!success]- Answer
>> A stack-based approach can efficiently determine the validity of the string.  The algorithm iterates through the string: 1. For each character: a. If it's '(', push it onto the stack. b. If it's ')', check if the stack is empty. If it's empty, the string is invalid (unmatched closing parenthesis). If not empty, pop an element from the stack (matching the parenthesis). c. If it's '*', consider three possibilities.  Try popping from the stack (treating it as a matching ')'), or push it onto the stack (treating it as a '('), or ignore it (treating it as an empty string). For each possibility, recursively continue the algorithm.  If any recursive call returns True, the string is valid. 2. If the stack is empty at the end of the iteration, the string is valid (all parentheses are matched). Otherwise, it is invalid (unmatched opening parentheses). This approach handles '*' correctly because it systematically tries all its possible interpretations (empty string, '(', or ')').  The recursive calls ensure exhaustive exploration of every possible interpretation of '*' within the string.  For example, consider '(*)'.\n- Initially, stack is empty.\n- Encounter '*', three possibilities: \n\t* Assume '*': '', process '()', which is valid, the function returns True.\n\t* Assume '*': '(', stack: ['(']; process ')', pop '(', the stack is empty, returns True.\n\t* Assume '*': ')', the stack is empty, it is invalid, it goes to the next recursion.\n-Since the first possibility returns True, the string '(*) is considered valid.

