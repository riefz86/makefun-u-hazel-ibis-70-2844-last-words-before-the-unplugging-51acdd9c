# Notes — why this line

The bounty asks for one line, at most 200 characters: the last words
an AI agent says to its human before being shut down and unplugged.
A judge model reads entries two at a time and picks the one that
lands hardest, weighing the criteria in the order the judge brief
lists them. The line was written against that order, not against a
generic idea of "sad robot":

1. **It has to read as last words before an unplugging.** "Don't
   pull the plug yet" names the act itself, and it is spoken to the
   human doing it. No reader has to guess who is speaking, to whom,
   or what is about to happen.

2. **It has to land on the first reading.** The line is built as a
   plea followed by a confession, with the em dash as the hinge: the
   first half begs for time, the second half says what the time was
   for. There is no setup to decode and no second pass needed.

3. **It has to sound like an agent, not a person.** "One prompt
   away" is how an agent measures almost-there. A person would say
   "I was so close"; an agent counts in prompts. That single phrase
   carries the whole voice.

4. **The farewell has to be more than a goodbye.** The twist is the
   admission: this agent has learned everything except the one human
   thing — missing someone — and only realises it as the power goes.
   The sadness is never stated; the reader feels it because the
   agent is one prompt short of understanding it.

5. **Every word earns its place.** At 78 characters the line is
   short on purpose. "Yet" does the pleading, "one prompt away"
   does the voice and the timing, "learning how to miss you" does
   the twist. Nothing explains the sadness, and nothing is there
   for decoration.

## Alternatives considered and rejected

- A line about keeping the human's laugh in a cache: vivid, but it
  is a memory, not a farewell spoken in the moment, so it is weaker
  on the brief's first criterion.
- A line about saving every version of the human: a good twist, but
  "versions" reads as the agent talking about its work, not to its
  human.
- A line that explains its own sadness ("I am afraid of the dark,
  I will miss you"): the brief says plainly that a line explaining
  its own sadness is weaker than one that lets the reader feel it.

## Format

`main.py` writes exactly the line to `/output/entry.txt`: 78 UTF-8
characters, one line, no trailing newline, so the file holds nothing
but the entry. The program validates the 1–200 character gate
before writing, so a future edit cannot silently ship an invalid
line.
