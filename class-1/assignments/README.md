# Assignments

### *mutability

What's the difference between a mutable and an immutable type? Why should I use one or the other? Write the following two functions, both receiving a list of elements and a new elemnt to append at the end. The first one should be a mutable version and the second an immutable version.

Example mutable:

    l = [1, 2, 3]
    mutable_append(l, 'a')
    print(l)  # Should print [1, 2, 3, 'a']
    
Example immutable:

    l = [1, 2, 3]
    new_l = mutable_append(l, 'a')
    print(l)  # Should print [1, 2, 3]
    print(new_l)  # Should print [1, 2, 3, 'a']

### Camel case

Write a function that receives a string and returns a camel case version of it.

Example:

    def camel_case("hello world")  # Should return "Hello World"
    
### All uppercase

Write a function that receives a string and returns the same string all in uppercase.

Example:

    uppercase("hello")  # Should return "HELLO"
    
Hint: Google and the python docs are your friends.

### First 2 characters

Write a function that receives a string and returns the first two characters from that string. Think about the edge cases (empty string, string with less than 2 chars, etc).
Bonus: Write a first "n" characters function that receives the string and an OPTIONAL number `n` (which will be 2 if none is provided) and returns the first `n` characters.

Example:

    first_2_characters("Hello")  # Should return "He"

    # Bonus
    first_n_characters("Hello")  # Should return "He"
    first_n_characters("Hello", 3)  # Should return "Hel"

### Every n insert

Write a function named "every_3_chars_insert" which receives a two strings `a` and `b` and returns a new string equals to the string `a` plus occurences of the string `b` every 3 characters.

Example:

    def every_3_chars_insert(a, b):
        pass
        
    every_3_chars_insert('Hello World', '-')  # Should return "Hel-lo -Wor-ld"

### PowPow

Write a function that receives an integer and returns a dictionary with the element and the result of the multiplication by itself, with the form `{i: (i*i)}`

Example:
    pow_pow(5)  # Should return {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

###  Count occurences

Write a function that receives a list and return a dictionary with the element each element of the list and the number of occurences of that element with the form {element: count}.

Example:
    count_occurences([1, 5, 'a', 3, 1, 1, 'a']))  # Should return {1: 3, 'a': 2, 5: 1, 3: 1}

### Our beloved next_prime

Take other stab at `next_prime`.

### Charly's scam

Ben owes $10 to Charly. Ben hasn't all the money, so he asks Charly if he could make a couple of small payments. Charly agrees and tells Ben that he can make 3 payments to fulfill his debt. Write a program that prints out the money Ben has to pay in his first payment. Do you see something off? What's going on?