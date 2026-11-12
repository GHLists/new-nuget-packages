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

## Latest list — 2026-11-12 14:20 UTC

New packages created between 2026-11-12 13:21 UTC and 2026-11-12 14:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-12T14-20-49-223344Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-12 13:22:16 | [AppWeaver.Spec.Foundation.DotNet.VerticalSlice](https://www.nuget.org/packages/AppWeaver.Spec.Foundation.DotNet.VerticalSlice) | 1.0.0 | Bytestrone India Private Limi… | AppWeaver foundation pack: Vertical Slice (CQRS / Fast Endpoints) (dotnet-webap… |
| 2026-11-12 13:27:49 | [WinUia.Recording](https://www.nuget.org/packages/WinUia.Recording) | 0.3.1 | Buning Software | Record the screen while a Windows UI test runs, using ffmpeg. Optional companio… |
| 2026-11-12 13:32:24 | [HoneyDrunk.Memory.Providers.Data](https://www.nuget.org/packages/HoneyDrunk.Memory.Providers.Data) | 0.2.0 | HoneyDrunk Studios | Durable HoneyDrunk agent-memory store over HoneyDrunk.Data's Entity Framework l… |
| 2026-11-12 13:40:35 | [Prahelika.Calculators](https://www.nuget.org/packages/Prahelika.Calculators) | 0.0.1-alpha | Prahelika Dutta (PD) | A calculator library for .NET with basic, scientific and finance calculators. |
| 2026-11-12 13:45:28 | [Google.Apis.MyBusinessBusinessInformation.v1alpha](https://www.nuget.org/packages/Google.Apis.MyBusinessBusinessInformation.v1alpha) | 1.78.0.4329 | Google LLC | Google APIs Client Library for working with Mybusinessbusinessinformation v1alp… |
| 2026-11-12 13:52:55 | [Snail.MCP.Playwright](https://www.nuget.org/packages/Snail.MCP.Playwright) | 0.1.0 | orldev | MCP server that lets AI agents search the web and read pages through a real bro… |
| 2026-11-12 13:55:42 | [UnambitiousFx.Synapse.Authorization](https://www.nuget.org/packages/UnambitiousFx.Synapse.Authorization) | 2.9.0 | UnambitiousFx | Authorization for UnambitiousFx.Synapse: actor, role, scope and resource behavi… |
| 2026-11-12 13:59:38 | [Ekom.U19](https://www.nuget.org/packages/Ekom.U19) | 1.1.0 | Vettvangur | Ekom - E-Commerce solution for Umbraco 19+ |
| 2026-11-12 13:59:45 | [Ekom.Web.U19](https://www.nuget.org/packages/Ekom.Web.U19) | 1.1.0 | Vettvangur | Ekom Web assets for Umbraco 19. |
| 2026-11-12 14:08:14 | [Tesserae.A2UI](https://www.nuget.org/packages/Tesserae.A2UI) | 26.11.7978 | Curiosity GmbH | Tesserae.A2UI renders A2UI (Agent-to-User Interface) v1.0 messages as a live Te… |
| 2026-11-12 14:14:02 | [VisioForge.CrossPlatform.OpenCV.Linux.arm64](https://www.nuget.org/packages/VisioForge.CrossPlatform.OpenCV.Linux.arm64) | 2026.11.12.2 | VisioForge | OpenCV computer vision libraries package for VisioForge .NET SDKs. Enables adva… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
