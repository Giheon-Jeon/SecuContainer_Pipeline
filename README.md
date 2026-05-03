# 🛡️ SecuContainer_Pipeline
### 컨테이너 공급망 보안을 위한 하드닝 파이프라인 (Container Supply Chain Security Hardening)

<p align="center">
  <img width="200" height="200" alt="project_logo" src="https://raw.githubusercontent.com/aquasecurity/trivy/main/docs/imgs/trivy-logo.png" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Security-Hardening-brightgreen?style=for-the-badge&logo=shield" />
  <img src="https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue?style=for-the-badge&logo=github-actions" />
  <img src="https://img.shields.io/badge/Docker-Distroless-2496ED?style=for-the-badge&logo=docker" />
</p>

---

## 📖 프로젝트 개요
본 프로젝트는 현대적인 클라우드 네이티브 환경에서 **컨테이너 공급망 보안(Supply Chain Security)**의 중요성을 실증하고, 이를 자동화된 파이프라인을 통해 해결하는 프로세스를 구현합니다. 

의도적으로 취약하게 설계된 베이스라인 앱(`vulnerable-app`)과 보안 최적화가 적용된 앱(`hardened-app`)을 비교 분석하여, **이미지 경량화, 취약점(CVE) 제거, 권한 최소화**의 효과를 가시화합니다.

---

## 📌 주요 기능
1. **취약한 베이스라인(Vulnerable Baseline)**: 
   - 레거시 환경(Ubuntu 18.04), Root 권한, 불필요한 패키지 및 취약한 의존성(Log4j 2.14.1)을 포함한 대조군 구축.
2. **자동화된 취약점 스캔(Automated Scanning)**: 
   - GitHub Actions와 Trivy를 통합하여 빌드 시점에 OS 및 라이브러리 취약점을 전수 조사.
3. **Fail-Fast 파이프라인**: 
   - Python 기반 커스텀 파서를 통해 High/Critical 취약점 발견 시 배포 프로세스를 즉시 차단.
4. **이미지 하드닝(Image Hardening)**: 
   - Distroless 기반 멀티 스테이지 빌드, Non-root 설정, 보안 패치가 적용된 라이브러리 사용.
5. **규정 준수 및 리포팅**: 
   - Dockerfile 보안 모범 사례 검증 및 하드닝 개선 지표를 담은 통합 보안 리포트 자동 생성.

---

## 🛠 기술 스택

### Security & Infrastructure
| Category | Technology | Reason |
| :--- | :--- | :--- |
| **Scan Engine** | ![Trivy](https://img.shields.io/badge/Trivy-000000?style=flat-square&logo=trivy&logoColor=white) | 가장 신뢰받는 오픈소스 컨테이너 스캔 엔진 |
| **Runtime** | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) | 컨테이너화 및 이미지 하드닝의 표준 |
| **CI/CD** | ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white) | 워크플로우 자동화 및 보안 게이트웨이 구축 |
| **Base Image** | ![Distroless](https://img.shields.io/badge/Google-Distroless-4285F4?style=flat-square&logo=google&logoColor=white) | 쉘이 제거된 최소형 런타임 이미지로 공격 표면 제거 |

### Language & Framework
- ![Java](https://img.shields.io/badge/Java-11-ED8B00?style=flat-square&logo=java) ![Spring Boot](https://img.shields.io/badge/Spring_Boot-2.6.2-6DB33F?style=flat-square&logo=spring-boot)
- ![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=flat-square&logo=python) (Automation & Reporting)

---

## 🚀 수행 단계 (Project Phases)

### Phase 1. 취약한 환경 구축
- **Base**: `ubuntu:18.04`
- **User**: `root`
- **Vulnerability**: Log4j CVE-2021-44228 탑재
- **Overhead**: `curl`, `net-tools`, `vim` 등 불필요한 도구 포함

### Phase 2. 스캔 및 차단 자동화
- Trivy JSON 결과를 `scripts/scan_parser.py`로 분석
- 보안 임계치(High 이상) 초과 시 워크플로우 실패 처리

### Phase 3. 인프라 하드닝
- **Multi-stage Build**: 빌드 도구와 소스 코드를 실행 이미지에서 완전히 분리
- **Distroless Java**: OS 라이브러리를 최소화하여 90% 이상의 CVE 제거
- **Non-root USER**: UID 65532 사용으로 호스트 권한 탈취 방지

### Phase 4. 보안 설정 검증
- `scripts/compliance_checker.py`를 통한 Dockerfile 정적 분석
- 권한 설정, 베이스 이미지 적절성 등 린트 작업 수행

### Phase 5. 결과 리포팅
- 하드닝 성과를 가시화하는 `reports/security_hardening_report.md` 생성
- 이미지 크기 및 취약점 감소 지표 자동 산출

---

## 🏗 프로젝트 구조
```text
.
├── 📁 .github/workflows/     # CI/CD 파이프라인 (Trivy Scan 포함)
├── 📁 vulnerable-app/        # 취약한 베이스라인 애플리케이션
├── 📁 hardened-app/          # 하드닝이 적용된 애플리케이션
├── 📁 scripts/               # 파이프라인 자동화 스크립트 (Python)
│   ├── scan_parser.py        # CVE 스캔 결과 분석
│   ├── compliance_checker.py # Dockerfile 규정 준수 체크
│   └── report_generator.py   # 보안 리포트 생성
├── 📁 reports/               # 자동 생성된 보안 리포트 저장소
└── README.md                 # 프로젝트 문서화
```

---

## 🤝 협업 및 자동화 규칙
- **Branching Strategy**: `main` ← `BE-전기헌-(번호)`
- **Commit Message**: `{emoji} {tag}: {message} 구현` (예: `✨ Feat: 하드닝 로직 구현`)
- **Security First**: 모든 커밋은 로컬 보안 검증 스크립트 통과 필수

---

## 🤖 AI 활용 방식
**Antigravity (Google Deepmind)**를 통해 보안 아키텍처 설계 및 파이프라인 전 과정을 자동화했습니다.

---
© 2026 SecuContainer Team. Licensed under [MIT](LICENSE).