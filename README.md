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

## Latest list — 2026-09-30 13:20 UTC

New packages created between 2026-09-30 12:22 UTC and 2026-09-30 13:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-30T13-20-25-610389Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-30 12:24:53 | [VestaProtocol.Core](https://www.nuget.org/packages/VestaProtocol.Core) | 0.1.3 | Jesper Andersson | Shared protocol types, event/identity primitives, and conflict-resolution helpe… |
| 2026-09-30 12:24:54 | [VestaProtocol.Client](https://www.nuget.org/packages/VestaProtocol.Client) | 0.1.3 | Jesper Andersson | .NET client library for the Vesta protocol: WebSocket connection, Ed25519 ident… |
| 2026-09-30 12:47:02 | [Vintus.Telemetry](https://www.nuget.org/packages/Vintus.Telemetry) | 9.0.46-g9534d85c29 | Vintus | Plug-and-play OpenTelemetry for Vintus APIs: logs, traces and metrics to an OTL… |
| 2026-09-30 12:53:28 | [AravisSharp](https://www.nuget.org/packages/AravisSharp) | 0.8.36 | Alexandre | C# bindings for the Aravis industrial camera library (GenICam/GigE Vision/USB3… |
| 2026-09-30 12:57:24 | [Shiny.Mediator.AppFunctions](https://www.nuget.org/packages/Shiny.Mediator.AppFunctions) | 6.10.0-beta-0001 | Allan Ritchie | Shiny Mediator - expose mediator requests and commands to Siri, Shortcuts, Appl… |
| 2026-09-30 13:06:01 | [Wang.Seamas.Shared](https://www.nuget.org/packages/Wang.Seamas.Shared) | 1.0.0 | Seamas Wang | Share with multiple projects |
| 2026-09-30 13:11:08 | [Bannerlord.ReferenceAssemblies.GUI.v3.EarlyAccess](https://www.nuget.org/packages/Bannerlord.ReferenceAssemblies.GUI.v3.EarlyAccess) | 1.9.0.3526 | BUTR | The UI of Mount & Blade II: Bannerlord as data, for analyzers that check UI pat… |
| 2026-09-30 13:11:09 | [Bannerlord.ReferenceAssemblies.GUI.v3](https://www.nuget.org/packages/Bannerlord.ReferenceAssemblies.GUI.v3) | 1.5.3.122374-beta | BUTR | The UI of Mount & Blade II: Bannerlord as data, for analyzers that check UI pat… |
| 2026-09-30 13:11:10 | [Bannerlord.ReferenceAssemblies.GUI.v3.NavalDLC](https://www.nuget.org/packages/Bannerlord.ReferenceAssemblies.GUI.v3.NavalDLC) | 1.4.7.117484 | BUTR | The UI of the NavalDLC DLC of Mount & Blade II: Bannerlord as data, for analyze… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
