# Day 3 — AI Verification Chain Lab

## Objective

The objective of this lab was to verify AI-generated placement statistics using a 3-step verification chain:

1. Gemini AI generated the claims
2. Perplexity AI provided cited references
3. Primary sources were manually checked for validation

This lab demonstrated that AI-generated information may sound authoritative but still require human verification.

---

# Verification Matrix

| # | Claim | AI Source | Perplexity Check | Primary Source URL | Verdict |
|---|---|---|---|---|---|
| 1 | The average B.Tech placement package in Indian engineering colleges in 2025 was ₹6.2 LPA | Gemini AI | Perplexity provided NASSCOM and AICTE references | https://nasscom.in | PARTIAL |
| 2 | 78% of Tier-1 college students received at least one placement offer in 2025 | Gemini AI | AICTE and India Skills Report references returned | https://www.aicte-india.org | FALSE |
| 3 | TCS hired approximately 40,000 freshers in 2025 | Gemini AI | Perplexity cited TCS Annual Report | https://www.tcs.com | VERIFIED |
| 4 | IT services accounted for 56% of engineering placements in India in 2025 | Gemini AI | Perplexity returned NASSCOM links | https://nasscom.in | NO PRIMARY SOURCE FOUND |
| 5 | Median IIT placement package in 2025 was ₹18.5 LPA | Gemini AI | India Skills Report cited | https://wheebox.com/india-skills-report.htm | PARTIAL |

---

# Reflection

The claim that looked most authoritative but was actually weakest was:

> “78% of Tier-1 college students received at least one placement offer in 2025 according to AICTE.”

Gemini presented the statistic confidently, and Perplexity initially appeared to support it with citations. However, after opening the primary AICTE source, the exact percentage and year combination could not be found. The report discussed placement trends generally, but the specific statistic was either misquoted or unsupported.

This demonstrated an important lesson:

> AI confidence does not equal factual correctness.

The verification step must always be performed by humans, even when AI systems provide citations and professional-looking responses.

---

# Key Learnings

- AI models can hallucinate statistics
- Citations alone do not guarantee correctness
- Primary source verification is essential
- Human validation is critical in AI workflows
- Verification is a skill, not a button

---

# Conclusion

In this lab, I learned how to validate AI-generated information using a verification chain involving Gemini AI, Perplexity AI, and primary-source analysis. The exercise highlighted the importance of critical thinking and responsible AI usage in research and decision-making workflows.