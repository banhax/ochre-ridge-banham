OCHRE RIDGE LITHIUM MINE  
AI and Robotics Scoping Report  
Prepared for: Sandra Chen, CTO, Ochre Ridge Resources  
Prepared by: Xavier Banham, AI Consultancy  
Date: 9/10/2026  

Executive Summary  

### 1. Context and Methodology  

Gus requested a few things, with a great deal of them being superfluous and/or unreasonable.
Specifically, everything he requested was as follows:
* Autonomous ore smelling robots, 
  * e.g. a robot that can 'sniff' to high-grade ore veins

* Laser-guided rock blasting, he wanted the dogs to be able to
  * set charges,
  * target them with lasers,
  * and then detonate them remotely
  
* High-speed inspection via robots
  * e.g. dogs sprinting around at **60 km/h** (?!)
  * and full site inspection before every shift

* A robot dog army, yes, he requested
  * **Twenty** Unitree Go2 robot dogs
  * They would only answer to the AI systems,
  * and ignore everything else
  
* Predictive ore grade AI, which means
  * utilising the 40 years of geological survey data,
  * and feed it to an AI to predict where the best places to mine would be
  
* And finally, the robots should talk to each other
  * in a language that humans can't intercept
  * done via a proprietary AI comms protocol

### 1.1 Technical Definitions
**AI** refers to current artifical intelligence technology, which is frequently used as a blanket term for various different sub-technologies. Such as ML, or machine-learning (computers learning things via reinforcement learning and other techniques), and/or deep-learning, which is the gold-standard of AI at this current moment, due to its underlying neural networks designed to mimic how the human brain works.

Examples in the context of Ochre Ridge could include...
* AI could be used to decipher commands spoken in natural language (english), and translate them into something a machine would understand.
* Machine-learning could be used to detect faults in machinery before they occur, allowing for predictive maintenance
* and lastly, Deep-learning could be utilised to mimic Gus (as he requested) to command these new planned AI systems

### 2. Feasible Applications

1. Robot dog army
   * Having a large quantity of robot dogs each doing their own tasks could streamline a lot of the more monotonous mine tasks
   * It's feasible as the main hurdle to overcome is actually purchasing the dogs, which clearly is not an issue. Another limitation is commanding the dogs, which is an in-progress development project.
   * There will always be great risk with implementing these AI dogs, especially cyber-security but also safety for personnel working on the mine. The recommended priority is **low**.
2. Robots communicating in a language undecipherable by humans
   * This could yield a great deal of cyber-security bonuses as the data would be unable to be intercepted and abused by a bad actor
   * It's feasible as AI models already utilise secret languages to communicate with each other, as observed by a lot of research
   * There's a fundamental risk of having a completely closed-loop AI system; if something goes wrong, how would we fix it, or even know? Recommended priority: **low**.
3. Autonomous ore-sniffing robots
   * This would be used to direct the mining operations to locations with higher yields of ore, increasing profits and decreasing wasted materials
   * It is feasible, as long as we have a consistent way to detect ore via 'smell' (or more likely, chemical signatures?)
   * There actually isn't a great amount of risk involved with this, due to it being a non-intrusive addition. Recommended priority: **high**.

### 3. Proposals Assessed as Not Currently Feasible

1. Laser-guided rock blasting
   * The logistics of strapping explosives to dogs alone is ludicrous, but laser-guided targetting in an environment as volatile and full of reflective surfaces and gases is a terrible idea.
   * For this idea to be remotely feasible, we would need a way to safely provide and arm explosives for the robot dogs, but also a laser targeting system that the dogs do not currently possess. The timeframe for implementing something like this would be months, if we were to build a system from scratch and source the necessary components.
2. Predictive ore-grade AI
   * Whilst the idea is smart, the earth being organic and ore deposits not following a pre-defined pattern, an AI based purely on predicting the location of ore would provide very minimal success
   * This can't be feasible due to things out of our control, there isn't a timeframe to implement this.
3. High-speed inspection robots
   * The current systems that the robot dogs utilise for object avoidance are no-where near quick and precise enough to allow for the dogs to sprint down an ever-changing, and dangerous mine shaft at 60 km/h; without the exceptional risk of damage to themselves or other entities.
   * This could be feasible, if we equipped the dogs with another option for obstacle avoidance that could keep up with the demands required of them. The expected timeframe for implementation could be anywhere from weeks to months.

### 4. Recommended Implementation Sequence
From most important to least important to implement...

1. Autonomous ore-sniffing robots
   * You would need specialised sensors, and some system to process visual data (OpenCV)
2. Robot dog army
   * You would have to purchase the twenty robot dogs (Ollama + Llama 3.1 8B for a local model, which would help to process data from the dogs)
3. Robot's own language
   * This requires very little to get working, simply allow models to communicate and specify your requirements (Ollama + Llama 3.1 8B)

### 5. Risk Assessment

This whole program is extremely optimistic and for lack of a better word, childish. The gained risks would be astronomical when you consider the heightened chance of cyber attacks on the mine, the risks of having fully autonomous AI robots controlling *everything* (without human supervision or interaction), and finally the massive amount of moving parts that all need to fit together perfectly and fall into place, which is incredibly unreasonable.

Below are three of Australia's AI ethics principles, which this project doesn't abide by...
1. Fairness - Replacing all humans with AI is not fair and is discriminatory for human workers and their rights
2. Contestability - There is no due process to speak of in regards to issues or complaints regarding these proposed AI systems, which is not only ethically wrong, but also incredibly unsafe
3. Accountability - These AI robots are being expected to only listen to a central AI system; with **SPECIFIC MENTION OF DISREGARDING HUMAN INTERVENTION**

### 6. Conclusion and Next Steps

In conclusion, a lot of what Gus has requested is either impossible, or incredibly unsafe or unrealistic. Despite this however, there are some interesting and smart ideas that could be implemented with a lot of benefit to Ochre Ridge. I think it would a good idea to authorise the ore-sniffing to get some R&D time, but the other options are your discretion.  

### Appendix A - Gus Interview Transcript
The file is within the 'at1-gus-report' folder, under the name of 'gus-interview-transcript.md'

### Appendix B - Token Analysis Output
The file is within the 'at1-gus-report' folder, under the name of 'gus-token-analysis-output.txt'

### Appendix C - NLP Concepts Explained
To explain some of the concepts mentioned, and additional important concepts...
1. **Tokenisation** is the process of breaking down strings of characters into small and easy-to-compute units called tokens, allowing for easier processing by AI models.
2. **Stop word filtering and Lemmatisation** are each techniques very frequently using in NLP to 'cleanse' text and make it standardised before it is then fed to an AI model.
3. **Dependency Parsing** is a technique used in NLP to decipher meaning and analyse the usage and structure of grammar within a piece of text.
4. **Named Entity Recognition** acts to spot and classify objects from an unstructured piece of text, before assigning them different categories based upon a variety of techniques.
5. **The six levels of language analysis** refers to a framework devised to break down language as a concept into six neat and defined levels. They are as follows...
   1. Phonology
   2. Syntax
   3. Semantics
   4. Conceptual
   5. Belief
   6. And paralinguistic level

### Appendix D - Chatbot Testing Summary
The file is within the 'portfolio' folder, under the name of 'week-05-chatbot-testing-output.md', with more detail being included in the 'week-05-notes.md' file