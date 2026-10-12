import spacy
import tiktoken
from collections import Counter

# spaCy pipeline from Week 4 — load with your custom entity ruler
nlp = spacy.load("en_core_web_sm")
# Add your EntityRuler patterns here (from spacy-pipeline.py in Week 4)

gus_email = """From: gus.hargreaves@ochreridge.com.au
To: AI Consultancy Team
Subject: ROBOT REQUIREMENTS — OCHRE RIDGE LITHIUM MINE — URGENT AND CONFIDENTIAL

Team,

Thank you for joining the project. I'll keep this brief.

I want every dangerous job at Ochre Ridge done by a robot within five years. Not most jobs. Every job. I have the budget. I need the vision.

Here is what I am thinking. First: autonomous ore smell detection. I have been told AI can detect patterns in data that humans cannot. Lithium ore has a specific chemical signature. I want a robot that can smell its way to the highest-grade deposits and redirect the drilling operation in real time. If dogs can do it, a robot certainly can.

Second: laser-guided blasting systems. The robots set the charges, target with lasers, and detonate remotely. No human in the blast zone. Ever. I want this operational within eighteen months.

Third: high-speed inspection robots. The tunnels are 4.2 metres wide. A robot travelling at 60km/h could cover the full shaft network in under two hours. I want a complete inspection report generated automatically before each shift.

Fourth: a robot dog army. I have seen the Unitree Go2. I want twenty of them operating autonomously underground. They report to no one except the AI system. The AI system reports to me.

Fifth: predictive ore grade AI. Feed in all the geological survey data we have — forty years of it — and have the AI tell us where to drill next. I want 95% accuracy. I understand this is technically possible because I read an article about it.

Sixth and finally: the robots must be able to communicate with each other in a language humans cannot intercept. I want a proprietary AI communications protocol. This is non-negotiable for security reasons.

Budget is not a constraint. Timeline is. I want a progress report in seven days.

GUS HARGREAVES
Owner and Executive Chairman, Ochre Ridge Resources Pty Ltd"""

doc = nlp(gus_email)

# Token count with tiktoken
enc = tiktoken.get_encoding("cl100k_base")
token_ids = enc.encode(gus_email)
print(f"tiktoken count: {len(token_ids)} tokens")

# spaCy: entities
print("\n--- Entities ---")
for ent in doc.ents:
    print(f"  {ent.text:35} {ent.label_}")

# Content word frequency — what does Gus talk about most?
content_tokens = [
    token.lemma_.lower()
    for token in doc
    if not token.is_stop and not token.is_punct and not token.is_space
    and token.pos_ in ("NOUN", "VERB", "PROPN", "NUM")
]
print("\n--- Most frequent content words ---")
for word, count in Counter(content_tokens).most_common(15):
    print(f"  {word:20} {count}")