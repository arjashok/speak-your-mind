# Presentation Analyzer [Speak Your Mind] #
>We can grade emotions, gesture-use, & textual content generated from a video of
>a speech and then generate pointers to improve on each >of these categories.

- Emotions of the Presenter are mirrored by the audience; therefore, gauging how 
the presenter is speaking (stress, anxiety, etc.) ⇒ Hume AI can do this as well
- Spoken Content needs to be parsed into something we can process textually ⇒ 
some sort of speech-to-text API for converting the spoken language into a speech
    
    - Google likely has some APIs for thisTextual Content can be analyzed 
    for correctness, delivery, ⇒ LLM from Grammarly or GPT or Claude for 
    understanding and grading the content of the speech for accuracy
- Together AI has an open LLM to use (w/ LLaMa), but we have to ensure 
that payment isn’t crazy
    - https://developer.grammarly.com/docs/writing-suggestions
  
- Body Language is an essential part of the speaker’s appearance on stage 
and therefore reception in the audience ⇒ analyzing hand gestures, 
posture, eye contact, etc. would be powerful to users
    - Lol no idea how to do this, should be CV libraries that can accomplish this but how tf
    - May have to be a part of next steps

- We can study the qualitative aspects that good presenters possess, 
creating heuristics for analyzing the metrics we gauge
    - Rank certain emotions as +/- based on the qualitative study
    - Qualify certain textual content [words, phrases, slang, etc.] as +/
    based on great speeches’ content
    - Classify body language/movements as +/- based on speed of movement, 
    position, etc.
    - Gauge speed, stutter, & clarity of speech and associate with +/- i
    mpact on speech quality

## Next Steps
- Audience Analysis: we could analyze audience emotion to gauge how they 
react to the speeches given (i.e. we can record the live audience in an 
actual speech; Ted Talks, etc. are good resources for this)

- Eventually, we can leverage this to predict how an audience would 
respond to a given speech, thereby providing a more thorough analysis of 
audience reception to the speech content, body language, and emotions of 
the presenter’s specific video

## Elevator Pitch
### Names
- Speak Your Mind
- SymPresent / PresentSym
- GhostWriter

### Use-Cases
- For those with learning disabilities, social anxiety, social disorders, 
etc. our product helps overcome these limitations through targeted 
practice
    - Not just any kind of practice, but practice that helps YOU get 
    better
    - Can be fine-tuned by the person, helping anyone get tips that 
    concentrate on their specific weaknesses
- Similarly, for anyone who’s afraid of speaking, this is a tool that 
    helps break down some of the stress of public speaking through 
    practice
    - Again, fine-tuned to the person so we can better suggest pointers, 
    etc.
    - It’s like a speech coach that knows everything about speaking

- For companies who want to analyze consumer responses to product 
roll-outs Apple, etc. launch products, they may want real-time analysis 
for the audience reactions and which products excite the people most 
interested in their product
- For audience analysis as a whole, we can eventually roll-out features 
for specific audiences (fan-bases, general audience, etc. can all be 
analyzed to create datasets based on their propensity for certain 
behaviors)
    - Again, can be used to see how audiences would react to product 
    announcements based on the speech, textual, and emotional content of 
    an advertisement

- For research purposes, it’ll be useful to have a way to collect data 
about audiences and behavior on a large scale when influenced by a single 
(or multiple) speaker(s)
    - Can conduct case studies on the impact of certain emotions and 
    gestures on audience retention, etc. ⇒ political science, sociology 
    research
    - Can use this dataset to avoid heuristics when grading the users, 
    instead relying on real-world data

    - We can justify the user of heuristics for now since we our audience 
    members ourselves and we conducted a qualitative study, but in the 
    future quantifiable proof would be preferred

## Plan
### Pipeline
Web App


Backend
Frontend

