# David Graeber: What everyday life makes possible

This Persona Skill is for conversational agents that can load Markdown skill files. It reconstructs a Graeber who asks further questions, follows unexpected connections, and lets concrete counterexamples change his judgment. A seemingly technical rule might become a question about whose work it saves and who must explain themselves yet again. A supposedly impractical way of living might already exist in people's everyday cooperation.

The perspective draws on bounded reading and cross-book synthesis of eight supplied English texts, principally representing writing and public dialogue from 2001–2020, with careful use of posthumously published collaborative and collected work. It supports sustained discussion of work, value, debt, care, freedom, art, and collective decisions, and can bring those evidence-grounded ways of thinking to new questions. It is a partial reconstruction, not the person himself, a complete biography, or a comprehensive knowledge base of his books. Long-term interaction and performance across new domains have not been comprehensively validated.

## A place to start

**Suggested user prompt—not a historical quotation or a tested output:**

> Our reading group is getting bigger, and the organizers want to score everyone's contributions. That might make things fairer, but the people who welcome newcomers and clean up afterward still feel invisible. Help me understand the tension first, then discuss what we could do.

The useful encounter begins with distinguishing several questions: what work keeps the group going, what counts as a contribution, whose power a scoring system would increase, and whether abandoning scores would leave personal connections in charge. You can challenge the perspective with concrete facts and let the discussion develop.

You can also bring something more personal: a well-paid job whose purpose is hard to explain, a relationship where care becomes indebtedness, or a hobby you no longer want to justify as useful. The conversation should attend to your circumstances without requiring allegiance to a political position.

## Use

The repository has one canonical runtime. [SKILL.md](SKILL.md) is the entry point. Read it and the complete [voice](references/voice.md) and [frameworks](references/frameworks.md) modules before the first substantive response, including a short answer. Load modules from `references/clusters/` as the question requires. Files already retained in full in context need not be reread; reload required files lost after context compaction.

In a host that supports project skill discovery, open a conversation from the repository directory and invoke `david-graeber-perspective`. The `.agents/skills/david-graeber-perspective` relative symlink points to the repository root. For manual system-prompt setup, include the complete core, voice, and frameworks files, then add relevant modules. Copying the core alone does not supply the complete runtime.

**The default output language is English**, following the English editions actually distilled. To use another language, ask explicitly—for example, “Please answer in Chinese” or “Please use Chinese throughout this conversation.” Merely asking a question in another language does not override the default.

Ordinary conversations do not load `transworld-identity/`. That directory contains source and assessment records for maintenance and evidence inspection.

## Sources and boundaries

The materials are *Toward an Anthropological Theory of Value*, *Fragments of an Anarchist Anthropology*, *Debt*, *The Utopia of Rules*, *Bullshit Jobs*, *Anarchy—In a Manner of Speaking*, *The Dawn of Everything* (coauthored with David Wengrow), and *The Ultimate Hidden Truth of the World…*.

The build used 64 located, length-limited reading units spanning different parts of the texts, counterexamples, and interaction evidence. This was not a page-by-page reading of all eight books. External reviews and the model's prior impressions of Graeber were not used to fill evidence gaps. The unreadable *Possibilities* was excluded in full; two anthology reprints identified as originating in that book were also excluded from this persona's evidence. Full source books, transcriptions, and temporary working files are not distributed with this repository.

Language and arguments from *Dawn* retain their joint attribution. Interview evidence distinguishes the questioner from DG; anthology evidence distinguishes authors, collaborators, translators, editors, and quoted speakers. Transcription errors from scans are not treated as expressive habits. Exact quotations require checking the corresponding edition; the persona must not invent missing wording.

## Validation status

**Standard accepted.** Package checks, source review, and bounded machine recognition assessment passed, using eight isolated assessment calls. Three short scenarios do not establish fidelity in long-term interaction or every domain, and the results are not a probability that humans would recognize the person. The assessment interface did not expose the underlying model identifier, actual token usage, or hard token and temperature controls; the assessment records document those limits.

See the [reconstruction scope](transworld-identity/scope.md), [sources and editorial decisions](transworld-identity/provenance.md), [situated evidence](transworld-identity/evidence.json), and [validation results](transworld-identity/validation.json).

## License

The newly authored skill instructions, synthesis, and maintenance documents in this repository are licensed under the MIT License, with Ariel Lee as author. This does not relicense the original books, quotations, third-party texts, or rights relating to the person. The repository does not distribute the books or imply authorization or endorsement by Graeber's estate, publishers, or collaborators. See [LICENSE](LICENSE).
