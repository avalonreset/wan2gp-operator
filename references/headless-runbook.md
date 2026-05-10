# Wan2GP Headless Runbook

Use this workflow for reliable batch rendering from saved Wan2GP queue/settings files.

This runbook is agent-facing. A user should be able to ask Codex or Claude for a
result in plain language, then let the operator translate that intent into a
WanGP process file, a dry-run, a headless run, and a diagnosis loop if anything
fails.

Preferred entrypoint:
```bash
python scripts/wan2gp_operator.py <command>
```

## 1. Confirm Inputs

- Wan2GP root folder exists and contains `wgp.py`
- Process file exists and is one of:
  - `.zip` from "Save Queue" (includes attachments)
  - `.json` from "Export Settings" (references existing media paths)

## 2. Detect Hardware Baseline

```bash
python scripts/wan2gp_operator.py bootstrap
```

Use suggested defaults as your first run profile.

## 3. Plan Command

```bash
python scripts/wan2gp_operator.py plan \
  --wan-root <WAN2GP_ROOT> \
  --process <QUEUE_OR_SETTINGS_FILE> \
  --output-dir <OUTPUT_DIR>
```

## 4. Dry-Run First

```bash
python scripts/wan2gp_operator.py run \
  --wan-root <WAN2GP_ROOT> \
  --process <QUEUE_OR_SETTINGS_FILE> \
  --output-dir <OUTPUT_DIR> \
  --dry-run
```

## 5. Execute Batch

```bash
python scripts/wan2gp_operator.py run \
  --wan-root <WAN2GP_ROOT> \
  --process <QUEUE_OR_SETTINGS_FILE> \
  --output-dir <OUTPUT_DIR> \
  --log-file logs/wan2gp-headless.log
```

## 6. Diagnose Failures

```bash
python scripts/wan2gp_operator.py diagnose --log-file logs/wan2gp-headless.log
```

Apply one remediation at a time, then retest.

