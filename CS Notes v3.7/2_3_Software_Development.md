# 1.2.3 Software Development

## Programming Methodologies

Software can be developed using a variety of approaches. The approach chosen depends on the type of software being developed, but most **software development life cycles (SDLCs)** share a common set of stages.

### Common SDLC Stages

**Analysis:** **Stakeholders** state what they require from the finished product. This information is used to **clearly define the problem** and the **system requirements**. Requirements may be defined by analysing strengths and weaknesses of the current solution, and considering the types of data involved, including inputs, outputs, stored data and the volume of data.

**Design:** The different aspects of the new system are designed, covering inputs (volume, methods, frequency), outputs (volume, methods, frequency), security features (level required, access levels), hardware setup (compatibility), and user interface (menus, accessibility, navigation). A **test plan** may also be designed at this stage.

**Development:** The design is used to split the project into **individual, self-contained modules**, which are allocated to teams for programming.

**Testing:** The program is tested against the test plan formed during the Design stage. Four types of testing are relevant:

| Test Type | Carried Out By | Basis | Key Detail |
|---|---|---|---|
| **Alpha testing** | Software development teams (in-house) | Internal | Bugs are pinpointed and fixed before release |
| **Beta testing** | End-users | External | Conducted after alpha testing; user feedback informs the next development stage |
| **White box testing** | Software development teams | **Internal structure** of the program | All **possible routes** through the program are tested |
| **Black box testing** | Can be in-house or end-users | **Inputs and outputs** only | Testers have **no knowledge of the internal structure** of the software |

**Implementation:** Once testing has been used to make appropriate changes, the software is **installed onto the users' systems**. This may involve installation, customisation, and training.

**Evaluation:** The **effectiveness of the software** is evaluated **against the system requirements** defined at the analysis stage. Criteria considered include **robustness**, **reliability**, **portability**, and **maintainability**.

**Maintenance:** Errors or improvements are **flagged by end-users**. Programmers regularly send out **software updates** to fix bugs, address security issues, or make needed improvements.

---

### Waterfall Lifecycle

The **waterfall model** is a **sequential** software development process divided into distinct phases. Each phase must be **completed before the next one begins**, progressing linearly from start to finish.

The stages in order are: Requirements/Analysis, Design, Implementation/Development, Testing, Deployment, and Maintenance.

The analysis stage includes a **feasibility study** in which designers evaluate the feasibility of the project using **TELOS**:

| Letter | Factor | Question |
|---|---|---|
| **T** | Technical | Is the project possible considering the technology available and accessible? |
| **E** | Economic | Can the project be financed in the short-term and the long-term? |
| **L** | Legal | Can the project be completed within the law? |
| **O** | Operational | Can the project be successfully implemented and maintained? |
| **S** | Scheduling | Can the project be completed given the time available? |

If a change needs to be made, programmers must **revisit all levels** between the current stage and the stage where the change is needed. This makes the model **inflexible** and unsuitable for projects with changing requirements. Users have **little input** as they are only involved at the very beginning (analysis) and end (evaluation) of the lifecycle.

**Benefits:** Simple and linear, easy to understand and follow. Each phase has specific deliverables and **clear milestones**, making progress easy to measure. Well-documented throughout.

**Drawbacks:** Inflexible to changes once started. Expensive and time-consuming to fix problems discovered late. No built-in risk analysis. The sequential nature may lead to a longer development cycle. Limited user involvement.

**Suitability:** Static, low-risk projects where **requirements are well understood and unlikely to change**, needing little user input, such as general-purpose software. Works well when high quality and compliance are essential.

---

### Agile Methodologies

**Agile** refers to a **collection of methodologies** that aim to improve the **flexibility of software development** and **adapt to changes in user requirements faster**.

The problem is broken down into **sections which are developed in parallel**. The design and analysis phases often occur together, and different sections of software can be at **different stages of development** simultaneously. A **working prototype** is **delivered early on** and prototypes are built upon and improved in an **iterative** manner, so that **new prototypes are delivered regularly** throughout the development cycle.

In agile development, there is **less focus on documentation** and more priority is given to **user satisfaction**.

**Benefits:** Produces high-quality code. Flexible to changing requirements. Regular user input throughout.

**Drawbacks:** Poor documentation. Requires consistent interaction between user and programmer.

**Suitability:** Small to medium projects with unclear initial requirements.

---

### Extreme Programming (XP)

**Extreme programming** is an **agile model** that promotes **adaptability** and high **customer involvement**. The development team consists of a **pair of programmers** alongside a **representative end-user**.

The model is built on **user stories**: system requirements are specified by the end-user and used when designing the program. Requirements are often written in the form "As a user, I want to..."

The aim of **paired programming** is to produce **high-quality code**, as code is written by one person and critiqued by the other, so it is improved as it is written. Programmers work **no longer than forty hours a week** to ensure quality is not compromised.

Development follows an iterative sprint-based cycle:

1. **Identify user stories and requirements** with stakeholders (functional and non-functional)
2. **Sprint planning:** break down requirements into tasks, select features for the current **sprint** (a short time-boxed development period, usually 1-4 weeks), and define the sprint goal
3. **Design the solution** with a focus on simple and adaptable design, not heavy upfront documentation
4. **Develop the features**, often using pair programming or small teams
5. **Test continuously** with unit testing, integration testing, and acceptance testing during the sprint (testing is ongoing, not saved for the end)
6. **Sprint review:** demo working software to stakeholders and collect feedback
7. **Sprint retrospective:** the team reflects on what went well and what needs improving, focusing on **team performance and process optimisation**
8. **Release:** deploy working software to users
9. **Repeat** with updated priorities and feedback

Each iteration generates a **working version** of the program, meaning it could function as the final product.

The iterative nature of development means it is hard to produce high-quality documentation, which is less of a priority. For XP to be effective, programmers must **communicate effectively**.

**Benefits:** Produces high-quality code. Constant user involvement means high usability. Highly adaptable, can respond to changes even late in development. Emphasises technical excellence with continuous testing.

**Drawbacks:** High cost of two people working on one project. Teamwork is essential. End-user may not always be able to be present. May lead to **scope creep** (uncontrolled changes in requirements). Intensive collaboration can lead to burnout. May lack documentation.

**Suitability:** Small to medium projects with unclear initial requirements requiring excellent usability, where requirements can change and customer involvement is high.

---

### Spiral Model

The **spiral model** is built on **four key stages** with the focus of effectively managing **risk-heavy projects**. It **combines** aspects of both **iterative (agile)** and **sequential (waterfall)** processes.

The four stages, repeated in each spiral loop, are:

1. **Planning:** define objectives, alternatives, and constraints for the current phase (analysing system requirements)
2. **Risk analysis:** identify and assess potential risks, and plan **mitigation strategies** (pinpointing and mitigating risks)
3. **Engineering:** develop the next version of the product, including design, coding, testing, and integration
4. **Evaluation and feedback:** review progress with stakeholders and plan the next iteration

The process repeats, spiralling through these stages, with each loop representing a development phase until the final product is ready. If the project is found to be **too risky** at any point, the project is **terminated**.

**Benefits:** Thorough **risk-analysis and mitigation**. Caters to changing user needs. Produces prototypes throughout. Provides early partial working solutions, enabling early usage and feedback. Allows for changes and adaptations at various stages.

**Drawbacks:** Hiring risk assessors to analyse risks is **expensive**. Lack of focus on code efficiency. High costs due to constant prototyping. Can be complex and harder to manage. Time-consuming due to emphasis on planning and iterations. Not suitable for small projects.

**Suitability:** **Large, complex, risk-intensive projects** with a high budget, where requirements may change and risk management is essential.

---

### Rapid Application Development (RAD)

**RAD** is an **iterative methodology** that emphasises **fast and iterative development** using **partially functioning prototypes** which are **continually built-upon**.

The steps in the model are:

1. **Requirement planning:** gather general system requirements, define constraints and assumptions. User requirements are initially gathered using **focus groups**.
2. **User design and prototyping:** collaborate with users to develop prototypes, ensuring alignment with user needs. An **incomplete version** of the solution is given to the user to trial.
3. **Construction or iterative development:** build the system incrementally with continuous **user feedback** and adaptation, generating improved prototypes.
4. **Cutover or deployment:** transition the product into the live environment, including user training, support, and documentation.
5. **Maintenance and updates:** continue to adapt and improve the system based on user feedback.

This process continues until the prototype matches the requirements of the end-users, at which point it becomes the **final product**.

RAD is commonly used where **user requirements are incomplete or unclear at the start**. However, as requirements change over the course of the project, additions and changes made to the code may be **inefficient**.

**Benefits:** Caters to changing user requirements. Highly usable finished product. Focus on core features, reducing development time. Enables rapid development and delivery at relatively low cost. Clients are involved throughout.

**Drawbacks:** Poorer quality documentation. Fast pace may reduce code quality. Requires skilled and collaborative team members. Can lead to scope creep.

**Suitability:** Small to medium, low-budget projects with short time-frames, where **rapid delivery is required** and requirements can be developed and refined on the go.

---

## Merits, Drawbacks and Uses of Programming Methodologies

| Methodology | Merits | Drawbacks | Suitable For |
|---|---|---|---|
| **Waterfall** | Straightforward to manage. Clearly documented. Clear stages and milestones. | Lack of flexibility. No risk analysis. Limited user involvement. Expensive to fix late problems. | Static, low-risk projects with well-defined, stable requirements needing little user input (e.g. general-purpose software) |
| **Agile** | Produces high-quality code. Flexible to changing requirements. Regular user input. | Poor documentation. Requires consistent user-programmer interaction. | Small to medium projects with unclear initial requirements |
| **Extreme Programming (XP)** | Produces high-quality code. Constant user involvement means high usability. Highly adaptable. | High cost of paired work. Teamwork essential. End-user may not be present. Scope creep risk. Burnout risk. | Small to medium projects with unclear requirements requiring excellent usability and high customer involvement |
| **Spiral** | Thorough risk-analysis and mitigation. Caters to changing needs. Produces prototypes throughout. Incremental releases. | Expensive (risk assessors). Lack of focus on code efficiency. Complex to manage. Not for small projects. | Large, complex, risk-intensive projects with a high budget |
| **RAD** | Caters to changing requirements. Highly usable product. Fast development. Focus on core features. | Poorer documentation. Fast pace may reduce code quality. Collaboration dependency. Scope creep risk. | Small to medium, low-budget projects with short time-frames requiring rapid delivery |

---

## Writing and Following Algorithms

An **algorithm** is a **set of instructions used to solve a problem**. Algorithms are core to computer science and can be used to tackle a wide range of problems. All good algorithms have certain **key qualities**:

- **Inputs must be clearly defined**, specifying what is valid and what is invalid
- Must always produce a **valid output for any defined input**
- Must be able to **deal with invalid inputs**
- Must always reach a **stopping condition**
- Must be **well-documented** for reference
- Must be **well-commented** so modifications can easily be made

---

## Worked Example: Choosing a Methodology

**Scenario:** A software team producing De-Duplicator is adding a new feature to detect duplicated images. The team must choose between Extreme Programming and the Waterfall lifecycle.

**Approach to answering:** Introduce both methodologies with key features. Compare and contrast them. Identify specifics from the scenario (new feature, existing team). Recommend one methodology with justification.

**Model answer:** XP is flexible and allows continuous feedback, which suits a project adding a new feature where the best implementation approach may need to be discovered iteratively. Waterfall is organised but inflexible, making it difficult if the team uncovers unexpected problems while adding the feature. Given the project involves adding a new feature to existing software (where requirements may evolve during development), XP is the better choice because its flexibility and iterative feedback loops align with the need for ongoing adjustments. Waterfall's rigidity would make it difficult to adapt if requirements change mid-development.

---

## Exam Tips

- When asked to **recommend a methodology** for a scenario, always link specific features of the methodology to specific details in the scenario. Do not just list generic advantages.
- Be able to clearly distinguish between **white box** (tests internal structure, all paths) and **black box** (tests inputs/outputs, no knowledge of internals) testing.
- Remember **TELOS** as a mnemonic for the feasibility study factors in the waterfall model.
- Know that **agile** is an umbrella term for a collection of methodologies (XP is one specific type of agile).
- The key difference between **RAD** and **XP** in exam answers: RAD emphasises partially functioning prototypes and focus groups, while XP emphasises pair programming, user stories, and sprint cycles.
- For comparison questions, always include merits, drawbacks, and suitability for each methodology discussed.
