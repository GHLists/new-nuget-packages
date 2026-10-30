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

## Latest list — 2026-10-30 23:20 UTC

New packages created between 2026-10-30 22:21 UTC and 2026-10-30 23:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-30T23-20-24-209806Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 22:30:04 | [Doconut.NET6.Signer](https://www.nuget.org/packages/Doconut.NET6.Signer) | 26.10.0 | Smallize | Digital signature plugin for Doconut.NET6 (sign PDF and Word documents, with ce… |
| 2026-10-30 22:31:01 | [Doconut.NET8.Signer](https://www.nuget.org/packages/Doconut.NET8.Signer) | 26.10.0 | Smallize | Digital signature plugin for Doconut.NET8 (sign PDF and Word documents, with ce… |
| 2026-10-30 22:31:48 | [Doconut.NETStandard.Signer](https://www.nuget.org/packages/Doconut.NETStandard.Signer) | 26.10.0 | Smallize | Digital signature plugin for Doconut.NETStandard (sign PDF and Word documents,… |
| 2026-10-30 22:32:38 | [Doconut.NETFramework.Signer](https://www.nuget.org/packages/Doconut.NETFramework.Signer) | 26.10.0 | Smallize | Digital signature plugin for Doconut.NETFramework (sign PDF and Word documents,… |
| 2026-10-30 22:33:55 | [WebMarket.DbProvider](https://www.nuget.org/packages/WebMarket.DbProvider) | 0.1.0 | Tarveiz | Access to the shared WebMarket PostgreSQL database via EF Core and Dapper |
| 2026-10-30 22:47:07 | [mrhamburg.SecretsManager](https://www.nuget.org/packages/mrhamburg.SecretsManager) | 0.0.1 | mrhamburg | Core abstraction library for unified secret management across multiple providers |
| 2026-10-30 22:47:08 | [mrhamburg.SecretsManager.AliyunKms](https://www.nuget.org/packages/mrhamburg.SecretsManager.AliyunKms) | 0.0.1 | mrhamburg | Aliyun KMS secret provider for SecretsManager |
| 2026-10-30 22:47:08 | [mrhamburg.SecretsManager.AwsSecretsManager](https://www.nuget.org/packages/mrhamburg.SecretsManager.AwsSecretsManager) | 0.0.1 | mrhamburg | AWS Secrets Manager provider for SecretsManager |
| 2026-10-30 22:47:09 | [mrhamburg.SecretsManager.AzureKeyVault](https://www.nuget.org/packages/mrhamburg.SecretsManager.AzureKeyVault) | 0.0.1 | mrhamburg | Azure Key Vault secret provider for SecretsManager |
| 2026-10-30 22:47:10 | [mrhamburg.SecretsManager.Conjur](https://www.nuget.org/packages/mrhamburg.SecretsManager.Conjur) | 0.0.1 | mrhamburg | CyberArk Conjur secret provider for SecretsManager |
| 2026-10-30 22:47:10 | [mrhamburg.SecretsManager.FileSystem](https://www.nuget.org/packages/mrhamburg.SecretsManager.FileSystem) | 0.0.1 | mrhamburg | Filesystem-backed secret provider with AES-256-GCM encryption for SecretsManager |
| 2026-10-30 22:47:11 | [mrhamburg.SecretsManager.GoogleSecretManager](https://www.nuget.org/packages/mrhamburg.SecretsManager.GoogleSecretManager) | 0.0.1 | mrhamburg | Google Cloud Secret Manager provider for SecretsManager |
| 2026-10-30 22:47:12 | [mrhamburg.SecretsManager.IBMCloudSecretsManager](https://www.nuget.org/packages/mrhamburg.SecretsManager.IBMCloudSecretsManager) | 0.0.1 | mrhamburg | IBM Cloud Secrets Manager provider for SecretsManager |
| 2026-10-30 22:47:13 | [mrhamburg.SecretsManager.Infisical](https://www.nuget.org/packages/mrhamburg.SecretsManager.Infisical) | 0.0.1 | mrhamburg | Infisical secret provider for SecretsManager |
| 2026-10-30 22:47:13 | [mrhamburg.SecretsManager.OVH](https://www.nuget.org/packages/mrhamburg.SecretsManager.OVH) | 0.0.1 | mrhamburg | OVHcloud secret provider for SecretsManager |
| 2026-10-30 22:47:14 | [mrhamburg.SecretsManager.OracleVault](https://www.nuget.org/packages/mrhamburg.SecretsManager.OracleVault) | 0.0.1 | mrhamburg | Oracle Vault secret provider for SecretsManager |
| 2026-10-30 22:47:15 | [mrhamburg.SecretsManager.Passbolt](https://www.nuget.org/packages/mrhamburg.SecretsManager.Passbolt) | 0.0.1 | mrhamburg | Passbolt secret provider for SecretsManager |
| 2026-10-30 22:47:15 | [mrhamburg.SecretsManager.PostgreSql](https://www.nuget.org/packages/mrhamburg.SecretsManager.PostgreSql) | 0.0.1 | mrhamburg | PostgreSQL secret provider with AES-256-GCM encryption at rest for SecretsManag… |
| 2026-10-30 22:47:16 | [mrhamburg.SecretsManager.Scaleway](https://www.nuget.org/packages/mrhamburg.SecretsManager.Scaleway) | 0.0.1 | mrhamburg | Scaleway Secret Manager provider for SecretsManager |
| 2026-10-30 22:47:17 | [mrhamburg.SecretsManager.TencentCloud](https://www.nuget.org/packages/mrhamburg.SecretsManager.TencentCloud) | 0.0.1 | mrhamburg | Tencent Cloud Secret Manager provider for SecretsManager |
| 2026-10-30 22:47:17 | [mrhamburg.SecretsManager.Vault](https://www.nuget.org/packages/mrhamburg.SecretsManager.Vault) | 0.0.1 | mrhamburg | HashiCorp Vault secret provider for SecretsManager |
| 2026-10-30 22:50:17 | [CsCom](https://www.nuget.org/packages/CsCom) | 1.0.0 | Pavel Fedarovich | Generates COM interop assemblies and projects from type libraries using source-… |
| 2026-10-30 22:50:17 | [CsCom.Build](https://www.nuget.org/packages/CsCom.Build) | 1.0.0 | Pavel Fedarovich | Generates source-generated COM interop code from type libraries and interop ass… |
| 2026-10-30 22:50:18 | [CsCom.Runtime](https://www.nuget.org/packages/CsCom.Runtime) | 1.0.0 | Pavel Fedarovich | Runtime support library for the COM interop assemblies generated by CsCom using… |
| 2026-10-30 22:55:26 | [Soenneker.HuggingFace.OpenApiClientUtil](https://www.nuget.org/packages/Soenneker.HuggingFace.OpenApiClientUtil) | 11.0.5 | Jake Soenneker | A thread-safe utility for obtaining HuggingFace's OpenApiClient singleton. |
| 2026-10-30 22:56:59 | [N1co.EPay](https://www.nuget.org/packages/N1co.EPay) | 0.1.0 | n1co | Server-side SDK of the n1co ePay API for .NET: payment intents, card sessions,… |
| 2026-10-30 22:59:59 | [Lemon.Book.Shell](https://www.nuget.org/packages/Lemon.Book.Shell) | 0.1.1 | Tracy Ma | The shell of the Lemon books: an Avalonia book with page turning, narration, le… |
| 2026-10-30 23:00:01 | [Lemon.Book.Shell.Desktop](https://www.nuget.org/packages/Lemon.Book.Shell.Desktop) | 0.1.1 | Tracy Ma | The Lemon books' desktop pieces: narration players for Windows and macOS, and s… |
| 2026-10-30 23:00:04 | [Lemon.Book.Shell.Browser](https://www.nuget.org/packages/Lemon.Book.Shell.Browser) | 0.1.1 | Tracy Ma | The Lemon books' web pieces: narration through Web Audio, settings in localStor… |
| 2026-10-30 23:00:30 | [Extrode.Pare.Cli](https://www.nuget.org/packages/Extrode.Pare.Cli) | 0.6.3 | Extrode | pare: strips TypeScript type syntax to JavaScript. Framework-dependent .NET too… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
