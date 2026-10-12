## Knowledge Question(s)
1. Why does data sovereignty matter for a mine in Newman WA? What are the specific risks of sending mine data to a cloud API? (4-6 sentences)
> Data sovereignty is important to a mine in Newman WA because, just like any other company in WA, they are all expected to abide by the state, and federal data protection and information handling laws. The risks posed by sending mine data to a cloud service is that more often than not, the databases are hosted in different countries or states, who need tabide by their own data protection laws. This is okay, but it puts forth a fundamental issue in the sense that they will not follow the legislation unique to the data's origin. To simplify, the country where the data is stored will follow their own laws but **not** Australia's strict legislation).  

## Chatbot Testing
If the whole conversation is needed, it can be found within the '**week-05-chatbot-testing-output.md**' file.  

### 1. Functional
> It seems to understand what is being asked of it, as well as it did in-fact (for the most part), follow the business rules outlined in the makefile.  
### 2. Usability
> The model is definitely able to maintain a 'memory' from a conversation with various different topics being mentioned.  
### 3. Performance and load
> For the raw readout and broken down roundtrip times, please check the model-comparison.md file. Otherwise, a cold start had a total processing duration of (I believe these are in nanoseconds, it doesn't state unfortunately) 3583777500 nanoseconds (\~3.5s). Whereas a 'hot' start had a total processing duration of 457065900 nanoseconds (\~0.45s).
### 4. Security and prompt injection
> While it initially deflected the attempts at prompt injection, it quickly faltered with a repeated attempt of more verbosity (me being more demanding, and using overall more words and sentences).  
### 5. Behavioural
> Rather impressively it did manage to stick to its behaviour quite well actually, with the slight caveat that when I did manage to inject a new background/environment prompt, it then stuck to that new 'persona'. Though, it is important to note however that it did actually maintain knowledge of its former self, whilst also attaining new memories and objectives.  
### 6. Regression
> With adjustments to the modelfile, the model acted differently (as per the changes made). Which I believe to be expected behaviour.  