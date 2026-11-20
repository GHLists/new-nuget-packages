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

## Latest list — 2026-11-20 08:19 UTC

New packages created between 2026-11-20 07:21 UTC and 2026-11-20 08:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-20T08-19-46-123765Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-20 07:21:42 | [Suwgate.Architecture](https://www.nuget.org/packages/Suwgate.Architecture) | 0.1.0 | Manomenu | The build defaults of a .NET repository (warnings as errors, latest-all analyze… |
| 2026-11-20 07:21:43 | [Suwgate.Database](https://www.nuget.org/packages/Suwgate.Database) | 0.1.0 | Manomenu | Database guards for the xUnit tests of a .NET application (migration scripts, S… |
| 2026-11-20 07:21:53 | [Goo.SoftwareRenderer](https://www.nuget.org/packages/Goo.SoftwareRenderer) | 0.32.0 | Xaz | Optional Mesa lavapipe fallback for Goo on Windows x64 and Linux x64. |
| 2026-11-20 07:29:36 | [NativeSecrets](https://www.nuget.org/packages/NativeSecrets) | 1.0.1 | dja-cobi | Lightweight, AOT-compatible cross-platform secret storage for .NET with native… |
| 2026-11-20 07:56:10 | [NativeCompressions.LZ4.Runtime.linux-musl-arm64](https://www.nuget.org/packages/NativeCompressions.LZ4.Runtime.linux-musl-arm64) | 1.3.3 | Cysharp | LZ4 native runtime for linux-musl-arm64 (Alpine and other musl distributions). |
| 2026-11-20 07:56:11 | [NativeCompressions.LZ4.Runtime.linux-musl-x64](https://www.nuget.org/packages/NativeCompressions.LZ4.Runtime.linux-musl-x64) | 1.3.3 | Cysharp | LZ4 native runtime for linux-musl-x64 (Alpine and other musl distributions). |
| 2026-11-20 07:56:28 | [NativeCompressions.Zstandard.Runtime.linux-musl-arm64](https://www.nuget.org/packages/NativeCompressions.Zstandard.Runtime.linux-musl-arm64) | 1.3.3 | Cysharp | Zstandard native runtime for linux-musl-arm64 (Alpine and other musl distributi… |
| 2026-11-20 07:56:29 | [NativeCompressions.Zstandard.Runtime.linux-musl-x64](https://www.nuget.org/packages/NativeCompressions.Zstandard.Runtime.linux-musl-x64) | 1.3.3 | Cysharp | Zstandard native runtime for linux-musl-x64 (Alpine and other musl distribution… |
| 2026-11-20 08:03:03 | [Serval.Configuration](https://www.nuget.org/packages/Serval.Configuration) | 0.2.0 | Caprine Logic | Dotenv configuration files with explicit key mappings and standard .NET host in… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
