# HostGuard Project Principles

This document is the architectural and operational constitution of HostGuard. Every design decision, implementation, and review must comply with these principles.

## 1. Virtual Machine Integrity

The integrity of virtual machines is more important than backup execution. An incomplete or deferred operation is preferable to any action that may compromise a virtual machine.

## 2. No Automatic System Upgrades

HostGuard never performs automatic system upgrades. Operating system and host lifecycle decisions remain under explicit administrator control.

## 3. No Automatic Dependency Installation

HostGuard never installs dependencies automatically. Missing prerequisites must be reported clearly without changing the system.

## 4. Auditability

Every action must be auditable. Operational decisions, relevant context, and outcomes must be represented in a form suitable for later review.

## 5. Reversibility

Every destructive action must be reversible whenever possible. When reversibility cannot be guaranteed, the limitation must be explicit before execution.

## 6. Abort on Uncertainty

If there is uncertainty, HostGuard must abort the operation. Ambiguous state, incomplete validation, or insufficient evidence must never be interpreted as permission to proceed.

## 7. Predictability over Automation

HostGuard prioritizes predictability over automation. Behavior must be explicit, deterministic, and understandable to an administrator.
