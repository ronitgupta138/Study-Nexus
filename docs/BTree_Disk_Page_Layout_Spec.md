# B+ Tree Disk Slotted Page Architecture Specification

## 1. Slotted Page Layout
- Standard 4KB disk page partition:
  - Header (24 bytes): Page ID, LSN, free space pointer, slot count, page type (leaf vs internal).
  - Slot Array (growing downward): Array of 2-byte offsets pointing to individual cell records.
  - Cell Storage (growing upward): Variable-length key-value payload entries.
