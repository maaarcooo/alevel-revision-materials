# 1.3.2 Databases

## Relational Databases

A **database** is an organised collection of data that allows easy storage, retrieval, and management of information. Electronic databases offer key benefits: data is easier to add, delete, modify, and update; data can be backed up and copied more easily; and multiple users from multiple locations can access the same database simultaneously.

A **Database Management System (DBMS)** is software used to create and manage databases. Examples include MySQL, Oracle, Microsoft SQL Server, and PostgreSQL.

### Core Terminology

| Term | Definition |
|------|-----------|
| **Field** | A single piece of data in a record (also called an attribute or column) |
| **Record** | A group of related fields representing one complete data entry (a row) |
| **Table** | A collection of records with a similar structure |
| **Entity** | An item of interest about which information is stored (becomes a table in a relational database) |
| **Attribute** | A characteristic of an entity; a category about which data is collected |

### Flat File Databases

A **flat file** database consists of a single file (one table). It is typically based around a single entity and its attributes. Flat files are written in the notation:

**EntityName**(<u>Attribute1</u>, Attribute2, Attribute3, ...)

where the underlined attribute is the primary key.

**Example:** `Car(`<u>`CarID`</u>`, Age, Price)`

Flat files are simple to understand but cause **data redundancy** (the same data repeated across records), **inefficient storage**, and are **harder to maintain**. If data such as a tutor's name changes, every record containing that name must be found and updated individually. Missing any instance causes **inconsistent data**.

### Relational Databases

A **relational database** organises data into multiple linked tables, one per entity. It uses keys to connect related data, which reduces data redundancy, makes efficient use of storage, and is easier to maintain. Because each piece of data is stored only once, changing it in one place updates it across the entire database, avoiding inconsistency.

### Primary Keys

A **primary key** is a unique identifier for each record in a table. No two records may share the same primary key value. In entity notation, the primary key is shown by underlining it.

A **compound primary key** (also called a **composite primary key**) is a combination of two or more fields that together uniquely identify each record. Neither field alone is unique, but their combination is.

### Foreign Keys

A **foreign key** is an attribute in one table that refers to the primary key of another table. It creates a link (relationship) between the two tables. In entity notation, the foreign key is shown using an asterisk (*).

**Example:** In a Doctor-Patient system, `DoctorID` is the primary key in the Doctor table and appears as a foreign key in the Patient table, linking each patient to their doctor.

### Secondary Keys

A **secondary key** is a field (or fields) that is indexed for faster searching. Users rarely query by primary key because they do not normally remember ID numbers. A secondary key is set up on a commonly searched attribute (e.g. surname) so the database can be ordered and searched efficiently on that field.

### Indexing

**Indexing** is a technique for storing the position of each record ordered by a given attribute, enabling fast lookup and retrieval. It works like the index of a book: rather than scanning every page, you look up the term in the index to go directly to the right location.

The primary key is **automatically indexed**. However, since users rarely search by primary key, **secondary keys** are indexed to speed up searches on commonly queried fields. Indexing allows the DBMS to skip to the relevant records directly instead of examining every record sequentially.

---

## Entity Relationship Modelling

An **entity** is something worthy of capturing and storing data about (e.g. students, orders, products, customers). Entities become tables in a relational database.

### Relationship Types

There are three types (degrees) of relationships between entities:

| Relationship | Description | Example |
|-------------|-------------|---------|
| **One-to-one** | Each entity instance links to exactly one instance of the other entity | Husband — Wife |
| **One-to-many** | One instance of entity A links to many instances of entity B, but each instance of B links to only one A | Doctor — Patient (one doctor treats many patients) |
| **Many-to-many** | Instances of entity A link to many instances of entity B and vice versa | Students — Courses (each student takes many courses; each course has many students) |

### Entity Relationship Diagrams (ERDs)

An **ERD** represents the entities (tables) in a database and the relationships between them. Entities are drawn as boxes with the entity name inside. Relationships are drawn using **crow's feet notation**:

- **One-to-one:** a single line connecting both entities
- **One-to-many:** a single line on the "one" side, a branching crow's foot on the "many" side
- **Many-to-many:** crow's feet on both sides

ERDs reveal two important things: the names of all tables, and which tables will contain a foreign key. When an entity has a "many" relationship against it, that table will contain a foreign key linking to the primary key of the connected entity.

### Resolving Many-to-Many Relationships

Many-to-many relationships **cannot be directly implemented** in a relational database. They must be resolved by creating a **link table** (also called a junction or bridge table) between the two entities. This converts one many-to-many relationship into two one-to-many relationships. The link table typically contains the primary keys of both original tables as foreign keys, and together they form a composite primary key.

---

## Data Normalisation

**Normalisation** is the process of organising a relational database to achieve the best possible layout. Its goals are to reduce data duplication, improve data accuracy and consistency, ensure records can be added and removed without issues, and allow complex queries to be carried out.

### First Normal Form (1NF)

A table is in 1NF if it satisfies all of the following:

- **Atomic values:** each column contains only single, indivisible values (no lists or arrays in a field)
- **No repeating groups:** columns must not contain multiple values of the same type
- **Unique column names:** each column has a distinct name within the table
- **A unique identifier (primary key):** each row is distinguishable from all others

**Example of a 1NF violation:** a "Name" field containing "John Smith" is not atomic because it combines first name and surname. Splitting it into "FirstName" and "Surname" fields makes each value atomic.

### Second Normal Form (2NF)

A table is in 2NF if:

- It is already in **1NF**
- It has **no partial dependencies**: every non-key attribute is fully dependent on the **entire** primary key, not just part of it

2NF only applies to tables with a **compound (composite) primary key**. If a non-key attribute depends on only one part of the composite key, there is a partial dependency. The solution is to move the partially dependent attribute into a separate table.

**Example:** A table with a composite key of (CourseCode, Date) where "CourseTitle" depends only on CourseCode and not on Date has a partial dependency. CourseTitle should be moved to a separate Course table.

### Third Normal Form (3NF)

A table is in 3NF if:

- It is already in **2NF**
- It has **no transitive dependencies**: every non-key attribute depends solely on the primary key and not on any other non-key attribute

If a non-key attribute determines another non-key attribute, there is a transitive dependency. The solution is to move the transitively dependent attributes into a separate table and link it using a foreign key.

**Example:** A Film table with FilmID (PK), Title, Certificate, and Description where Description depends on Certificate (not directly on FilmID) has a transitive dependency. Certificate and Description should be moved to a separate Certificate table.

**Exam tip:** For 2NF, always state that the table must first be in 1NF. For 3NF, always state that the table must first be in 2NF. Examiners expect this prerequisite to be mentioned explicitly.

---

## Capturing, Selecting, Managing and Exchanging Data

### Capturing Data

Data must be input into a database, and the method chosen depends on context:

- **Manual entry:** data typed directly into the system (e.g. survey responses from pedestrians)
- **Forms:** structured input fields that collect and organise user data in a defined format; common in web applications
- **OMR (Optical Mark Recognition):** a machine detects marked areas on paper (e.g. shaded bubbles); used for multiple-choice exams, surveys, and lottery tickets
- **OCR (Optical Character Recognition):** converts printed or handwritten text into digital format; useful for digitising documents
- **MICR (Magnetic Ink Character Recognition):** banks use this to scan cheques. Details (excluding the amount) are printed in magnetic ink that a computer can read; the amount must be entered manually
- **Sensors:** devices that detect changes in the environment and convert physical signals into digital data; enable automated, real-time data collection (temperature, pressure, proximity, light, motion, humidity, gas, force, acoustic, magnetic sensors)
- **Barcodes:** machine-readable representations of data using patterns of lines or shapes. **1D barcodes** use parallel lines of varying widths (e.g. on retail products). **2D barcodes** use geometric patterns such as squares or dots (e.g. QR codes). Barcodes offer fast, accurate data entry and reduce human error.
- **Data mining:** the process of discovering hidden patterns, correlations, and insights from large datasets using techniques from machine learning, statistics, and AI. Applications include customer segmentation in marketing, fraud detection in finance, disease prediction in healthcare, and quality control in manufacturing.

### Selecting Data

Data can be selected using SQL queries (covered below) or through **Query By Example (QBE)**.

**QBE** is a user-friendly, visual interface for constructing database queries. Users enter criteria in a grid or form representing database fields, and the QBE system translates this into an equivalent SQL query. QBE supports filtering, sorting, joining, and aggregation without requiring knowledge of SQL syntax.

| QBE Benefits | QBE Drawbacks |
|-------------|--------------|
| Easy to learn and use for non-technical users | Less powerful and flexible than SQL for complex queries |
| Visual interface makes queries simple to understand and modify | May not support advanced features such as stored procedures or triggers |
| More accessible than writing raw SQL | Can be slower than SQL for large datasets or complex operations |

### Managing Data

After creation, a database must support adding new data, editing/modifying existing data, and deleting data. This is achieved using a **database manipulation language (DML)** such as SQL, or through the built-in facilities of a DBMS.

### Exchanging Data

Data can be transferred between systems using several methods:

- **EDI (Electronic Data Interchange):** a standardised electronic method for transferring documents and data between businesses without human interaction. Reduces paper usage and streamlines transactions.
- **CSV (Comma Separated Values):** a simple plain-text format that stores tabular data using commas to separate values. Widely supported and easy to parse.
- **JSON (JavaScript Object Notation):** a lightweight, human-readable format using key-value pairs. Common in web applications for data interchange.
- **APIs (Application Programming Interfaces):** sets of protocols allowing different software applications to communicate. Enable developers to integrate services, facilitate data exchange between platforms, and can be RESTful, SOAP-based, or other types. APIs encourage code reuse, simplify development, and enable seamless integration.
- **Memory sticks (USB flash drives):** portable storage devices using flash memory and USB connections. Plug-and-play, compact, and durable (no moving parts), but have limited storage capacity compared to external hard drives, risk data loss from physical damage or theft, and have slower transfer speeds.
- **Email:** electronic messaging for exchanging files and messages. Fast, convenient across devices, and supports attachments, but has file size limits, security risks (phishing, spam), privacy concerns (interception), and reliability issues (server problems, spam filters).

---

## SQL (Structured Query Language)

**SQL** is a **declarative language** used to interact with and manipulate databases through a DBMS. SQL is part of the **declarative programming paradigm** (synoptic link: 1.2.4 Types of Programming Language).

### SELECT, FROM, WHERE

`SELECT` retrieves specified fields from a table. `FROM` specifies which table to query. `WHERE` filters results based on a condition.

```sql
SELECT MovieTitle, DatePublished
FROM Movie
WHERE DatePublished BETWEEN #01/01/2000# AND #31/12/2005#
```

Use `SELECT *` to retrieve all fields. The `*` wildcard means "all columns."

### LIKE and Wildcards

`LIKE` filters data based on a pattern. The `%` wildcard matches any sequence of characters.

```sql
SELECT Name, Country
FROM Customers
WHERE Country LIKE 'U%';
```

This returns customers whose country starts with "U" (e.g. UK, USA).

### AND / OR

`AND` requires all conditions to be true. `OR` requires at least one condition to be true.

```sql
SELECT * FROM Customers
WHERE City = 'London' OR City = 'Paris';
```

### ORDER BY

`ORDER BY` sorts results. Values are placed in **ascending** order by default. Appending `DESC` sorts in **descending** order.

```sql
SELECT MovieTitle, DatePublished
FROM Movie
ORDER BY DatePublished DESC;
```

### JOIN (INNER JOIN)

`JOIN` combines rows from multiple tables based on a common field. The `ON` clause specifies the matching condition.

```sql
SELECT Movie.MovieTitle, Director.DirectorName, Movie.MovieCompany
FROM Movie
JOIN Director
ON Movie.DirectorName = Director.DirectorName;
```

### Nested SELECT

A `SELECT` statement placed inside another `SELECT` statement (a subquery). The inner query executes first, and its result is used by the outer query.

```sql
SELECT *
FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees);
```

This returns all employees whose salary exceeds the average salary.

### CREATE TABLE

`CREATE TABLE` defines a new table, specifying each attribute's name, data type, whether it is the primary key, and whether it can be left empty.

```sql
CREATE TABLE TableName
(
  Attribute1  INTEGER NOT NULL PRIMARY KEY,
  Attribute2  VARCHAR(20) NOT NULL,
  ...
)
```

> ⚠ Check: the PMT source places a comma between `NOT NULL` and `PRIMARY KEY` in the `CREATE TABLE` syntax (`INTEGER NOT NULL, PRIMARY KEY,`). Standard SQL writes `INTEGER NOT NULL PRIMARY KEY` without the separating comma unless using a table-level constraint.

#### SQL Data Types

| Data Type | Description |
|-----------|-------------|
| **CHAR(n)** | Fixed-length string of exactly n characters |
| **VARCHAR(n)** | Variable-length string with maximum length n |
| **BOOLEAN** | TRUE or FALSE |
| **INTEGER / INT** | Whole number |
| **FLOAT** | Number with a floating decimal point |
| **DATE** | Date value (Day/Month/Year) |
| **TIME** | Time value (Hour/Minute/Second) |
| **CURRENCY** | Monetary amount |

Each attribute in `CREATE TABLE` must specify: whether it is the primary key, its data type, and whether it must be filled in (`NOT NULL`).

### ALTER TABLE

`ALTER` modifies the structure of an existing table.

**Add a column:**
```sql
ALTER TABLE TableName
ADD AttributeX DataType;
```

**Delete a column:**
```sql
ALTER TABLE TableName
DROP COLUMN AttributeX;
```

**Modify a column's data type:**
```sql
ALTER TABLE TableName
MODIFY COLUMN AttributeX NewDataType;
```

### INSERT INTO

Inserts a new record into a table.

```sql
INSERT INTO TableName (column1, column2, ...)
VALUES (value1, value2, ...);
```

> ⚠ Check: the PMT source omits the table name from the `INSERT INTO` syntax, writing `INSERT INTO (column1, column2, ...)`. The table name is required after `INSERT INTO`.

### UPDATE

Modifies existing records in a table.

```sql
UPDATE TableName
SET column1 = value1, column2 = value2
WHERE columnX = value;
```

### DELETE

Removes records from a table based on a condition.

```sql
DELETE FROM TableName
WHERE columnX = value;
```

### DROP TABLE

Deletes an entire table and all its data permanently.

```sql
DROP TABLE TableName;
```

*(Beyond source: `DELETE` removes specific records but keeps the table structure. `DROP TABLE` removes the entire table including its structure. This distinction is commonly tested.)*

---

## Referential Integrity

**Referential integrity** ensures consistency between related tables in a relational database. It guarantees that every foreign key value either matches an existing primary key value in the linked table, or is null (if permitted). If two tables are linked, a record in the referenced table cannot be deleted or altered in a way that would leave orphaned foreign key values in the other table.

### Foreign Key Constraints and Cascade Actions

When a referenced primary key is updated or deleted, cascade actions define what happens to related foreign key records:

| Action | Effect |
|--------|--------|
| **CASCADE** | Automatically applies the same change (update/delete) to all related records |
| **SET NULL** | Sets the foreign key value to null in related records |
| **SET DEFAULT** | Sets the foreign key value to its default in related records |
| **NO ACTION / RESTRICT** | Prevents the change if related records exist |

**Benefits:** ensures data consistency and accuracy; prevents orphaned records. **Drawbacks:** can impact performance due to additional integrity checks; may require additional planning and design.

---

## Transaction Processing

A **transaction** is a sequence of database operations treated as a single unit of work. A single operation, or a collection of related operations, can constitute a transaction. For example, a bank transfer consists of a withdrawal from one account and a deposit into another. Both operations must succeed together, or neither should happen.

### Problems in Transaction Processing

- **Concurrency:** simultaneous transactions may access or modify the same data, causing inconsistencies
- **Deadlock:** two or more transactions each wait for the other to release a locked resource, causing indefinite waiting and no progress
- **Data integrity:** a transaction failing mid-execution may leave the database in an inconsistent state
- **Isolation:** one user's transaction may affect another user's transaction, producing unpredictable outcomes
- **Durability issues:** a system failure after a transaction is confirmed may result in data loss

### Deadlock Example

User 1 locks Record A and then tries to access Record B. Simultaneously, User 2 locks Record B and then tries to access Record A. Each user waits for the other to release their lock. Neither can proceed, creating a deadlock.

### Solutions

- **Locking:** prevents two transactions from accessing the same data simultaneously
- **Deadlock prevention/detection:** ordering resource requests or implementing timeout mechanisms
- **Logging and recovery:** maintaining a log of all changes so the system can recover to a consistent state after a crash
- **Commit and rollback:** `COMMIT` saves all changes permanently; `ROLLBACK` reverts all changes made in the transaction
- **Two-phase commit protocol:** in distributed systems, ensures a transaction is committed across all participating nodes, or not at all
- **Timestamping:** assigns a unique timestamp to each transaction for ordering

### ACID Properties

**ACID** is a set of rules that all Database Management Systems must follow to ensure data integrity and reliable transaction processing.

| Property | Meaning |
|----------|---------|
| **Atomicity** | A transaction must be processed in its entirety or not at all. If any operation fails, the entire transaction is rolled back. Partial transactions do not occur. |
| **Consistency** | A transaction must maintain referential integrity rules. The database starts in a consistent state and must end in a consistent state. |
| **Isolation** | Simultaneous execution of transactions must produce the same result as if they were executed sequentially. Intermediate states are not visible to other transactions. |
| **Durability** | Once a transaction has been committed, it persists permanently regardless of subsequent failures (e.g. power cuts). |

### Record Locking

**Record locking** prevents simultaneous access to the same record, avoiding inconsistencies and lost updates. While one user edits a record, the lock prevents others from modifying it.

**Lock granularity** refers to the size of the locked data, ranging from a single row to an entire table.

| Lock Type | Description |
|-----------|-------------|
| **Shared lock (read lock)** | Multiple transactions can read the record simultaneously, but none can modify or delete it until all shared locks are released |
| **Exclusive lock (write lock)** | Only one transaction can access and modify the record; all other transactions are blocked from reading or writing until released |

The main problem with record locking is **deadlock** (see above).

### Redundancy

In the context of transaction processing and data protection, **redundancy** is the process of maintaining one or more copies of the data in **physically different locations**. If one copy is damaged (e.g. by hardware failure or disaster), the other copies remain unaffected and can be recovered. This is distinct from data redundancy within tables (unnecessary duplication), which normalisation aims to eliminate.

*(Beyond source: the term "redundancy" has two meanings in database contexts. In normalisation, it refers to unwanted duplication of data within or across tables, which is eliminated through normalisation. In the context of spec point 1.3.2 f), it refers to deliberate backup copies stored in separate physical locations for disaster recovery. Both meanings may appear in exam questions, so identify the context carefully.)*

---

## Key SQL Commands Summary

| Command | Purpose | Example Syntax |
|---------|---------|---------------|
| `SELECT ... FROM` | Retrieve data from a table | `SELECT col1, col2 FROM Table;` |
| `WHERE` | Filter results by condition | `WHERE col > value` |
| `LIKE` | Pattern matching with `%` wildcard | `WHERE name LIKE 'J%'` |
| `AND` / `OR` | Combine/alternate conditions | `WHERE x = 1 AND y = 2` |
| `ORDER BY` | Sort results (ASC default, DESC) | `ORDER BY col DESC` |
| `JOIN ... ON` | Combine rows from multiple tables | `JOIN Table2 ON T1.key = T2.key` |
| `Nested SELECT` | Subquery within a query | `WHERE col > (SELECT AVG(col) FROM T)` |
| `CREATE TABLE` | Define a new table | `CREATE TABLE T (col TYPE NOT NULL PRIMARY KEY)` |
| `ALTER TABLE` | Add, drop, or modify columns | `ALTER TABLE T ADD col TYPE` |
| `INSERT INTO` | Add a new record | `INSERT INTO T (cols) VALUES (vals)` |
| `UPDATE ... SET` | Modify existing records | `UPDATE T SET col = val WHERE condition` |
| `DELETE FROM` | Remove specific records | `DELETE FROM T WHERE condition` |
| `DROP TABLE` | Delete an entire table | `DROP TABLE T` |
| `*` (wildcard) | Select all columns | `SELECT * FROM T` |
| `%` (wildcard) | Match any character sequence in `LIKE` | `WHERE col LIKE '%text%'` |
