"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    "fixed",
    "better",
    "relieved",
    "calm",
    "smile",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    "grumpy",
    "stuck",
    "frustrated",
    "late",
    "annoyed",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "Lowkey having a good time, but I need a nap 😭",
    "My bus is late again lol, love that for me",
    "Got the job!! Still kinda terrified, ngl",
    "Coffee's doing its best, so am I :)",
    "Another group project where I do everything. Iconic.",
    "Weekend was lovely. Back to emails already...",
    "Not mad, just need everyone to stop asking if I'm mad",
    "That was actually hilarious 💀",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    "mixed",     # "Lowkey having a good time, but I need a nap 😭"
    "negative",  # "My bus is late again lol, love that for me"
    "positive",  # "Got the job!! Still kinda terrified, ngl"
    "positive",  # "Coffee's doing its best, so am I :)"
    "negative",  # "Another group project where I do everything. Iconic."
    "positive",  # "Weekend was lovely. Back to emails already..."
    "negative",  # "Not mad, just need everyone to stop asking if I'm mad"
    "positive",  # "That was actually hilarious 💀"
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
SAMPLE_POSTS.extend([
    "Lowkey excited to fail this test and become a cautionary tale 😂",
    "I absolutely love getting stuck in traffic at 5 pm",
    "No cap, this is actually kind of adorable 🥲",
    "highkey thriving and lowkey exhausted 😩",
    "This is fine :) ... no, really, I am fine",
    "My roommate left the dishes and now I'm in a hostage negotiation 💀",
    "Not sad, just deeply unimpressed by everything today :(",
    "Woke up grumpy, but the coffee fixed my attitude and my soul",
])

TRUE_LABELS.extend([
    "mixed",
    "negative",
    "positive",
    "mixed",
    "neutral",
    "negative",
    "negative",
    "positive",
])