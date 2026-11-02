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

## Latest list — 2026-11-02 12:21 UTC

New packages created between 2026-11-02 11:20 UTC and 2026-11-02 12:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T12-21-48-399629Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-02 11:35:16 | [DubUrl.Authentication.Snowflake](https://www.nuget.org/packages/DubUrl.Authentication.Snowflake) | 0.56.0 | Cédric L. Charlier | Snowflake native authorization-code/PKCE sessions for DubUrl. |
| 2026-11-02 11:35:17 | [DubUrl.Authentication.SqlServer](https://www.nuget.org/packages/DubUrl.Authentication.SqlServer) | 0.56.0 | Cédric L. Charlier | Native SqlClient token authentication and optional Microsoft Entra adapters for… |
| 2026-11-02 11:35:41 | [DubUrl.ProviderTesting](https://www.nuget.org/packages/DubUrl.ProviderTesting) | 0.56.0 | Cédric L. Charlier | Reusable live provider QA contracts for DubUrl provider modules. |
| 2026-11-02 11:38:29 | [PackageTerms](https://www.nuget.org/packages/PackageTerms) | 0.1.1 | Paul Thomas | Finds NuGet dependencies whose terms changed: packages that went commercial or… |
| 2026-11-02 11:40:26 | [Pug.Sqetch.Deployment.Cli](https://www.nuget.org/packages/Pug.Sqetch.Deployment.Cli) | 0.1.0 | Pug | Sqetch deploy: bundle Sqetch projects and deploy the bundles to a database thro… |
| 2026-11-02 11:47:59 | [Lspiguel.Xrm.D365AgentCompanionMcp](https://www.nuget.org/packages/Lspiguel.Xrm.D365AgentCompanionMcp) | 1.2026.10.1 | Luciano Spiguel | XrmToolBox plugin that exposes a local Model Context Protocol (MCP) endpoint ov… |
| 2026-11-02 12:00:41 | [Skymly.DotNetMcp](https://www.nuget.org/packages/Skymly.DotNetMcp) | 5.0.0 | Skymly | MCP server for .NET symbol analysis, XAML, source-generator attribution, and re… |
| 2026-11-02 12:01:42 | [Tai.FileManagement.Provider.FileSystem](https://www.nuget.org/packages/Tai.FileManagement.Provider.FileSystem) | 0.0.1 | Tai | Reusable ABP business attachment and file lifecycle management |
| 2026-11-02 12:01:43 | [Tai.FileManagement.Application.Contracts](https://www.nuget.org/packages/Tai.FileManagement.Application.Contracts) | 0.0.1 | Tai | Reusable ABP business attachment and file lifecycle management |
| 2026-11-02 12:01:44 | [Tai.FileManagement.Domain.Shared](https://www.nuget.org/packages/Tai.FileManagement.Domain.Shared) | 0.0.1 | Tai | Reusable ABP business attachment and file lifecycle management |
| 2026-11-02 12:01:44 | [Tai.FileManagement.Domain](https://www.nuget.org/packages/Tai.FileManagement.Domain) | 0.0.1 | Tai | Reusable ABP business attachment and file lifecycle management |
| 2026-11-02 12:01:45 | [Tai.FileManagement.HttpApi.Client](https://www.nuget.org/packages/Tai.FileManagement.HttpApi.Client) | 0.0.1 | Tai | Reusable ABP business attachment and file lifecycle management |
| 2026-11-02 12:01:46 | [Tai.FileManagement.EntityFrameworkCore](https://www.nuget.org/packages/Tai.FileManagement.EntityFrameworkCore) | 0.0.1 | Tai | Reusable ABP business attachment and file lifecycle management |
| 2026-11-02 12:01:46 | [Tai.FileManagement.HttpApi](https://www.nuget.org/packages/Tai.FileManagement.HttpApi) | 0.0.1 | Tai | Reusable ABP business attachment and file lifecycle management |
| 2026-11-02 12:01:47 | [Tai.FileManagement.Application](https://www.nuget.org/packages/Tai.FileManagement.Application) | 0.0.1 | Tai | Reusable ABP business attachment and file lifecycle management |
| 2026-11-02 12:01:48 | [Tai.FileManagement.Provider.Aliyun](https://www.nuget.org/packages/Tai.FileManagement.Provider.Aliyun) | 0.0.1 | Tai | Reusable ABP business attachment and file lifecycle management |
| 2026-11-02 12:05:26 | [Pug.Sqetch.Cli](https://www.nuget.org/packages/Pug.Sqetch.Cli) | 0.1.0 | Pug | Sqetch: author database schema changes as plans and group them into releases. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
