# Japanese-English-Car-Terms
Created a simple app using streamlit to search for car terms in Japanese and in English and show its translation to the other language. 

## Why is it so slow? 
Well for one, I am not a seasoned programmer yet. For two, I am using streamlit's option dropdown as a type of autofill, which it is not at all desinged for. With 700 items, and with the dataframe needing to be reloaded and looped through, it takes some time on weaker CPUs.  

## Optimization? 
Yes. Currently it is reading from an excel which has useless information that I need to remove in code. In the next update it will just be in a singluar database file with only the relavant information. This should speed it up somewhat. Also streamlit has a cache function which should also help.
