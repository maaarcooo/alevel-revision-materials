# 1.3.4 Web Technologies

## HTML

**HTML (HyperText Markup Language)** is the foundational language used to structure content on the web. It allows a browser to interpret and render a webpage by describing the **structure and order** of the page. HTML uses **tags** written in **angle brackets** (`<tag>`, `</tag>`). Most tags are opened and closed (e.g. `<html>` and `</html>`), while some are **self-closing** (e.g. `<img>`, `<link>`).

### The Head

The `<head>` section contains information about the web page that is **not displayed on the page itself**. Some content inside the head tag is shown in the **browser tab** (e.g. the page title). It is enclosed by `<head>` and `</head>`.

**Page title:** The `<title>` element sets the text displayed in the browser tab. It is placed inside the `<head>` section.

```html
<title>Sample Webpage</title>
```

**External stylesheet:** External CSS files are linked in the `<head>` using the `<link>` element. The `rel` attribute is set to `"stylesheet"` and the `href` attribute contains the path to the CSS file. Stylesheets are loaded in the order they are listed, so hierarchy matters.

```html
<link rel="stylesheet" type="text/css" href="styles.css">
```

### The Body

The `<body>` section contains the **main content** of the web page (text, images, videos, hyperlinks, tables, etc.). It is enclosed by `<body>` and `</body>`, and its content is displayed in the browser window.

### HTML Tags

| Tag | Purpose |
|---|---|
| `<html>` | Root element; all other HTML elements sit inside it |
| `<head>` | Defines the browser tab/window heading area (metadata, title, stylesheet links) |
| `<title>` | Sets the text shown in the browser tab |
| `<body>` | Defines the main visible content area |
| `<h1>` to `<h6>` | Heading styles in decreasing prominence; `<h1>` is the highest level |
| `<p>` | Defines a paragraph, separated by a line space above and below |
| `<img>` | Embeds an image (self-closing); requires `src` attribute; optional `alt`, `height`, `width` |
| `<a>` | Anchor tag for hyperlinks; uses `href` attribute for the target URL |
| `<ol>` | Ordered (numbered) list |
| `<ul>` | Unordered (bullet point) list |
| `<li>` | Defines each item within `<ol>` or `<ul>` |
| `<div>` | Generic container used to group elements; often used with CSS to style sections |
| `<form>` | Creates a form for user input |
| `<input>` | Creates interactive controls within a form (e.g. textbox, submit button) |
| `<link>` | Links to additional files such as CSS stylesheets |
| `<script>` | Embeds or references JavaScript code |

### Headings

Headings (`<h1>` through `<h6>`) communicate **page organisation and structure**. They guide the user's eye and help them locate information quickly. They should be used **hierarchically**, with `<h1>` the most prominent. Headings are also important for **accessibility** (screen readers use them for navigation) and **Search Engine Optimisation (SEO)**, as search engines use them to understand page content and structure.

### Images

The `<img>` tag is **self-closing** (no `</img>` needed). Key attributes:

- `src` specifies the image file path or URL
- `alt` provides **alternative text** for screen readers or when the image cannot load; also helps search engines understand the image
- `height` and `width` set dimensions

```html
<img src="photo.png" alt="Description" width="200" height="100">
```

### Links (Anchor Tag)

The `<a>` tag creates **hyperlinks**. The `href` attribute specifies the destination URL. The clickable text sits between the opening and closing tags.

```html
<a href="https://www.example.com">Click here</a>
```

An **image can be made into a hyperlink** by nesting `<img>` inside `<a>`:

```html
<a href="booking.htm"><img src="ticket.png"></a>
```

### Lists

**Ordered lists** (`<ol>`) display numbered items. **Unordered lists** (`<ul>`) display bullet points. Each item is wrapped in `<li>` tags nested inside the list element.

```html
<ol>
  <li>First item</li>
  <li>Second item</li>
</ol>
```

### Forms and Input

The `<form>` tag creates a form for user input. The `<input>` tag sits inside `<form>` and creates interactive controls. The `type` attribute controls the kind of input: `"text"` for a textbox, `"number"` for numeric input, `"email"` for email input, `"submit"` for a submit button. The `name` attribute identifies the input field.

```html
<form action="/submit" method="post">
  <label for="email">Email:</label>
  <input type="email" id="email" name="email">
  <input type="submit" value="Submit">
</form>
```

### Classes and Identifiers

**Classes** and **identifiers (IDs)** are attributes assigned to HTML elements to target them for styling.

| Feature | Class | Identifier (ID) |
|---|---|---|
| HTML attribute | `class="name"` | `id="name"` |
| CSS selector | `.name` (full stop prefix) | `#name` (hash prefix) |
| Uniqueness | **Multiple elements** can share the same class | **Only one element** per page can have a given ID |
| Purpose | Apply consistent styling across many elements | Style a single, unique element |

```html
<div class="subject" id="maths">
  <h2>Maths</h2>
</div>
```

```css
.subject { border: 1px solid black; margin: 10px; }
#maths { background-color: #FFDDDD; }
```

The class `.subject` applies to every element with `class="subject"`, while `#maths` applies only to the single element with `id="maths"`.

> ⚠ Check: the PMT source (page 9) has the code comments and HTML usage for classes and identifiers **swapped** (the `.example` CSS block is labelled "defining an identifier" and paired with `<div id='example'>`, and vice versa for `#`). The correct mapping is: `.` selector pairs with `class` attribute (many elements); `#` selector pairs with `id` attribute (unique element). The Save My Exams source and the text descriptions in the PMT source itself confirm the correct version shown above.

### Embedding JavaScript

The `<script>` tag embeds or references JavaScript. An external script is linked via the `src` attribute:

```html
<script src="script.js"></script>
```

**Exam tip:** When writing HTML in an exam, spelling and syntax must be exact. Copy filenames and URLs from the question precisely, preserving case.

---

## CSS

**Cascading Style Sheets (CSS)** is a language used to **define the style or appearance** of a webpage. CSS specifies how HTML elements look and can be applied to tags (e.g. `h1`, `p`), classes, and identifiers.

### Internal vs External CSS

| Form | Description |
|---|---|
| **Internal/embedded CSS** | Written inside `<style>` tags directly in the HTML document |
| **External CSS** | Written in a separate `.css` file and linked to the HTML via `<link>` in the `<head>` |
| **Inline CSS** | Applied directly to an element using the `style` attribute, e.g. `<p style="color: red;">` |

When CSS is used **inline** within the HTML, it takes **priority over** any external stylesheet and overrides it. Multiple CSS sources can be combined.

### CSS Syntax

Each CSS rule begins with a **selector** (element name, class, or ID), followed by **curly brackets** containing property-value pairs separated by colons and terminated by semicolons.

```css
body {
  margin: 0px;
  padding: 0px;
  background-color: white;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 18px;
  text-align: center;
}
```

### Selectors

- **Element selector:** targets all instances of a tag, e.g. `h1 { color: blue; }`
- **Class selector:** prefix with `.`, e.g. `.infoBox { background-color: green; }`
- **ID selector:** prefix with `#`, e.g. `#menu { background-color: brown; }`

### CSS Properties

| Property | Effect | Example Value |
|---|---|---|
| `background-color` | Sets background colour | `lightblue`, `#FFDDDD` |
| `border-color` | Sets border colour | `black`, `orange` |
| `border-style` | Sets border line style | `solid`, `dashed` |
| `border-width` | Sets border thickness | `2px` |
| `color` | Sets **font/text colour** | `#ff0000`, `blue` |
| `font-family` | Sets typeface | `Arial`, `Helvetica, sans-serif` |
| `font-size` | Sets text size | `14px`, `18px` |
| `height` | Sets element height | `200px` |
| `width` | Sets element width | `200px` |
| `margin` | Space outside an element | `10px` |
| `padding` | Space inside an element | `10px` |
| `text-align` | Horizontal text alignment | `center`, `left` |

### Colours in CSS

Colours can be specified by **name** (e.g. `red`, `lightblue`, `orange`) or by **hex code** (e.g. `#FF0000`). Every pair of characters in a hex code represents the **red, green, or blue** channel respectively: `#FF0000` is pure red, `#00FF00` is pure green, `#0000FF` is pure blue.

**Exam tip:** CSS uses the **American spelling** `color`, not `colour`. Writing `colour` will not work. Use `:` (colon) not `=` in property declarations.

---

## JavaScript

**JavaScript** is a **scripting language** used primarily to add **interactivity** and **dynamic functionality** to websites. It is **interpreted** rather than compiled, meaning the browser interprets the code each time a page is loaded, independently of processor architecture. JavaScript is a **multi-paradigm** language (synoptic link to 1.2.4 Programming Paradigms).

### Purpose of JavaScript

JavaScript is primarily used for **client-side scripting**: it runs directly in the user's web browser. Its roles include:

- **Interactive features:** image sliders, drop-down menus, interactive maps
- **Dynamic content:** infinite scrolling, content that changes based on user actions (e.g. different descriptions on hover)
- **Form validation:** checking required fields, verifying email format, enforcing password strength requirements, all in real time without a server round-trip
- **Data manipulation:** filtering product lists, sorting tables, updating charts in real time

JavaScript can respond to user actions, update HTML element content, and communicate with servers to send or retrieve data.

### Advantages of Using JavaScript

- The local computer can handle invalid data **before** it is sent to the server
- **Eases the load** on busy servers
- **Reduces web traffic**

### Data Types in JavaScript

| Data Type | Description | Examples |
|---|---|---|
| **Integer** | Whole numbers (positive or negative) | `10`, `-5`, `0` |
| **Real** | Numbers with a fractional part | `3.14`, `-2.5` |
| **Char** | A single character | `'a'`, `'B'`, `'$'` |
| **String** | A sequence of characters | `"Hello World"`, `"1234"` |
| **Boolean** | True or false values | `true`, `false` |

### Variables and Constants

**Variables** store data that can **change** during program execution. **Constants** store data that **remains the same**.

```javascript
let score = 10;        // variable (declared with let)
const PI = 3.14;       // constant (declared with const)
```

Variable naming rules: must start with a letter, cannot contain spaces, can contain letters, numbers, `_` or `$`, must not use reserved words (`if`, `while`, `for`, etc.).

*(Beyond source: `var` was used before 2015 to declare variables but creates global-scope variables, which is considered bad practice. `let` (block-scoped) replaced it from ES6 onwards.)*

### Outputs in JavaScript

**Changing the content of an HTML element** via the DOM (Document Object Model):

```javascript
chosenElement = document.getElementById("example");
chosenElement.innerHTML = "Hello World";
```

`document.getElementById()` retrieves an element by its ID. The `innerHTML` property allows direct modification of the HTML content within that element.

**Writing directly to the document:**

```javascript
document.write("Hello World");
```

**Displaying an alert box:**

```javascript
alert("Hello World");
```

### Selection (If Statements)

Selection chooses which lines of code to execute depending on whether a condition is true or false. There are three programming constructs: **sequence**, **selection**, and **iteration**.

**Comparison operators:**

| Operator | Meaning | Notes |
|---|---|---|
| `==` | Equal to (value) | Performs type coercion (`5 == "5"` is `true`) |
| `===` | Strict equal (value and type) | No coercion (`5 === "5"` is `false`) |
| `!=` | Not equal (value) | Performs type coercion |
| `!==` | Strict not equal (value or type) | No coercion |
| `>` | Greater than | |
| `<` | Less than | |
| `>=` | Greater than or equal to | |
| `<=` | Less than or equal to | |

**If statement:**

```javascript
if (number > 0) {
  console.log("Positive");
}
```

**If-else statement:**

```javascript
if (number > 0) {
  console.log("Positive");
} else {
  console.log("Not positive");
}
```

**If-else if-else statement:**

```javascript
if (score >= 90) {
  console.log("Excellent!");
} else if (score >= 80) {
  console.log("Good.");
} else {
  console.log("Needs improvement.");
}
```

Conditions can use **boolean operators** to combine checks: `&&` (AND) requires both sides true, `||` (OR) requires at least one side true. Example: `if (number >= 1 && number <= 6)` checks the number is between 1 and 6 inclusive.

**Exam tip:** `IF number < 0 AND number > 100` checks for a number simultaneously below 0 AND above 100 (impossible, so always false). To check if a number is outside 1-99, use `OR`: `IF number < 0 OR number > 100`.

### Switch Case

**Switch case** provides an alternative to multiple `if-else if` chains when comparing a single expression against many possible values.

```javascript
const grade = 'B';
switch (grade) {
  case 'A':
    console.log('Excellent!');
    break;
  case 'B':
    console.log('Good.');
    break;
  case 'C':
    console.log('Fair.');
    break;
  default:
    console.log('Needs improvement.');
}
```

The expression is compared against each `case` label. If a match is found, the corresponding code block executes. The `break` statement prevents **fall-through** (execution continuing into the next case). Without `break`, execution falls through to subsequent cases until a `break` is reached. The `default` block runs if no case matches.

**Fall-through** can be used deliberately to group cases:

```javascript
switch (day) {
  case 'Monday':
  case 'Tuesday':
  case 'Wednesday':
  case 'Thursday':
  case 'Friday':
    console.log('Weekday');
    break;
  case 'Saturday':
  case 'Sunday':
    console.log('Weekend');
    break;
}
```

### For Loops

A **for loop** repeats a block of code for a **specified number of iterations**. It has three parts: initialisation, condition, and increment/decrement.

```javascript
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
// Outputs: 1, 2, 3, 4, 5
```

**Iterating over an array:**

```javascript
const fruits = ["apple", "banana", "orange"];
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}
```

`i++` is shorthand for `i = i + 1`.

**For...in loop:** Iterates through the indices of a data structure such as an array.

```javascript
const fruits = ['apple', 'banana', 'orange'];
for (let index in fruits) {
  console.log('Index: ' + index + ', Value: ' + fruits[index]);
}
```

### While Loops

A **while loop** repeats a block of code as long as a condition remains **true**. Used when the number of iterations is **unknown in advance**.

```javascript
let i = 1;
while (i <= 5) {
  console.log(i);
  i++;
}
```

**Password check example:**

```javascript
let password = '';
while (password !== 'secret') {
  password = prompt('Enter the password:');
}
console.log('Access granted!');
```

### Do While Loops

A **do while loop** executes the code block **at least once** before checking the condition.

```javascript
let roll;
let desiredNumber = 6;
do {
  roll = Math.floor(Math.random() * 6) + 1;
  console.log('Rolled:', roll);
} while (roll !== desiredNumber);
```

The code block runs first, then the condition is evaluated. If true, the loop repeats. If false, it terminates.

### Strings

A **string** is a sequence of characters enclosed in single (`'`) or double (`"`) quotes.

**String length:** The `.length` property returns the number of characters.

```javascript
const message = 'Hello, world!';
console.log(message.length); // Output: 13
```

**Substring extraction:** The `.substring(start, end)` method extracts characters from `start` index up to but not including `end` index. Omitting the second parameter extracts to the end of the string.

```javascript
const message = 'Hello, world!';
message.substring(0, 5);  // "Hello"
message.substring(7);     // "world!"
```

### Arithmetic Operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition (or string concatenation) | `5 + 3` | `8` |
| `-` | Subtraction | `10 - 4` | `6` |
| `*` | Multiplication | `3 * 5` | `15` |
| `**` | Exponentiation | `3 ** 3` | `27` |
| `/` | Division | `10 / 2` | `5` |
| `%` | Modulus (remainder) | `10 % 3` | `1` |
| `++` | Increment by 1 | `counter++` | |
| `--` | Decrement by 1 | `counter--` | |

**Operator precedence** follows BIDMAS/BODMAS. Parentheses `()` can override precedence: `2 + 3 * 4` gives `14`, but `(2 + 3) * 4` gives `20`.

The `+` operator also **concatenates strings**: `'John' + ' ' + 'Doe'` produces `'John Doe'`.

### Boolean (Logical) Operators

| Operator | Meaning | Behaviour |
|---|---|---|
| `&&` | AND | Returns `true` only if **both** operands are true |
| `\|\|` | OR | Returns `true` if **at least one** operand is true |
| `!` | NOT | Negates the value (`!false` gives `true`) |

### Nested Statements

**Nesting** is placing one block of code inside another. Common with if statements and loops.

**Nested if statements** allow more complex decision logic:

```javascript
if (x > 0) {
  if (y > 0) {
    console.log('Both x and y are positive.');
  } else {
    console.log('x is positive, but y is not.');
  }
} else {
  console.log('x is not positive.');
}
```

**Nested loops** iterate over multi-dimensional data. To find the total iterations of the inner loop, **multiply** outer iterations by inner iterations. For example, an outer loop of 3 and inner loop of 5 gives 3 * 5 = 15 total inner iterations.

```javascript
const matrix = [[1,2,3],[4,5,6],[7,8,9]];
let sum = 0;
for (let i = 0; i < matrix.length; i++) {
  for (let j = 0; j < matrix[i].length; j++) {
    sum += matrix[i][j];
  }
}
// sum = 45
```

### Functions and Procedures

**Functions** are reusable blocks of code that perform a specific task, can accept **parameters** (arguments), and **return a value**.

```javascript
function addNumbers(a, b) {
  return a + b;
}
const result = addNumbers(5, 10); // result = 15
```

**Procedures** are similar but **do not return a value**. In JavaScript, a procedure is a function without a `return` statement (or with `return` and no value).

```javascript
function greetUser(name) {
  console.log('Hello, ' + name);
}
greetUser('Alice');
```

Best practices: use descriptive names, clear parameter names, keep functions short and focused, and use explicit `return` statements in functions.

**Exam tip:** When completing code in an exam, spell existing identifier names exactly as given. Do not include currency symbols (e.g. `£`) in calculations.

---

## Search Engine Indexing

A **search engine** is a program that searches through a **database of internet addresses** looking for resources based on criteria set by the user. The order in which results are displayed is critical, as it determines which websites users visit. Search engines must display the most **high-quality, relevant** content at the top.

Search engines work in three stages: **crawling**, **indexing**, and **ranking**.

### Crawling

**Web crawlers** (also called **spiders**, bots, or robots) are software programs that discover web pages by **following links from one webpage to another**, systematically traversing the web. They start from a set of **seed URLs** and visit pages linked from those URLs.

Crawlers follow **rules and guidelines set by website owners** using mechanisms like the **`robots.txt`** file, which directs crawlers on which areas of a site to explore or avoid, respecting privacy preferences.

When a crawler reaches a page, it **fetches the HTML content** and examines the HTML structure. It retrieves information such as **text content, headings, links, and metadata** (information specified by the website owner). The retrieved HTML is **broken down into individual components** by identifying **elements, tags, and attributes** that hold valuable information like titles and headings.

### Indexing

The extracted data is **indexed**: stored in a **structured manner** within the search engine's database. Each word in the document is included in the index as an entry, along with the **word's position** on the page. The index allows for **quick retrieval and ranking** of relevant pages in response to user queries.

### Ranking

When a user enters a query, the search engine searches the index for matching pages and returns results it believes are the **highest quality and most relevant** to the query.

### Benefits of Crawling and Indexing

**Improved search results:** Indexing allows search engines to provide **relevant, up-to-date** results and match user searches with appropriate content, so users find what they need quickly.

**Efficient retrieval:** Search engines do not need to scan the entire web for every query. They search their **indexed data** to produce results quickly.

**Ranking and relevance:** Indexing enables search engines to **assess the relevance and quality** of web pages. Ranking algorithms analyse indexed data and consider factors such as **keyword relevance, backlinks, and user engagement**.

**Freshness and updates:** Crawlers **periodically revisit** indexed pages to detect updates and changes, ensuring search results display the **latest content** currently available. If a page has been updated but not re-crawled, it may no longer be relevant to a user's search.

---

## PageRank Algorithm

The **PageRank algorithm** ranks web pages to determine the order in which they are displayed in search results. Higher-ranked pages appear first. It was originally developed by **Larry Page and Sergey Brin**, the founders of Google, and is used by many search engines.

Its purpose is to evaluate web pages based on their **perceived relevance and importance**, providing search results that go beyond simple keyword matching.

### Key Elements

**Link analysis:** PageRank analyses the **structure of links between pages**. Each inbound link acts as a **"vote"** for the target page, with the voting weight determined by the **importance of the linking page**. Pages with more **high-quality inbound links** are deemed more valuable and rank higher.

**Link weight distribution:** A page's importance is **shared** among the pages it links to, distributing a **portion of its importance** with each outgoing link. Higher-quality pages therefore have greater influence on the ranking of pages they link to.

**Iterative calculation:** Initially, every page is assigned the **same value**. In subsequent iterations, each page's significance is **re-evaluated** by considering the weighted impact of its inbound links. The process repeats until rankings **stabilise**.

**Damping factor ($d$):** A value between **0 and 1**, usually set to **0.85**. It represents the probability that a user will **not follow a link** on a page and will instead jump to a **random new page**. It prevents the algorithm from getting stuck in **infinite loops** and makes the model more realistic.

### The PageRank Formula

$$PR(x) = (1 - d) + d \left[ \frac{PR(T_1)}{C(T_1)} + \frac{PR(T_2)}{C(T_2)} + \cdots + \frac{PR(T_n)}{C(T_n)} \right]$$

Where:

- $PR(x)$ = PageRank of page $x$
- $T_1 \ldots T_n$ = pages that link **to** page $x$
- $C(T_n)$ = total count of **outbound links** from page $T_n$
- $d$ = damping factor (usually 0.85)

The formula sums the PageRank contribution from every page linking to $x$. Each contribution equals the linking page's rank divided by its total number of outgoing links. The damping factor scales this sum, and the base term $(1-d)$ ensures every page retains a minimum rank.

### Worked Method

The data structure used to represent link relationships is a **directed graph**, where **nodes** represent web pages and **arcs** (directed edges) represent links between pages. The direction of each arc indicates which page links to which.

To calculate PageRank iteratively:

1. Assign an initial PageRank of 1 to all pages
2. Apply the formula to compute new PageRank values for every page
3. Feed the new values back into the formula for the next iteration
4. Repeat until values converge (stabilise)

With each iteration, the values refine and converge toward stable rankings. The page with the highest final PageRank is ranked first.

*(Beyond source: the football analogy from Save My Exams helps conceptualise this: each player is a page, each pass is a link. A player's "rank" depends on how many passes they receive and from how highly ranked the passing players are. Ranks update continuously throughout the game, and at the end, players can be sorted by their final rating.)*

### Factors Influencing Modern Search Rankings

The original PageRank algorithm focused on link analysis, but modern search engines consider many additional factors:

| Factor | Description |
|---|---|
| **Relevance** | Keywords used, quality of content, and how well it matches the search query |
| **User engagement** | Click-through rates, time spent on page (dwell time), and bounce rates |
| **Authority and trust** | Domain age, quality backlinks from reputable sources (e.g. government sites, the BBC), trustworthy content |
| **Content freshness** | Priority given to frequently updated pages with up-to-date information |
| **Mobile-friendliness** | Mobile compatibility of web pages; Google primarily uses the mobile version of a site's content for ranking |

### Limitations

PageRank is **not the only factor** determining search rankings. Search engines use **multiple algorithms** and factors to provide diverse, relevant, high-quality results. The details of the PageRank algorithm have **evolved over time** as search engines adapt to new challenges and user expectations.

**Exam tips:**
- You will not be asked to perform the full PageRank calculation, just to understand the overall concept of how it works.
- Do not mention Google specifically in exam answers, as PageRank is used by many search engines.

---

## Server and Client Side Processing

### Server Side Processing

**Server side processing** is when a client sends data to a **server** for it to be processed. No information is processed on the client computer. Common server side languages include **PHP** (Hypertext Pre-processor), **Python**, **Ruby**, **Java**, and **SQL**.

PHP is specifically designed for web development and focuses on completing tasks on the server:

- **Data retrieval and manipulation:** interacting with databases, processing data, generating dynamic content
- **Server operations:** performing operations not accessible to the client, such as retrieving and displaying information from a database
- **Form processing:** handling form submissions, processing submitted data, performing validations or database operations on the server side

| Benefits | Drawbacks |
|---|---|
| **Improved security:** sensitive data handled securely on the server; access control and protection against web vulnerabilities | **Increased server load:** complex processing tasks can consume server resources and decrease performance under many concurrent requests |
| **Powerful computation:** server resources can perform advanced calculations and interact with databases | **Latency:** communication with the server introduces delays, leading to slower response times compared to client side processing |
| **Consistency:** consistent behaviour across different devices and browsers, as processing logic is centralised | **Dependency on server infrastructure:** downtime or performance issues affect the entire web application |
| **Scalability:** can add more servers or optimise infrastructure to handle increasing traffic | **Limited real-time interactivity:** typically requires a round-trip to the server for each user action |
| **No plugins required;** not browser dependent | **More complex development** and setup compared to client side processing |

### Client Side Processing

**Client side processing** is when a client processes data on a **local device** (usually the web browser), with no processing on the server. This is also called **client side scripting** and primarily uses **JavaScript**.

Client side processing enables **interactive and dynamic experiences** without constantly requesting data from the server:

- **Form validation:** validating user input in real time with instant feedback (e.g. checking required fields, email format, password strength) without a server round-trip
- **DOM manipulation:** modifying the Document Object Model to make dynamic changes to a web page's content and structure (adding/removing elements, updating text, changing styles, managing events, e.g. dark mode toggle)
- **AJAX requests:** communicating with the server **asynchronously** in the background, dynamically updating content **without requiring a full page reload**

| Benefits | Drawbacks |
|---|---|
| **Enhanced user experience:** interactive, dynamic experiences without frequent server requests or page reloads | **Security risk:** client side code is visible to users, so sensitive information or operations can be exposed or tampered with |
| **Reduced server load:** offloading processing to the client improves scalability and resource utilisation | **Browser/device compatibility:** client side code depends on the browser's capabilities and support; may vary across devices |
| **Real-time feedback:** instant validation of user input reduces server round-trips | **Page load time:** large or complex operations can slow page loading, requiring substantial processing power |
| **Dynamic content:** JavaScript allows seamless, engaging updates to page content | **JavaScript dependency:** if the user's browser does not support or has disabled JavaScript, functionality may break or become inaccessible |
| **Offline functionality:** web applications can work without an active internet connection using client side technologies | **Intellectual property risk:** client side code is accessible, allowing easier viewing, copying, and modification |

### Choosing Between Server and Client Side Processing

The choice depends on the **specific requirements** of the task:

- **Client side** is better for: immediate user feedback, real-time interactions, dynamic user interfaces, data manipulation within the browser. JavaScript is the primary language.
- **Server side** is better for: accessing databases, handling sensitive data, complex business logic, server-specific operations. PHP and other server side languages are commonly used.

**Why both are often used together:** JavaScript validation runs client side so invalid data can be caught **before** reaching the server, reducing unnecessary server load. However, because JavaScript can be **amended or circumvented** by users (e.g. disabled in the browser), the server must **re-validate** data on arrival to ensure security. Client side validation improves user experience; server side validation ensures data integrity.

**Worked example reasoning:** A website uses JavaScript to check email format client side (instant feedback, reduces server load), then rechecks on the server (because JavaScript can be bypassed, ensuring only valid data is processed).

---

## Key Terminology Summary

| Term | Definition |
|---|---|
| **HTML** | Markup language defining the structure and content of web pages |
| **CSS** | Language defining the visual style and appearance of web pages |
| **JavaScript** | Interpreted scripting language adding interactivity and dynamic functionality to websites |
| **Tag** | An HTML element written in angle brackets (e.g. `<p>`, `</p>`) |
| **Self-closing tag** | An HTML tag that does not require a closing tag (e.g. `<img>`, `<link>`) |
| **Class** | A CSS selector (`.`) that can be applied to multiple HTML elements |
| **Identifier (ID)** | A CSS selector (`#`) that targets a single unique HTML element |
| **DOM** | Document Object Model; the structured representation of an HTML page that JavaScript can manipulate |
| **Search engine** | A program that searches a database of internet addresses for resources matching user criteria |
| **Web crawler (spider)** | Software that traverses the web by following links, collecting information to build a search index |
| **Metadata** | Information about a web page specified by the website owner |
| **robots.txt** | A file that directs web crawlers on which areas of a site to explore or avoid |
| **PageRank** | Algorithm that ranks web pages based on the quantity and quality of inbound links |
| **Damping factor** | A value (usually 0.85) representing the probability a user jumps to a random page instead of following a link |
| **Server side processing** | Data is sent to and processed on a remote server (e.g. PHP, Python) |
| **Client side processing** | Data is processed locally in the user's browser (e.g. JavaScript) |
| **AJAX** | Asynchronous JavaScript communication with a server, allowing dynamic content updates without full page reloads |
| **Inline CSS** | CSS written directly within an HTML element's `style` attribute |
| **External CSS** | CSS written in a separate file and linked to the HTML document |
| **SEO** | Search Engine Optimisation; practices that improve a page's ranking in search results |

## Key Formulas

| Formula | Description |
|---|---|
| $PR(x) = (1 - d) + d \sum_{i=1}^{n} \frac{PR(T_i)}{C(T_i)}$ | PageRank of page $x$, where $T_i$ are pages linking to $x$, $C(T_i)$ is the outbound link count from $T_i$, and $d$ is the damping factor (usually 0.85) |
