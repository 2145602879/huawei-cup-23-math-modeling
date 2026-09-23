# AI disclosure checklist

Create an `ai_use_log.json` (or equivalent table) for every AI-assisted contribution:

| field | required content |
|---|---|
| tool | product name, model/version, developer/company |
| release_date | version/model release date, if available |
| date_used | when the tool was used |
| purpose | information, ideation, modeling, data analysis, writing, code, or other |
| input_summary | concise description or stored prompt reference; do not leak secrets |
| output_used | what was retained, quoted, transformed, or rejected |
| verification | derivation, source check, independent recomputation, tests |
| postprocessing | team edits, parameter choices, filtering, and human decisions |
| paper_location | where the disclosure/citation appears |

Required handling:

- Rewrite prose in the team’s own language.
- Do not cite an AI answer as the source of a theorem, formula, dataset, or factual claim when a reliable primary source can be found.
- For unverifiable AI-suggested models/formulas, either reject them or label them exactly as AI-assisted and document the risk; never omit derivation or source checking.
- For AI-assisted data analysis, place a note adjacent to the result.
- For AI-assisted code, put the required metadata comment at the beginning of the program.
- If the problem asks for prompts or strategy, include the input and post-processing record with frameworks, open-source components, route, assumptions, parameters, and hyperparameters.

Suggested code comment (adapt metadata to the actual tool):

```text
# 本程序及代码是在人工智能工具辅助下完成的；工具：<名称>，版本/型号：<版本>，开发机构/公司：<机构>，版本发布日期：<日期>。
```

