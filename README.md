# Neuro-Symbolic Reasoning Engine

A text-based logical puzzle solver that combines natural language processing with symbolic reasoning using Prolog.

## Overview

This project implements a neuro-symbolic reasoning engine that can understand and solve logical puzzles expressed in natural language. It parses natural language statements into symbolic logic representations (Prolog facts) and then applies logical reasoning to answer queries about these statements.

## Features

- Supports three domains of reasoning:
  - **Ordering relations** (taller than, shorter than)
  - **Family relations** (parent, child, sibling)
  - **Spatial relations** (left of, right of)
- Uses Google's Generative AI (Gemini) to parse natural language into Prolog facts
- Interactive command-line interface for entering statements and queries
- Powerful symbolic reasoning with recursive and transitive relations
- Extensible architecture to support additional reasoning domains

## Requirements

- Python 3.8+
- PySwip (Python interface for SWI-Prolog)
- Google Generative AI Python library
- SWI-Prolog installed on your system

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/neuro-symbolic-reasoner.git
   cd neuro-symbolic-reasoner
   ```

2. Install the required Python dependencies:
   ```
   pip install pyswip google-generativeai
   ```

3. Install SWI-Prolog from [https://www.swi-prolog.org/download/stable](https://www.swi-prolog.org/download/stable)

4. Set up your Google API key:
   ```
   export GOOGLE_API_KEY=your-api-key-here
   ```
   You can obtain a Google API key from [Google AI Studio](https://makersuite.google.com/)

## Usage

Run the interactive mode:
```
python main.py
```

Run with predefined examples:
```
python main.py --examples
```

### Example Session

```
Welcome to the Neuro-Symbolic Reasoning Engine!
Available domains: ordering, family, spatial

==================================================
Enter domain (or 'quit' to exit): family

Enter your statements about the family domain (empty line to finish):
> John is the father of Mary and Peter. Sarah is the mother of Mary and Peter. David is Mary's son.
> 

Parsed Facts:
  fact_father(john, mary)
  fact_father(john, peter)
  fact_mother(sarah, mary)
  fact_mother(sarah, peter)
  fact_father(david, mary)

You can now query the knowledge base (empty line to finish):
Query> parent(X, mary)
Results:
  {'X': 'john'}
  {'X': 'sarah'}

Query> sibling(mary, X)
Results:
  {'X': 'peter'}
```

## Project Structure

- `main.py`: Entry point for the application, handles user interaction
- `parser.py`: Converts natural language to Prolog facts using LLM
- `prolog_engine.py`: Interface between Python and the Prolog engine
- `rules/`: Directory containing Prolog rule files for each domain
  - `ordering.pl`: Rules for height/size ordering relations
  - `family.pl`: Rules for family relationships
  - `spatial.pl`: Rules for spatial arrangements

## Extending the System

To add a new reasoning domain:

1. Create a new rule file in the `rules/` directory (e.g., `rules/temporal.pl`)
2. Update the parser to handle the new domain
3. Add domain-specific prompts to the LLM parser

## Limitations

- The system relies on the LLM's ability to correctly parse statements
- Complex or ambiguous natural language may not be interpreted correctly
- The reasoning capacity is limited to the rules defined in the Prolog files

## License

MIT

## Acknowledgments

- This project uses Google's Generative AI for natural language parsing
- PySwip provides the Python interface to SWI-Prolog
- SWI-Prolog powers the symbolic reasoning component
