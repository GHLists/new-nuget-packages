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

## Latest list — 2026-11-22 19:19 UTC

New packages created between 2026-11-22 18:19 UTC and 2026-11-22 19:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T19-19-27-813806Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 18:21:44 | [AIKernel.Providers.Cosmos](https://www.nuget.org/packages/AIKernel.Providers.Cosmos) | 0.1.4 | Takuya Sogawa | Optional, authenticated scene observation jobs and NVIDIA Cosmos Reasoner trans… |
| 2026-11-22 18:22:08 | [AIKernel.Providers.Distributed](https://www.nuget.org/packages/AIKernel.Providers.Distributed) | 0.1.4 | Takuya Sogawa | Authenticated HTTP and MCP application hosting and multi-server connections for… |
| 2026-11-22 18:34:26 | [Fuaran.MVU](https://www.nuget.org/packages/Fuaran.MVU) | 0.1.0 | Andrew J. Willshire | Fuaran.MVU: a model-update-view runtime whose components are pure, whose effect… |
| 2026-11-22 18:34:27 | [Fuaran.MVU.Browser](https://www.nuget.org/packages/Fuaran.MVU.Browser) | 0.1.0 | Andrew J. Willshire | Fuaran.MVU.Browser: the standard client kinds for Fuaran.MVU in the browser. Th… |
| 2026-11-22 18:34:27 | [Fuaran.MVU.Kernel](https://www.nuget.org/packages/Fuaran.MVU.Kernel) | 0.1.0 | Andrew J. Willshire | Fuaran.MVU.Kernel: the proved core of the Fuaran.MVU model-update-view runtime.… |
| 2026-11-22 18:34:28 | [Fuaran.MVU.React](https://www.nuget.org/packages/Fuaran.MVU.React) | 0.1.0 | Andrew J. Willshire | Fuaran.MVU.React: mounts a Fuaran.MVU component in React. A model store React r… |
| 2026-11-22 18:34:28 | [Fuaran.MVU.Session](https://www.nuget.org/packages/Fuaran.MVU.Session) | 0.1.0 | Andrew J. Willshire | Fuaran.MVU.Session: an optional session log for the Fuaran.MVU runtime. Each de… |
| 2026-11-22 18:34:29 | [Fuaran.MVU.Testing](https://www.nuget.org/packages/Fuaran.MVU.Testing) | 0.1.0 | Andrew J. Willshire | Fuaran.MVU.Testing: the test harness for Fuaran.MVU components — a runtime over… |
| 2026-11-22 18:36:35 | [Confeature.OpenFeature](https://www.nuget.org/packages/Confeature.OpenFeature) | 0.1.0 | MakerLabs | OpenFeature provider for the Confeature .NET SDK. |
| 2026-11-22 18:50:09 | [fakedatacli](https://www.nuget.org/packages/fakedatacli) | 1.0.0 | Leandro Alves | Gerador de dados fakes brasileiros com Bogus (locale pt_BR). CLI embalada como… |
| 2026-11-22 19:05:31 | [wpf-locator-doctor-mcp](https://www.nuget.org/packages/wpf-locator-doctor-mcp) | 0.2.0 | swechhap | MCP server for WPF testability: lets AI assistants (Claude Code, GitHub Copilot… |
| 2026-11-22 19:05:32 | [wpf-locator-doctor](https://www.nuget.org/packages/wpf-locator-doctor) | 0.2.0 | swechhap | Testability scorecard for WPF apps: checks the AutomationIds your UI tests depe… |
| 2026-11-22 19:11:20 | [OpenPEData](https://www.nuget.org/packages/OpenPEData) | 0.0.1 | factorybyte64 | Open reader for TIA Portal project files without TIA Portal: opens project fold… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
