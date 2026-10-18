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

## Latest list — 2026-10-18 19:18 UTC

New packages created between 2026-10-18 18:19 UTC and 2026-10-18 19:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-18T19-18-45-574035Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-18 18:28:41 | [RzR.Infrastructure.DependencyResolver](https://www.nuget.org/packages/RzR.Infrastructure.DependencyResolver) | 2.0.0 | RzR | A straightforward, lightweight, minimalistic implementation of Dependency Injec… |
| 2026-10-18 18:28:49 | [RA.Utilities.Dispatcher](https://www.nuget.org/packages/RA.Utilities.Dispatcher) | 10.0.0 | Redon Alla | Provides a lightweight, source-generated mediator (dispatcher) for CQRS, includ… |
| 2026-10-18 18:35:45 | [Egami.Fonts.Substitutes](https://www.nuget.org/packages/Egami.Fonts.Substitutes) | 1.0.0 | Lars Dytterud | Open, metric-compatible substitutes for the fonts documents name most, for Egam… |
| 2026-10-18 18:57:27 | [Novolis.IO.ConnectedDevices](https://www.nuget.org/packages/Novolis.IO.ConnectedDevices) | 2026.1.1.60 | Novolis | Cross-platform HID connected-device discovery and raw input streams. |
| 2026-10-18 18:57:34 | [DotnetCronner.OpenTelemetry](https://www.nuget.org/packages/DotnetCronner.OpenTelemetry) | 0.2.0 | Malte | OpenTelemetry instrumentation for DotnetCronner: registers the scheduler's metr… |
| 2026-10-18 19:03:09 | [DesharpCore](https://www.nuget.org/packages/DesharpCore) | 1.0.0 | rsobrepena | DesharpCore - C#/VB .NET debuging utility to dump or log structured variables,… |
| 2026-10-18 19:06:01 | [FrApp42.WPF.Pwsh](https://www.nuget.org/packages/FrApp42.WPF.Pwsh) | 1.0.0 | FrApp42 | WPF control hosting a real PowerShell session through ConPTY |
| 2026-10-18 19:09:18 | [Wyrd](https://www.nuget.org/packages/Wyrd) | 0.3.0 | Amin Chouaibi | Deterministic event-driven processes for .NET: pure deciders, declarative sagas… |
| 2026-10-18 19:09:19 | [Wyrd.Tool](https://www.nuget.org/packages/Wyrd.Tool) | 0.3.0 | Amin Chouaibi | Generate AsyncAPI and Mermaid documentation from Wyrd contracts and processes. |
| 2026-10-18 19:09:20 | [Wyrd.Testing](https://www.nuget.org/packages/Wyrd.Testing) | 0.3.0 | Amin Chouaibi | Testing for Wyrd: Given/When/Then scenarios for slices and projections that rea… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
