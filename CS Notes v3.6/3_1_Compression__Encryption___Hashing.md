# 1.3.1 Compression, Encryption and Hashing

## Compression

**Compression** is the process of reducing the file size of data so that more files can be stored in the same amount of storage space. Compression is particularly important for transferring files over networks or the Internet: larger files take longer to transfer, so compressing files results in faster **transmission times** and lower **bandwidth consumption**. Applications such as Google Photos compress files so they can be quickly searched for and downloaded.

### Lossy vs Lossless Compression

There are two categories of compression: **lossy** and **lossless**.

**Lossy compression** reduces the size of a file by permanently removing some of its data. The discarded data is chosen to minimise perceptible quality loss, for example removing very high or very low audio frequencies that are least noticeable to the human ear, or reducing colour depth in images. The result may be a more pixelated image or less clear audio recording. Because the removed data is completely discarded, the original file cannot be recovered from the lossy-compressed version. The process is **irreversible**.

**Lossless compression** reduces the size of a file without losing any information. The original file can be fully recovered (reconstructed) from the compressed version, preserving complete **data integrity**.

| | Lossy | Lossless |
|---|---|---|
| **Data loss** | Some data permanently discarded | No data lost |
| **Reversibility** | Irreversible | Fully reversible |
| **File size reduction** | Greater reduction | Smaller reduction than lossy |
| **Benefits** | Greatly reduced file sizes, suitable for **media streaming** where some loss is acceptable | Maintains **original data**, best for text and data requiring integrity |
| **Drawbacks** | Irreversible loss of quality, not suitable for text or **archival storage** | Larger file sizes than lossy, requires higher bandwidth when streaming |
| **Example formats** | JPEG, MP3, MP4 | PNG, FLAC, ZIP |

**Recommending a compression type:** evaluate the application's requirements. If **data integrity** is imperative (e.g. text files, program code, archival storage), recommend **lossless compression**. If achieving a **small file size** or **quick data transfer** is prioritised and some data loss is acceptable (e.g. social media images, streaming media), choose **lossy compression**. The choice always depends on the specific scenario requirements.

**Worked example (method).** A high-resolution logo for a client's brand identity requires **lossless** compression because pixel-perfect clarity must be preserved for professional printing and high-definition media. A social media campaign image suits **lossy** compression because the significant file size reduction allows faster uploads and loading, and the slight quality degradation is acceptable given the platform's fast-paced, transient nature.

> *(Beyond source: PNG is a common lossless image format; JPEG is a common lossy image format. FLAC and ZIP are common lossless formats for audio and general data respectively.)*

### Run Length Encoding

**Run length encoding (RLE)** is a form of **lossless compression** that condenses consecutive identical elements into a single value paired with a count.

How it works: repeated consecutive values are removed and replaced with one occurrence of the data item together with the number of times it is repeated.

**Example (value-then-count notation):** The string `AAAAAABBBBBCCC` is compressed to `A6B5C3`, meaning A repeated 6 times, B repeated 5 times, C repeated 3 times.

**Example (count-then-value notation):** The string `AAAABBBCCDAA` is compressed to `4A3B2C1D2A`, meaning 4 As, 3 Bs, 2 Cs, 1 D, 2 As.

> *(Beyond source: both notations are valid RLE representations. Exam questions will specify the convention to use.)*

RLE is used in bitmap images to compress sequences of the same colour. For instance, a line with 5 red pixels followed by 3 blue pixels could be represented as `5R3B`.

**Limitation:** RLE relies on consecutive pieces of data being the same. If there is little repetition in the data, RLE does not offer a great reduction in file size and may even increase it (each unique element still needs a count).

**Worked example (decompression).** The RLE sequence `3C3M4C` decompresses to `CCCMMMCCCC` by repeating each character the number of times indicated.

**Worked example (compression).** The raw sequence `CCCCOLLLCCCCCMOCCCCC` compresses to `4C1O3L5C1M1O5C` by counting consecutive occurrences of each character.

**Worked example (pseudocode).** A function `longest` takes a string and returns the length of the longest continuous run of 'C' characters:

```
function longest(s)
    max_count = 0
    current_count = 0
    for each char in s
        if char == 'C' then
            current_count = current_count + 1
            if current_count > max_count then
                max_count = current_count
            endif
        else
            current_count = 0
        endif
    endfor
    return max_count
endfunction
```

This iterates through the string, incrementing a counter for consecutive 'C' characters and resetting it when a different character is encountered, while tracking the maximum count seen.

### Dictionary Encoding

**Dictionary encoding** (also called **dictionary coding**) is another method of **lossless compression**. Frequently occurring pieces of data (words, phrases, or byte sequences) are replaced with shorter unique codes (indices). The compressed data is stored alongside a **dictionary** that maps each index back to the original data, allowing the original to be fully restored.

This method is effective for both **text** and **binary data**.

**Example.** Given the passage:

*We shall go on to the end. We shall fight in France, we shall fight on the seas and oceans, we shall fight with growing confidence and growing strength in the air, we shall defend our island, whatever the cost may be.*

Frequently occurring phrases ("We shall", "fight", "the", "on", "in", "and") are assigned dictionary indices:

| Index | Phrase |
|---|---|
| 1 | We shall |
| 2 | fight |
| 3 | the |
| 4 | on |
| 5 | in |
| 6 | and |

The passage becomes: `1 go 4 to 3 end. 1 2 5 France, 1 2 4 3 seas 6 oceans, 1 2 with growing confidence 6 growing strength 5 3 air, 1 defend our island, whatever 3 cost may be.`

The original passage was **95 characters** long; the dictionary-coded version is **53 characters** long. The shorter string requires **less space** in memory or storage.

**Critical point:** data compressed using dictionary encoding must be transferred **alongside its dictionary**. Without the dictionary, the compressed data cannot be decoded and is unusable.

**RLE vs Dictionary Coding comparison:** RLE is more effective when data has lots of consecutive repetition. Dictionary coding is more versatile (handles non-consecutive repetition and longer patterns) but may require more computational resources to build and maintain the dictionary.

## Encryption

**Encryption** is the process of converting **readable data** (plaintext) into an **unreadable format** (ciphertext) to **secure** data from **unauthorised access** during transmission or storage. Encryption methods use **keys**, which are specialised algorithms/programs designed to **scramble** (encrypt) or **unscramble** (decrypt) data. Modern devices and technologies (e.g. web browsers using the HTTPS protocol) provide a basic level of encryption by default, meaning most people transfer sensitive data **without thinking about it**.

### Symmetric Encryption

In **symmetric encryption**, both the sender and receiver share the **same private key**. This key is distributed between them in a process called a **key exchange** and is used for both **encrypting and decrypting** data.

The private key must be kept **secret**. If the key is intercepted during the key exchange, a **bad actor** can **decrypt all messages intercepted** in transmission.

Symmetric encryption is usually **faster** than asymmetric encryption, making it ideal for encrypting **large amounts of data** (e.g. bulk file encryption, database encryption). The significant downside is **the challenge of securely sharing this key** between sender and receiver.

**How it works (diagram description):** The sender encrypts a plaintext message (e.g. "Hello!") using the shared key, producing ciphertext (e.g. "¤%&=%&..."). This ciphertext is transmitted over the network. The receiver decrypts the ciphertext using the same shared key, recovering the original plaintext ("Hello!"). Both sides use identical keys.

### Asymmetric Encryption

**Asymmetric encryption** uses **two keys**: a **public key** for encryption and a **private key** for decryption. Together these form a **key pair** and are **mathematically related** to one another. The public key can be published **anywhere** (freely available to anyone), while the private key must be kept secret and is stored locally by its owner.

Unlike symmetric encryption, a single key cannot both encrypt and decrypt. Messages encrypted with the recipient's **public key** can only be decrypted with the recipient's **private key**, which should only be in the possession of the recipient. The public and private keys are created at the same time and are **designed to work together**.

**Sending a confidential message:** If someone wants to send you a message, they find your public key (e.g. from a key server), encrypt the message with it, and transmit it. **Only you** can decrypt it using your private key.

**Digital signatures:** If you want to prove a message was sent by you, you encrypt it using your **private key**. **Anyone can decrypt it** using your public key (which is freely available), and by successfully doing so, they can verify that only you could have encrypted it (since only you hold the private key). This forms the basis of **digital signatures**.

Asymmetric encryption is typically **slower than symmetric encryption**. It is generally used for **more secure and smaller** data transactions, such as **passwords**, **bank details**, and government communications.

**How it works (diagram description):** Alice wants to send a confidential message ("CALL ME TODAY") to Bob. Alice encrypts the message using Bob's public key, producing ciphertext ("dh12#djdi2+rg"). Bob decrypts the ciphertext using his private key (which only he holds), recovering the original message. Even if the ciphertext is intercepted, it cannot be decrypted without Bob's private key.

### Choosing an Encryption Type

| Encryption Type | Suitable For | Reasons to Choose |
|---|---|---|
| **Symmetric** | Large files, databases | Fast and efficient for bulk data. The same person encrypts and decrypts, e.g. when backing up data. |
| **Asymmetric** | Confidential/secret communications | Sharing highly secure data, e.g. passwords, government communications. Solves the key distribution problem. |

**Symmetric encryption is fast** but has key-sharing issues; **asymmetric is slower** but solves those issues. The choice depends on the **situation's needs**: whether **speed** or **security** is more critical.

**Societal impact of encryption:** Encryption is critical for protecting people from data misuse. Asymmetric encryption forms the backbone of secure online transactions and communications (digital signatures, secure key exchange). Symmetric encryption enables fast encryption of large datasets within secure networks. However, highly secure communication methods can also be exploited for nefarious purposes such as organised crime. Both methods together enable secure data transmission, enhance online commerce, and protect individual privacy.

## Hashing

**Hashing** is a process in which an input (called a **key**) is converted into a **fixed-size** string of characters (called a **hash** or **digest**) using a **hash function** (algorithm). The same input always produces the same hash, providing **consistency**. Even a minor change in the input produces a radically different hash, giving it **sensitivity to data changes**.

| Input Text | Hash Algorithm | Truncated Hash Digest |
|---|---|---|
| "hello123" | SHA-256 | 8d9389d5a0375bd6b028bc0368003333 |
| "hello124" | SHA-256 | 9ac12bac3a0843a1917b1c4a0f77a76d |
| "password1" | SHA-256 | e99a18c428cb38d5f260853678922e03 |
| "password2" | SHA-256 | ad0234829205b9033196ba818f7a872b |

Unlike encryption, the output of a hash function **cannot be reversed** to recover the original input. Hashing is a **one-way function**.

### Common Hashing Algorithms

| Algorithm | Status |
|---|---|
| **MD5** (Message Digest 5) | Widely used but considered weak due to **vulnerabilities to collision attacks** |
| **SHA-1** (Secure Hash Algorithm 1) | Previously used in **SSL certificates** and **software repositories**, now considered weak |
| **SHA-256** (part of the SHA-2 family) | Used in **cryptographic applications** and **data integrity checks**, considered secure for most practical purposes |
| **SHA-3** | Most recent member of the **Secure Hash Algorithm family**, designed for higher levels of **security** |

### Comparison of Encryption and Hashing

| | Encryption | Hashing |
|---|---|---|
| **Purpose** | Securing data for transmission or storage; reversible | Data verification, quick data retrieval; irreversible |
| **Reversibility** | Can be decrypted to original data | Cannot be reversed to original data |
| **Keys** | Uses keys for encryption and decryption | No keys involved |
| **Processing speed** | Generally slower for strong methods | Generally faster |
| **Use cases** | Secure communications, file storage | Password storage, data integrity checks |
| **Algorithm types** | Symmetric, Asymmetric | MD5, SHA-1, SHA-256, etc. |
| **Security** | Varies; depends on key management | One-way function; secure but susceptible to collisions |
| **Data length** | Output length varies; could be same or longer than input | Fixed-length output |
| **Change in output** | Small input change produces significantly different output | Small input change produces significantly different output |
| **Typical operations** | Encrypt, Decrypt | Hash, Verify |

### Uses of Hashing

**Password storage.** Hashing is commonly used for storing passwords securely:

1. When the user first signs up, the password they provide is **hashed**.
2. The **hashed password** is stored in the database, not as plaintext.
3. When users log in, the system **hashes the password entered by the user during the login** attempt.
4. The hashed password is **compared against the stored hash** in the database.
5. If the hashes match, the user is **authenticated** and granted access. If they do not match, access is denied.

**Security benefits:** Even if the **database** is compromised, the attacker only gains access to the **hashed passwords**, which cannot be reversed to obtain the original passwords. Not storing passwords in plaintext minimises the risk and potential legal repercussions of a **data breach**. Users' **raw passwords** are not exposed, reducing the impact of any breach. Since the hash function always produces the same output for the same input, password verification is quick.

**Hash tables.** A **hash table** is a data structure that holds **key-value pairs**. It is formed from a **bucket array** and a **hash function**, and allows data lookup in **constant time** ($O(1)$ average case). When data needs to be inserted, it is used as the key for the hash function and stored in the bucket corresponding to the resulting hash. Hash tables are used extensively in **caches** and **databases** where large amounts of data need to be stored with constant access times.

**Hash table diagram description:** Keys (e.g. "John Smith", "Lisa Smith", "Sam Doe", "Sandra Dee") are passed through a hash function. Each key maps to an index in a bucket array (indices 00 to 15). "John Smith" maps to 01, "Lisa Smith" to 02, "Sam Doe" to 04, and "Sandra Dee" also to 02, creating a collision.

A good **hash function** should uniformly distribute keys across the hash table, resulting in a balanced and efficient data retrieval. It is computationally more **efficient** to **query using the hash digest** value than other attributes, because hash digests have a fixed length, making it **easier** for the computer to compare them **rather than variable-length strings** like email addresses.

**Data integrity verification.** When data is **transferred** over a network, it is susceptible to **loss of packets** or **malicious interference**. Hashing enables verification of **integrity of data**: if the **same data** hashed by the **same hashing function** produces the **same digest** at both ends, the data has not been altered during transmission. Comparing two fixed-size hashes is **computationally less intensive** than full string comparison.

### Collisions

If two different pieces of data (keys) produce the **same** hash, a **collision** is said to have occurred. Methods to resolve collisions include:

- Storing items **together in a list** (chaining) under the same hash value
- Using a **second hash function** to generate a new hash (rehashing/open addressing)

### Properties of a Good Hash Function

A good hash function should:

- Have a **low chance of collision** (distribute keys uniformly)
- Be **quick to calculate**
- Produce an output that is **smaller than the input**, otherwise searching for the hash could take longer than simply searching for the key directly

**Worked example (hashing a URL).** A hash function processes a website URL as follows: (1) remove characters up to and including the first dot, (2) remove characters from and after the next dot, (3) convert to uppercase, (4) sum the ASCII values. For `www.exam.net`: step 1 gives `exam.net`, step 2 gives `exam`, step 3 gives `EXAM`, step 4 gives $69 + 88 + 65 + 77 = 299$. For `www.foo.co.uk`: step 1 gives `foo.co.uk`, step 2 gives `foo`, step 3 gives `FOO`, step 4 gives $70 + 79 + 79 = 228$.

**Worked example (pseudocode for hash function):**

```
function hash(siteName)
    firstDot = locate(siteName, ".")
    remainingString = siteName[firstDot + 1:]
    secondDot = locate(remainingString, ".")
    requiredString = upper(remainingString[:secondDot])
    sum = 0
    for each char in requiredString
        sum = sum + asc(char)
    endfor
    return sum
endfunction
```

This uses `locate()` to find dot positions, string slicing to extract the domain name, `upper()` to convert to uppercase, and `asc()` to get ASCII values for summation.

## Key Terms Summary

| Term | Definition |
|---|---|
| **Compression** | Reducing file size to save storage space and speed up data transfer |
| **Lossy compression** | Compression that permanently removes some data; irreversible |
| **Lossless compression** | Compression that preserves all original data; fully reversible |
| **Run length encoding (RLE)** | Lossless compression replacing consecutive repeated values with a value-count pair |
| **Dictionary encoding** | Lossless compression replacing frequent data patterns with shorter index codes stored in a dictionary |
| **Encryption** | Converting readable data into an unreadable format to prevent unauthorised access |
| **Symmetric encryption** | Encryption using a single shared private key for both encryption and decryption |
| **Asymmetric encryption** | Encryption using a public key (encrypt) and private key (decrypt) pair |
| **Key exchange** | Process of distributing a shared key between sender and receiver in symmetric encryption |
| **Key pair** | The mathematically related public and private keys used in asymmetric encryption |
| **Digital signature** | Authentication method where the sender encrypts with their private key to prove identity |
| **Hashing** | One-way process converting input into a fixed-size hash/digest |
| **Hash function** | Algorithm that performs the hashing conversion |
| **Digest** | The fixed-size output of a hash function |
| **Hash table** | Data structure using a hash function and bucket array for constant-time key-value lookup |
| **Collision** | When two different inputs produce the same hash value |
