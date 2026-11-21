# Lab 6 step-to-commit map

The original Part A commits are retained. The subsequent steps below were replayed and validated now from the supplied `Lab6_Steps.md`; they are not backdated development evidence.

## Retained Part A

```text
9f487a8 chore: initialize Lab 6 exercise structure
c3b919f test: cycle 1 RED - register_adds_hours
91c6162 feat: cycle 1 GREEN - register_adds_hours
6648ecb refactor: cycle 1 REFACTOR - register_adds_hours
dcea832 test: cycle 2 RED - cannot_go_over_18_hours
95a40f2 feat: cycle 2 GREEN - cannot_go_over_18_hours
9466b1e refactor: cycle 2 REFACTOR - cannot_go_over_18_hours
ff10ee6 test: cycle 3 RED - cannot_register_same_course_twice
72d3487 feat: cycle 3 GREEN - cannot_register_same_course_twice
fb7f599 refactor: cycle 3 REFACTOR - cannot_register_same_course_twice
9edbbaf test: cycle 4 RED - drop_removes_course
090ac86 feat: cycle 4 GREEN - drop_removes_course
69022d5 refactor: cycle 4 REFACTOR - drop_removes_course
cff28d1 test: cycle 5 RED - drop_unknown_course_raises
ffdf104 feat: cycle 5 GREEN - drop_unknown_course_raises
9a34fe0 refactor: cycle 5 REFACTOR - drop_unknown_course_raises
```

## Replayed steps

| Commit | Step | Verification |
|---|---|---|
| `955122d` | docs: Task A1 explain the limits of 100 percent coverage | One-sentence coverage answer retained from the original submission. |
| `92979df` | chore: Part B step 1 configure Behave imports | Import setup matches the supplied guide. |
| `0edf325` | test: Part B step 2 describe registration rules in Gherkin | Feature parses: three scenarios and one outline with three examples. |
| `93ad1bf` | feat: Part B step 3 implement the registration step definitions | Behave: 6 scenarios passed, 0 failed. |
| `44b8da1` | docs: Part B step 4 record the six passing baseline scenarios | Baseline Behave run before Task B1: 6 scenarios passed, 0 failed. |
| `72439b6` | test: Task B1 RED add the drop-course scenario | Behave fails as expected because the drop step is undefined; six existing scenarios still pass. |
| `98a717b` | feat: Task B1 GREEN implement the drop-course step | Behave: 7 scenarios and 28 steps passed, 0 failed. |
| `3ac5e0e` | chore: Part C step 0 preserve the original invoice implementation | Existing 5 registration tests pass; legacy invoice preserved verbatim for comparison. |
| `abd5a09` | docs: Task C1 identify invoice code smells and design principles | Six smells documented against the unchanged legacy baseline. |
| `86920cb` | test: Part C step 1 characterize the legacy invoice totals | 8 tests pass, including all 3 invoice totals against the legacy implementation. |
| `e873ed4` | refactor: Part C step 2 name the invoice pricing constants | All 8 tests pass; legacy totals remain 7200, 3600 and 17000 EGP. |
| `c2abf37` | refactor: Part C step 3 extract fee policies and isolate invoice calculations | All 8 tests pass; calculate from total hours, close files with with, and move display to the caller as specified. |
| `5929e2d` | refactor: Part C step 4 replace conditional dispatch with a policy registry | All 8 tests pass; policy selection uses the POLICIES dictionary. |
| `618e694` | refactor: Part C step 5 inject the invoice writer | All 8 tests pass; FileWriter remains the default and make_invoice accepts an injected writer. |
| `0bea72a` | test: Part C step 5 verify invoice output with a fake writer | 9 tests pass, including the injected-writer assertion without invoice disk I/O. |
| `999dbdf` | docs: Part C record the optional invoice complexity check | Ruff C901 passes at maximum complexity 1. |
| `b4f5cc9` | test: Task C2 RED specify the 25 percent sibling discount | Expected failure: KeyError 'sibling'; 9 existing tests pass. |
| `837c922` | feat: Task C2 GREEN add SiblingPolicy without changing make_invoice | All 10 tests pass; only the sibling class and registry entry were added to invoice.py. |
| `71ee467` | docs: Part D scenario 1 describe the happy path | 1 project Gherkin scenario(s) parse successfully; specifications only, as requested by Part D. |
| `866bdb9` | docs: Part D scenario 2 describe the expired QR error | 2 project Gherkin scenario(s) parse successfully; specifications only, as requested by Part D. |
| `185eddd` | docs: Part D scenario 3 describe the duplicate attendance edge case | 3 project Gherkin scenario(s) parse successfully; specifications only, as requested by Part D. |
| `a1bae34` | docs: submission record 10 passing tests and 100 percent coverage | Fresh Windows pytest run: 10 passed; registration.py and invoice.py both have 100 percent statement coverage. |
| `b4d23e0` | docs: submission capture the complete passing Behave output | Fresh Behave run: 1 feature, 7 scenarios and 28 steps passed; 0 failed. |
| `0fa3e6f` | docs: submission retain the supplied coverage screenshot | Existing screenshot retained from the original submission; fresh Windows results are in coverage_output.txt. |
| `5658923` | docs: submission explain verification commands and the replayed history | README records evidence provenance, the preserved original branch, and the scope of the project specifications. |
