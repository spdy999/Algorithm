
```dataview
TABLE Date, Difficulty, Techniques, Note, Sites, Techniques, Walkthrough, Companies
FROM -"Obsidian Templates"
WHERE project="Leetcode" and progress=true
SORT progress desc, date desc
```


```dataview
TABLE Progress, Date, Difficulty, Techniques, Note, Sites, Techniques, Walkthrough
FROM -"Obsidian Templates"
WHERE project= "Leetcode" and progress="InCompleted"
SORT progress desc, date desc
```




