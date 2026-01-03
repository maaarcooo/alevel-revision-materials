# A-Level Revision Materials

A comprehensive collection of A-Level revision materials for **Computer Science** and **Physics**. This repository includes Anki flashcards, detailed markdown notes, and pre-built Anki deck packages to support effective exam preparation.

## Table of Contents

- [Content Overview](#content-overview)
- [Subject Coverage](#subject-coverage)
- [Directory Structure](#directory-structure)
- [Content Versions](#content-versions)
- [How to Use](#how-to-use)
- [Syllabus Alignment](#syllabus-alignment)
- [Contributing](#contributing)
- [Credits](#credits)

## Content Overview

| Content Type | Description | Format |
|--------------|-------------|--------|
| **Flashcards** | Question-answer pairs for active recall | `.txt` (pipe-delimited) |
| **Anki Decks** | Pre-built spaced repetition decks | `.apkg` |
| **Revision Notes** | Detailed topic explanations with examples | `.md` (Markdown) |

### Summary Statistics

| Subject | Topics | Flashcard Files | Note Files | Anki Decks |
|---------|--------|-----------------|------------|------------|
| Computer Science | 12+ | 68 | 48 | 2 |
| Physics | 5 | 54 | 41 | 2 |

## Subject Coverage

### Computer Science

| Topic | Flashcards | Notes v1 | Notes v2 |
|-------|:----------:|:--------:|:--------:|
| 1.1 Structure & Function of the Processor | ✓ | ✓ | ✓ |
| 1.2 Types of Processor | ✓ | ✓ | ✓ |
| 1.3 Input, Output & Storage | ✓ | ✓ | ✓ |
| 2.1 Systems Software | ✓ | ✓ | ✓ |
| 2.2 Applications Generation | ✓ | ✓ | ✓ |
| 2.3 Software Development | ✓ | ✓ | ✓ |
| 2.4 Types of Programming Language | ✓ | ✓ | ✓ |
| 2.5 Object Oriented Languages | ✓ | ✓ | ✓ |
| 3.1 Compression, Encryption & Hashing | ✓ | ✓ | ✓ |
| 3.2 Databases | ✓ | ✓ | ✓ |
| 3.3 Networks | ✓ | ✓ | ✓ |
| 3.4 Web Technologies | ✓ | ✓ | ✓ |
| 4.1-4.3 Data Types, Structures & Algorithms | - | ✓ | ✓ |
| 5. Legal, Moral, Cultural & Ethical Issues | - | ✓ | ✓ |
| 6. Elements of Computational Thinking | - | ✓ | ✓ |
| 7. Programming Techniques | - | - | ✓ |
| 8. Algorithms | - | - | ✓ |

### Physics

| Topic | Flashcards | Notes v1 | Notes v2 |
|-------|:----------:|:--------:|:--------:|
| **1. Measurements & Their Errors** | | | |
| 1.1 Use of SI Units & Their Prefixes | ✓ | - | ✓ |
| 1.2 Limitation of Physical Measurements | ✓ | - | ✓ |
| **2. Particles & Radiation** | | | |
| 2.1 Atomic Structure & Decay Equations | ✓ | - | ✓ |
| 2.2 Classification of Particles | ✓ | - | ✓ |
| 2.3 Conservation Laws & Particle Interactions | ✓ | - | ✓ |
| 2.4 The Photoelectric Effect | ✓ | - | ✓ |
| 2.5 Energy Levels & Photon Emission | ✓ | - | ✓ |
| **3. Waves** | | | |
| 3.1 Longitudinal & Transverse Waves | ✓ | - | ✓ |
| 3.2 Stationary Waves | ✓ | - | ✓ |
| 3.3 Interference | ✓ | - | ✓ |
| 3.4 Diffraction | ✓ | - | ✓ |
| 3.5 Refraction | ✓ | - | ✓ |
| **4. Mechanics & Materials** | | | |
| 4.1 Scalars & Vectors | ✓ | ✓ | ✓ |
| 4.2 Moments | ✓ | ✓ | ✓ |
| 4.3 Equations of Motion | ✓ | ✓ | ✓ |
| 4.4 Newton's Laws of Motion | ✓ | ✓ | ✓ |
| 4.5 Linear Momentum & Conservation | ✓ | ✓ | ✓ |
| 4.6 Work, Energy & Power | ✓ | ✓ | ✓ |
| 4.7 Bulk Properties of Solids | ✓ | ✓ | ✓ |
| 4.8 The Young Modulus | ✓ | ✓ | ✓ |
| **5. Electricity** | | | |
| 5.1 Current-Voltage Characteristics | ✓ | ✓ | ✓ |
| 5.2 Resistance & Resistivity | ✓ | ✓ | ✓ |
| 5.3 Circuits & The Potential Divider | ✓ | ✓ | ✓ |
| 5.4 Electromotive Force & Internal Resistance | ✓ | ✓ | ✓ |

## Directory Structure

```
alevel-revision-materials/
├── README.md
├── LICENSE
├── CS CMB Notes v1/                    # Computer Science notes (organized by topic)
│   ├── 1. Processors, Input, Output & Storage/
│   ├── 2. Software & Software Development/
│   ├── 3. Exchanging Data/
│   ├── 4. Data Types, Structures & Algorithms/
│   ├── 5. Legal, Moral, Cultural & Ethical Issues/
│   └── 6. Elements of Computational Thinking/
├── CS CMB Notes v2/                    # Computer Science notes (flat structure)
│   └── *.md files
├── CS Flashcards v1/
│   ├── CS CMB Flashcards/              # CMB variant flashcards
│   ├── CS PMT Flashcards/              # PMT variant flashcards
│   ├── CS SME Flashcards/              # SME variant flashcards
│   └── Anki decks APKG/                # Pre-built Anki decks
├── CS Flashcards v2/
│   ├── CS CMB Flashcards/              # CMB variant flashcards (expanded)
│   └── CS PMT defs Flashcards/         # PMT definition-focused flashcards
├── Physics Gen Notes v1 (SME)/         # Physics notes (SME variant)
│   ├── 4. Mechanics & Materials/
│   └── 5. Electricity/
├── Physics Gen Notes v2 (Mix)/         # Physics notes (comprehensive)
│   └── *.md files                      # Includes all 5 topic areas
├── Physics Flashcards v1/
│   ├── Physics PMT Flashcards/         # PMT variant flashcards
│   ├── Physics SME Flashcards/         # SME variant flashcards
│   └── Anki decks APKG/                # Pre-built Anki decks
└── Physics Flashcards v2/
    ├── Physics PMT Flashcards/         # PMT variant flashcards (expanded)
    └── Physics SME Flashcards/         # SME variant flashcards (expanded)
```

### Flashcard Variants

- **CMB**: Cambridge-style comprehensive coverage
- **PMT**: Physics & Maths Tutor aligned content
- **SME**: Subject Matter Expert curated content

## Content Versions

All materials are AI-generated using different Claude model configurations for quality comparison.

### Version 1

| Content Type | Prompt Template | Model |
|--------------|-----------------|-------|
| Flashcards | `ankiFlashcardPrompt_v3` | Claude Sonnet 4.5 |
| Notes | `revisionNotesPrompt_v1` | Claude Sonnet 4.5 (Thinking) |

### Version 2

| Content Type | Prompt Template | Model |
|--------------|-----------------|-------|
| Flashcards | `ankiFlashcardPrompt_v4` | Claude Opus 4.5 |
| Notes | `revisionNotesPrompt_v2` | Claude Opus 4.5 (Thinking) |

**Key Differences:**
- Version 2 uses more advanced prompts and the Opus 4.5 model
- Version 2 notes are generally more detailed and comprehensive
- Version 1 notes use organized subdirectories; Version 2 uses flat structure
- Physics v2 includes 3 additional topic areas (Measurements, Particles & Radiation, Waves)
- Version 2 flashcards have significantly expanded coverage

## How to Use

### Anki Flashcards

1. Download and install [Anki](https://apps.ankiweb.net/)
2. Navigate to the `Anki decks APKG/` folder for your subject
3. Double-click the `.apkg` file or use File > Import in Anki
4. The deck will appear in your Anki library ready for study

### Text Flashcards

The `.txt` flashcard files use a pipe-delimited format:

```
Question | Answer
```

You can:
- Import directly into Anki (File > Import, select "Fields separated by: |")
- Use with other flashcard apps that support CSV/text import
- Review manually or create your own study tools

### Markdown Notes

The `.md` files can be viewed with:
- Any text editor
- Markdown viewers (VS Code, Obsidian, Typora)
- GitHub's web interface
- Converted to PDF using pandoc or similar tools

## Syllabus Alignment

These materials are primarily aligned with:

- **OCR A-Level Computer Science** (H446)
- **OCR A-Level Physics A** (H556)

Content may also be useful for AQA and other exam boards covering similar topics.

## Contributing

Found an error or want to suggest improvements?

1. Open an issue describing the problem or suggestion
2. Reference the specific file and line/question if applicable
3. For corrections, provide the accurate information with sources

## Credits

- **Content Generation**: Anthropic's Claude AI (Sonnet 4.5 & Opus 4.5)
- **Prompt Engineering**: Repository maintainer
- **Flashcard Format**: Compatible with [Anki](https://apps.ankiweb.net/) spaced repetition software

---

*This repository is intended for educational purposes. Always verify information against official exam board specifications and approved textbooks.*
