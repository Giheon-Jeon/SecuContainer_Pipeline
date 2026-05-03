# SecuContainer_Pipeline
## 컨테이너 공급망 보안을 위한 하드닝 파이프라인 구축 프로젝트

<p align="center">
  <img width="170" height="170" alt="project_logo" src="https://raw.githubusercontent.com/aquasecurity/trivy/main/docs/imgs/trivy-logo.png" />
</p>

<p align="center">
  <strong>SecuContainer Team</strong><br>
  보안이 내재화된 안전한 컨테이너 이미지를 만듭니다.
</p>

---

## 📌 목차
- [주요 기능](#-주요-기능)
- [🛠 기술 스택 및 선정 이유](#-기술-스택-및-선정-이유)
- [🏗 아키텍처 및 폴더 구조](#-아키텍처-및-폴더-구조)
- [🤝 협업 및 자동화 규칙](#-협업-및-자동화-규칙)
- [🤖 AI 활용 방식](#-ai-활용-방식)

---

## ✨ 주요 기능
1. **취약한 베이스라인 구축**: 취약점이 포함된 레거시 환경을 구축하여 하드닝 효과를 대조합니다.
2. **CI/CD 통합 자동 진단**: Trivy를 활용하여 빌드 시점에 취약점을 자동으로 식별하고 차단합니다.
3. **이미지 하드닝 적용**: Distroless/Alpine 적용 및 Non-root 설정을 통한 공격 표면 최소화.
4. **런타임 보안 검증**: CIS Benchmark 및 시크릿 관리 검증을 통한 배포 환경 안정성 확보.
5. **보안 리포트 자동 생성**: 하드닝 성과를 가시화하는 PDF/HTML 리포트를 자동 생성합니다.

---

## 🛠 기술 스택 및 선정 이유

### Frontend / Backend
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=java&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white)

- **Java/Spring Boot**: 엔터프라이즈 환경에서 가장 널리 사용되는 스택으로, 공급망 보안의 중요성이 큽니다.

### 인프라 및 보안
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Trivy](https://img.shields.io/badge/Trivy-000000?style=for-the-badge&logo=trivy&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

- **Trivy**: 컨테이너 이미지의 OS 패키지 및 라이브러리 취약점(CVE) 스캔에 최적화된 도구입니다.
- **Python**: 스캔 결과 파싱 및 리포트 생성을 위한 유연한 스크립팅 언어입니다.

---

## 🏗 아키텍처 및 폴더 구조
유지보수성과 확장성을 고려한 **기능 단위(Feature-based) 구조** 채택
```text
├── 📁 .github/               # CI/CD 워크플로우 (Actions)
├── 📁 vulnerable-app/        # 취약한 베이스라인 앱 및 Dockerfile
├── 📁 hardened-app/          # 보안 강화가 적용된 앱 (예정)
├── 📁 scripts/               # 스캔 파서 및 자동화 스크립트
├── 📁 reports/               # 생성된 보안 리포트 저장소
└── 📁 docs/                  # 프로젝트 관련 문서
```

<br>

## 🤝 협업 및 자동화 규칙

- `Git Flow`: main → BE-전기헌-(번호) 브랜치 전략
- `Commit Convention`: `{emoji} {tag}: {message} 구현` 형식 준수
- `Security First`: 모든 커밋 전 보안 검사 및 테스트 수행

<br>

## 🤖 AI 활용 방식
**Antigravity (Google Deepmind)**를 활용한 페어 프로그래밍

**처리 과정:**
1. 요구사항 분석 및 아키텍처 설계
2. 단계별 하드닝 코드 및 스크립트 구현
3. 취약점 분석 및 개선 리포트 생성

**기술 스택:**
- Gemini 2.0 Flash
- GitHub Actions Integration
- Python Data Processing