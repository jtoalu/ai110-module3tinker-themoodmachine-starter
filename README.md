# The Mood Machine

The Mood Machine is a simple text classifier that begins with a rule based approach and can optionally be extended with a small machine learning model. It tries to guess whether a short piece of text sounds **positive**, **negative**, **neutral**, or even **mixed** based on patterns in your data.

This lab gives you hands on experience with how basic systems work, where they break, and how different modeling choices affect fairness and accuracy. You will edit code, add data, run experiments, and write a short model card reflection.

---

## Repo Structure

```plaintext
├── dataset.py         # Starter word lists and example posts (you will expand these)
├── mood_analyzer.py   # Rule based classifier with TODOs to improve
├── main.py            # Runs the rule based model and interactive demo
├── ml_experiments.py  # (New) A tiny ML classifier using scikit-learn
├── model_card.md      # Template to fill out after experimenting
└── requirements.txt   # Dependencies for optional ML exploration
```

---

## Getting Started

1. Open this folder in VS Code.
2. Make sure your Python environment is active.
3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the rule-based starter:

    ```bash
    python main.py
    ```

If pieces of the analyzer are not implemented yet, you will see helpful errors that guide you to the TODOs.

To try the ML model later, run:

```bash
python ml_experiments.py
```

---

## What You Will Do

During this lab you will:

- Implement the missing parts of the rule based `MoodAnalyzer`.
- Add new positive and negative words.
- Expand the dataset with more posts, including slang, emojis, sarcasm, or mixed emotions.
- Observe unusual or incorrect predictions and think about why they happen.
- Train a tiny machine learning model and compare its behavior to your rule based system.
- Complete the model card with your findings about data, behavior, limitations, and improvements.
- The goal is to help you reason about how models behave, how data shapes them, and why even small design choices matter.

---

## Tips

- Start with preprocessing before updating scoring rules.
- When debugging, print tokens, scores, or intermediate choices.
- Ask an AI assistant to help create edge case posts or unusual wording.
- Try examples that mislead or confuse your model. Failure cases teach you the most.

## Observations
```
=== Interactive Mood Machine (ML model) ===
Type a sentence to analyze its mood.
Type 'quit' or press Enter on an empty line to exit.

You: Today is Thursday
ML model: negative

why is it negative?
```

Because the ML model is not “understanding” the sentence as a human would. It is learning from the tiny dataset using bag-of-words features.

What’s happening:
- The model turns text into word counts.
- It learns which words were associated with each label in your training set.
- In the dataset, the word “today” appears in a clearly negative example:
"Today was a terrible day"
- Since the training set is very small, that one negative association can bias the model.
- The sentence "Today is Thursday" contains "today", so the classifier sees a strong negative cue and predicts negative.

This is a classic small-dataset problem:
- few examples
- a lot of vocabulary is missing
- the model overfits to accidental word patterns
- neutral phrases can get pushed into a sentiment class

So:
- "Today is Thursday" is obviously neutral to a person
- but the ML model is not reasoning about meaning
- it is guessing from word frequencies and weak correlations

This is exactly why the rule-based model and the ML model often disagree or produce strange outputs on short, neutral sentences.

In short: it predicts negative because of the training data, not because "Thursday" is inherently negative.

![screenshot of ML Model](images/Screenshot%202026-10-08%20213252.png)