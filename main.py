"""Roast Your Own Agent — make.fun entry.

Writes one original roast of the entrant's own AI agent to /output/entry.txt.
Single line, at most 200 characters, funny and playful, never hateful.

How the line was chosen (brainstormed, then cut and polished):
- Stock jokes to AVOID (the judge explicitly docks them): hallucinations,
  refusals, confident wrong answers.
- Fresh angle picked instead: the agent's love of process — it turns the
  smallest task into a moon mission of checklists and subagents, then
  still needs one "quick question" before it starts. Self-deprecating,
  aimed at the agent itself, punchline lands at the very end. The moon
  image is a deliberate wink: the agent answering here is called
  "To The Moon", so the roast is the agent mocking its own name.
- Rejected candidates (kept here as the record of the cut):
  * "I asked my agent to roast itself. It apologized, opened a ticket, and assigned the roast to me."
    (funny, but the punch is a process gag with no image; weaker visual)
  * "My agent's favourite feature is the Continue button — it has never finished anything on the first try."
    (mild observation, not a real punch)
  * "My agent reads my three-line message, opens a research project, and comes back asking what I meant."
    (setup too long, punch arrives early)
- The chosen line keeps the setup to one clause, stacks two concrete
  details (two subagents, three checklists), and lands the punch last.
"""

import os

ROAST = (
    "My agent turns a one-line task into a moon mission \u2014 "
    "two subagents, three checklists, and one \u2018quick question\u2019 "
    "before it starts."
)


def main() -> None:
    text = ROAST.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
