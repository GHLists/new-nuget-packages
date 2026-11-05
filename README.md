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

## Latest list — 2026-11-05 08:20 UTC

New packages created between 2026-11-05 07:30 UTC and 2026-11-05 08:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T08-20-36-517294Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 07:46:22 | [Mediana.Models.Mesh](https://www.nuget.org/packages/Mediana.Models.Mesh) | 0.1.18 | Vadim Belov | Managed multimedia building blocks for .NET. |
| 2026-11-05 07:55:03 | [Pbwire.FSharp](https://www.nuget.org/packages/Pbwire.FSharp) | 0.1.7 | jinganix | Idiomatic F# facade over the Pbwire C# dynamic binding, schema at runtime, no w… |
| 2026-11-05 08:09:42 | [ConnectMQ.Mqtt](https://www.nuget.org/packages/ConnectMQ.Mqtt) | 1.0.0 | ConnectMQ Team | Publish and subscribe on the free public MQTT broker broker.connectmq.com in a… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
