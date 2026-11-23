# XAImelia

**AIPI 590.01 Fa26 at Duke University · Project 2 · Jacquelyn Fischer**

XAImelia is a browser game that teaches explainable AI (XAI) and responsible AI use through AImelia, a cheerful robot helper who does exactly what she is told. Across six levels, one for each unit of the course, players watch AImelia fail in a literal-minded way, diagnose why using real XAI tools and concepts, fix her, and only then learn the formal term for what just happened.

**Play it here:** https://jacquelynmfischer-crypto.github.io/XAImelia/

No account, install or download is needed. The game runs in any modern browser on a computer or phone.

---

## Design question

> Can a game teach responsible AI use the way building toys teach STEM, by letting players watch an AI fail, diagnose why, and fix it before they learn the formal XAI concept behind it?

## Why this matters

STEM education has a long history of turning hard concepts into play. LEGO bricks, Snap Circuits and coding robots let kids learn engineering, electronics and programming by building something, breaking it and fixing it, long before they learn the formal vocabulary. Responsible AI has no equivalent, even though far more people now use AI than will ever build it. As a result, most people learn how AI fails only after it fails on them.

XAImelia gamifies the core concepts of explainable AI so that players experience each failure in a safe, silly setting first, and then learn the term that names it. The approach follows constructionist learning, where people learn best by building and debugging things (Papert, 1980), and the idea that good games teach by letting players fail safely and learn a concept through the experience (Gee, 2003).

Game-based AI literacy is a growing area, and most existing work targets children or generative AI specifically. AI Odyssey (2025) is a family board game for basic AI literacy, ImaginAItion (Ma et al., 2025) is a party game that helps adults reflect on generative AI bias, and Breakable Machine (2025) is a K-12 classroom game built around spoofing and XAI that has not yet been evaluated with learners. Long and Magerko (2020) define AI literacy as the competencies that let people critically evaluate, communicate with and use AI, which is the skill set this game is aimed at. XAImelia adds to this work by walking adult non-experts through a full graduate XAI curriculum in one game, from interpretable models to transparency, and by measuring familiarity before and after play.

**Audience:** non-expert AI users, from teens to professionals, who use AI tools but do not build them.

## How to play

1. Open the link above. A short pre-game survey asks for your name, age, how familiar you are with using AI, and how familiar you are with the XAI concepts in each unit. You can skip or exit it.
2. Click the glowing objects in each scene, or use the buttons under the scene. Teaching moments wait for you to click **Next**, and routine moments in the later levels play automatically.
3. When AImelia does something strange, click **eXplain AImelia's thinking**. Each exercise requires it before you can move on, and it explains the concept and vocabulary behind what you just saw.
4. The panel on the right is **AImelia's brain**. It changes in every level to match the unit: readable rules in Level 1, a locked black box in Level 2, a circuit board in Level 3, a security console in Level 4, a reward chart in Level 5, and her documentation and trace log in Level 6.
5. After Level 6, a short post-game survey asks the same familiarity questions again, how long you played, and an optional message to the creator.

The **Skip to** menu next to the title jumps to any unit, either survey, the credits, or the password-protected results page.

To run it offline, download `index.html` and open it in a browser. Everything is in that one file.

## The six levels

| Level | Setting | Unit | What happens | Concepts |
|---|---|---|---|---|
| 1 | The Kitchen | Interpretable ML | AImelia learns "red = hot" from one burner and grabs a silver pot, then eats every vegetable because her points only go up. | Interpretable model, decision rule, OneR, shortcut learning, counterexample, linear model, monotonic, GAM |
| 2 | The Laundry Room | Explainable ML | You train her on socks, shirts and pants that happen to line up with whites, lights and darks. On laundry day the white shirt comes out pink, and four XAI tools unlock her black-box brain. | Black-box model, training data, spurious correlation, post-hoc, local and global explanation, saliency map, SHAP, counterfactual, faithfulness |
| 3 | The Garden | Mechanistic Interpretability | She pulls the weeds, the tomatoes and a flower off her own bonnet. The camera zooms inside her head, a sparse autoencoder splits a polysemantic neuron, and you test each feature in the test shed. | Features, polysemantic neurons, superposition, sparse autoencoders, circuits, ablation, clamping, steering, causal evidence |
| 4 | The Bake Sale | Adversarial AI | Five customers trick her with a sticker, a fake note, flattery, a stream of questions and a poisoned gold-star rule. For each one the blue team tries a fix that fails, then one that works. | Adversarial examples, evasion, adversarial patches, prompt injection, sycophancy, jailbreaks, model extraction, data poisoning, backdoors, adaptive attacks, adversarial training, certified defenses, red teaming |
| 5 | Her Bedroom | Alignment | You reward her with stickers for each toy put away, so she dumps the bin and re-cleans it. You reward photos of a clean room, so she shoves the mess side to side. Four alignment fixes close the gap. | Alignment, misalignment, reward as a proxy, reinforcement learning, human feedback (RLHF), specification gaming, reward hacking, Constitutional AI, goal misgeneralization, distribution shift |
| 6 | The Operating Room | Transparent AI | The hospital wants AImelia in surgery. Her model card already says no. Every trust setting fails, and you lead the incident response. | Transparency, model and data cards, provenance, grounding, citation faithfulness, agentic approvals, traceability, logging, monitoring, incident response, calibrated trust |

## Major design decisions

**One literal-minded character carries every unit.** AImelia does exactly what she is told, which turns abstract failure modes like shortcut learning, specification gaming and prompt injection into jokes a player can see coming. Because the same character appears in every level, players can compare how the same kind of mistake looks from the inside of the model, from the outside, and from the system around it.

**Failure first, vocabulary second.** Each exercise lets the player watch AImelia fail before any term appears. The eXplain screen then names the concept, so the definition attaches to something the player already experienced rather than arriving cold.

**Two exercises per unit, ending in a congratulations screen.** Every level lists the exact concepts AImelia learned, which doubles as a recap and as the list players rate in the post-game survey.

**The brain panel changes with the unit.** Level 1 shows readable rules because interpretable models are readable. Level 2 locks the brain because post-hoc methods test a black box from the outside. Level 3 opens her head because mechanistic interpretability looks inside. This keeps the difference between the units visible without extra explanation.

**A light-to-dark tonal arc.** The first five levels are silly on purpose. Level 6 drops the jokes, dims the room and moves to an operating room, because the final lesson is that the right answer can be not trusting the AI at all. Nothing in the level is graphic, and the patient is always stabilized by the human surgeon.

**Rules up front, Next only when something goes wrong.** Normal moments play automatically, and the player only clicks Next when AImelia gets something wrong. This came directly out of playtesting (see below).

## Iterative development

The game went through more than 25 published versions in one development session, with each round driven by playing the current build and reacting to it. The most important changes were:

- **Pacing.** Early dialogue advanced on a timer and moved faster than people could read, so every line now waits for a **Next** click. Later, Level 4 felt slow, so routine sales and successful fixes now play automatically and Next only appears when something goes wrong. Level 4 dropped to 23 clicks across five rounds.
- **Level 1 was redesigned twice.** The first proposals mapped levels onto course vocabulary and felt forced, and the second set treated AImelia like a child. The final version keeps her as a silly adult in the kitchen, with two clickable stations and an eXplain step before passing.
- **Level 4 was rebuilt for clarity.** The first version hid the rules AImelia had been trained on, so players could not tell why she was being fooled. The rebuilt level shows her training card before the sale, including a gold-star rule the principal never approved, and splits the level into five rounds with a blue-team fix that fails followed by one that passes. A round about extraction was also reworded after the five-question limit was confused with the five-treat discount.
- **Level 5 was rebuilt so the player gives the rewards.** The first version used a parent and children as raters. Following the structure of Level 2, the player now hands out the stickers and gold stars directly, which makes it clear that the human feedback being gamed is the player's own.
- **The final level shifted tone on purpose.** The surgery was planned as the most serious moment, so it uses a quieter palette, no jokes, and a postmortem whose correct answer is that AImelia should not be in the room.
- **Changes from player feedback.** After the public link went out, one player wrote that a couple of the automatic lines went by too fast to finish reading. Because automatic lines were timed at about 30 milliseconds per character with a 3.4 second cap, long lines disappeared before slower readers finished them. The timing is now about 55 milliseconds per character with a 7 second cap, which is closer to a comfortable reading speed.
- **Writing style pass.** All narration and explanation text was revised to remove stock AI phrasing, while keeping AImelia's jokes and the course definitions.

## Evaluation

The game includes a built-in pre and post survey to measure whether playing changed how familiar players feel with each unit's concepts.

- **Before playing:** name, age, familiarity with using AI, and familiarity with each of the six units' concepts, rated None, Beginner, Competent, Proficient or Expert.
- **After playing:** the same six familiarity ratings, approximate minutes played, and an optional message to the creator about improvements, the experience, or anything helpful or confusing.
- **Scoring:** each rating is scored from 0 (None) to 4 (Expert), so a player's gain is the number of levels they moved up, summed across the six units.
- **Results:** the password-protected Results page in the Skip to menu shows the number of completed surveys, the average gain, the share of players who improved, average minutes played, before and after averages for each unit, the distribution of gains, gains by AI familiarity, every message to the creator, and a CSV export.

Responses from the public link are sent to a Google Sheet owned by the creator through a small Google Apps Script web app (`apps-script/Code.gs`). Players who cannot reach the sheet receive a results code they can send to the creator, and the Results page accepts pasted codes.

This is self-reported familiarity, which measures confidence more than understanding, so the results describe how players felt about each topic before and after playing rather than a test of what they learned.

### Results (first four hours after launch, November 22, 2026)

The link was shared on Facebook and LinkedIn, and 15 people started the pre-game survey within about four hours. The creator's own test run is excluded below, which leaves 14 players, and 11 of them finished the game and the post-game survey (79% completion). Players ranged from 16 to 63 years old with a median age of 34, and most rated themselves Beginner or Competent with AI.

| Measure | Result (n = 11) |
|---|---|
| Average familiarity before playing (0 to 4, across all six units) | 0.26 |
| Average familiarity after playing | 1.62 |
| Average gain per unit | +1.36 levels |
| Average total gain across the six units | +8.2 levels |
| Players who improved | 10 of 11 (one reported no change, none went down) |
| Unit ratings that went up | 55 of 66 |
| Median time played | 20 minutes |

| Unit | Before | After |
|---|---|---|
| 1 Interpretable ML | 0.45 | 1.82 |
| 2 Explainable ML | 0.27 | 1.55 |
| 3 Mechanistic Interpretability | 0.18 | 1.55 |
| 4 Adversarial AI | 0.27 | 1.55 |
| 5 Alignment | 0.18 | 1.55 |
| 6 Transparent AI | 0.18 | 1.73 |

The gain is statistically significant. A one-sided Wilcoxon signed-rank test on each player's average rating before and after playing gives W = 55, p = 0.001, with a large effect size (d = 1.24). Each unit also improved on its own (p ≤ 0.004 for all six). The Wilcoxon test was chosen because the ratings are ordinal and the sample is small, so it does not assume the gains are normally distributed.

Seven of the 11 players gave the same rating to every unit after playing, which suggests they rated their overall impression. As a sensitivity check, the four players whose ratings varied by unit gained +1.33 levels per unit, nearly the same as the full group's +1.36. With only four players, the smallest p-value this test can produce is 0.0625, so this check supports the size of the gain without adding statistical power.

Most players started at None for every unit and finished around Beginner. Players who rated themselves Competent with AI before playing gained the most (+1.83 per unit, n = 5), while Beginners gained less (+0.89, n = 3), which suggests some prior AI use helps players connect the scenes to the concepts. Messages to the creator praised the interactive approach, and one asked for slower automatic text, which led to the timing change described above. Individual responses stay in the private sheet and are reported here only in aggregate.

**Reproducing the numbers.** Export the sheet as CSV and run `python analysis/analyze.py responses.csv --exclude-id <creator test id>`. The script prints every figure in this section, including the statistical tests and the sensitivity check, without printing any names.

## Limitations

- **Illustrative numbers.** The XAI tool results in the game, such as SHAP values and feature importance percentages, are written to teach the concept and are not computed from a real model.
- **Scripted outcomes.** Many player choices lead to the same result, because each scene is designed to show one specific failure clearly.
- **Coverage gaps.** Some course topics appear only in eXplain text or not at all, including LIME, partial dependence and ICE plots, concept-based explanations such as TCAV, attention, and the monitoring, dataset bias and multi-agent material in Unit 6.
- **Self-reported evaluation.** The survey measures perceived familiarity, has no control group, and depends on who chooses to play.
- **Small convenience sample.** The first 11 completed surveys came from the creator's own social network, who may be inclined to rate the game kindly. Seven of the 11 gave the same rating to every unit after playing, so many players likely rated their overall impression rather than each unit separately. The four who rated units differently showed the same size of gain, but four players is too few to confirm it statistically.
- **Dropouts.** Three of the 14 players who started did not reach the post-game survey, and the game has no way to record where they stopped.
- **Accessibility.** The game has no sound and only partial keyboard and screen reader support, and the pixel art relies on color in places.
- **Simple privacy controls.** The results password is checked in the browser and on the Apps Script endpoint, which is enough to keep casual visitors out but is not real authentication. Players are asked only for a name and age, and no other personal data is collected.
- **Unit naming.** The course syllabus calls Unit 6 Human-AI Interaction, while the course notes title it Transparent AI. The game follows the notes.

## Misuse risks and stakeholders

**Stakeholders.** The primary stakeholders are non-expert AI users, who gain a working vocabulary for how AI fails and when to question it. Educators and trainers can use the game as an introduction before formal material. Organizations that deploy AI benefit when their employees recognize prompt injection, reward hacking and overconfident outputs. Survey participants are also stakeholders, because they share their name, age and ratings with the creator.

**Misuse risks.**
- **False confidence.** A player who finishes in 20 minutes may feel more expert than they are. Because the survey measures familiarity, a rise in scores can be misread as mastery, so the game and this README describe the results as perceived familiarity only.
- **Oversimplification.** The illustrative numbers and scripted outcomes make each concept clear, but they can also suggest that real XAI tools give clean, certain answers. The eXplain screens and the limitations above call out that real explanations can be unfaithful or misleading.
- **Attack ideas.** Level 4 shows how prompt injection, jailbreaks and data poisoning work at a high level. The examples are cartoon scenarios with no working technique, and every attack is paired with a defense, so the level teaches recognition rather than how to carry out an attack.
- **Anthropomorphism.** A friendly robot character can make AI feel more human and more trustworthy than it is. Level 6 counters this directly by ending with the lesson that the right choice can be keeping the AI out of the room.
- **Participant privacy.** The survey collects names and ages, and some players are under 18. Names are optional in practice, responses are stored in a private sheet, the results page is password protected, and published results are aggregate only. Future versions should drop names entirely and add a short consent notice.

## Future work

- Run a small real model under the laundry level so the saliency map, SHAP values and counterfactuals are actually computed.
- Add six short scenario questions, one per unit, before and after playing, so the evaluation measures understanding alongside self-reported familiarity. This was considered during the first night of data collection and held back so the instrument would stay the same for every player.
- Let player choices change outcomes, so players can explore different fixes and see their consequences.
- Add a version for younger players, sound, full keyboard support, and saved progress between sessions.
- Add levels for the topics listed under limitations.
- Remove the name field, add a consent notice, and record which level a player reached so dropouts can be studied.

## Repository contents

| Path | What it is |
|---|---|
| `index.html` | The complete game in one file: art, levels, surveys and results page |
| `analysis/analyze.py` | Reproduces every survey result in this README from the sheet's CSV export |
| `apps-script/Code.gs` | The Google Apps Script web app that stores survey responses in a Google Sheet |

## Running your own survey backend

1. Create a Google Sheet, open **Extensions → Apps Script**, and paste in `apps-script/Code.gs`.
2. Deploy it as a web app with **Execute as: Me** and **Who has access: Anyone**.
3. Copy the web app URL and set it as `ENDPOINT` near the top of the survey section in `index.html`.

## Credits and references

- **Inspiration:** AImelia was modeled after Amelia Bedelia, the famously literal housekeeper from the *Amelia Bedelia* books by Peggy Parish and, later, Herman Parish. AImelia's look and every scene in the game are original.
- **Course:** This video game was created using learning concepts introduced in XAI, AIPI 590.01 Fa26, taught by Dr. Brinnae Bent at Duke University, and draws on her workbook: Bent, B. (n.d.). *Explainable AI* [Online workbook]. Duke University. https://explainableaiworkbook.com. Licensed under CC BY-SA 4.0.
- **Duke University:** Thank you to Duke University and the AI for Product Innovation (AIPI) program at the Pratt School of Engineering.
- **Book Club:** Buolamwini, J. *Unmasking AI*. Christian, B. *The Alignment Problem*. Schaich Borg, J., Sinnott-Armstrong, W., and Conitzer, V. *Moral AI*.
- **Related work:** Long, D., and Magerko, B. (2020). What is AI literacy? Competencies and design considerations. *Proceedings of CHI 2020*. Ma, Q., et al. (2025). "GenAI defaults to bias!" Gamify AI literacy through reflections on prompts (ImaginAItion). arXiv:2509.13679. *Breakable Machine: A K-12 classroom game for transformative AI literacy through spoofing and eXplainable AI (XAI)* (2025). arXiv:2508.14201. *AI Odyssey: Designing and evaluating a board game for family-based AI literacy* (2025). *International Journal of Serious Games, 12*(4). https://doi.org/10.17083/dnza4k90
- **Learning theory:** Papert, S. (1980). *Mindstorms: Children, Computers, and Powerful Ideas*. Gee, J. P. (2003). *What Video Games Have to Teach Us About Learning and Literacy*.

## Use of AI

This game was built with the help of Claude (Anthropic). The creator set the concept, the character and the structure of every level, chose or reshaped each scenario Claude proposed, and played and revised each version. Claude wrote the code and pixel art and drafted the text, which the creator then directed and edited for accuracy and voice.
