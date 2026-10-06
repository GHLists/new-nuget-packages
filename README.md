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

## Latest list — 2026-10-06 14:21 UTC

New packages created between 2026-10-06 13:22 UTC and 2026-10-06 14:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-06T14-21-21-637126Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-06 13:22:43 | [OnnxRuntimeSharp](https://www.nuget.org/packages/OnnxRuntimeSharp) | 0.1.0 | nietras | Low-level ONNX Runtime C API interop in modern C#. Cross-platform, trimmable an… |
| 2026-10-06 13:29:15 | [Corner49.CosmosDB](https://www.nuget.org/packages/Corner49.CosmosDB) | 10.0.142 | Corner49.CosmosDB | Package Description |
| 2026-10-06 13:29:23 | [Corner49.ServiceBus](https://www.nuget.org/packages/Corner49.ServiceBus) | 10.0.142 | Corner49.ServiceBus | Package Description |
| 2026-10-06 13:30:51 | [Kurrent.Pulumi.KurrentCloud](https://www.nuget.org/packages/Kurrent.Pulumi.KurrentCloud) | 0.3.1 | Kurrent | A Pulumi package for creating and managing Kurrent Cloud resources. |
| 2026-10-06 13:35:47 | [RG3.ClosedXML](https://www.nuget.org/packages/RG3.ClosedXML) | 10.1.1 | rg@rg1008.com | 1、基于 ClosedXML 二次调整依赖包，把包名从 ClosedXML改成RG3.ClosedXML 2、excel处理，基于.netcore 10 |
| 2026-10-06 13:36:58 | [AnsiSharp](https://www.nuget.org/packages/AnsiSharp) | 0.1.0 | AnsiSharp Contributors | A cross-platform ANSI terminal library for .NET providing colors, styles, curso… |
| 2026-10-06 13:38:11 | [OmniEurope.Performance](https://www.nuget.org/packages/OmniEurope.Performance) | 0.1.0 | OmniEurope contributors | A minimal, unstyled ASP.NET Core page that measures the request performance of… |
| 2026-10-06 13:41:43 | [E2E](https://www.nuget.org/packages/E2E) | 0.1.2 | hardkoded | Community .NET port of the e2e agentic testing framework. Describe a goal, driv… |
| 2026-10-06 13:41:44 | [E2E.Cli](https://www.nuget.org/packages/E2E.Cli) | 0.1.2 | hardkoded | The e2e command for the E2E .NET port: sign in to a model subscription (ChatGPT… |
| 2026-10-06 13:41:45 | [E2E.NUnit](https://www.nuget.org/packages/E2E.NUnit) | 0.1.2 | hardkoded | NUnit fixture for the E2E .NET port. Each test gets an engine session, and the… |
| 2026-10-06 13:46:28 | [CodeMaster.XshlFramework.Foundation](https://www.nuget.org/packages/CodeMaster.XshlFramework.Foundation) | 1.0.0 | CodeMaster | CodeMaster Ref |
| 2026-10-06 14:14:32 | [NetArcaWs](https://www.nuget.org/packages/NetArcaWs) | 0.5.0 | NetArcaWs .NET contributors | Native .NET 10 multitenant ARCA clients, WSAA, complete typed SOAP contracts, d… |
| 2026-10-06 14:14:34 | [NetArcaWs.Tool](https://www.nuget.org/packages/NetArcaWs.Tool) | 0.5.0 | NetArcaWs .NET contributors | CLI para generar solicitudes locales de certificados ARCA y consultar certifica… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
