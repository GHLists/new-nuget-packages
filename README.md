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

## Latest list — 2026-10-12 09:22 UTC

New packages created between 2026-10-12 08:19 UTC and 2026-10-12 09:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T09-22-26-103917Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 08:21:12 | [OpenLog](https://www.nuget.org/packages/OpenLog) | 1.0.0 | OpenLog Contributors | Production-ready structured logging for .NET 8+ Web APIs. Console, rolling file… |
| 2026-10-12 08:21:28 | [ediri.DockerAgent](https://www.nuget.org/packages/ediri.DockerAgent) | 0.1.1 | dirien | A Pulumi provider for Docker Agent (docker-agent): define AI agent configuratio… |
| 2026-10-12 08:39:48 | [Eternet.Build.Workspaces](https://www.nuget.org/packages/Eternet.Build.Workspaces) | 2.0.0 | Eternet | Evaluated project graphs and warm analysis workspaces shared by EAC and ETP. |
| 2026-10-12 08:39:50 | [Eternet.Build.Workspaces.Worker](https://www.nuget.org/packages/Eternet.Build.Workspaces.Worker) | 2.0.0 | Eternet | Owner-scoped workspace worker server for SDK-selected EAC and ETP hosts. |
| 2026-10-12 08:56:20 | [Notato.Aspire](https://www.nuget.org/packages/Notato.Aspire) | 0.2.0 | Notato contributors | Notato in a .NET Aspire app host. AddNotato() runs the Notato board, the server… |
| 2026-10-12 08:58:29 | [AppDeployHub.Forge.PcAgent](https://www.nuget.org/packages/AppDeployHub.Forge.PcAgent) | 1.1.0 | Cezar Wagenheimer | AppDeployHub Forge PC Agent (Windows): installs and runs Android builds from th… |
| 2026-10-12 09:00:20 | [NepalPayments.FonePay](https://www.nuget.org/packages/NepalPayments.FonePay) | 0.1.0 | Siraj Oli | Unofficial .NET client for the Fonepay Checkout intent API: bank list, intent Q… |
| 2026-10-12 09:06:11 | [AutoUpdater.Net](https://www.nuget.org/packages/AutoUpdater.Net) | 1.0.0 | EL01 | A .NET library developed and maintained by EL01. |
| 2026-10-12 09:13:39 | [CymruBlazor.Testing](https://www.nuget.org/packages/CymruBlazor.Testing) | 1.13.0 | CymruBlazor Contributors | bUnit helpers for testing apps built with CymruBlazor: a test context with the… |
| 2026-10-12 09:13:40 | [CymruBlazor.Testing.Axe](https://www.nuget.org/packages/CymruBlazor.Testing.Axe) | 1.13.0 | CymruBlazor Contributors | Browser accessibility tests for apps built with CymruBlazor: renders a componen… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
