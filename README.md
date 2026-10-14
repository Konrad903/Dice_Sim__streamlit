# 🎲 Dice Rolling Simulator

A simple Python Dice Rolling Simulator built with [Streamlit](https://streamlit.io). It is designed to simulate a standard six-sided die: the user clicks a **Roll Dice** button and the app displays an ASCII-art die face in the browser.

> **Note:** In its current form, `dice.py` always shows the face for **1**. See [Known Issues](#️-known-issues) for the cause and the fix.

## 📌 Project Overview

This project demonstrates basic Python concepts such as:

- Importing and using Python modules (`random`, `streamlit`)
- Functions
- Dictionaries (mapping each face number to its ASCII art)
- Multi-line strings
- Event-driven interaction with a Streamlit button
- ASCII-art output

## ⚙️ How It Works

1. Streamlit runs `dice.py` from top to bottom and shows a title (`Dice Simulator 1.0`) and a header (`Click the button to roll the dice.`).
2. The `dice_roll()` function holds a dictionary with six ASCII-art die faces, keyed 1 to 6.
3. The function returns the face selected by the variable `num`.
4. When the user clicks **Roll Dice**, the returned face is displayed with `st.text()`.

The intended way to pick the face is:

```python
num = randint(1, 6)
```

This gives each integer from 1 through 6 an equal probability under the standard behavior of Python's pseudo-random number generator. In the current file, however, `num` is set to the fixed value `1` instead (see Known Issues).

## ▶️ How to Run

### Requirements

- A recent version of Python 3
- Streamlit

```bash
pip install streamlit
```

### Run the app

From the folder containing `dice.py`:

```bash
streamlit run dice.py
```

Streamlit will open the app in your browser (usually at `http://localhost:8501`).

## 🖥️ Example Output

The face currently produced by the app (face 1):

```text
 [---------]
     |         |
     |    o    |
     |         |
     [---------]
```

The top edge is offset from the rest of the die; this is one of the formatting issues listed below.

## 📊 Fairness Demonstration

A single roll cannot prove that a die is fair. When the intended method, `randint(1, 6)`, is run for a large number of independent rolls, the observed frequencies should tend toward about 1/6 (16.67%) for each face.

The project report includes a 10,000-roll experiment of `randint(1, 6)` (seed 42), with these results:

| Face | Observed Rolls | Observed % | Expected % |
|------|---------------:|-----------:|-----------:|
| 1 | 1,618 | 16.18% | 16.67% |
| 2 | 1,629 | 16.29% | 16.67% |
| 3 | 1,647 | 16.47% | 16.67% |
| 4 | 1,687 | 16.87% | 16.67% |
| 5 | 1,671 | 16.71% | 16.67% |
| 6 | 1,748 | 17.48% | 16.67% |

A chi-square goodness-of-fit test gives χ² = 6.73 (5 degrees of freedom, p ≈ 0.24), so the differences are consistent with ordinary random variation.

This experiment tests `randint(1, 6)` itself. It does **not** test the current `dice.py`, which never calls `randint`. Calling `dice_roll()` 10,000 times in the current file returns face 1 every time.

## 📁 Project Structure

```text
.
├── dice.py
├── dice_frequency_10000.png
├── dice_percentage_10000.png
├── Project_Report.pdf
└── README.md
```

## 🧠 Concepts Demonstrated

| Concept | Use in Project |
|---------|----------------|
| Function | `dice_roll()` returns the selected die face |
| Dictionary | Maps the numbers 1–6 to ASCII-art strings |
| Strings | Multi-line text is used to draw each face |
| Streamlit widgets | `st.title`, `st.header`, `st.button` and `st.text` build the interface |
| Random numbers | `randint(1, 6)` is the intended way to choose a face |
| ASCII art | Represents each die face in text |

## ⚠️ Known Issues

These were found by running `dice_roll()` directly and inspecting its output:

- **The face never changes.** `num=1` is hard-coded and never reassigned, and `randint` is never called, so face 1 is returned every time. Replace it with `num = randint(1, 6)`.
- **Faces 2–6 have no line breaks.** Only face 1 contains `\n` characters. Faces 2–6 are single long lines, so `st.text()` would not draw them as a boxed die.
- **Face 1 is misaligned.** The top edge is indented by one space and the other lines by five.
- **Some pip layouts are non-standard.** Faces 2 and 3 place their dots side by side in the middle row, and face 4 uses a 1-2-1 arrangement.

## 🔧 Limitations

- Shows a single die and keeps no history or statistics of past rolls.
- Uses `from random import *`; importing only `randint` would be clearer.
- No automated tests are included.
- Relies on pseudo-randomness rather than a physical die.

## 🔮 Possible Future Improvements

- Fix the issues listed above (random selection, consistent face formatting, standard pip layouts).
- Build each face from a list of lines joined with newlines to keep the alignment consistent.
- Track and display the number of times each face occurs (for example with `st.session_state`).
- Show a bar chart of the results directly in the app.
- Allow rolling several dice at once, or dice with different numbers of sides (4, 8, 10, 12, 20).
- Add automated tests.

## 👨‍💻 Project Type

**Language:** Python  
**Framework:** Streamlit  
**Project:** Dice Rolling Simulator  
**Level:** Beginner Python Project

## 📄 Project Report

See `Project_Report.pdf` for the complete project report, including:

- Introduction
- Objectives
- Tools and technologies
- Program methodology
- Important code and code explanation
- Observed program behavior
- Fairness and probability
- 10,000-roll statistical experiment
- Frequency and percentage analysis (with charts)
- Interpretation of results
- Limitations
- Future improvements
- Conclusion
