from __future__ import annotations

from collections import Counter
import re
from typing import Dict, List

STOPWORDS = {
    "the", "and", "or", "to", "of", "in", "for", "with", "a", "an", "on", "as", "at", "by", "is", "are", "be",
    "this", "that", "we", "you", "your", "our", "it", "from", "will", "have", "has", "had", "must", "required",
    "requirements", "role", "job", "description", "resume", "cv", "candidate", "experience", "skills", "skill",
    "years", "year", "work", "ability",
}

SKILL_PATTERNS = [
    ("python", re.compile(r"\bpython\b", re.I)),
    ("javascript", re.compile(r"\bjavascript\b|\bjs\b", re.I)),
    ("typescript", re.compile(r"\btypescript\b", re.I)),
    ("react", re.compile(r"\breact\b", re.I)),
    ("node.js", re.compile(r"\bnode(?:\.js)?\b", re.I)),
    ("django", re.compile(r"\bdjango\b", re.I)),
    ("flask", re.compile(r"\bflask\b", re.I)),
    ("sql", re.compile(r"\bsql\b|postgres|mysql|sqlite", re.I)),
    ("aws", re.compile(r"\baws\b|amazon web services", re.I)),
    ("docker", re.compile(r"\bdocker\b", re.I)),
    ("kubernetes", re.compile(r"\bkubernetes\b|\bk8s\b", re.I)),
    ("git", re.compile(r"\bgit\b|github|gitlab", re.I)),
    ("testing", re.compile(r"\btesting\b|pytest|jest|unit test|integration test", re.I)),
    ("api", re.compile(r"\bapi\b|rest|graphql", re.I)),
    ("communication", re.compile(r"communication|stakeholder|collaboration|cross-functional", re.I)),
    ("leadership", re.compile(r"leadership|mentor|mentoring|manage|management", re.I)),
    ("agile", re.compile(r"\bagile\b|scrum|kanban", re.I)),
]


def _normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9+.#/\-\s]", " ", text.lower())


def _tokens(text: str) -> List[str]:
    return [t for t in re.findall(r"[a-z0-9+.#/-]+", _normalize(text)) if t not in STOPWORDS and len(t) > 1]


def _extract_skills(text: str) -> List[str]:
    found = []
    for skill, pattern in SKILL_PATTERNS:
        if pattern.search(text):
            found.append(skill)
    return found


def score_resume_against_jd(resume_text: str, jd_text: str) -> Dict[str, object]:
    """Score how well a resume matches a job description using simple keyword overlap.

    Returns a dict with a 0-100 score, brief reasoning, and a list of likely missing skills.
    """
    resume_norm = _normalize(resume_text)
    jd_norm = _normalize(jd_text)

    jd_skills = _extract_skills(jd_norm)
    resume_skills = _extract_skills(resume_norm)

    jd_tokens = Counter(_tokens(jd_norm))
    resume_tokens = Counter(_tokens(resume_norm))

    weighted_hits = 0
    weighted_total = 0
    matched = []
    missing = []

    for skill in jd_skills:
        weighted_total += 3
        if skill in resume_skills:
            weighted_hits += 3
            matched.append(skill)
        else:
            missing.append(skill)

    jd_common = [t for t, c in jd_tokens.items() if c >= 2 and len(t) >= 3]
    for term in jd_common:
        if term in {"experience", "responsible", "responsibilities"}:
            continue
        weighted_total += 1
        if resume_tokens.get(term, 0) > 0:
            weighted_hits += 1
        elif term not in missing and term not in matched:
            missing.append(term)

    score = 0 if weighted_total == 0 else round(100 * weighted_hits / weighted_total)
    score = max(0, min(100, score))

    if score >= 80:
        band = "strong match"
    elif score >= 60:
        band = "good match"
    elif score >= 40:
        band = "partial match"
    else:
        band = "weak match"

    reasoning_parts = [f"{band} based on overlap between resume and JD."]
    if matched:
        reasoning_parts.append(f"Matched key requirements: {', '.join(matched[:8])}.")
    if missing:
        reasoning_parts.append(f"Likely gaps: {', '.join(missing[:8])}.")

    return {
        "score": score,
        "reasoning": " ".join(reasoning_parts),
        "missing_skills": missing[:10],
    }


# Usage example
resume = "Software engineer with 4 years of experience in Python, Django, SQL, Git, and AWS. Built APIs and worked in agile teams."
jd = "We need a Python engineer with Django, PostgreSQL, Docker, AWS, and strong communication skills."

result = score_resume_against_jd(resume, jd)
print(result)