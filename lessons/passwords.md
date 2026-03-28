---
layout: page
title:  Passwords
nav_exclude: true
author: Ibrahim Albluwi
---

<style>
h2 {
    font-weight: 400;           /* normal weight, not bold */
    font-family: "Open Sans", sans-serif;  /* different font face */
    color: #3b7dc0ff;             /* optional: different color */
}

h3 {
    font-weight: 500;           /* bold weight */
    font-family: "Open Sans", sans-serif;  /* different font face */
    color: #9c0101ff;             /* optional: different color */
}

.img-soft {
    width: 75%;
    border-radius: 14px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.15);  
}
</style>

# Passwords
{: .no_toc}

![Comic: My Password is Password123](https://cdn.shopify.com/s/files/1/0077/2554/7593/files/important-password-the-introverted-attorney-lawyer-comic_600x600.png?v=1614183796)

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Protecting Your Password

### Shoulder Surfing

Assume that as you are typing your password, someone peeks over your shoulder and notices that you have typed **6 lowercase letters**, but couldn't tell which ones. How easy would it be for them to guess your password?

They can _brute-force_ it by trying all possible combinations of 6 lowercase letters until they find the correct one. Since there are 26 possible lowercase letters, there are:

$$26^6 = 308,915,776\approx 309 \textrm{ million}$$

different possible passwords made of 6 lowercase letters. This might sound safe. After all, any website is likely to lock them out if they provide an incorrect password a few times! 

{: .example-title }
> A PYTHON NOTE
>
> Instead of using `input()` to read passwords in your Python programs, you can use the `getpass` module, which hides the password as you type it. Here is a simple example:
>
>```python
>import getpass
>password = getpass.getpass("Enter your password: ")
>print("You entered:", password)
>```

### Brute-Force Attacks

Imagine if the password database of your website was leaked and the attacker had access to it ([this could happen even with top websites!](https://www.mcafee.com/blogs/internet-security/26-billion-records-released-the-mother-of-all-breaches/)). Typically, websites store passwords **hashed** (i.e., transformed to an unreadable format as will be explained later). Hence, your password should still be unreadable by the attacker. However, the attacker now has an easy way to crack your password!

Knowing your hashed password, they can try to hash the $$308,915,776$$ possible passwords and see if any match your hashed password. This can be done on a laptop in a matter of hours, and on a stronger computer with multiple GPUs in a matter of seconds or less!

### Protecting Your Password

Most websites currently require passwords to be at least 8 characters long, and to contain a combination of uppercase letters, lowercase letters, numbers, and special characters. How secure does this make the password? 

{: .example-title }
> Do The Math
>
> If the password has 8 lowercase characters, the number of possible passwords is:
>
> $$26^8 = 208,827,064,576\approx 209 \textrm{ billion}$$
> 
> If the password has also uppercase characters, the number is:
>
> $$(26 + 26)^8 = 53,459,729,000,000\approx 53 \textrm{ trillion}$$
>
> If it also has numbers:
>
> $$(26 + 26 + 10)^8 = 218,340,110,000,000\approx 218 \textrm{ trillion}$$
>
> Assume also that there is also one of 32 special characters:
>
> $$(26 + 26 + 10 + 32)^8 = 6,095,689,400,000,000\approx 6 \textrm{ quadrillion}$$

Adding such requirements can make it practically impossible even for the fastest computers to crack the password using naive brute-force attacks.

{: .highlight-title }
> 🔗 **LINK**
>
> The following website provides estimates for how long it takes to crack your password!
> [https://bitwarden.com/password-strength/](https://bitwarden.com/password-strength/){:target="_blank"}

While the above requirements make passwords more secure, they also make them harder to remember. People tend to use the same password across multiple websites, or use small variations of the same password (e.g., `Password1!`, `Password_1234`, etc.). This makes it easier for attackers to guess passwords using more sophisticated methods than brute-force attacks.


### Dictionary Attacks

Passwords that are easy to remember often follow common patterns or use common words. Therefore, attackers try to exploit this by using a predefined list of common passwords (a _dictionary_). Instead of trying all possible combinations of characters, they try to hash each password from the dictionary and see if it matches the hashed password they are trying to crack. This can be much faster than brute-force attacks, and surprisingly effective!

{: .important-title }
> 📖 Definition
>
> **A Dictionary Attack** is an attempt to guess the password based on a predefined list of strings. The list can contain English words (hence the name _dictionary_), common strings found in passwords (e.g., `password`, `1234`), or actual passwords collected from previous breaches. The attacker typically uses software to create variations of the strings in the dictionary (e.g., appending a number or a special character).

{: .highlight-title }
> 🔗 **OPTIONAL LINK**
>
> Watch a live demo of dictionary attacks:
> [Password Cracking on Computerphile](https://www.youtube.com/watch?v=7U-RbOKanYs&ab_channel=Computerphile){:target="_blank"}


## Storing Passwords

No sane application stores its users' passwords in plaintext. Not even the application administrators should be able to read such sensitive information. Let alone the possibility of hackers getting unauthorized access to the files storing these passwords. The minimum that should be done is to store the passwords in some hashed format.

How can the application authorize users if they don't know their passwords?

The typical procedure is as follows:
1. When a user creates an account or changes their password, the application hashes the password and stores it.
2. When the user tries to log in, the application hashes the password they provide and compares it to the stored hashed version. If they match, the user is authorized.

### Hashing Passwords

For the above procedure to be secure, passwords must undergo a **one-way** transformation method that does **not** allow recovering the original password. For example, the application should not use an encryption method like _one-time pads_, because given the encrypted password and the key, it is possible to recover the original password.

For storing passwords, **cryptographic hashing** is typically used. A cryptographic hash function takes an input (in our case, the password) and produces a fixed-size string of characters, which appears random. There is no key involved in this process and it is computationally infeasible to reverse the process (i.e., to recover the original password from its hashed version). 

The following code snippet shows how to use the [`hashlib`](https://docs.python.org/3/library/hashlib.html) library to generate a _hashed_ version of a password. This piece of code uses a hash function named `SHA256`.

```python
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
    
print(' mypassword: ', hash_password("mypassword"))
print(' mypassword: ', hash_password("mypassword"))  # same output as above
print('mypassword1: ', hash_password("mypassword1")) # different output
print('          1: ', hash_password("1"))           # different output
print('          2: ', hash_password("2"))           # different output
```

Note that the same password always produces the same hash, while different passwords produce different hashes. Note also that even a small change in the password (e.g., adding a `1` at the end) produces a completely different hash.

### Is This Enough?

Imagine an attacker who is collecting usernames and hashed passwords from many different leaked databases. Now, assume that they notice the same hashed password appearing multiple times, associated with different usernames. What can they conclude from this?

If the attacker successfully cracks one of the passwords (e.g., using a dictionary attack), they can immediately know the passwords of all other users who have the same hashed password! Therefore, it is important to make sure that even if two users have the same password, their hashed passwords look different. This is typically done using a technique called **salting**.

Applications typically add a **salt** to every password before hashing it. A salt is an extra random string (different for different users) added to the password before hashing it and stored alongside the password (often in plaintext). This way, if two users use the same password, their hashes will look different, because their salts are different.

Here is the typical procedure for using salts:

1. When a user creates an account, the application generates a random salt (a random sequence of characters).
2. The application creates a new string made by appending the salt to the user's password.
3. The application hashes the resulting string and stores both the salt and the hashed string.

When the user tries to log in:
1. The application retrieves the stored salt for that user. 
2. Creates a string by appending the salt to the password provided by the user.
3. Hashes the resulting string, and compares it to the stored hashed string for the user. 

This way, even if two users have the same password, their hashed passwords will look different because of the different salts.

### Making It Even More Secure

Some cryptographic hash functions (like `SHA256`) are very fast. While this might sound good, it is bad for security reasons. A slow hash function makes the job of a hacker harder, because the time needed for a brute-force attack not only depends on how many passwords will be tested, but also how long it takes to test a single password! Therefore, it is advisable to use libraries like [`bcrypt`](https://pypi.org/project/bcrypt/) and [`scrypt`](https://pypi.org/project/scrypt/), which provide slow (i.e., more secure) hashing algorithms.


## Summary

Here is a summary of best practices for storing passwords securely:
1. Store passwords hashed.
2. Use a one-way hash function for hashing.
3. Use a unique salt for each password before hashing.
4. Use a slow hash function designed for password storage (e.g., bcrypt, scrypt).

{: .highlight-title }
> 🔗 **OPTIONAL LINK**
>
> The following video summarizes nicely how passwords should be stored:
> [Studying With Alex: Password Storage Tier List](https://www.youtube.com/watch?v=qgpsIBLvrGY&ab_channel=StudyingWithAlex)
