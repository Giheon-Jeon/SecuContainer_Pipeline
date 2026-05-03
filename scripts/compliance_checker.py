import re
import sys
import argparse

def check_dockerfile_compliance(file_path):
    issues = []
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)

    # 1. Check for USER root
    if re.search(r'USER\s+root', content, re.IGNORECASE) or 'USER' not in content:
        # If USER is not specified, it defaults to root
        if 'USER' not in content:
            issues.append("[CRITICAL] USER not specified (defaults to root)")
        else:
            issues.append("[CRITICAL] Explicitly running as root user")

    # 2. Check for base image (Ubuntu/Debian vs Alpine/Distroless)
    if re.search(r'FROM\s+ubuntu|FROM\s+debian', content, re.IGNORECASE):
        issues.append("[WARNING] Using heavy base image (Ubuntu/Debian). Consider Alpine or Distroless.")

    # 3. Check for unnecessary packages
    if re.search(r'apt-get\s+install.*(curl|net-tools|vim|wget|ping)', content, re.IGNORECASE):
        issues.append("[ADVISORY] Dockerfile contains potentially unnecessary tools (curl, wget, etc.)")

    # 4. Check for hardcoded secrets (Basic check)
    if re.search(r'(API_KEY|PASSWORD|TOKEN|SECRET)\s*=\s*["\'].+["\']', content, re.IGNORECASE):
        issues.append("[CRITICAL] Potential hardcoded secret detected")

    if issues:
        print(f"--- Compliance Report for {file_path} ---")
        for issue in issues:
            print(issue)
        return len([i for i in issues if "[CRITICAL]" in i])
    else:
        print(f"No compliance issues found for {file_path}.")
        return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check Dockerfile for security compliance.")
    parser.add_argument("files", nargs='+', help="Dockerfile paths to check")
    
    args = parser.parse_args()
    
    total_critical = 0
    for f in args.files:
        total_critical += check_dockerfile_compliance(f)
    
    if total_critical > 0:
        print(f"\nTotal Critical Compliance Issues: {total_critical}")
        # sys.exit(1) # We can decide whether to fail the build here or just report
    else:
        print("\nAll Dockerfiles passed compliance check.")
