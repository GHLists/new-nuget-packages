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

## Latest list — 2026-10-29 19:20 UTC

New packages created between 2026-10-29 18:22 UTC and 2026-10-29 19:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T19-20-46-573484Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 18:34:52 | [Trexon.Configuration](https://www.nuget.org/packages/Trexon.Configuration) | 1.0.0 | Trexoncorp | Typed environment settings for .NET with defaults, aliases, prefixes, dotenv, v… |
| 2026-10-29 18:38:12 | [StbImageNext](https://www.nuget.org/packages/StbImageNext) | 1.0.0 | StbImageSharpTeam | C# Image Library based on StbImageNext, StbImageWriteSharp, StbImageResizeSharp… |
| 2026-10-29 18:46:17 | [InventiveRhythm.fluXis.Modes.Keys](https://www.nuget.org/packages/InventiveRhythm.fluXis.Modes.Keys) | 2026.1029.0 | fluXis.Modes.Keys | A community-driven rhythm game with a focus on creativity and expression. |
| 2026-10-29 18:49:22 | [Gapfy.Echo.ApiExplorer](https://www.nuget.org/packages/Gapfy.Echo.ApiExplorer) | 0.2.8 | Gapfy | Authenticated developer UI and endpoint mock routing for ASP.NET Core applicati… |
| 2026-10-29 18:49:29 | [Gapfy.Echo.Mock.Runner](https://www.nuget.org/packages/Gapfy.Echo.Mock.Runner) | 0.2.8 | Gapfy | Run isolated Echo HTTP mock snapshots and test commands without remote services. |
| 2026-10-29 18:49:33 | [Gapfy.Echo.Offline](https://www.nuget.org/packages/Gapfy.Echo.Offline) | 0.2.8 | Gapfy | Versioned, validated Echo mock snapshots for reproducible offline execution. |
| 2026-10-29 18:53:57 | [NltkNet.Runtime.osx-arm64](https://www.nuget.org/packages/NltkNet.Runtime.osx-arm64) | 2.0.0 | Denis Kazakov | Portable CPython 3.12 and NLTK runtime for NltkNet on osx-arm64. |
| 2026-10-29 18:53:59 | [NltkNet.Runtime.win-x64](https://www.nuget.org/packages/NltkNet.Runtime.win-x64) | 2.0.0 | Denis Kazakov | Portable CPython 3.12 and NLTK runtime for NltkNet on win-x64. |
| 2026-10-29 18:54:01 | [NltkNet.Runtime.linux-x64](https://www.nuget.org/packages/NltkNet.Runtime.linux-x64) | 2.0.0 | Denis Kazakov | Portable CPython 3.12 and NLTK runtime for NltkNet on linux-x64. |
| 2026-10-29 19:01:37 | [DocQL.Net](https://www.nuget.org/packages/DocQL.Net) | 1.0.0 | Nertil Poci | Package Description |
| 2026-10-29 19:06:50 | [redb.Route.DataFormats.Mime](https://www.nuget.org/packages/redb.Route.DataFormats.Mime) | 4.5.0 | redbase | MIME multipart data format for redb.Route (MimeKit), as Camel's mimeMultipart:… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
