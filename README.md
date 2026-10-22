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

## Latest list — 2026-10-22 12:22 UTC

New packages created between 2026-10-22 11:20 UTC and 2026-10-22 12:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T12-22-15-928721Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 11:25:16 | [Wisdom.Markdown](https://www.nuget.org/packages/Wisdom.Markdown) | 1.0.0 | Wisdom | 自研 Markdown 解析与渲染，接入统一文档模型。Self-contained Markdown parser and renderer bridged… |
| 2026-10-22 11:26:55 | [Wisdom.Ppt](https://www.nuget.org/packages/Wisdom.Ppt) | 1.0.0 | Wisdom | 自研 PPTX 演示文稿读写。Self-contained PPTX presentation reader and writer. |
| 2026-10-22 11:27:07 | [PasswordHasher.Abstractions](https://www.nuget.org/packages/PasswordHasher.Abstractions) | 0.1.0 | S.T.A.R.T.S.E.V. | Core interfaces and result types for the PasswordHasher library. |
| 2026-10-22 11:28:31 | [OxyKit.Render.Client](https://www.nuget.org/packages/OxyKit.Render.Client) | 0.1.0 | OxyKit.Render | Typed HttpClient SDK for OxyKit.Render Local and Cloud APIs. |
| 2026-10-22 11:28:32 | [OxyKit.Render.Contracts](https://www.nuget.org/packages/OxyKit.Render.Contracts) | 0.1.0 | OxyKit.Render | Shared request/response contracts for OxyKit.Render Local and Cloud. |
| 2026-10-22 11:28:58 | [OxyKit.Mail.Client](https://www.nuget.org/packages/OxyKit.Mail.Client) | 0.1.0 | OxyKit.Mail | Typed HttpClient SDK for OxyKit.Mail send (API key / Bearer). Not a dashboard c… |
| 2026-10-22 11:28:58 | [OxyKit.Mail.Contracts](https://www.nuget.org/packages/OxyKit.Mail.Contracts) | 0.1.0 | OxyKit.Mail | Shared send request/response contracts for OxyKit.Mail (API key / integrator su… |
| 2026-10-22 11:36:53 | [Dut00.AppInfo](https://www.nuget.org/packages/Dut00.AppInfo) | 1.0.0 | Kuba | Adds an /appinfo endpoint to ASP.NET Core applications that returns JSON descri… |
| 2026-10-22 11:36:54 | [Dut00.AppInfo.Build](https://www.nuget.org/packages/Dut00.AppInfo.Build) | 1.0.0 | Kuba | Extends the Dut00.AppInfo /appinfo endpoint with build details: informational v… |
| 2026-10-22 11:36:55 | [Dut00.AppInfo.Configuration](https://www.nuget.org/packages/Dut00.AppInfo.Configuration) | 1.0.0 | Kuba | Extends the Dut00.AppInfo /appinfo endpoint with the list of configuration file… |
| 2026-10-22 11:36:56 | [Dut00.AppInfo.ConnectionStrings](https://www.nuget.org/packages/Dut00.AppInfo.ConnectionStrings) | 1.0.0 | Kuba | Extends the Dut00.AppInfo /appinfo endpoint with the application's connection s… |
| 2026-10-22 11:36:57 | [Dut00.AppInfo.Container](https://www.nuget.org/packages/Dut00.AppInfo.Container) | 1.0.0 | Kuba | Extends the Dut00.AppInfo /appinfo endpoint with container and Kubernetes detai… |
| 2026-10-22 11:36:57 | [Dut00.AppInfo.Environment](https://www.nuget.org/packages/Dut00.AppInfo.Environment) | 1.0.0 | Kuba | Extends the Dut00.AppInfo /appinfo endpoint with process details (ID, start tim… |
| 2026-10-22 11:36:58 | [Dut00.AppInfo.Runtime](https://www.nuget.org/packages/Dut00.AppInfo.Runtime) | 1.0.0 | Kuba | Extends the Dut00.AppInfo /appinfo endpoint with the .NET runtime, runtime iden… |
| 2026-10-22 11:36:59 | [Dut00.AppInfo.Server](https://www.nuget.org/packages/Dut00.AppInfo.Server) | 1.0.0 | Kuba | Extends the Dut00.AppInfo /appinfo endpoint with the addresses the server liste… |
| 2026-10-22 11:41:17 | [DmiLib.001](https://www.nuget.org/packages/DmiLib.001) | 1.0.0 | Bam4000 | Package Description |
| 2026-10-22 11:52:56 | [Moongate.Hosting](https://www.nuget.org/packages/Moongate.Hosting) | 0.20.0 | Squid Development | Generic host layer for Moongate applications: startup services, event bus, plug… |
| 2026-10-22 11:55:33 | [TstackApimaticSDK](https://www.nuget.org/packages/TstackApimaticSDK) | 0.0.1 | Muhammad Rafay | Sample SDKs for Tstack by APIMatic |
| 2026-10-22 12:00:55 | [AppWeaver.Core](https://www.nuget.org/packages/AppWeaver.Core) | 1.0.0 | Team AppWeaver | Core abstractions and services for building component-based applications in the… |
| 2026-10-22 12:01:01 | [BlackSharp.Platform.Startup](https://www.nuget.org/packages/BlackSharp.Platform.Startup) | 1.2.4 | BlackSharp.Platform.Startup | Cross-platform startup services for applications. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
