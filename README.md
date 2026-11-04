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

## Latest list — 2026-11-04 06:18 UTC

New packages created between 2026-11-04 05:20 UTC and 2026-11-04 06:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-04T06-18-41-324344Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-04 05:36:51 | [Pydantic.OpAmp.Core.Native](https://www.nuget.org/packages/Pydantic.OpAmp.Core.Native) | 0.1.1 | Pydantic.OpAmp.Core.Native | The shared OpAMP client core for Pydantic.OpAmp.Client, compiled for each platf… |
| 2026-11-04 05:36:52 | [Pydantic.OpAmp.Client](https://www.nuget.org/packages/Pydantic.OpAmp.Client) | 0.1.1 | Pydantic.OpAmp.Client | An OpAMP client for .NET, on the shared OpAMP core (Rust, as a native library) |
| 2026-11-04 05:36:53 | [Pydantic.OpAmp.Extensions.Hosting](https://www.nuget.org/packages/Pydantic.OpAmp.Extensions.Hosting) | 0.1.1 | Pydantic.OpAmp.Extensions.Hos… | An OpenTelemetry .NET SDK set up in code (services.AddOpenTelemetry()) under an… |
| 2026-11-04 05:36:54 | [Pydantic.OpAmp.AutoInstrumentation](https://www.nuget.org/packages/Pydantic.OpAmp.AutoInstrumentation) | 0.1.1 | Pydantic.OpAmp.AutoInstrument… | A plugin for OpenTelemetry .NET automatic instrumentation: the SDK under an OpA… |
| 2026-11-04 05:46:10 | [Plot3D.Avalonia](https://www.nuget.org/packages/Plot3D.Avalonia) | 1.0.1 | Plot3D.Avalonia Contributors | A lightweight, high-performance and AOT friendly 3D plotting control for Avalon… |
| 2026-11-04 06:12:58 | [RForge.Blazor.AutoApi.Abstractions](https://www.nuget.org/packages/RForge.Blazor.AutoApi.Abstractions) | 1.0.0 | Rumhyek | Attributes and exception types for the RForge Blazor Auto API source generator.… |
| 2026-11-04 06:12:59 | [RForge.Blazor.Components](https://www.nuget.org/packages/RForge.Blazor.Components) | 1.0.0 | Rumhyek | A light weight blazor component library that makes use of Bulma.css and focuses… |
| 2026-11-04 06:12:59 | [RForge.Blazor.Events](https://www.nuget.org/packages/RForge.Blazor.Events) | 1.0.0 | Rumhyek | Typed events and reactive state for Blazor components, wherever they sit in the… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
