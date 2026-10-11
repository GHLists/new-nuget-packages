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

## Latest list — 2026-10-11 05:19 UTC

New packages created between 2026-10-11 04:20 UTC and 2026-10-11 05:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-11T05-19-47-687691Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-11 04:22:47 | [Rulealize.Plugin.Text](https://www.nuget.org/packages/Rulealize.Plugin.Text) | 1.0.0 | Reny | Questions about text for a Rulealize rule set, the same on every runtime: str.t… |
| 2026-10-11 05:06:18 | [CodeBrix.Audio.FlacWriter.BsdLicenseForever](https://www.nuget.org/packages/CodeBrix.Audio.FlacWriter.BsdLicenseForever) | 1.0.284.304 | Jeremy Ellis | Lossless FLAC encoding for CodeBrix.Audio. FlacEncoder turns float or integer s… |
| 2026-10-11 05:11:30 | [OneAuth.Client.AspNetCore](https://www.nuget.org/packages/OneAuth.Client.AspNetCore) | 0.3.0 | OneAuth | OneAuth 统一身份权限中心的 ASP.NET Core 接入 SDK：按用户有效权限注水（PermissionClaimsTransformer + E… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
