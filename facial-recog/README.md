# Facial Recognition
For use in audience versus speaker testing, we want to segement frames 
that we analyze into just the faces we can capture in decent quality.

NOTE: by design, we are avoiding the use of:
    - Occluded faces ==> may end up misleading the HUME models, thus 
    giving us unreliable or misleading data
    - Dimly-lit faces ==> similarly, faces without sufficient light 
    shining on them may be harder for HUME to process, therefore 
    motivating us to remove them

The most effective way to accomplish these things? Don't finetune the 
model for these edge cases. If a basic transformer driver facial 
recognition model can't derive enough information from a photo, then 
chances are any data we could've gotten with a more fine-tuned model 
would anyways be misleading.

In terms of sampling, as long as the sample is random (i.e. the light in 
the audience isn't scattered too much and the pre-trained model is fair 
for **all skin-tones**), we can assume that just gauaging a few audience 
members at a time will be representative of the entire population of 
audience members.
