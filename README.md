# ModelML Enterprise AI Platform Control Plane

Independent proof-of-work inspired by the public ModelML infrastructure role.

This project models the infrastructure guardrails needed for an enterprise AI platform operating in sensitive financial-data environments: Kubernetes, Terraform, GitHub Actions, observability, private networking, databases, cost controls, and audit-ready evidence for SOC 2 / ISO 27001 / GDPR-aligned operations.

> This is based only on the public role description. It does not represent ModelML's private architecture.

## Core idea

Product teams should be able to move fast, but infrastructure should continuously prove that production controls are in place.

```text
Developer change
      |
      v
GitHub Actions
      |
      +--> test/build/scan
      +--> terraform plan
      +--> policy checks
      |
      v
Kubernetes / cloud deployment
      |
      +--> private networking
      +--> workload identity
      +--> encrypted storage
      +--> observability
      +--> backup / recovery
      |
      v
Evidence collector
      |
      +--> SOC 2 evidence
      +--> ISO 27001 evidence
      +--> GDPR controls
      +--> cost / reliability telemetry
      |
      v
READY / BLOCKED
```

## What the control plane checks

### Kubernetes
- multi-AZ node/workload strategy
- requests/limits
- PodDisruptionBudget
- health probes
- network policies
- workload identity
- secret management
- image pinning
- deployment rollback
- audit logging

### Terraform
- reusable modules
- remote state
- state locking
- environment isolation
- reviewed plans
- drift detection
- least-privilege IAM
- encryption defaults
- tagging / ownership
- policy enforcement

### CI/CD — GitHub Actions
- branch protection
- required reviews
- short-lived cloud credentials
- dependency scanning
- container scanning
- IaC scanning
- artifact provenance
- environment approvals
- rollback path
- audit trail

### Networking
- private subnets
- explicit ingress/egress
- VPC segmentation
- load balancers
- DNS ownership
- VPN/private access
- firewall/security-group controls
- no public database exposure

### Data
- PostgreSQL/MySQL/NoSQL production readiness
- encryption at rest
- TLS in transit
- automated backups
- restore testing
- retention policy
- blob/object storage controls
- secrets rotation
- data residency awareness

### Observability
- metrics
- logs
- distributed traces
- correlation IDs
- SLOs
- alert ownership
- on-call routing
- deployment markers
- audit logs
- sensitive-data redaction

### Security / compliance evidence
- access reviews
- least privilege
- asset inventory
- change approvals
- audit logging
- backup evidence
- restore-test evidence
- vulnerability remediation
- incident records
- retention/deletion controls
- vendor / dependency evidence

## Audit evidence model

Compliance should not be a spreadsheet exercise performed once before an audit.

A production system should continuously produce machine-readable evidence:

```text
control_id
resource
owner
evidence_source
evidence_timestamp
status
exception
exception_expiry
```

Examples:
- IAM policy snapshot -> access control evidence
- GitHub PR approval -> change-management evidence
- Terraform plan -> infrastructure change evidence
- backup job + restore test -> availability evidence
- CloudTrail/audit log -> security-event evidence
- vulnerability scan -> remediation evidence
- data retention configuration -> GDPR evidence

## Enterprise AI-specific controls

AI/document-processing systems can touch highly sensitive customer content. This project therefore assumes:
- no production data in developer laptops by default
- strict tenant isolation
- private service-to-service traffic
- redaction of sensitive data from logs/traces
- scoped access to raw documents
- immutable audit history for privileged actions
- explicit retention/deletion policies
- human approval for high-risk infrastructure changes
- break-glass access with expiry and review

## Run locally

```bash
python -m unittest -v tests.test_gate
python src/cli.py examples/production.json
python src/cli.py examples/unsafe.json
```

## 30 / 60 / 90 day approach

### First 30 days
- map production architecture and ownership
- baseline Kubernetes/Terraform/GitHub Actions
- identify audit gaps and manual evidence
- map top incident and cost drivers
- define minimum production-readiness contract

### 31-60
- improve reusable Terraform modules
- standardize CI/CD guardrails
- unify logs/metrics/traces
- automate evidence capture
- validate backups and recovery
- tighten private networking and access paths

### 61-90
- reduce manual audit effort
- mature on-call/SLOs
- enforce cost ownership and capacity controls
- automate drift/risk detection
- make guardrails self-service for product teams

## Success metrics
- deployment failure rate
- MTTR
- SLO attainment
- % infrastructure changes through reviewed IaC
- % audit controls with automated evidence
- restore-test success rate
- privileged-access exception age
- cloud cost per workload/customer
- alert actionability
- manual compliance toil
