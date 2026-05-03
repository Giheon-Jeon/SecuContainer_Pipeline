import json
import sys
import argparse

def parse_trivy_report(file_path, fail_level="HIGH"):
    levels = ["UNKNOWN", "LOW", "MEDIUM", "HIGH", "CRITICAL"]
    fail_idx = levels.index(fail_level.upper())
    
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}.")
        sys.exit(1)

    vulnerabilities_found = []
    
    # Trivy JSON structure: data['Results'] is a list of targets
    if 'Results' in data:
        for result in data['Results']:
            if 'Vulnerabilities' in result:
                for vuln in result['Vulnerabilities']:
                    severity = vuln.get('Severity', 'UNKNOWN').upper()
                    if severity in levels and levels.index(severity) >= fail_idx:
                        vulnerabilities_found.append({
                            'ID': vuln.get('VulnerabilityID'),
                            'PkgName': vuln.get('PkgName'),
                            'Severity': severity,
                            'Title': vuln.get('Title', 'No Title')
                        })

    if vulnerabilities_found:
        print(f"!!! SECURITY VULNERABILITIES DETECTED (Level >= {fail_level}) !!!")
        for v in vulnerabilities_found:
            print(f"[{v['Severity']}] {v['ID']} in {v['PkgName']}: {v['Title']}")
        print(f"\nTotal: {len(vulnerabilities_found)} vulnerabilities found.")
        sys.exit(1)
    else:
        print(f"No vulnerabilities found at or above {fail_level} level.")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse Trivy scan results and fail if vulnerabilities found.")
    parser.add_argument("file", help="Path to Trivy JSON report")
    parser.add_argument("--level", default="HIGH", help="Failure threshold (LOW, MEDIUM, HIGH, CRITICAL)")
    
    args = parser.parse_args()
    parse_trivy_report(args.file, args.level)
