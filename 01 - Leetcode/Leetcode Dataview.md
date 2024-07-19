---
Updated: 2024-07-19
---

```dataview
TABLE Created, Updated, Difficulty, Techniques, Note, TODO, Sites, Walkthrough, Companies
FROM -"Obsidian Templates"
WHERE project="Leetcode" and progress=true
SORT updated desc, created desc
```


```dataview
TABLE Progress, TODO, Created, Updated, Difficulty, Techniques, Note, Sites, Techniques, Walkthrough
FROM -"99 - Obsidian Templates"
WHERE project="Leetcode" and progress!=true
SORT updated desc 
```
