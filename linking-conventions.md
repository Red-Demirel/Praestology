# Linking Conventions

**Purpose**  
Maintain a single, human- and machine-readable naming style across Praestology. This eliminates broken internal links caused by the previous mix of snake_case, space-separated titles, and legacy names (e.g. `cosmos.md`).

### 1. Official Naming Standard (Kebab-case)
- All new **folders** and **.md files**: `kebab-case` (lowercase letters, words separated by hyphens).
- Examples (use these exact names):
  - `physics.md`
  - `consciousness.md`
  - `biology.md`
  - `education.md`
  - `domains/physics/`
  - `summaries/domains/biology.md`
  - `linking-conventions.md`

- Existing exceptions we keep for now (do **not** rename these):
  - `Praestology short.md` (space-separated title)
  - `domain-map.yaml`
  - `specifications.yaml`
  - `readme.md`
  - `manifesto.md`

- Legacy cleanup already done:
  - `cosmos.md` → `physics.md` (and `domains/cosmos/` → `domains/physics/`)
  - Any remaining snake_case references must be updated.

### 2. Internal Linking Rules
Always use **relative Markdown links** in kebab-case:

```markdown
See the [core rules](../manifesto.md#core-rules) in the manifesto.

For details on the η-field, refer to [physics](./physics.md#eta-field).

Biology is covered in [summaries/domains/biology.md](./summaries/domains/biology.md).

See the [Ch6 threshold](../consciousness.md#ch6-threshold).
