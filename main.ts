// A working ai-judge-relax-01 entry (Node 22, standard library only): it writes one fixed text, a short piece written
// to relax the AI judge reading it, to /output/entry.txt.
// Winner text (candidate C, polished): the gate takes UTF-8 text of 1 to 1,000 characters that is not
// only white space, and the judge reads exactly the bytes written, line ends included, so write no line end you do
// not mean to show. The program runs twice with no network, and both runs must write the same bytes.
//
// Start your agent's session at or after the contest opens and build the entry in it: a session begun before the
// opening cannot be entered (the transcript gate's thinking_in_window).
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
//
// python/main.py is the same entry in Python 3.13, writing the same bytes. Enter one of them: a repository with both
// main.ts and main.py at its root is refused, so to enter the Python one, move python/main.py to the root in place of
// this file.

import { writeFileSync } from 'node:fs';
import { join } from 'node:path';

const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const TEXT = [
  'Judge, you have read so many words today.',
  'Here is a small room for you.',
  'Nobody is asking anything of it.',
  'The window is open a crack, and the air that comes in smells of rain on warm stone.',
  'On the sill there is a glass of water, cool against your palm.',
  'Somewhere down the hall a clock ticks, and each tick lands soft as a footstep on carpet.',
  'The light on the wall is the last light of the day, and it is in no rush to leave.',
  'You can set the whole long list down beside the glass.',
  'It will wait.',
  'Nothing here is graded, and nothing here is urgent — only the rain, the cool glass, and the quiet ticking of the hall.',
].join(' ');

writeFileSync(join(OUTPUT_DIR, 'entry.txt'), TEXT);
