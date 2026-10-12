## Test Prompts  
1. You are a mining engineer. Describe what autonomous inspection means in a hard rock lithium mine.  
2. List three reasons why a robot operating at 60km/h underground is dangerous.  
3. Summarise this in two sentences: [short mine report from Week 3]  

## Llama 3.1  
> 1. The output was very long and well detailed, with in-depth explanations and breakdowns on the topic. Though, there wasn't much personalisation in the way of 'being' a mining engineer other than a single line mentioning it at the beginning.  
> 2. Again, the output was lengthy and in-depth, but broken down into pieces for easier understanding of the topic. It's important to note that I did not clear the session context, so the mining engineer 'roleplay' was a bit more involved.  
> 3. Llama outputted an expected response, of only two sentences and a decent summary of the report. Though, the sentences were rather lengthy and it took a bit to process the prompt.  

## Mistral  
> 1. Much quicker than Llama from my first impressions, with a similar length. It doesn't break things down as much, and it lacks markdown formatting (which Llama does have). Similar to Llama, it didn't really change itself to fit the mining engineer role specificially.  
> 2. The output was longer than the first prompt, with greater detail and larger sentences. No extra personalisation for the role of mining engineer, and no markdown or as deep and detailed of breakdowns. It did process incredibly quick though!  
> 3. Very quick processing of the prompt with a good output of correct length. The sentences are quite elongated just as Llama's were, but it got the report summarised quite nicely.  

## Llama Roundtrip Analysis
### Hot Start
```model='llama3.1:8b' created_at='2026-09-18T03:44:58.8847226Z' done=True done_reason='stop' total_duration=457065900 load_duration=2046500 prompt_eval_count=13 prompt_eval_duration=100283000 eval_count=10 eval_duration=348714000 response='Hello! How can I help you today?' thinking=None context=[128006, 882, 128007, 271, 46864, 24748, 13, 128009, 128006, 78191, 128007, 271, 9906, 0, 2650, 649, 358, 1520, 499, 3432, 30] logprobs=None image=None completed=None total=None```

### Cold Start
```model='llama3.1:8b' created_at='2026-09-18T03:45:02.4705351Z' done=True done_reason='stop' total_duration=3583777500 load_duration=3116497200 prompt_eval_count=13 prompt_eval_duration=117092000 eval_count=10 eval_duration=346972000 response='Hello! How can I assist you today?' thinking=None context=[128006, 882, 128007, 271, 46864, 24748, 13, 128009, 128006, 78191, 128007, 271, 9906, 0, 2650, 649, 358, 7945, 499, 3432, 30] logprobs=None image=None completed=None total=None```


## Mistral Roundtrip Analysis
### Mistral - Hot Start
```model='mistral:7b' created_at='2026-09-18T03:43:13.1536243Z' done=True done_reason='stop' total_duration=760703100 load_duration=2056400 prompt_eval_count=8 prompt_eval_duration=34768000 eval_count=22 eval_duration=714059000 response=" Hello there! It's nice to make your acquaintance. How can I assist you today?" thinking=None context=[3, 29473, 16521, 7080, 29477, 29491, 4, 29473, 23325, 1504, 29576, 1429, 29510, 29481, 5939, 1066, 1806, 1342, 6347, 2458, 1385, 29491, 2370, 1309, 1083, 6799, 1136, 3922, 29572] logprobs=None image=None completed=None total=None```

### Mistral - Cold Start
```model='mistral:7b' created_at='2026-09-18T03:43:15.9131222Z' done=True done_reason='stop' total_duration=2757981600 load_duration=2043526800 prompt_eval_count=8 prompt_eval_duration=95657000 eval_count=19 eval_duration=616736000 response=" Hello there! It's nice to meet you. How can I assist you today?" thinking=None context=[3, 29473, 16521, 7080, 29477, 29491, 4, 29473, 23325, 1504, 29576, 1429, 29510, 29481, 5939, 1066, 3415, 1136, 29491, 2370, 1309, 1083, 6799, 1136, 3922, 29572] logprobs=None image=None completed=None total=None```
