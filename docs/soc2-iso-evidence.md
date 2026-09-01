# SOC 2 / ISO 27001 Evidence Automation

Map technical controls to evidence sources instead of manually reconstructing history before audits.

Examples:
- GitHub PR approvals -> change management
- Terraform state/plan history -> controlled infrastructure changes
- IAM snapshots -> access controls
- audit logs -> privileged activity
- vulnerability scans -> remediation
- backup + restore tests -> availability
- inventory/tags -> asset ownership

Each exception should have an owner, reason, approval, and expiry date.
