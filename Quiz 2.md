---
sources:
  - "[[678. Valid Parenthesis String]]"
---
> [!question] Which of the following input strings would the function deem as 'valid'?
> a) (*
> b) )(
> c) *)
> d) ()
>> [!success]- Answer
>> a) (*

> [!question] Select all the valid strings from the following options:
> a) ()
> b) (*)
> c) (*))
> d) )(
> e) (*)(
> f) **
>> [!success]- Answer
>> a) ()
>> b) (*)
>> c) (*))

> [!question] According to the rules, the string `(**` could be interpreted as `____` or `____` or `____`.
>> [!success]- Answer
>> ((, (), 

> [!question] Match the following inputs with their corresponding outputs:
>> [!example] Group A
>> a) (*))
>> b) (*)
>> c) )(
>> d) )*
>> e) ()
>> f) *(
>
>> [!example] Group B
>> n) true
>> o) true
>> p) false
>> q) true
>> r) false
>> s) false
>
>> [!success]- Answer
>> a) -> n)
>> b) -> n)
>> c) -> p)
>> d) -> p)
>> e) -> n)
>> f) -> p)

> [!question] Describe a scenario where the flexibility offered by the '*' character might be useful in a real-world application involving parentheses balancing or string parsing.  Provide a specific example and explain its relevance.
>> [!success]- Answer
>> In a scenario involving potentially malformed or incomplete data, such as receiving a stream of parentheses from a sensor which sometimes loses a character, the '*' can act as a placeholder for a missing parenthesis. For example, if the expected string was '()()' but the received stream was '(*()', the '*' can be treated as a ')' and the function would deem this acceptable.  This allows for more robust parsing of real-world data, accommodating potential errors or missing information. It is especially useful for creating more resilient applications to handle noisy data or handle data from unreliable sources.

> [!question] Explain why the input string '(*' is considered valid according to the provided rules.
>> [!success]- Answer
>> The '*' can be interpreted as a '(', making the string '()', which is valid because it satisfies all the rules: it has a matching pair of parentheses, the left parenthesis comes before the right, and every parenthesis has a match.

> [!question] The function described only accepts strings containing '(', ')', and '*'.
>> [!success]- Answer
>> True

> [!question] Which of the following input strings would the function deem as 'valid'?
> a) (*
> b) )(
> c) *)
> d) ()
>> [!success]- Answer
>> a) (*

