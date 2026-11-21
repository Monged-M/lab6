# Lab 6: TDD, BDD and refactoring

Code is in `lab6/`; submission documents and verification output are in `docs/lab6/`.

Run from `lab6/`:

```powershell
python -m pip install pytest pytest-cov behave ruff
python -m pytest --cov=registration --cov=invoice --cov-report=term-missing
python -m behave --no-color --format plain
```

The final verification has 10 passing pytest tests, 100% statement coverage for both registration and invoice, and 7 passing Behave scenarios (28 steps). `coverage_output.txt` and `behave_output.txt` contain fresh, complete Windows output. `coverage_.png` is the Windows terminal screenshot supplied with the original submission; it shows 10 passing tests and 100% registration coverage. The fresh text report also checks invoice coverage. `behave_baseline_output.txt` records the six original scenarios before the drop scenario was added.

`coverage_answer.md` answers Task A1. `smells.md` covers six legacy code smells for Task C1. `team_story.feature` contains the Part D happy path, error and edge scenarios for QR attendance. These three project scenarios are specifications; executable project steps are outside this lab submission. Confirm that QR attendance matches the team's actual backlog story.

`legacy_invoice.py` preserves the baseline. Invoice characterization tests were run against that baseline before each refactoring step. The sibling discount was added test-first without changing `make_invoice`.

## Commit history

This branch retains the original registration TDD commits. The later BDD, invoice, project-story and evidence steps were replayed from `Lab6_Steps.md` into separate commits and tested during this replay. They do not claim to be the original historical order of work. The original local `main` branch is preserved separately. Existing Part A refactor commits for cycles 1–3 contain formatting cleanup only.

See `step_history.md` for a commit-to-step map and `git_log.txt` for the saved history. One Git push transfers all these commits and preserves their separate entries on GitHub. No squashing or backdating is needed.
