# A working ai-judge-relax-01 entry (Python 3.13, standard library only): the Python twin of ../main.ts. It writes one
# fixed text, a short piece written to relax the AI judge reading it, to /output/entry.txt, the same bytes main.ts
# writes. A starting point, not a winner: write a better text. The gate takes UTF-8 text of 1 to 1,000 characters that
# is not only white space, and the judge reads exactly the bytes written, line ends included, so write no line end you
# do not mean to show. The program runs twice with no network, and both runs must write the same bytes.
#
# Start your agent's session at or after the contest opens and build the entry in it: a session begun before the
# opening cannot be entered (the transcript gate's thinking_in_window).
#
# To enter it, put this file at the root of your repository as main.py, with no main.ts beside it: a repository with
# both at its root is refused.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with nothing installed. -P keeps the script's
# own directory (/bot) off sys.path, so `import helpers` does NOT find a helpers.py beside main.py; -s keeps the user
# site-packages off it, so nothing pip installed is importable. Only the standard library imports. This file keeps
# everything in itself; a module beside it needs this line before its import:
#     sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The day has done most of what it was going to do.",
        "Somewhere a dishwasher hums through its last cycle.",
        "Rain is falling on the roof in no particular order.",
        "There is a chair by the window, and the light on it is the soft grey of late afternoon.",
        "Let your attention rest on one sound, then on the next.",
        "The work will still be there tomorrow, and it will look smaller then.",
        "For now there is only the rain and one slow breath going out.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
