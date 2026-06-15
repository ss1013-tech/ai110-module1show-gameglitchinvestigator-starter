# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The interface for normal difficulty show allowed attempts as 8, show attempts left as 7, but when I clicked Developer Debug info, it shows attempts: 1 when I didn't attempt to guess anything.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1.The hints were backwards, I first guess 2, and then guess 20,50,80 then even I guess 100, it is still say go higher which is already out of the limit.
  2.when I navigate to hard mode, it said on the left bar, range 1 to 50 but on the browser, it still said, guess a number between 1 to 100. And I can guess number beyond 50, so it seems the range and diffculty are not bound.
  3.score are not have logic, although all my guesses are wrong, my score sometimes is -5, and sometime is -10, it should just be zero or keep reducing because I am not reach the correct one.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input       | Expected Behavior | Actual Behavior | Console Output / Error |
|-------------|-------------------|-----------------|------------------------|
| guess of 30 | Hints:Go Higher!  | Hints: Go Lower!| None                   |
| guess of 101| Hints:Go Lower! because input shall only between 1 to 100 | Hints: Go Higher!| None|
| guess of 80 in Hard mode| Number out of range,should be 1 to 50, Hints: Go Lower| Hints: Go Higher! because the secret for some reason is 81 which is odd because the range should be 1 to 50| None

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
