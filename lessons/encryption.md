---
layout: page
title:  Encryption
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

.figure-soft {
    text-align: center;
    margin: 20px 0;
}

</style>


# Security and Encryption
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

You have probably heard about _hackers_, _viruses_, and _data breaches_ in the news. Computer security is about protecting your data and systems against such threats. The three main goals of computer security, often referred to as the **CIA Triad**, are:

1. **Confidentiality**: Ensuring that sensitive information is accessible only to authorized individuals (e.g., using passwords, encryption, etc.).
2. **Integrity**: Ensuring the data is not altered or tampered with by unauthorized individuals.
3. **Availability**: Ensuring that information and resources are accessible to authorized users when needed.

Here are some real-world examples illustrating the importance of these goals:

### Confidentiality

Imagine some of your sensitive information (like your password or credit card number) being published online for anyone to see. **Data breaches** are incidents where unauthorized individuals gain access to confidential data. They happen more often than you might think. Here are two notable examples:

<img alt="Sony PlayStation Network Logo" src="https://upload.wikimedia.org/wikipedia/commons/a/ac/PlayStation_Network_logo_%282015%29.png" style="width: 65%; display:block; margin: 20px auto;">

1. In 2011, [Sony's PlayStation Network was hacked](https://en.wikipedia.org/wiki/2011_PlayStation_Network_outage), exposing 77 million user accounts due to improper password encryption. Leaked data included usernames, passwords, and billing addresses, leading to a 23-day network shutdown and $171 million in damages.

<img alt="Marriott International Logo" src="https://vectorseek.com/wp-content/uploads/2023/10/marriott-international-Logo-Vector.svg-.png" style="display:block; margin: 20px auto; width: 35%;">

2. In 2018, [Marriott International disclosed](https://consumer.ftc.gov/consumer-alerts/2018/12/marriott-data-breach) a data breach affecting 500 million guests. Hackers stole sensitive data like: passport numbers, phone numbers, credit card information, and reservation details. Marriott was fined $24 million by the UK Information Commissioner’s Office (ICO) for failing to meet cybersecurity standards.

[This website](https://informationisbeautiful.net/visualizations/worlds-biggest-data-breaches-hacks/) provides a nice visualization of major data breaches over the years. You will notice that major entities like Facebook, Microsoft, and the Chinese Government have all been involved in significant data breaches, and that breaches continue to occur frequently.

### Availability

<img alt="Dyn Logo" src="/11102-f25/lessons/images/dyn.png" style="display:block; margin: 20px auto; width: 95%;">

In 2016, the [Dyn attack](https://en.wikipedia.org/wiki/2016_Dyn_cyberattack) disrupted access to major websites like Twitter, Netflix, PayPal, HBO, Airbnb, and Reddit. These companies used a company named Dyn for a critical operation: translating human-friendly domain names (like `twitter.com`) into IP addresses that computers use to identify each other on the network. Attackers created a massive network of compromised computers and used them to overwhelm Dyn's servers with requests, making their services unavailable. 

This is just one example of what is referred to as a [**Denial of Service (DoS)**](http://en.wikipedia.org/wiki/Denial-of-service_attack) attack. Another example is the [MafiaBoy attacks](https://en.wikipedia.org/wiki/MafiaBoy) in 2000, which targeted major websites like Yahoo!, eBay, CNN, and `fifa.com` causing widespread outages. The attacker was a 15-year-old student who used a network of university computers that he compromised to launch the attacks. 

<figure class="figure-soft">
    <img 
        src="https://media.npr.org/assets/img/2015/02/07/mike44-ae7fb019b4e67042097efda8e64b81c2ac4ded20.jpg" 
        alt="Michael Demon Calce" 
        class="img-soft" style="display:block; margin: 20px auto; width: 45%;"
    >
    <figcaption>Michael Demon Calce: The Mafiaboy</figcaption>
</figure>


Many larger scale and more recent DoS attacks have occurred, targeting various organizations and services, causing significant disruptions and financial losses.


### Integrity

Consider a scenario where an attacker alters the content of a bank transaction. For example, changing a transfer amount from $100 to $10,000 without authorization. This compromises the integrity of the transaction data, leading to financial loss and mistrust in the banking system.

A famous example of an integrity attack is the [Stuxnet worm](https://en.wikipedia.org/wiki/Stuxnet) discovered in 2010. Stuxnet was a malicious computer software (called a worm) that specifically targeted Iran's nuclear facilities. It altered the control software controlling uranium enrichment, which caused centrifuges to spin out of control and ultimately damage the equipment. This attack demonstrated how cyber threats could compromise the integrity of critical infrastructure.

<img alt="Stuxnet" src="https://i.guim.co.uk/img/static/sys-images/Guardian/About/General/2011/5/30/1306781568985/Mahmoud-Ahmadinejad-visit-007.jpg?width=465&dpr=1&s=none&crop=none" class="img-soft" style="display:block; margin: 20px auto; width: 65%;">

In this lesson, we will explore one of the fundamental techniques used to ensure confidentiality and integrity: **encryption**.

## Encryption

Encryption is the process of converting plain text (readable data) into ciphertext (unreadable data), such that only an authorized person can convert it back to plain text. Below are a few examples of encryption techniques:

### Shift Ciphers

A simple encryption technique is to substitute each letter in the plaintext with another letter. One of the simplest ways is to shift each letter by a fixed number of places in the alphabet.

For example, using a shift of 1, the letter `a` would be replaced by `b`, `b` would be replaced by `c`, and so on, with `z` wrapping around to `a`. Hence, the word `hello` would be encrypted as `ifmmp`.

<iframe src="{{ '/lessons/rotation.html' | relative_url }}" 
        width="100%" 
        height="300" 
        frameborder="0"
        style="border: none;">
</iframe>
Here is a simple Python implementation of a function that generates a rotation table:

```python
def get_rot_table(shift):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    rotated = alpha[shift:] + alpha[:shift]

    # map each letter to its rotated counterpart
    table = {}
    for i in range(len(alpha)):
        table[alpha[i]] = rotated[i]
    return table
```

The following function uses the table to substitute letters in the given text:

```python
def substitute(text, table):
    result = ''
    for char in text:
        if char in table:
            result += table[char]
        else:
            result += char  # keep unknown characters unchanged
    return result
```

Now, we can use the above functions to encrypt a message using a rotation cipher:

```python
def rot_encrypt(text, shift):
    table = get_rot_table(shift)
    return substitute(text, table)
```

To decrypt the message, we need to shift the letters back by the same amount.

```python
def rot_decrypt(text, shift):
    table = get_rot_table(26 - shift)
    return substitute(text, table)
```

This method is often referred to as **Caesar Cipher**, because it was reportedly used by Julius Caesar to communicate with his officials. However, this method is not secure at all by modern standards.


### Brute Force Attacks

A brute force attack is a method used to break encryption by systematically trying all the possibilities until the correct one is found. 

For example, if an attacker wants to break a message encrypted with a rotation cipher, they don't really need to know the amount of rotation made (e.g. 13). They could try all 26 possible rotations (from 0 to 25). 

Here is a simple Python implementation of a brute force attack on a rotation cipher:

```python
def break_rot_cipher(ciphertext):
    for shift in range(26):
        decrypted_text = rot_decrypt(ciphertext, shift)
        print("Shift:", shift, "->", decrypted_text)
```

If we run the above function with the ciphertext `uryyb`, we would see all possible decryptions, and we can easily identify `hello` when the shift is 13.

### Substitution Ciphers

Shift ciphers are a specific type of substitution cipher, where each letter is replaced by another letter based on a fixed shift. In a more general substitution cipher, each letter can be replaced by any other letter, not necessarily following a fixed pattern.

Here is a simple Python function that generates a random substitution table that can be used for encryption and decryption:

```python
import random

def get_random_table():
    letters = list("abcdefghijklmnopqrstuvwxyz")
    
    # create a shuffled copy of the letters
    shuffled = letters[:]
    random.shuffle(shuffled)

    # create the substitution table
    table = {}
    for i in range(len(letters)):
        table[letters[i]] = shuffled[i]
    return table
```

We can then use this table to encrypt and decrypt messages similarly to the shift cipher.

```python
def encrypt(plaintext, table):
    return substitute(plaintext, table)

def decrypt(ciphertext, table):
    # create the reverse substitution table
    reverse = {}
    for key in table.keys():
        value = table[key]
        reverse[value] = key

    return substitute(ciphertext, reverse)
```

### Breaking Substitution Ciphers

In the 9th century, [Al-Kindi](https://en.wikipedia.org/wiki/Al-Kindi) pioneered breaking substitution ciphers using letter frequency analysis. The intuition is simple:

- Pick a large  book and analyze the frequency of letters in the book to know which letters typically appear more than which letters.

- Analyze the frequency of letters in the encrypted message and try to decrypt the letters based on their frequency.

The work of Al-Kindi is considered to have paved the way for modern [cryptanalysis](https://en.wikipedia.org/wiki/Cryptanalysis). 

Here is a table showing the English language letter frequency:
<img alt="alt text" src="/11102-f25/lessons/images/frequency.png" class="img-soft" style="display:block; margin: 20px auto; width: 75%;">


### One Time Pads

To make frequency analysis ineffective, we can substitute each letter with a different letter each time it appears in the message.

To achieve this, let's go back to the shift cipher. Instead of using a fixed shift for the entire message, we can use a different shift for each letter in the message. This requires a key that is as long as the message itself, where each character in the key indicates the shift to be used for the corresponding character in the message.

**Example**
```
Message:  h e l l o
Key:      3 1 4 1 5
```
Using the above key, we would encrypt the message using shift 3 for `h`, shift 1 for `e`, shift 4 for `l`, shift 1 for the second `l`, and shift 5 for `o`.

The **key** is called a **one-time pad** because it is used only once for a single message. It is typically generated randomly to ensure security.

Here is a simple Python implementation of the one-time pad encryption. We'll assume the key is provided as a list of integers representing the shifts for each character in the plaintext.

```python
def encrypt(plaintext, key):
    result = ''
    for i in range(len(plaintext)):
        char = plaintext[i]
        shift = key[i]
        result += rot_encrypt(char, shift)
    return result
```

To decrypt the message, we simply use the `rot_decrypt` function instead of `rot_encrypt` in the above function.

### Problems With One-Time Pads

Let's assume that you liked to use one-time pads for sending messages to your friends. You will immediately run into the following problem:

> _How will you securely share the one-time pad (the key) with your friend before sending the encrypted message?_

This is known as the **key distribution problem**. If you can securely share the key, then you can simply share the message itself without encryption. However, if you cannot securely share the key, then the one-time pad is useless.

This problem is common to all encryption techniques that require a shared secret key. Next, we will explore some techniques to solve the key distribution problem.

## Public Key Cryptography

Alice and Bob don't know anything about encryption. They want to send messages to each other, but they are worried that someone might intercept their messages and read them.

Alice thought of putting the message in a box and locking it with a padlock. She would then send the locked box to Bob, who would unlock it with the key to the padlock. However, they are stuck, because this requires also sending the key to Bob, which means that if someone gets hold of the key and the box, they can open it and read the message.

### A Clever Solution

Alice and Bob arrived at a simple but clever solution using two padlocks:

1. Alice puts her message in a box and locks it with her padlock.
2. She sends the locked box to Bob.
3. Bob receives the locked box, but he cannot open it because he doesn't have the key to Alice's padlock.
4. Bob adds his own padlock to the box (now the box has two padlocks) and sends it back to Alice.
5. Alice receives the box, removes her padlock, and sends the box (still locked with Bob's padlock) back to Bob.
6. Bob receives the box and removes his padlock, finally opening the box and reading the message.

Now, they have successfully sent a message without ever sharing the keys to their padlocks. Even if someone intercepted the box at any point, they would not be able to open it because they would need both padlocks' keys.

This scenario illustrates the concept of **public key cryptography**, where communication can happen securely without sharing secret keys in advance.

### Public and Private Keys

In public key cryptography, each person has two keys:
1. **Public Key**: This key is shared with everyone. It is used to encrypt messages.
2. **Private Key**: This key is kept secret. It is used to decrypt messages.

Let's say Alice wants to send a message to Bob:
1. Bob shares his public key with Alice.
2. Alice uses Bob's public key to encrypt her message.
3. Alice sends the encrypted message to Bob.
4. Bob uses his private key to decrypt the message.

This way, even if someone intercepts the encrypted message, they cannot read it without Bob's private key.

Creating such public and private keys relies on complex mathematical calculations that are beyond the scope of this lesson. However, you can see public key cryptography in action in protocols like HTTPS, which secures your web browsing.

Here is a simple illustration of how public key cryptography works:
1. Open your browser and go to: `https://portal.psut.edu.jo/`
2. Click on the padlock (🔒) icon in the address bar to view the security details .
3. You will see information about the website's _certificate_, which includes a public
    key.

<img alt="SSL Certificate" src="/11102-f25/lessons/images/public-key.png" class="img-soft" style="display:block; margin: 20px auto; width: 75%;">

This key is the public key of `portal.psut.edu.jo`. Your browser uses this public key to encrypt any sensitive information (like your username and password) before sending it to the website. Only the website, which has the corresponding private key, can decrypt this information.

### Message Integrity

Alice wants to send a message to Bob. She does not care about confidentiality, but she wants to ensure that Bob knows the message is really from her and has not been altered on the way to him by an attacker. What can she do?

Alice can encrypt (sign) the message with her **private** key. Anyone who receives the message can decrypt (verify) it using Alice's **public** key. If the decryption is successful, Bob can be sure that the message was indeed sent by Alice (since only Alice has her private key) and that it has not been altered (since any change to the message would result in a failed decryption).

{: .warning-title }
> ⚠️ **NOTE**
>
> The above discussion is a simplified explanation to illustrate the basic concepts. In practice, integrity is not achieved by simply encrypting with the private key. Instead, techniques like digital signatures and hash functions are used to ensure message integrity and authenticity.

### Putting It All Together

Alice can combine both confidentiality and integrity by doing the following:

1. Encrypt the message with Bob's public key.
2. Encrypt (sign) the resulting ciphertext with her private key.

When Bob receives the message, he can do the following:
1. Decrypt (verify) the message with Alice's public key.
2. Decrypt the resulting ciphertext with his private key.

This way, Bob can be sure that the message is confidential (only he can read it) and that it is authentic (it was sent by Alice and has not been altered).

{: .warning-title }
> ⚠️ **NOTE**
>
> Again, the above is an oversimplified explanation to illustrate the basic concepts.

### A Note on Speed

Public key cryptography is computationally intensive and slower than encryption methods that use shared secret keys (like the one-time pad). They use complex mathematical operations that require more processing power.

In practice, public key cryptography is used not for encrypting large messages directly, but rather for securely exchanging a short shared secret key. Once both parties have established the shared secret key using public key cryptography, they can use faster encryption methods to encrypt and decrypt their messages using the shared secret key.