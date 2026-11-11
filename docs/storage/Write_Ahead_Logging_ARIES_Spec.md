# ARIES Crash Recovery Protocol Specification

## 1. Recovery Phases
1. Analysis Pass: Scans log forward from last checkpoint to identify dirty pages and active uncommitted transactions.
2. Redo Pass: Repeats history forward to restore state up to interruption moment.
3. Undo Pass: Scans backward to reverse actions of uncommitted active transactions.
