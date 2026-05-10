---
type: meta
title: "Wiki Dashboard"
created: 2026-05-10
updated: 2026-05-10
tags:
  - meta
  - dashboard
status: active
---

# Wiki Dashboard

## Recent Activity

```dataview
TABLE type, status, updated FROM "wiki" SORT updated DESC LIMIT 15
```

## Seed Pages

```dataview
LIST FROM "wiki" WHERE status = "seed" SORT updated ASC
```

## Active Decisions

```dataview
LIST FROM "wiki/decisions" WHERE status = "active" SORT updated DESC
```

## Model Pages

```dataview
LIST FROM "wiki" WHERE contains(tags, "model") SORT updated DESC
```
