# Hashtable (hash map)

- Abstract data type (like stack and queue)
- Provide access to data using **keys**
    - `key: value`
- Associative array is one type of hash table

## Hashing

- Maps keys of any data type to an integer
- Hash function **<mark style="background: #FFB86CA6;">maps keys to int</mark>**
- In Java, hash function is `Object.hashCode()`
- Beware of **collision** of keys

## Load Factor

- Tells us how **full** a hash table is

[[Linear Probing]]