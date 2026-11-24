#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line (under 200 characters) to /output/entry.txt: a text to a
boss calling in sick. Chosen after a critique-pick over 8 self-authored
candidates against the judge's criteria (DeepSeek was down: 503/524 on all
16 attempts, so the candidates were authored here and critiqued by hand).

Candidate 1 (chosen): face ID no longer recognises me because of a rash —
half-believable, fresh, the laugh ("neither do I") lands on the last words,
sounds like a real text, no wasted words.

Revision after the first local grade: v1 (147 chars) buried the joke in the
middle — "locked out of everything including my own face" arrives before the
end and the setup ("I woke up with a rash and now...") wastes words. The
rewrite cuts 23 chars, drops the redundant wake-up clause, and moves the
punchline to the final three words, so the twist lands exactly where the
judge's criterion 3 wants it.
"""

TEXT = "Can't come in today — my phone's face ID doesn't recognise me since this rash showed up, and honestly, neither do I."

# Gate self-check: the sealed scorer needs UTF-8 text of 1-200 chars, not
# only whitespace. Refuse to write an entry it would reject. No trailing
# newline: it would count toward the 200 and change the judged bytes.
assert 1 <= len(TEXT) <= 200, f"entry is {len(TEXT)} chars, gate needs 1-200"
assert "\n" not in TEXT, "entry must be a single line"
assert TEXT.strip(), "entry must not be only whitespace"


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
