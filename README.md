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

## Latest list — 2026-10-03 08:22 UTC

New packages created between 2026-10-03 07:21 UTC and 2026-10-03 08:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T08-22-03-952407Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 07:49:44 | [Universal.Operative.Sdk.Codex.OpenAI](https://www.nuget.org/packages/Universal.Operative.Sdk.Codex.OpenAI) | 1.0.0 | Andrew Ong | OpenAI image generation backend for the Codex toolset. |
| 2026-10-03 07:50:01 | [Universal.Operative.Sdk.Codex.OpenAI.ChatGpt](https://www.nuget.org/packages/Universal.Operative.Sdk.Codex.OpenAI.ChatGpt) | 1.0.0 | Andrew Ong | Codex-token image generation backend for the Codex toolset. |
| 2026-10-03 07:53:22 | [SegregatedStorage.AspNetCore](https://www.nuget.org/packages/SegregatedStorage.AspNetCore) | 2.0.0 | Steffen Skov | Extension to SegregatedStorage adding support for mapping REST endpoints for you |
| 2026-10-03 08:06:41 | [PostSharp.Tool](https://www.nuget.org/packages/PostSharp.Tool) | 2027.0.2-preview | PostSharp Technologies | The postsharp command line tool: registers licence keys, reads and edits the co… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
