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

## Latest list — 2026-10-29 18:22 UTC

New packages created between 2026-10-29 17:21 UTC and 2026-10-29 18:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T18-22-02-001564Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 17:23:41 | [LunaCsUil](https://www.nuget.org/packages/LunaCsUil) | 0.1.0 | Carlos Luna | Unofficial client for the UIL Computer Science problems API at api.lunaghs.dev.… |
| 2026-10-29 17:31:22 | [SplitSecure.StepAuth](https://www.nuget.org/packages/SplitSecure.StepAuth) | 0.1.0 | SplitSecure | StepAuth service-provider client. |
| 2026-10-29 17:32:34 | [KirisameY.Randomizer](https://www.nuget.org/packages/KirisameY.Randomizer) | 0.0.1 | KirisameY.Randomizer | Package Description |
| 2026-10-29 17:38:33 | [replay.blackice.template](https://www.nuget.org/packages/replay.blackice.template) | 1.0.0 | replay | replay.re BlackICE bundle template for dotnet new -- Visit docs.replay.re for m… |
| 2026-10-29 17:40:15 | [PowerCraft.Notion.Core](https://www.nuget.org/packages/PowerCraft.Notion.Core) | 0.1.0 | The Code Kitchen | Typed kernel for PowerCraft.Notion: Notion pages materialised to a device as pr… |
| 2026-10-29 17:41:26 | [Resourcefull.AspNetCore](https://www.nuget.org/packages/Resourcefull.AspNetCore) | 3.1.0 | Zachary Fry | ASP.NET Core support for Resourcefull: serve downloads with their headers and c… |
| 2026-10-29 17:43:14 | [Codemetr.CSharp.Cover.Tool](https://www.nuget.org/packages/Codemetr.CSharp.Cover.Tool) | 0.1.0 | codemetr | codemetr-csharp-cover command line: C# test coverage per type and member (Cover… |
| 2026-10-29 17:51:20 | [Foothill.Cli](https://www.nuget.org/packages/Foothill.Cli) | 0.13.0 | Foothill Solutions | `fts` - seven commands for a project consuming the FTS platform packages, inclu… |
| 2026-10-29 17:51:21 | [Foothill.Template](https://www.nuget.org/packages/Foothill.Template) | 0.18.0 | Foothill Solutions | `dotnet new` templates for the FTS platform: `fts-api` scaffolds a service comp… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
