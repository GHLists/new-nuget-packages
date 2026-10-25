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

## Latest list — 2026-10-25 13:21 UTC

New packages created between 2026-10-25 12:19 UTC and 2026-10-25 13:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-25T13-21-00-224197Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-25 12:19:51 | [sxsi.osx-x64](https://www.nuget.org/packages/sxsi.osx-x64) | 2.0.0 | Alexandre Mutel | CodeAlta Desktop: a desktop workspace for agentic AI coding on your local proje… |
| 2026-10-25 12:19:54 | [sxsi.win-arm64](https://www.nuget.org/packages/sxsi.win-arm64) | 2.0.0 | Alexandre Mutel | CodeAlta Desktop: a desktop workspace for agentic AI coding on your local proje… |
| 2026-10-25 12:22:50 | [NetEvolve.HealthPublishers.Slack](https://www.nuget.org/packages/NetEvolve.HealthPublishers.Slack) | 1.15.41 | NetEvolve, samtrion | Contains an IHealthCheckPublisher implementation that pushes health report resu… |
| 2026-10-25 12:22:52 | [NetEvolve.HealthPublishers.Webhook](https://www.nuget.org/packages/NetEvolve.HealthPublishers.Webhook) | 1.15.41 | NetEvolve, samtrion | Contains an IHealthCheckPublisher implementation that pushes health report resu… |
| 2026-10-25 12:32:58 | [BozForge.Bogus.Turkiye](https://www.nuget.org/packages/BozForge.Bogus.Turkiye) | 0.1.0 | Hüseyin Bozdemir | Türkiye'ye özgü test verisi için Bogus eklentisi: kontrol haneleri tutan TCKN v… |
| 2026-10-25 12:39:52 | [HslCommunication_MIT](https://www.nuget.org/packages/HslCommunication_MIT) | 1.0.0 | HslCommunication | HslCommunication MIT开源版, API兼容对齐V12.8, PLC采集通信库，支持: Modbus，Siemens，Mitsubishi，O… |
| 2026-10-25 12:42:15 | [HeimdallFramework.Templates](https://www.nuget.org/packages/HeimdallFramework.Templates) | 4.0.0 | Bradley Ables | Heimdall ASP.NET Core templates for hosted rendering integrations and static si… |
| 2026-10-25 12:44:08 | [Logdash](https://www.nuget.org/packages/Logdash) | 0.1.0 | JakubK | Simple .NET Client for Logdash |
| 2026-10-25 12:53:19 | [Roslyn_IngeniousCommon](https://www.nuget.org/packages/Roslyn_IngeniousCommon) | 1.0.0 | Yuji Kanda | CSharp_IngeniousAnalyzer と XUnit_IngeniousGenerator が共有する Roslyn の共通部品（ソースのパッケー… |
| 2026-10-25 12:55:25 | [RepoLore.Cli](https://www.nuget.org/packages/RepoLore.Cli) | 1.0.0 | Elias Aliche | RepoLore: local, offline operational memory for developers and coding agents, s… |
| 2026-10-25 12:57:38 | [Novolis.Blazor.Components](https://www.nuget.org/packages/Novolis.Blazor.Components) | 2026.1.1.9 | Novolis | Graphical Profile chrome components for Blazor hosts: shell, cards, dialogs, li… |
| 2026-10-25 12:57:40 | [NSail.Messaging.Queue](https://www.nuget.org/packages/NSail.Messaging.Queue) | 0.1.351 | Leonardo Porro,Emmanuel Arias | NSail.Messaging.Queue, part of NSail Stack: a .NET modular-monolith framework (… |
| 2026-10-25 12:58:21 | [EnvironmentCopySnapshotRestore](https://www.nuget.org/packages/EnvironmentCopySnapshotRestore) | 1.2026.10.1 | Saad ZAGHLOUL | Before copying production over a sandbox, snapshot what is specific to the sand… |
| 2026-10-25 13:05:58 | [Themis.Inference.MIGraphX](https://www.nuget.org/packages/Themis.Inference.MIGraphX) | 2.0.1 | Themis contributors | Optional AMD MIGraphX plugin execution-provider integration for Themis ONNX inf… |
| 2026-10-25 13:06:41 | [BarakoCMS.Services](https://www.nuget.org/packages/BarakoCMS.Services) | 5.3.0 | Arnel Robles | Registry of outside services for barakoCMS: register a service, take its heartb… |
| 2026-10-25 13:06:49 | [BarakoCMS.Tagging](https://www.nuget.org/packages/BarakoCMS.Tagging) | 5.3.0 | Arnel Robles | Tagging and taxonomy for barakoCMS: vocabularies, terms that can nest, and term… |
| 2026-10-25 13:10:20 | [SjolystInnovation.AppKit.VatThreshold](https://www.nuget.org/packages/SjolystInnovation.AppKit.VatThreshold) | 1.0.0 | Sjølyst Innovation AS | The Norwegian VAT registration threshold of 50 000 kroner in any period of twel… |
| 2026-10-25 13:13:20 | [SarifKit](https://www.nuget.org/packages/SarifKit) | 1.0.0 | Winner-Timothy Bolorunduro | Zero-dependency, Native-AOT-ready reader/writer for SARIF 2.1.0. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
