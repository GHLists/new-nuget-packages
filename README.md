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

## Latest list — 2026-10-25 20:20 UTC

New packages created between 2026-10-25 19:19 UTC and 2026-10-25 20:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-25T20-20-29-059295Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-25 19:24:21 | [Heossi.Saar](https://www.nuget.org/packages/Heossi.Saar) | 1.3.0 | HEOSSI (Pte.) Ltd. | Thin .NET client over the Saar command-line interface. |
| 2026-10-25 19:35:05 | [MonoDetour.Interop.HarmonyX](https://www.nuget.org/packages/MonoDetour.Interop.HarmonyX) | 0.7.17 | Hamunii | Hooks HarmonyX at runtime to make it and MonoDetour play nice together. |
| 2026-10-25 19:37:26 | [Nanov.Kafka](https://www.nuget.org/packages/Nanov.Kafka) | 2.16.0.2 | Confluent Inc.;Andreas Heider… | Nanov.Confluent.Kafka under the Nanov.Kafka namespace for use side by side with… |
| 2026-10-25 19:40:31 | [haveno-dotnet](https://www.nuget.org/packages/haveno-dotnet) | 0.0.1 | atsamd21 | A library used to interact with the Haveno gRPC API |
| 2026-10-25 20:11:37 | [Efizzy.Doc2Pdf](https://www.nuget.org/packages/Efizzy.Doc2Pdf) | 1.0.0 | Efizzy | High-performance, zero-dependency .NET library to convert Word (.docx, .doc), H… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
