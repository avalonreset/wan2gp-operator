# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 0.4.x   | Yes       |
| < 0.4   | No        |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly. **Do not open a public issue.**

**Email:** benjamin@avalonreset.com

### What to include

- Description of the vulnerability
- Steps to reproduce
- Affected version(s)
- Potential impact

### Response timeline

- **Acknowledgment:** within 48 hours
- **Initial assessment:** within 5 business days
- **Fix or mitigation:** within 30 days for confirmed vulnerabilities

### Scope

This project is a CLI operator skill that orchestrates Wan2GP. Security concerns most relevant to this project include:

- Command injection via user-supplied prompts or file paths
- Path traversal in log file or output handling
- Unsafe deserialization of state files (`.wan2gp_operator_state.json`)
- Exposure of local file system paths in logs or error output

### Disclosure

We follow coordinated disclosure. Once a fix is available, we will credit the reporter (unless they prefer to remain anonymous) and publish a security advisory.