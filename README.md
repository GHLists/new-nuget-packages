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

## Latest list — 2026-11-15 10:21 UTC

New packages created between 2026-11-15 09:21 UTC and 2026-11-15 10:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T10-21-29-586209Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 09:34:06 | [EasyImageSharp.Codecs](https://www.nuget.org/packages/EasyImageSharp.Codecs) | 1.3.1 | Farhan Lodi | Optional native codecs and colour management for EasyImageSharp in one package:… |
| 2026-11-15 09:35:03 | [EasyImageSharp.Web](https://www.nuget.org/packages/EasyImageSharp.Web) | 1.3.1 | Farhan Lodi | ASP.NET Core image middleware for EasyImageSharp: app.UseEasyImageSharp() resiz… |
| 2026-11-15 10:02:19 | [SharpZipLib.Lts](https://www.nuget.org/packages/SharpZipLib.Lts) | 1.4.3 | ICSharpCode,maintained fork b… | Maintained fork of SharpZipLib (drop-in: same assembly and namespaces, only the… |
| 2026-11-15 10:06:33 | [Mailtruss](https://www.nuget.org/packages/Mailtruss) | 0.1.1 | Mailtruss | .NET client for the Mailtruss email API. No dependencies. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
