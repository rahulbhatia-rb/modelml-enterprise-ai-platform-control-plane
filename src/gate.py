REQUIRED={'kubernetes': ['multi_az', 'requests_limits', 'pdb', 'health_probes', 'network_policies', 'workload_identity', 'secret_management', 'image_pinning', 'rollback', 'audit_logging'], 'terraform': ['reusable_modules', 'remote_state', 'locking', 'environment_isolation', 'reviewed_plan', 'drift_detection', 'least_privilege', 'encryption_defaults', 'tagging', 'policy_enforcement'], 'cicd': ['branch_protection', 'required_reviews', 'short_lived_credentials', 'dependency_scan', 'container_scan', 'iac_scan', 'artifact_provenance', 'environment_approval', 'rollback_path', 'audit_trail'], 'network': ['private_subnets', 'explicit_ingress_egress', 'segmentation', 'load_balancer', 'dns_owner', 'private_access', 'firewall_controls', 'no_public_database'], 'data': ['database_encryption', 'tls', 'automated_backups', 'restore_testing', 'retention_policy', 'object_storage_controls', 'secret_rotation', 'data_residency'], 'observability': ['metrics', 'logs', 'traces', 'correlation_ids', 'slos', 'alert_owner', 'oncall', 'deployment_markers', 'audit_logs', 'redaction'], 'compliance': ['access_reviews', 'asset_inventory', 'change_approvals', 'backup_evidence', 'restore_evidence', 'vuln_remediation', 'incident_records', 'retention_deletion', 'exception_expiry', 'evidence_timestamp'], 'ai_security': ['tenant_isolation', 'no_prod_data_local', 'document_access_scope', 'immutable_privileged_audit', 'break_glass_expiry', 'human_approval_high_risk']}

def evaluate(spec):
    findings=[]
    for section, fields in REQUIRED.items():
        values=spec.get(section,{})
        for field in fields:
            if not values.get(field): findings.append(f'{section}.{field} is required')
    return {'allowed': not findings,'findings':findings}
