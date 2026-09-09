# Personal AI Assistant

An AI assistant built as an end-to-end Azure and Microsoft Foundry learning project.

The system will progressively support:

- Resume-based RAG
- External tools such as weather
- Microsoft Foundry agents
- Azure AI Search
- Azure Blob Storage
- Identity-based authentication
- Managed Identity and RBAC
- Key Vault
- Application monitoring
- Evaluation
- Containerized deployment
- Infrastructure as Code
- CI/CD
- Development, staging, and production environments

## Architecture

The application is being developed progressively:

```text
User
  |
  v
FastAPI Application
  |
  v
Personal AI Assistant
  |
  +--> Foundry Agent
  |       |
  |       +--> Model
  |       +--> Resume Knowledge / RAG
  |       +--> External Tools
  |
  +--> Application Services
  |
  +--> Monitoring