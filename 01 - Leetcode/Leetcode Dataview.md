
```dataview
TABLE Created, Updated, Difficulty, Techniques, Note, Sites, Techniques, Walkthrough, Companies
FROM -"Obsidian Templates"
WHERE project="Leetcode" and progress=true
SORT modified desc
```


```dataview
TABLE Progress, Date, Difficulty, Techniques, Note, Sites, Techniques, Walkthrough
FROM -"Obsidian Templates"
WHERE project="Leetcode" and progress!="Completed" and progress!=true
SORT progress desc, date desc
```




