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

## Latest list — 2026-10-05 17:19 UTC

New packages created between 2026-10-05 16:19 UTC and 2026-10-05 17:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-05T17-19-27-698681Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-05 16:20:51 | [TriQL.Client.Compression](https://www.nuget.org/packages/TriQL.Client.Compression) | 1.0.0 | TriQL Contributors | LZ4 and Zstandard codec support for the TriQL Trino spooled protocol, isolated… |
| 2026-10-05 16:20:51 | [TriQL.Data.ADO](https://www.nuget.org/packages/TriQL.Data.ADO) | 1.0.0 | TriQL Contributors | An ADO.NET provider (DbConnection, DbCommand, DbDataReader) for Trino, built on… |
| 2026-10-05 16:20:52 | [TriQL.Client](https://www.nuget.org/packages/TriQL.Client) | 1.0.0 | TriQL Contributors | A .NET client and SDK for Trino (formerly Presto): session management, streamin… |
| 2026-10-05 16:20:52 | [TriQL.Client.Auth](https://www.nuget.org/packages/TriQL.Client.Auth) | 1.0.0 | TriQL Contributors | Cloud and enterprise authentication providers (Microsoft Entra ID, OAuth 2.0) f… |
| 2026-10-05 16:22:11 | [Ternary.Data.Core](https://www.nuget.org/packages/Ternary.Data.Core) | 0.1.2 | Jacob Dahlke | A framework to simplify working with data from multiple sources, including file… |
| 2026-10-05 16:22:16 | [Marey.Anim](https://www.nuget.org/packages/Marey.Anim) | 0.3.0 | Marey contributors | Animation as a pure function of time: a seekable, composable Anim<'a> with a ve… |
| 2026-10-05 16:22:19 | [Marey.Toolchain](https://www.nuget.org/packages/Marey.Toolchain) | 0.3.0 | Marey contributors | Resolution and invocation of the external programs Marey drives but does not sh… |
| 2026-10-05 16:22:20 | [Marey.Backend.Skia](https://www.nuget.org/packages/Marey.Backend.Skia) | 0.3.0 | Marey contributors | PNG and PDF output through SkiaSharp, with real text shaping via HarfBuzz. The… |
| 2026-10-05 16:22:21 | [Marey.Tools.Video](https://www.nuget.org/packages/Marey.Tools.Video) | 0.3.0 | Marey contributors | Encode a rendered frame sequence to video by shelling out to ffmpeg. Degrades t… |
| 2026-10-05 16:22:22 | [Marey.Tools.Tex](https://www.nuget.org/packages/Marey.Tools.Tex) | 0.3.0 | Marey contributors | Mathematical typesetting for Marey figures: TeX source on a scene's text runs b… |
| 2026-10-05 16:22:23 | [Ternary.Data.Csv](https://www.nuget.org/packages/Ternary.Data.Csv) | 0.1.2 | Jacob Dahlke | A framework to simplify working with data from multiple sources, including file… |
| 2026-10-05 16:22:55 | [Ternary.Data.MsSql](https://www.nuget.org/packages/Ternary.Data.MsSql) | 0.1.2 | Jacob Dahlke | A framework to simplify working with data from multiple sources, including file… |
| 2026-10-05 16:22:59 | [DecisionsDotNet](https://www.nuget.org/packages/DecisionsDotNet) | 0.0.1-preview | Adam Holm | Type-safe .NET client for TypeSafe AI Jev models and the OpenRouter Decisions A… |
| 2026-10-05 16:23:29 | [Ternary.Data.SqlLite](https://www.nuget.org/packages/Ternary.Data.SqlLite) | 0.1.2 | Jacob Dahlke | A framework to simplify working with data from multiple sources, including file… |
| 2026-10-05 16:38:23 | [tryAGI.Muse](https://www.nuget.org/packages/tryAGI.Muse) | 0.0.0-dev | tryAGI and contributors | C# SDK for the Muse Gadget API -- device API, encrypted multiplexed transport,… |
| 2026-10-05 16:49:54 | [Arjo.UmbracoVisualEditor](https://www.nuget.org/packages/Arjo.UmbracoVisualEditor) | 18.0.0 | Richard Ockerby | Edit Umbraco content on the page itself: the Visual editor renders your real fr… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
