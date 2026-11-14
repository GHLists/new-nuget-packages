# New NuGet packages

Hourly lists of packages newly created on
[nuget.org](https://www.nuget.org/), built from the [v3 catalog](
https://api.nuget.org/v3/catalog0/index.json) of every package operation
nuget.org publishes. Each package touched in the window is checked against
its registration index, whose earliest `published` timestamp decides whether
the package was created inside the window.
A GitHub Actions workflow runs every hour, fetches the packages created since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-nuget-packages-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-14 14:19 UTC

New packages created between 2026-11-14 13:21 UTC and 2026-11-14 14:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-14T14-19-59-178572Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-14 13:36:49 | [Supertext.Sdk](https://www.nuget.org/packages/Supertext.Sdk) | 0.6.0 | Supertext AG | Client for the Supertext AI translation API: translate HTML and texts, with lan… |
| 2026-11-14 13:45:43 | [ModularPipelines.Ansible](https://www.nuget.org/packages/ModularPipelines.Ansible) | 4.0.0 | Tom Longhurst | Helpers for interacting with Ansible configuration management CLI. |
| 2026-11-14 13:45:46 | [ModularPipelines.ArgoCd](https://www.nuget.org/packages/ModularPipelines.ArgoCd) | 4.0.0 | Tom Longhurst | Helpers for interacting with ArgoCD GitOps continuous delivery CLI. |
| 2026-11-14 13:45:52 | [ModularPipelines.Azure](https://www.nuget.org/packages/ModularPipelines.Azure) | 4.0.0 | Tom Longhurst | Helpers for interacting with Azure. |
| 2026-11-14 13:45:55 | [ModularPipelines.Buildah](https://www.nuget.org/packages/ModularPipelines.Buildah) | 4.0.0 | Tom Longhurst | Helpers for interacting with Buildah OCI container image builder CLI. |
| 2026-11-14 13:46:04 | [ModularPipelines.Cosign](https://www.nuget.org/packages/ModularPipelines.Cosign) | 4.0.0 | Tom Longhurst | Helpers for interacting with Cosign CLI for container signing and verification. |
| 2026-11-14 13:46:07 | [ModularPipelines.Distributed.Artifacts.S3](https://www.nuget.org/packages/ModularPipelines.Distributed.Artifacts.S3) | 4.0.0-beta | Tom Longhurst | S3-compatible distributed artifact store for ModularPipelines. Supports AWS S3,… |
| 2026-11-14 13:46:09 | [ModularPipelines.Distributed.Discovery.Redis](https://www.nuget.org/packages/ModularPipelines.Distributed.Discovery.Redis) | 4.0.0-beta | Tom Longhurst | Redis-based master endpoint discovery for distributed coordinators. Enables cro… |
| 2026-11-14 13:46:12 | [ModularPipelines.Distributed.Redis](https://www.nuget.org/packages/ModularPipelines.Distributed.Redis) | 4.0.0-beta | Tom Longhurst | Redis-based distributed coordinator for ModularPipelines, built on the Respire… |
| 2026-11-14 13:46:15 | [ModularPipelines.Distributed.SignalR](https://www.nuget.org/packages/ModularPipelines.Distributed.SignalR) | 4.0.0-beta | Tom Longhurst | SignalR-based distributed coordinator for ModularPipelines. Enables multi-proce… |
| 2026-11-14 13:46:23 | [ModularPipelines.Eksctl](https://www.nuget.org/packages/ModularPipelines.Eksctl) | 4.0.0 | Tom Longhurst | Helpers for interacting with eksctl Amazon EKS cluster management CLI. |
| 2026-11-14 13:46:28 | [ModularPipelines.Flux](https://www.nuget.org/packages/ModularPipelines.Flux) | 4.0.0 | Tom Longhurst | Helpers for interacting with Flux GitOps toolkit for Kubernetes CLI. |
| 2026-11-14 13:46:31 | [ModularPipelines.Flyway](https://www.nuget.org/packages/ModularPipelines.Flyway) | 4.0.0 | Tom Longhurst | Helpers for interacting with Flyway database migration tool CLI. |
| 2026-11-14 13:46:42 | [ModularPipelines.Go](https://www.nuget.org/packages/ModularPipelines.Go) | 4.0.0 | Tom Longhurst | Helpers for interacting with Go CLI. |
| 2026-11-14 13:46:48 | [ModularPipelines.Grype](https://www.nuget.org/packages/ModularPipelines.Grype) | 4.0.0 | Tom Longhurst | Helpers for interacting with Grype CLI for vulnerability scanning. |
| 2026-11-14 13:46:51 | [ModularPipelines.Hadolint](https://www.nuget.org/packages/ModularPipelines.Hadolint) | 4.0.0 | Tom Longhurst | Helpers for interacting with Hadolint Dockerfile linter CLI. |
| 2026-11-14 13:46:56 | [ModularPipelines.Homebrew](https://www.nuget.org/packages/ModularPipelines.Homebrew) | 4.0.0 | Tom Longhurst | Helpers for interacting with the Homebrew CLI. |
| 2026-11-14 13:46:59 | [ModularPipelines.Java](https://www.nuget.org/packages/ModularPipelines.Java) | 4.0.0 | Tom Longhurst | Helpers for interacting with Java build tools (Maven, Gradle). |
| 2026-11-14 13:47:01 | [ModularPipelines.Jq](https://www.nuget.org/packages/ModularPipelines.Jq) | 4.0.0 | Tom Longhurst | Helpers for interacting with jq JSON processor CLI. |
| 2026-11-14 13:47:04 | [ModularPipelines.Kind](https://www.nuget.org/packages/ModularPipelines.Kind) | 4.0.0 | Tom Longhurst | Helpers for interacting with Kind (Kubernetes IN Docker) CLI. |
| 2026-11-14 13:47:09 | [ModularPipelines.Liquibase](https://www.nuget.org/packages/ModularPipelines.Liquibase) | 4.0.0 | Tom Longhurst | Helpers for interacting with Liquibase database change management CLI. |
| 2026-11-14 13:47:14 | [ModularPipelines.Minikube](https://www.nuget.org/packages/ModularPipelines.Minikube) | 4.0.0 | Tom Longhurst | Helpers for interacting with Minikube CLI for local Kubernetes clusters. |
| 2026-11-14 13:47:17 | [ModularPipelines.NerdbankGitVersioning](https://www.nuget.org/packages/ModularPipelines.NerdbankGitVersioning) | 4.0.0 | Tom Longhurst | Helpers for interacting with the Nerdbank.GitVersioning nbgv CLI. |
| 2026-11-14 13:47:19 | [ModularPipelines.Newman](https://www.nuget.org/packages/ModularPipelines.Newman) | 4.0.0 | Tom Longhurst | Helpers for interacting with Newman Postman collection runner CLI. |
| 2026-11-14 13:47:25 | [ModularPipelines.OpenTelemetry](https://www.nuget.org/packages/ModularPipelines.OpenTelemetry) | 4.0.0 | Tom Longhurst | OpenTelemetry tracing, metrics, and OTLP export for Modular Pipelines. |
| 2026-11-14 13:47:27 | [ModularPipelines.Packer](https://www.nuget.org/packages/ModularPipelines.Packer) | 4.0.0 | Tom Longhurst | Helpers for interacting with HashiCorp Packer machine image builder CLI. |
| 2026-11-14 13:47:31 | [ModularPipelines.Podman](https://www.nuget.org/packages/ModularPipelines.Podman) | 4.0.0 | Tom Longhurst | Helpers for interacting with Podman daemonless container engine CLI. |
| 2026-11-14 13:47:33 | [ModularPipelines.Pulumi](https://www.nuget.org/packages/ModularPipelines.Pulumi) | 4.0.0 | Tom Longhurst | Helpers for interacting with Pulumi Infrastructure as Code CLI. |
| 2026-11-14 13:47:36 | [ModularPipelines.Python](https://www.nuget.org/packages/ModularPipelines.Python) | 4.0.0 | Tom Longhurst | Helpers for interacting with Python tooling (pip, etc.). |
| 2026-11-14 13:47:38 | [ModularPipelines.Rust](https://www.nuget.org/packages/ModularPipelines.Rust) | 4.0.0 | Tom Longhurst | Helpers for interacting with Cargo (Rust package manager) CLI. |
| 2026-11-14 13:47:41 | [ModularPipelines.Shellcheck](https://www.nuget.org/packages/ModularPipelines.Shellcheck) | 4.0.0 | Tom Longhurst | Helpers for interacting with ShellCheck shell script static analysis CLI. |
| 2026-11-14 13:47:44 | [ModularPipelines.Skopeo](https://www.nuget.org/packages/ModularPipelines.Skopeo) | 4.0.0 | Tom Longhurst | Helpers for interacting with Skopeo container image operations CLI. |
| 2026-11-14 13:47:49 | [ModularPipelines.Snyk](https://www.nuget.org/packages/ModularPipelines.Snyk) | 4.0.0 | Tom Longhurst | Helpers for interacting with Snyk security CLI. |
| 2026-11-14 13:47:51 | [ModularPipelines.SonarScanner](https://www.nuget.org/packages/ModularPipelines.SonarScanner) | 4.0.0 | Tom Longhurst | Helpers for interacting with SonarScanner CLI for SonarQube and SonarCloud. |
| 2026-11-14 13:47:54 | [ModularPipelines.Syft](https://www.nuget.org/packages/ModularPipelines.Syft) | 4.0.0 | Tom Longhurst | Helpers for interacting with Syft CLI for SBOM (Software Bill of Materials) gen… |
| 2026-11-14 13:47:59 | [ModularPipelines.Templates](https://www.nuget.org/packages/ModularPipelines.Templates) | 4.0.0 | Tom Longhurst | Templates for creating realistic ModularPipelines build, test, and publish pipe… |
| 2026-11-14 13:48:03 | [ModularPipelines.Testing](https://www.nuget.org/packages/ModularPipelines.Testing) | 4.0.0 | Tom Longhurst | Supported test harness for isolated ModularPipelines module tests. |
| 2026-11-14 13:48:06 | [ModularPipelines.Trivy](https://www.nuget.org/packages/ModularPipelines.Trivy) | 4.0.0 | Tom Longhurst | Helpers for interacting with Trivy security scanner CLI. |
| 2026-11-14 13:48:08 | [ModularPipelines.Vault](https://www.nuget.org/packages/ModularPipelines.Vault) | 4.0.0 | Tom Longhurst | Helpers for interacting with HashiCorp Vault secrets management CLI. |
| 2026-11-14 13:48:16 | [ModularPipelines.Yq](https://www.nuget.org/packages/ModularPipelines.Yq) | 4.0.0 | Tom Longhurst | Helpers for interacting with yq YAML/JSON/XML processor CLI. |
| 2026-11-14 13:55:17 | [Dwain.TextProgressbar](https://www.nuget.org/packages/Dwain.TextProgressbar) | 1.0.0 | Dwain Snickles | Custom WinForms ProgressBar control with three-color gradient rendering, config… |
| 2026-11-14 14:00:32 | [Egortech.GitLabSourceLink](https://www.nuget.org/packages/Egortech.GitLabSourceLink) | 0.2.0 | Egortech | Generates Source Link mappings that use the GitLab REST API, so that private re… |
| 2026-11-14 14:04:00 | [HoneyDrunk.AI.Providers.Anthropic](https://www.nuget.org/packages/HoneyDrunk.AI.Providers.Anthropic) | 0.3.0 | HoneyDrunk Studios | HoneyDrunk.AI Anthropic chat provider over the official Anthropic SDK. |
| 2026-11-14 14:05:45 | [Super](https://www.nuget.org/packages/Super) | 1.0.0 | Christoffer Artmann | A C# game engine you use as a library, with a 3D Vulkan renderer built in. Made… |
| 2026-11-14 14:08:00 | [Moonwell.AI](https://www.nuget.org/packages/Moonwell.AI) | 0.16.0 | mdlsvensson | Brains for Moonwell maps: components that think on a shared loop, and blackboar… |
| 2026-11-14 14:08:01 | [Moonwell.AI.Combat](https://www.nuget.org/packages/Moonwell.AI.Combat) | 0.16.0 | mdlsvensson | Combat for Moonwell maps' brains, on Moonwell.AI: a lane walker that walks a ro… |
| 2026-11-14 14:08:02 | [Moonwell.Simulation](https://www.nuget.org/packages/Moonwell.Simulation) | 0.16.0 | mdlsvensson | Fake Warcraft III world for running a map's code in .NET, faster than real time… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
