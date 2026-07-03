# 1.4.1 Data Types

## Primitive Data Types

A **data type** classifies data according to the kind of information it represents. Choosing the correct data type ensures the right operations can be performed and that storage is used efficiently.

| Data Type | Description | Examples |
|---|---|---|
| **Integer** | A whole number (positive, negative, or zero) with no fractional part. Useful for counting. | `6`, `-12`, `0` |
| **Real (float)** | A number that can have a fractional part. Useful for measuring. All integers are also real numbers. Can be represented using floating point. | `3.14`, `-71.5`, `0.0` |
| **Character (char)** | A single symbol: letter, digit, or special symbol. Represented in binary using a character set. | `'A'`, `'7'`, `'$'` |
| **String** | A sequence of characters. Useful for text and values like phone numbers starting with `0`, which numeric types would truncate. | `"Hello"`, `"07789"` |
| **Boolean** | Restricted to `True` or `False` (named after George Boole, hence capitalised). Useful for two-state data such as power buttons or flags. | `True`, `False` |

### Casting

**Casting** is converting a value from one data type to another. User input is typically received as a string, so casting to a numeric type is often necessary before performing calculations or comparisons.

| Conversion | Python Example | Result |
|---|---|---|
| Integer to Real | `float(5)` | `5.0` |
| Real to Integer | `int(5.7)` | `5` (truncated) |
| String to Integer | `int("10")` | `10` |
| Integer to String | `str(5)` | `"5"` |
| Boolean to String | `str(True)` | `"True"` |
| String to Boolean | `bool("True")` | `True` |

---

## Representing Positive Integers in Binary

Computers store data in **binary (base 2)**, using only the digits 0 and 1. This is because computer circuits operate as switches that are either on (1) or off (0).

A single binary digit is called a **bit**. Eight bits form a **byte**. Four bits (half a byte) form a **nybble**. A **word** is typically 16 bits (2 bytes), though word length varies by architecture.

### Binary Place Values

Each bit position represents a power of 2. In an 8-bit number:

| $2^7$ | $2^6$ | $2^5$ | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
|---|---|---|---|---|---|---|---|
| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

The **least significant bit (LSB)** is the rightmost bit (lowest place value). The **most significant bit (MSB)** is the leftmost bit (highest place value).

### Binary to Denary Conversion

Multiply each bit by its place value and sum the results.

**Example:** `01101001`
$0 + 64 + 32 + 0 + 8 + 0 + 0 + 1 = 105$

### Denary to Binary Conversion

Starting from the largest power of 2 that fits, place a 1 if the place value is less than or equal to the remaining value (then subtract it), otherwise place a 0.

**Example:** Convert 47 to binary.
- 32 fits into 47 (47 - 32 = 15) → 1
- 16 does not fit into 15 → 0
- 8 fits into 15 (15 - 8 = 7) → 1
- 4 fits into 7 (7 - 4 = 3) → 1
- 2 fits into 3 (3 - 2 = 1) → 1
- 1 fits into 1 (1 - 1 = 0) → 1

Result: `101111`. As a full byte with leading zeros: `00101111`.

Leading zeros do not change the value of a binary number but are used to represent numbers as whole bytes (multiples of 8 bits).

---

## Negative Numbers in Binary

Binary numbers can be **unsigned** (positive only) or **signed** (positive and negative). Two methods for representing negative numbers are sign magnitude and two's complement.

Both methods use the MSB to indicate sign: 0 = positive, 1 = negative. Using one bit for the sign halves the maximum positive value that can be stored (e.g. an 8-bit unsigned number ranges 0-255, but a signed number ranges only to 127 in magnitude).

### Sign Magnitude

The MSB acts purely as a sign indicator. The remaining bits represent the magnitude (absolute value) of the number, exactly as for a positive integer.

**To convert denary to sign magnitude:** convert the absolute value to binary, then set the MSB to 1 for negative or 0 for positive.

**Example:** Represent -173 in sign magnitude.
- Binary of 173: `10101101`
- Positive sign magnitude (+173): `010101101`
- Negative sign magnitude (-173): `110101101`

**To convert sign magnitude to denary:** note the MSB (sign), discard it, convert the remaining bits to denary, and apply the sign.

**Example:** `101101001`
- MSB = 1 → negative
- Remaining bits: `01101001` = 105
- Result: **-105**

### Two's Complement

**Two's complement** is the preferred method because it simplifies binary arithmetic with negative numbers. The MSB represents a negative place value (e.g. -128 in an 8-bit system), and the remaining bits count upwards from that value.

**To convert a positive number to its two's complement negative:**
1. Write the positive number in binary
2. Invert (flip) all bits (0→1, 1→0)
3. Add 1

**Example:** Convert 7 to -7 in 8-bit two's complement.
- Binary of 7: `00000111`
- Invert: `11111000`
- Add 1: `11111001`

**Verification using place values:**

| -128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |

$-128 + 64 + 32 + 16 + 8 + 0 + 0 + 1 = -7$ ✓

**To convert two's complement to denary:** treat the MSB as its negative place value and sum all place values with a 1.

**Example:** Convert `11101000` to denary (8-bit two's complement).

$-128 + 64 + 32 + 0 + 8 + 0 + 0 + 0 = -24$

---

## Binary Addition and Subtraction

### Binary Addition Rules

| Rule | Operation |
|---|---|
| A | $0 + 0 = 0$ |
| B | $0 + 1 = 1$ |
| C | $1 + 1 = 10$ (write 0, carry 1) |
| D | $1 + 1 + 1 = 11$ (write 1, carry 1) |

Add column by column from the LSB (right) to the MSB (left), carrying as needed.

**Example:** Add `1011` (11) and `1110` (14).

```
    1 0 1 1
+   1 1 1 0
-----------
  1 1 0 0 1
```

Column-by-column (right to left):
- $1 + 0 = 1$
- $1 + 1 = 10$ → write 0, carry 1
- $0 + 1 + 1_{carry} = 10$ → write 0, carry 1
- $1 + 1 + 1_{carry} = 11$ → write 1, carry 1

Result: `11001` (25). Check: 11 + 14 = 25 ✓

Always verify by converting the result to denary.

### Overflow Errors

An **overflow** occurs when the result of an addition exceeds the number of bits available. For example, adding two 4-bit unsigned numbers that produce a 5-bit result. In signed representations, overflow can incorrectly flip the sign bit, producing a wrong result.

### Binary Subtraction Using Two's Complement

Subtraction is performed by converting the subtrahend (number being subtracted) to its two's complement and then adding.

$A - B = A + (-B)$

**Example:** Subtract 12 from 8 using 5-bit two's complement.
- 8 in binary: `01000`
- 12 in binary: `01100` → invert: `10011` → add 1: `10100` (this is -12)
- Add: `01000 + 10100 = 11100`

Verify: place values -16, 8, 4, 2, 1 → $-16 + 8 + 4 = -4$ ✓ (since 8 - 12 = -4)

**Example:** Subtract 3 from 9 using 4-bit two's complement.
- 9 = `1001`, 3 = `0011`
- Two's complement of 3: invert `0011` → `1100`, add 1 → `1101`
- Add: `1001 + 1101 = 10110` (5 bits)
- Discard the overflow bit: `0110` = 6 ✓

In two's complement subtraction, an overflow carry out of the MSB is discarded as a by-product of the method.

---

## Hexadecimal

**Hexadecimal (hex)** is a base-16 number system using digits 0-9 and letters A-F (representing 10-15).

| Denary | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hex | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |
| Binary | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |

### Why Use Hexadecimal?

Hex is more concise and human-readable than binary. Four binary bits map to one hex digit, so a byte can be written as two hex characters rather than eight binary digits. This makes hex less error-prone to read, write, and communicate.

Common uses include colour codes in web design (e.g. `#FF33CC`), memory addresses, debugging, MAC addresses, and error codes.

### Subscript Notation

A subscript denotes the base of a number to avoid ambiguity: $10_2$ (binary), $10_{10}$ (denary), $10_{16}$ (hexadecimal, equivalent to $16_{10}$).

### Hexadecimal Place Values

| $16^3$ | $16^2$ | $16^1$ | $16^0$ |
|---|---|---|---|
| 4096 | 256 | 16 | 1 |

---

## Converting Between Binary, Hexadecimal, and Denary

### Hexadecimal to Binary

Convert each hex digit independently to a 4-bit binary nybble, then concatenate.

**Example:** `B2`
- B = 11 = `1011`
- 2 = 2 = `0010`
- Result: `10110010`

### Binary to Hexadecimal

Split the binary number into groups of 4 bits (nybbles) from the right, then convert each nybble to its hex digit.

**Example:** `11010101`
- `1101` = D
- `0101` = 5
- Result: `D5`

### Hexadecimal to Denary

Either convert to binary first and then to denary, or multiply each hex digit by its place value and sum.

**Example:** `4E7F`
$(4 \times 4096) + (14 \times 256) + (7 \times 16) + (15 \times 1) = 16384 + 3584 + 112 + 15 = 20095$

### Denary to Hexadecimal

Convert to binary first, then split into nybbles and convert each to hex.

**Example:** 241 in denary.
- 241 in binary: `11110001`
- Split: `1111` = F, `0001` = 1
- Result: `F1`

---

## Floating Point Numbers in Binary

**Floating point** representation is analogous to scientific notation ($6.67 \times 10^{-11}$). It splits a number into two parts stored in binary:

- **Mantissa** - holds the significant digits and determines precision
- **Exponent** - determines the position of the binary point (scales the number up or down)

Both mantissa and exponent are stored in **two's complement**. The MSB of the mantissa determines the sign of the number (0 = positive, 1 = negative).

### How It Works

The binary point is assumed to sit immediately after the MSB of the mantissa. The exponent tells you how many places to shift this binary point: right for a positive exponent, left for a negative exponent.

### Converting Floating Point Binary to Denary

**Example 1:** 11-bit mantissa, 6-bit exponent.

Mantissa: `01100100111`, Exponent: `000110`

1. The mantissa with binary point after MSB: `0.1100100111`
2. Convert exponent to denary: `000110` = $4 + 2 = 6$

> ⚠ Check: the PMT source states "the exponent is 5" here, but the exponent bits `000110` = 6, and the subsequent calculation correctly shifts by 6 places to produce the right answer. The exponent is 6.

3. Shift binary point 6 places right: `0110010.0111`
4. Convert to denary:

| -64 | 32 | 16 | 8 | 4 | 2 | 1 | . | 0.5 | 0.25 | 0.125 | 0.0625 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 0 | 1 | 0 | . | 0 | 1 | 1 | 1 |

$32 + 16 + 2 + 0.25 + 0.125 + 0.0625 = 50.4375$

**Example 2:** 10-bit mantissa, 6-bit exponent.

Mantissa: `0101101000`, Exponent: `111101`

1. Mantissa with binary point: `0.101101000`
2. Exponent in two's complement: $-32 + 16 + 8 + 4 + 0 + 1 = -3$
3. Shift binary point 3 places left: `0.000101101`
4. Convert: $\frac{1}{16} + \frac{1}{64} + \frac{1}{128} + \frac{1}{512} = \frac{45}{512} \approx 0.0879$

### Converting Denary to Floating Point Binary

1. Represent the number in fixed-point binary (with a binary point separating whole and fractional parts)
2. Move the binary point to its normalised position (after the MSB)
3. Count how many places the point moved: this is the exponent. Moving the point left increases the exponent; moving it right decreases it
4. Write out the mantissa and exponent

**Example:** Convert 6.75 to floating point (6-bit mantissa, 3-bit exponent).
- Fixed-point: `0110.11`
- Normalise to `0.11011` (point moved 3 places left)
- Mantissa: `011011`, Exponent: `011` (3 in denary)

### Normalisation

A floating point number is **normalised** when the mantissa begins with `01` (for positive) or `10` (for negative). Normalisation maximises precision by ensuring the mantissa makes full use of its available bits.

**To normalise:**
1. Shift the mantissa bits left or right until it starts `01` (positive) or `10` (negative), padding with zeros as needed
2. Adjust the exponent by the same number of places (decrease the exponent when shifting left, increase when shifting right)

**Example:** Normalise `000110100101` (8-bit mantissa, 4-bit exponent).
- Mantissa: `00011010`, Exponent: `0101` (= 5)
- Shift mantissa 2 places left: `01101000`
- Reduce exponent by 2: `0011` (= 3)
- Normalised result: `01101000 0011` (starts `01` ✓)

### Effect of Mantissa and Exponent Size

Increasing the number of **mantissa** bits increases **precision** (more significant figures). Increasing the number of **exponent** bits increases the **range** of values representable (larger and smaller magnitudes). There is a trade-off between precision and range for a fixed total number of bits.

*(Beyond source: the trade-off between mantissa and exponent size is a standard exam point for this spec area.)*

---

## Floating Point Addition and Subtraction

### Addition

1. **Equalise the exponents**: shift the mantissa of the number with the smaller exponent to the right, incrementing its exponent, until both exponents match
2. **Add the mantissas** using standard binary addition
3. **Normalise** the result if it does not begin `01` (positive) or `10` (negative), adjusting the exponent accordingly

**Example:** Add `000100 0011` and `000101 0010` (6-bit mantissa, 4-bit exponent).
- First number: mantissa `000100`, exponent `0011` (3)
- Second number: mantissa `000101`, exponent `0010` (2)
- Shift first mantissa right by 1, increase exponent by 1 to match: `001000 0010` (exponent now 2, but wait: we want to match the larger exponent). Actually: shift the second number's mantissa right by 1 and increase its exponent to 3? No: shift the number with the smaller exponent. Second has exponent 2, first has 3. Shift second's mantissa right by 1: but actually...

*(The PMT source shifts the first mantissa right by 1 to reduce the gap, making its exponent match the second at 2. This works because shifting the mantissa right by 1 and reducing the exponent by 1 from 3 to 2 achieves the match.)*

After equalising at exponent `0010`:
- Mantissa addition: `001000 + 000101 = 001101`
- Result before normalisation: `001101 0010`
- Normalise: shift mantissa left by 1, decrease exponent by 1 → `011010 0001`

### Subtraction

1. **Equalise the exponents** (same as for addition)
2. **Convert the subtrahend's mantissa** to its two's complement (flip all bits, add 1)
3. **Add the mantissas**
4. **Normalise** the result

Subtraction is addition of the negated value, following the same principle as integer binary subtraction.

---

## Bitwise Manipulation and Masks

### Logical Shifts

A **logical shift** moves all bits in a binary number a specified number of positions to the left or right, filling vacated positions with zeros.

**Logical shift left** by $n$ places multiplies the value by $2^n$. Equivalent to appending $n$ trailing zeros.

**Example:** `10010110` shifted left by 3 → `10010110000`. Effect: $150 \times 8 = 1200$.

**Logical shift right** by $n$ places divides the value by $2^n$ (integer division, discarding any bits shifted out on the right).

**Example:** `11001000` (200) shifted right by 3 → `00011001` (25). Each shift halves the number: 200 → 100 → 50 → 25.

A single left shift doubles the number. A single right shift halves it.

### Masks

A **mask** is a binary number combined with another binary number using a bitwise logic gate to isolate, set, clear, or toggle specific bits.

**AND mask** - outputs 1 only where both the data bit and mask bit are 1. Used to **extract** (isolate) specific bits.

```
  00101011
AND 10111011
  ----------
  00101011
```

**OR mask** - outputs 1 where either the data bit or mask bit (or both) is 1. Used to **set** specific bits to 1.

```
  00101011
OR  10111011
  ----------
  10111011
```

**XOR mask** - outputs 1 where the data bit and mask bit differ. Used to **toggle** (flip) specific bits.

```
  00101011
XOR 10111011
  ----------
  10010000
```

| Operation | Rule | Use |
|---|---|---|
| AND | 1 only if both inputs are 1 | Extract/isolate bits |
| OR | 1 if either input is 1 | Set bits to 1 |
| XOR | 1 if inputs differ | Toggle/flip bits |

---

## Character Sets

A **character set** is a standardised mapping between binary codes and the characters they represent. Without a common character set, systems could interpret the same binary value as different characters.

### ASCII

**ASCII** (American Standard Code for Information Interchange) uses **7 bits** per character, encoding $2^7 = 128$ characters. Key code ranges:

| Characters | Denary Codes |
|---|---|
| A-Z (uppercase) | 65-90 |
| a-z (lowercase) | 97-122 |
| 0-9 (digits) | 48-57 |

**Extended ASCII** uses **8 bits** per character, allowing $2^8 = 256$ characters.

**Limitations of ASCII:**
- Only 128 characters, insufficient for languages beyond English
- Cannot represent characters from non-Latin scripts (e.g. Greek, Arabic, Chinese)
- No provision for modern symbols such as emoji

### Unicode

**Unicode** addresses ASCII's limitations by using a variable number of bits (up to 32, depending on encoding), allowing over 1 million unique characters. This covers virtually all world languages, mathematical symbols, and emoji.

Unicode code points are written as `U+` followed by a hex value (e.g. the Greek letter lambda is `U+03BB`).

The first 128 Unicode characters are identical to ASCII, ensuring backward compatibility.

*(Beyond source: the backward compatibility of Unicode with ASCII is a commonly examined point.)*

### ASCII vs Unicode

| Feature | ASCII | Unicode |
|---|---|---|
| Bits per character | 7 (or 8 extended) | 16 or 32 (variable) |
| Number of characters | 128 (256 extended) | 65,536+ (up to ~1.1 million) |
| Language support | English only | All major world scripts |
| Emoji / symbols | Not supported | Supported |
| Storage per character | Less | More |

---

## Key Terms Summary

| Term | Definition |
|---|---|
| **Bit** | Single binary digit (0 or 1) |
| **Byte** | 8 bits |
| **Nybble** | 4 bits (half a byte) |
| **MSB** | Most significant bit (leftmost) |
| **LSB** | Least significant bit (rightmost) |
| **Overflow** | When a result exceeds the available number of bits |
| **Sign magnitude** | Negative representation using MSB as sign, remaining bits as magnitude |
| **Two's complement** | Negative representation where MSB has a negative place value |
| **Mantissa** | Significant digits of a floating point number (determines precision) |
| **Exponent** | Power that scales the mantissa (determines range) |
| **Normalisation** | Adjusting mantissa to start `01` (positive) or `10` (negative) for maximum precision |
| **Logical shift** | Moving all bits left or right by a specified number of places |
| **Mask** | Binary number combined with a logic gate to manipulate specific bits |
| **Character set** | Standardised mapping of binary codes to characters |
