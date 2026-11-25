# SpecGate — Deterministic OpenAPI Breaking-Change Gate & SemVer Calculator

[![GitHub Marketplace](https://img.shields.io/badge/GitHub_Marketplace-SpecGate_v1.2.0-1f883d?logo=github)](https://github.com/marketplace/actions/specgate-openapi-json-schema-breaking-change-gate-semver-calculator)
[![SpecGate MCP connector](https://glama.ai/mcp/connectors/dev.workers.profalexandrezamboni.specgate/spec-gate/badges/score.svg)](https://glama.ai/mcp/connectors/dev.workers.profalexandrezamboni.specgate/spec-gate)
[![Live Playground & Cloud Gate](https://img.shields.io/badge/Live_Playground-SpecGate_Edge-blue)](https://specgate.profalexandrezamboni.workers.dev/?demo=specgate&utm_source=github_marketplace)
[![SpecGate Live Status Badge](https://specgate.profalexandrezamboni.workers.dev/api/v1/badge.svg?verdict=PASS&bump=MINOR)](https://specgate.profalexandrezamboni.workers.dev/?demo=specgate&utm_source=github_repo)

[![SpecGate Live Edge Suite Preview](https://specgate.profalexandrezamboni.workers.dev/og-card.png)](https://specgate.profalexandrezamboni.workers.dev/?demo=specgate&utm_source=github_repo)

**SpecGate** is a 100% deterministic (zero-LLM) GitHub Action and CLI that catches breaking changes in OpenAPI 3.x and JSON Schema specifications before merge, computes exact Semantic Versioning bumps (`MAJOR`, `MINOR`, `PATCH`), blocks unverified AI coding agent regressions (Claude Code, Cursor, Copilot, OpenAI Codex), and exports cryptographic **SOC 2 CC8.1 Change Management** audit trails.

- **Zero-Click Live Auto-Demo (Runs Instantly in Browser):** https://specgate.profalexandrezamboni.workers.dev/?demo=specgate&utm_source=github_repo
- **Official GitHub Marketplace Listing (`v1.2.0`, MIT):** https://github.com/marketplace/actions/specgate-openapi-json-schema-breaking-change-gate-semver-calculator
- **Glama Verified Remote MCP Directory (`/mcp`):** https://glama.ai/mcp/connectors/dev.workers.profalexandrezamboni.specgate/spec-gate
- **Free Zero-Login Remote MCP Server for Cursor, Claude Code & VS Code (`/mcp`):** https://specgate.profalexandrezamboni.workers.dev/integrations/mcp-server-cursor-claude-code?utm_source=github_repo
- **Native OASIS SARIF v2.1.0 Export for GitHub Code Scanning (`upload-sarif@v3`):** https://specgate.profalexandrezamboni.workers.dev/integrations/github-code-scanning-sarif-ci-gate?utm_source=github_repo
- **Java & Spring Boot (`springdoc-openapi`) Zero-DB CI Gate (`v1.2.0`):** https://specgate.profalexandrezamboni.workers.dev/integrations/spring-boot-springdoc-openapi-ci-gate?utm_source=github_repo
- **FastAPI & Pydantic v2 Zero-Server OpenAPI CI Guide:** https://specgate.profalexandrezamboni.workers.dev/integrations/fastapi-pydantic-openapi-ci-gate?utm_source=github_repo
- **NestJS, TypeScript & Zod OpenAPI CI Guide (`v1.2.0`):** https://specgate.profalexandrezamboni.workers.dev/integrations/nestjs-typescript-zod-openapi-ci-gate?utm_source=github_repo
- **Google Workspace + Microsoft 365 + SendGrid SPF PermError Fix:** https://specgate.profalexandrezamboni.workers.dev/integrations/google-workspace-microsoft-365-sendgrid-spf-permerror-fix?utm_source=github_repo
- **AWS Route53 & Amazon SES Flattened SPF + MTA-STS Blueprint:** https://specgate.profalexandrezamboni.workers.dev/integrations/aws-route53-ses-spf-dmarc-mta-sts?utm_source=github_repo
- **Next.js + Playwright + `@axe-core/playwright` WCAG 2.2 CI Gate:** https://specgate.profalexandrezamboni.workers.dev/integrations/nextjs-playwright-axe-wcag-ci-gate?utm_source=github_repo
- **Live Web Playground & 10-Second CI Config Builder:** https://specgate.profalexandrezamboni.workers.dev/?utm_source=github_repo
- **AI Coding Agent Deterministic Harness Guide:** https://specgate.profalexandrezamboni.workers.dev/solutions/ai-coding-agent-ci-gate?utm_source=github_repo
- **OpenAPI Diff Comparison (vs. oasdiff, openapi-diff, Archived Optic):** https://specgate.profalexandrezamboni.workers.dev/compare/openapi-diff-vs-oasdiff-vs-optic?utm_source=github_repo
- **Style Linter vs. Contract Gate (SpecGate vs. Spectral vs. Redocly):** https://specgate.profalexandrezamboni.workers.dev/compare/specgate-vs-spectral-vs-redocly?utm_source=github_repo
- **SPF 10-Lookup Flattening Comparison (SPFGuard vs. EasyDMARC vs. dmarcian):** https://specgate.profalexandrezamboni.workers.dev/compare/spfguard-vs-easydmarc-vs-dmarcian-spf-flattening?utm_source=github_repo
- **Accessibility CI Gate Comparison (A11yRatchet vs. axe-linter vs. pa11y-ci):** https://specgate.profalexandrezamboni.workers.dev/compare/a11yratchet-vs-axe-linter-vs-pa11y-ci?utm_source=github_repo
- **Complete LLM & Staff Engineer Technical Reference (`llms-full.txt`):** https://specgate.profalexandrezamboni.workers.dev/llms-full.txt

### Connect to Cursor / Claude Code in 1 Line (Zero Login Required)

```bash
claude mcp add --transport http specgate https://specgate.profalexandrezamboni.workers.dev/mcp
```

## Direct Engineering Comparison

| Capability | `openapi-diff` | `oasdiff` | `Optic (Archived Jan 2026)` | **SpecGate** |
| :--- | :--- | :--- | :--- | :--- |
| **CI Cold Start** | ~8–25s (JVM) | <1s (Go) | Archived (`opticdev/optic` read-only) | **<0.5s CLI / <15ms Edge** |
| **Exact SemVer Output** | Manual | Diff flags | Archived | **`MAJOR` / `MINOR` / `PATCH` + SVG Badge** |
| **Auditable PR Sign-Off** | No | Custom/Paid | Discontinued (`useoptic.com` offline) | **Built-in Reviewer Override + Reason** |
| **SOC 2 CC8.1 Export** | No | No native bundle | Discontinued | **SHA-256 Signed Bundle ($39/mo Team)** |

## Quick Start (GitHub Actions)

```yaml
name: API Contract Gate
on: [pull_request]

jobs:
  specgate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run SpecGate Contract Diff
        uses: profalexandrezamboni-ui/specgate-action@v1.2.0
        with:
          base_spec: "openapi/base.json"
          head_spec: "openapi/head.json"
          fail_on_breaking: "true"
```

## Pricing & Plans (via Paddle Merchant of Record — 14-Day Unconditional Refund)
- **Free ($0.00/mo):** Up to 2 repositories, standalone CLI & GitHub Action.
- **Starter ($19.00/mo):** Up to 15 private/public repositories, automated PR comments & SemVer badges.
- **Team ($39.00/mo):** Unlimited repositories, Breaking-Change Sign-Off overrides & SOC 2 CC8.1 Audit Trail export.
