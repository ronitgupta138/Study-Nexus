# Strict Two-Phase Locking (SS2PL) Concurrency Invariants

## 1. Safety Guarantees
- Transactions acquire shared locks (S) for reads and exclusive locks (X) for writes.
- All acquired locks are held until transaction termination (COMMIT or ABORT), guaranteeing strict serializability and preventing cascading aborts.
