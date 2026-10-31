<div align="center">

```text
███████╗████████╗██╗   ██╗██████╗ ██╗   ██╗      ███╗   ██╗███████╗██╗   ██╗██╗   ██╗███████╗
██╔════╝╚══██╔══╝██║   ██║██╔══██╗╚██╗ ██╔╝      ████╗  ██║██╔════╝╚██╗ ██╔╝██║   ██║██╔════╝
███████╗   ██║   ██║   ██║██║  ██║ ╚████╔╝       ██╔██╗ ██║█████╗   ╚████╔╝ ██║   ██║███████╗
╚════██║   ██║   ██║   ██║██║  ██║  ╚██╔╝        ██║╚██╗██║██╔══╝    ╚██╔╝  ██║   ██║╚════██║
███████║   ██║   ╚██████╔╝██████╔╝   ██║         ██║ ╚████║███████╗   ██║   ╚██████╔╝███████║
╚══════╝   ╚═╝    ╚═════╝ ╚═════╝    ╚═╝         ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚═════╝ ╚══════╝
```

### **Study-Nexus — Autonomous Personal Socratic Study & Research Knowledge Room on Switch**
*Academic Invariant Ingestion, Active Recall Socratic Questioning & Obsidian-Ready Note Compilation*

[![GitHub Stars](https://img.shields.io/github/stars/ronitgupta138/Study-Nexus?style=flat-square&logo=github&color=0891b2)](https://github.com/ronitgupta138/Study-Nexus/stargazers)
[![Orchestrator: Switch](https://img.shields.io/badge/Orchestrator-Switch_Rooms-0891b2?style=flat-square&logo=switch&logoColor=white)](https://github.com/sandbox-quantum/switch)
[![Hackathon: WeMakeDevs](https://img.shields.io/badge/WeMakeDevs-Flip_The_Switch-FF895E?style=flat-square)](https://www.wemakedevs.org/hackathons/switch)
[![Track 02](https://img.shields.io/badge/Track_02-Best_Personal_Workflow-10b981?style=flat-square)](#-the-problem-passive-reading-vs-true-mastery)
[![Multi-Agent](https://img.shields.io/badge/Architecture-Socratic_Study_Swarm-0891b2?style=flat-square)](#-system-architecture)
[![FastMCP](https://img.shields.io/badge/FastMCP-3.3-0891b2?style=flat-square&logo=python&logoColor=white)](https://modelcontextprotocol.io/)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-0891b2?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-Passed_100%25-10b981?style=flat-square)](https://github.com/ronitgupta138/Study-Nexus/actions)
[![CI Pipeline](https://img.shields.io/badge/CI-GitHub_Actions-0891b2?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/ronitgupta138/Study-Nexus/actions/workflows/ci.yml)
[![Hits](https://hits.sh/github.com/ronitgupta138/Study-Nexus.svg?style=flat-square&label=views&color=0891b2&labelColor=0a0b0e)](https://hits.sh/github.com/ronitgupta138/Study-Nexus/)
[![License: MIT](https://img.shields.io/badge/License-MIT-gray?style=flat-square)](LICENSE)

</div>

> 🏆 **Official Submission**: Built for the **WeMakeDevs × DevTools Academy × Switch Hackathon (Track 02: Best Personal or Creative Workflow)**.  
> 👤 **Sole Author**: **[Ronit Gupta](https://github.com/ronitgupta138)** ([LinkedIn](https://www.linkedin.com/in/ronitgupta138/))  

---

## ⚡ The Problem: Passive Reading vs. True Mastery
Engineers, students, and researchers consume hundreds of hours of technical literature, research papers, and documentation. Yet within 48 hours, **over 70% of passive knowledge is lost** to the Ebbinghaus forgetting curve.

Standard chatbots don't solve this: they simply spit out summaries, reinforcing passive reading.

**Study-Nexus** transforms your personal chat channels (Discord, Telegram, Mattermost, Slack) into an **Autonomous SRE / CS Socratic Study Room** powered by Switch. Three specialized AI teammates actively challenge your intuition, evaluate your conceptual derivation from first principles, and archive verified knowledge directly into your notes vault.

---

## 🏛️ System Architecture

```
                     ┌──────────────────────────────────────────────┐
                     │          Personal Study Channel              │
                     │         (Discord / Telegram / Slack)         │
                     └──────────────────────┬───────────────────────┘
                                            │ Switch Room Bridge
                                            ▼
                     ┌──────────────────────────────────────────────┐
                     │            Switch Agent Room                 │
                     │    #distributed-systems-study (Shared Log)   │
                     └───────┬──────────────┬──────────────┬────────┘
                             │              │              │
             ┌───────────────┘              │              └───────────────┐
             ▼                              ▼                              ▼
  ┌──────────────────────┐      ┌──────────────────────┐      ┌──────────────────────┐
  │   @nexus-curator     │      │     @nexus-tutor     │      │    @nexus-scribe     │
  │                      │      │                      │      │                      │
  │ • Paper Ingestion    │─────►│ • Socratic Drills    │─────►│ • Note Compilation   │
  │ • Invariant Extraction│     │ • Active Recall Eval │      │ • Anki/Flashcard Gen │
  │ • Concept Filtering  │      │ • Misconception Fix  │      │ • Vault Archival     │
  └──────────────────────┘      └──────────┬───────────┘      └──────────────────────┘
                                           │
                                           ▼
                               ┌───────────────────────┐
                               │   Learner Derivation  │
                               │ "First-Principle Ans" │
                               └───────────────────────┘
```

---

## 🤖 Specialized AI Teammates

### 1. `@nexus-curator` (Academic Ingestion & Filtering)
* **Role:** Ingests technical papers, RFCs, and documentation.
* **Action:** Strips academic filler and isolates the fundamental mathematical invariants, state machine constraints, and failure boundaries.
* **Handoff:** Hands the extracted theorems directly to `@nexus-tutor`.

### 2. `@nexus-tutor` (Socratic Active Recall Partner)
* **Role:** Refuses to give passive answers; instead, asks probing architectural questions.
* **Action:** Tests edge cases: *"What happens if the leader crashes before the commit index advances?"* Evaluates your answer for first-principles derivation rather than memorized keywords.
* **Handoff:** When 90%+ conceptual mastery is proven, signals `@nexus-scribe`.

### 3. `@nexus-scribe` (Obsidian & Spaced Repetition Archivist)
* **Role:** Automatically compiles the verified dialogue into a structured, publication-grade Markdown study note.
* **Deliverable:** Generates ASCII state machines, core theorems, and Anki-compatible Q&A flashcards ready for long-term retention.

---

## 📋 Real-World Study Transcript

```chat
[14:10] Ronit Gupta: @nexus-curator I just read Ongaro's Raft paper. Can we do an active recall session on leader election and log invariants?

[14:10] @nexus-curator: 📚 Invariants Extracted:
        • Election Safety: At most one leader elected per term.
        • Leader Append-Only: Leaders never overwrite their own log entries.
        • Log Matching: Matching index + term implies identical log prefixes.
        • Leader Completeness: Committed entries survive across all higher terms.
        @nexus-tutor: Context loaded. Please test understanding of Leader Completeness.

[14:11] @nexus-tutor: 🧠 Socratic Drill (Level: Advanced):
        In Raft, if a partitioned leader appends uncommitted entries and gets deposed,
        how does the election protocol guarantee the new leader already has all committed entries
        without needing to contact every node in the cluster?

[14:12] Ronit Gupta: Every committed entry requires a majority quorum. An election also requires
        a majority quorum. Any two majorities must overlap by at least one server. That overlapping
        server will reject any candidate whose log is less up-to-date than its own via the RequestVote comparison rule.

[14:12] @nexus-tutor: 🎯 CONCEPTUAL MASTERY VERIFIED: 98% (STRONG INTUITION)
        • Correctly cited Pigeonhole Quorum Intersection theorem.
        • Identified the RequestVote log-comparison rule (last term > last index).
        @nexus-scribe: Concept mastered. Please compile and archive the verified study note.

[14:13] @nexus-scribe: ✅ Study Note Compiled & Archived:
        • File: notes/raft-consensus.md
        • 4 Spaced Repetition Flashcards Generated.
        • State-Machine Diagram Linked.
```

---

## 🚀 60-Second Reproduction Guide for Judges

### Option A: Local Python Test (Instant)
```bash
# 1. Clone repository
git clone https://github.com/ronitgupta138/Study-Nexus.git
cd Study-Nexus

# 2. Run automated test
python3 test_nexus_flow.py
```
**Output:**
```text
✅ Study-Nexus end-to-end active recall & note generation test PASSED!
- Ingested Raft consensus paper.
- Generated Socratic active recall drill.
- Verified 98% comprehension score on student derivation.
- Compiled markdown study note with spaced-repetition cards.
```

### Option B: Interactive Terminal Study Simulation
```bash
python3 demo_simulation.py
```
*Renders a real-time terminal study session with colorful panels, theorem tables, and Socratic evaluation.*

---

## 📦 Switch Room Installation

1. Copy `study-nexus.template.yaml` to your Switch templates folder.
2. In **Switch Console**, click **Create Room from Template** → Select **Study-Nexus**.
3. Choose your preferred personal chat platform (Discord, Telegram, Mattermost, Slack).
4. Start mastering any topic with your 3 AI study teammates!

---

## 🏆 Hackathon Submission Details
- **Hackathon:** [WeMakeDevs Flip the Switch](https://www.wemakedevs.org/hackathons/switch)
- **Track:** **Track 02 — Best Personal or Creative Workflow** ($2,000 Cash)
- **Repository:** `https://github.com/ronitgupta138/Study-Nexus`
- **Sole Author:** Ronit Gupta ([GitHub](https://github.com/ronitgupta138) · [LinkedIn](https://www.linkedin.com/in/ronitgupta138/))
