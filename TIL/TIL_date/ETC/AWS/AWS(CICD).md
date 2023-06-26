 

# AWS (CICD)

​    

## CodeCommit

- git같은 AWS의 버전 관리툴 (version control)
- 개인 repository를 무료로 사용가능
- repository 사이즈 제한없음
- 고가용성이 높고, 완전 관리되어짐
- 다른 툴들과 호환이 잘됨
- aws 클라우드내에만 코드가 저장되어 보안에 좋음
- 표준 git 명령어를 사용할 수 있지만 인증이 필요 
  - SSH
  - HTTPS
- IAM를 통한 권한관리가능
- KMS를 통해 코드가 암호화되어 사용자만 코드를 불러올 수 있음
- 계정 간 엑세스는 IAM역할을 생성하여 STS (AssumeRole API)를 이용함

|                          | CodeCommit        | GitHub                     |
| ------------------------ | ----------------- | -------------------------- |
| 코드리뷰 (Pull Requests) | O                 | O                          |
| AWS CodeBuild와의 호환   | O                 | O                          |
| 인증 (SSH, HTTPS)        | O                 | O                          |
| Security                 | IAM Users & Roles | GitHub Users               |
| Hosting                  | AWS가 통제        | GitHub / Github Enterprise |

​    

## CodePipeline

- AWS내에서 CI/CD를 조정해주는 비주얼 워크플로우툴
- CodeCommit, ECR, S3, Github등에서 소스 가져올 수 있음
- CodeBuild, Jenkins등의 빌드툴을 사용가능
- CodeBuild, Device Farm, 써드파티툴들로 테스트
- CodeDeploy, Elastic Beanstalk, CloudFormation, ECS, S3를 배포
- 진행과정중 수동으로 작업 검토할 수 있음
- 각 파이프라인은 아티팩트(파이프라인에서 생성되는 모든 것)를 만듬 
- 아티팩트는 S3버킷에 저장되고 다음 단계로 전달됨
- 아티팩트는 빌드툴에서 빌드된 후 다시 S3에 저장된 후 다름 단계로 저장됨
- CloudWatch Events (EventBridge), CloudTrail 등으로 감시

​    

## CodeBuild

- 빌드명령(Build instructions)
- `buildspec.yml` : 코드의 루트에 위치해야함
- CloudWatch Metrics, Events, Alarms