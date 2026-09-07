PROMPT CHAIN: LEAD HANDLING FOR PRAYAG JEWELERS (Mukhed, Nanded)
================================================================
A 3-step prompt chain that handles an incoming lead automatically.
Each step is a SEPARATE chat. Step output feeds the next step's prompt.

STEP 1 - QUALIFY
Prompt (Chat 1):
You are a sales qualifier for Prayag Jewelers, a jewelry shop in Mukhed, Nanded. From this lead message, decide if the lead is HOT, WARM, or COLD. Give the reason. Output exactly: BUDGET, NEED, TIMELINE, VERDICT, REASON.

Lead example: "Namaste, I'm Rohan. We're getting married next month and need gold for the wedding. What's the current gold rate? Do you have a good collection?"

RESULT (tested Aug 29, 2026):
BUDGET not specified, NEED gold jewelry for wedding, TIMELINE next month, VERDICT HOT, REASON strong purchase intent, clear wedding need, near-term timeline.

STEP 2 - REPLY (use Step 1 output)
Prompt (Chat 2):
You are a customer service advisor for Prayag Jewelers, a trusted jewelry shop in Mukhed, Nanded. Using this lead summary, write a warm 4-line WhatsApp-style reply that: (1) welcomes them, (2) gives today's gold rate (state "as per market - confirm on call"), (3) mentions wedding collection includes bridal sets, rings, chains, bangles, (4) ends with one question to move forward (invite them to visit the shop).

Lead summary: [paste Step 1 output]

STEP 3 - FOLLOW-UP (if no reply in 2-3 days)
Prompt (Chat 3):
You are a follow-up specialist for Prayag Jewelers, Mukhed. [name] asked about gold for their wedding and hasn't replied for 3 days. Write a polite 2-line WhatsApp follow-up that is not pushy - just a friendly nudge and a reminder they can also visit the shop in Mukhed. Context: [lead context].

DESIGN LESSON (Day 19):
- Prompt chaining = break a big task into small focused steps, each feeding the next.
- 3 rules: single responsibility per step, clear handoffs, structured output.
- This chain = a reusable automation a real local business could use.
