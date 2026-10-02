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

## Latest list — 2026-10-02 02:21 UTC

New packages created between 2026-10-02 01:20 UTC and 2026-10-02 02:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-02T02-21-17-141248Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-02 01:27:08 | [CodeBrix.Sdl3.ZlibLicenseForever](https://www.nuget.org/packages/CodeBrix.Sdl3.ZlibLicenseForever) | 1.0.275.85 | Jeremy Ellis | C# bindings for SDL3 (Simple DirectMedia Layer 3) with the SDL3 native librarie… |
| 2026-10-02 01:27:08 | [Akka.Serialization.V2](https://www.nuget.org/packages/Akka.Serialization.V2) | 1.6.0-beta1 | Akka.NET Team | MessagePack-backed source-generated serializers for Akka.NET SerializerV2. |
| 2026-10-02 01:39:20 | [Importable](https://www.nuget.org/packages/Importable) | 1.0.8 | Annogram | Turns ports (interfaces) and internal services into a strongly typed, fluent IS… |
| 2026-10-02 02:04:53 | [Wang.Seamas.Shared.AspNetCore](https://www.nuget.org/packages/Wang.Seamas.Shared.AspNetCore) | 1.0.1 | Seamas Wang | AspNetCore shared components (filters, middlewares, exception handling) for Sha… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
