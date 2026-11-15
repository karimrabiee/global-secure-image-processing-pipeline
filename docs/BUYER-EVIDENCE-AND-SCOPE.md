# Buyer Evidence Notes — Serverless Image Processing Portfolio

This repository is a portfolio architecture and implementation sample. It is not a client engagement, independent security audit, or certification. The evidence below follows the repository's own testing and limitations documents.

## What the project contains

- API Gateway and Lambda-based presigned upload flow.
- S3 upload and processed-image storage.
- SQS buffering and a dead-letter queue for failed processing messages.
- Lambda image processing with resized variants, watermarking, and metadata extraction.
- DynamoDB metadata storage.
- CloudFront private delivery using Origin Access Control.
- AWS WAF, KMS encryption, CloudWatch/SNS monitoring, CloudTrail, GuardDuty, and Security Hub components.
- Optional, feature-flagged data-plane DR components: S3 Cross-Region Replication, DynamoDB Global Tables, and CloudFront origin failover.

## Recorded validation in the repository

The project's `docs/testing-results.md` records owner-run tests for:
- Presigned upload and image processing.
- Metadata persistence.
- CloudFront delivery and denied direct S3 access.
- WAF XSS and SQLi test requests returning HTTP 403.
- A malformed message reaching the DLQ.
- S3 replication and DynamoDB replica checks during optional DR test windows.
- SNS alert delivery for a deliberately triggered alarm.

These are project-maintained records, not independent third-party verification. A buyer should review the underlying evidence and its date before treating a test as current.

## Important boundaries

The repository's own `docs/assumptions-and-limitations.md` states:
- The steady-state design is single-region for compute.
- Multi-region processing is not active-active.
- An ingestion-region outage requires manual redeployment of API Gateway and Lambda in the secondary region.
- Infrastructure changes are deployed manually; there is no CI/CD pipeline or automated drift detection.
- AWS Config integration is not implemented.
- Lambda performance settings have not been empirically tuned.
- WAF rate-based rules are not configured.
- Security Hub and GuardDuty findings are reviewed manually rather than through automated response.

Therefore, describe the multi-region component as a **feature-flagged DR design with recorded data-plane tests**, not as automatic full-stack regional failover or a production DR guarantee.

## Service problems this work can inform

- Designing an event-driven S3/Lambda/SQS processing flow.
- Reviewing a presigned upload and private object delivery pattern.
- Diagnosing SQS redrive/DLQ or Lambda processing behavior.
- Reviewing IAM, encryption, WAF, logging, and monitoring choices in a defined AWS scope.
- Documenting a manual recovery approach and its operational gaps.

These are service areas the portfolio can demonstrate. They do not imply that every buyer environment has the same implementation or that every control is production-ready.

## Delivery approach

1. Agree the exact AWS services, regions, resources, and desired outcome.
2. Begin with redacted configuration and read-only evidence.
3. Separate implemented controls from design-only recommendations.
4. Agree changes, acceptance checks, and rollback before applying anything.
5. Deliver a change summary, test output, limitations, and handover steps.

## Exclusions

No penetration testing, compliance certification, independent audit opinion, guaranteed uptime, guaranteed savings, or unapproved production changes. No long-lived credentials or root account access should be shared.
