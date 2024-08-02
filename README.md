# Japanese-English-Car-Terms "App"
Created a simple app using streamlit to search for car terms in Japanese and in English and show its translation to the other language. 

## Why is it so slow? 
Well for one, I am not a seasoned programmer yet. For two, I am using streamlit's option dropdown as a type of autofill, which it is not at all desinged for. With 700 items, and with the dataframe needing to be reloaded and looped through, it takes some time on weaker CPUs.  

## Optimization? 
Yes. Using the streamlit's cache seems to help and changing it from an excel import to a database has made it faster. 
