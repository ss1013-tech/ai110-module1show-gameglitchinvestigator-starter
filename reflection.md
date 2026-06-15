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
Copilot

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Bug: When I guess 30, which is lower than the actual secret: 42, hints said Go Lower, but hints should said go Higher. 

AI suggested:
  Look at this code in check_guess():
  if guess > secret:
      return "Too High", "📈 Go HIGHER!"
  else:
      return "Too Low", "📉 Go LOWER!"
  The problem: When your guess (30) is less than the secret (42), the code goes to the else branch and says "Go   LOWER!" — but that's backwards! If your guess is too low, you should go HIGHER.
  Why it's wrong:
  If guess > secret (your number is too big) → should say "Go LOWER"
  If guess < secret (your number is too small) → should say "Go HIGHER"
  The fix: Swap the messages:
  if guess > secret:
      return "Too High", "📈 Go LOWER!"  # ← flip this
  else:
      return "Too Low", "📉 Go HIGHER!"   # ← and this

How I verified: I agree the logic, ask AI to generate pytest, and then run it in live as well


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Bug: score logic is misleading and varies between -10, -5 and 0

AI suggest:
The score logic in logic_utils.py is still inconsistent for wrong guesses:
Too Low always subtracts 5.
Too High sometimes adds 5 on even attempts, then subtracts 5 on odd attempts.
That means a wrong guess can increase score, which feels odd for this game and matches what you’re noticing. If you want, I can patch it so wrong guesses are always penalized consistently (for example, always -5 and never below 0).

How I verified: I don't agree with AI suggestion, and I describe my suggestion to AI for it to evaluate, AI agree with me that my suggestion make more sense - start with 100, reduce 10 if incorrect and return score when correct.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? 
use pytest and test it live with streamlit

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I test negative number when UI running and at first it show too high as hints, so I think it should because the range didn't get bound, so I work with AI assistent to link the range and check the input before guess.


- Did AI help you design or understand any tests? How?
Yes, I tell AI to help me generate test for guess negative number, decimal, and extream larget number, and AI produce plan for the edge cases first and I reviewed it, ask AI to modify and I review again before it implement.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit is different from the traditional web app. Instead of keeping the program running continuously, it reruns the entire script from top to bottom whenever the user interacts with the page.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Not only test using unit pytest, but also test in real application.

- What is one thing you would do differently next time you work with AI on a coding task?
Understand what AI said first, try to come up with some edge case, plan ahead when it solid before implement.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
I think AI able to generated solid code but it may not have clear logic that easy for human understand, so as engineer, we should provide clear logic that we understand and then provide to AI for it to evaluate and implement.
