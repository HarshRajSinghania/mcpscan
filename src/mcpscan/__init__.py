"""
mcpscan
=======
Security scanner for MCP (Model Context Protocol) servers.

Detects prompt injection in tool descriptions, unsafe authentication,
path traversal, over-broad permissions, and more.
Zero dependencies. Pure Python 3.10+.

Quick start:
    from mcpscan import MCPScanner

    scanner = MCPScanner()
    result = scanner.scan_file("server-manifest.json")
    print(result.risk_level)  # CRITICAL / HIGH / MEDIUM / LOW / SAFE
    for finding in result.findings:
        print(finding.rule_id, finding.severity.value, finding.name)

CLI:
    mcpscan scan server.json
    mcpscan scan server.json --format json
    mcpscan rules
"""

from mcpscan.rules import ALL_RULES, MCPRule, Severity
from mcpscan.scanner import MCPBatchReport, MCPFinding, MCPScanner, MCPScanResult

__version__ = "1.0.0"
__author__ = "Linda Oraegbunam"
__all__ = [
    "MCPScanner",
    "MCPScanResult",
    "MCPBatchReport",
    "MCPFinding",
    "MCPRule",
    "Severity",
    "ALL_RULES",
]
