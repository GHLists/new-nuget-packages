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

## Latest list — 2026-11-14 04:21 UTC

New packages created between 2026-11-14 03:20 UTC and 2026-11-14 04:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-14T04-21-38-594194Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-14 03:32:45 | [Ecuafact.Sdk](https://www.nuget.org/packages/Ecuafact.Sdk) | 1.0.0 | Ecuanexus | Cliente oficial de Ecuafact para .NET: emite y consulta los seis comprobantes e… |
| 2026-11-14 03:32:57 | [Ecuafact.Sdk.Core](https://www.nuget.org/packages/Ecuafact.Sdk.Core) | 1.0.0 | Ecuanexus | Integracion con Microsoft.Extensions.DependencyInjection para Ecuafact.Sdk: Add… |
| 2026-11-14 03:42:15 | [GAMFrameWorkContracts](https://www.nuget.org/packages/GAMFrameWorkContracts) | 1.0.1.2 | WillGAM06 | Package Description |
| 2026-11-14 03:50:35 | [Lode](https://www.nuget.org/packages/Lode) | 0.3.0 | https://github.com/SimonCropp… | Alternative to Windows File Explorer. |
| 2026-11-14 03:54:55 | [Harp.SoundCard.App](https://www.nuget.org/packages/Harp.SoundCard.App) | 3.0.0 | harp-tech | App for generating, uploading and playing sounds on Harp Sound Card devices. |
| 2026-11-14 04:05:06 | [Lengko.DockingPanel.WinForm](https://www.nuget.org/packages/Lengko.DockingPanel.WinForm) | 1.0.0 | LengkoDev, Cas | Modern, high-performance, and responsive window docking suite for Windows Forms… |
| 2026-11-14 04:08:27 | [Laranet.Http](https://www.nuget.org/packages/Laranet.Http) | 0.2.1 | TheJavaZ | Optional convenience layer over HttpClient for typed, cancellation-aware API ca… |
| 2026-11-14 04:10:10 | [FluentSetup.Builder.Core](https://www.nuget.org/packages/FluentSetup.Builder.Core) | 1.2.0 | FluentSetup contributors | Build native Windows 11-style installers (a single Setup.exe) from .NET code: t… |
| 2026-11-14 04:10:11 | [FluentSetup.Cli](https://www.nuget.org/packages/FluentSetup.Cli) | 1.2.0 | FluentSetup contributors | fluentsetup: the command-line tool of FluentSetup. Builds native Windows 11-sty… |
| 2026-11-14 04:10:13 | [FluentSetup.MSBuild](https://www.nuget.org/packages/FluentSetup.MSBuild) | 1.2.0 | FluentSetup contributors | Builds a native Windows 11-style installer (Setup.exe) of your .NET app as part… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
