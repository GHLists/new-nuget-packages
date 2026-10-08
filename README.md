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

## Latest list — 2026-10-08 03:20 UTC

New packages created between 2026-10-08 02:20 UTC and 2026-10-08 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T03-20-49-67046Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 02:22:29 | [Promete.Web](https://www.nuget.org/packages/Promete.Web) | 2.1.0 | Ebise Lutica | Browser (.NET WebAssembly + WebGL2) backend for Promete |
| 2026-10-08 02:27:14 | [Blazor.Ink](https://www.nuget.org/packages/Blazor.Ink) | 1.0.0 | Blazor.Ink contributors | Blazor-native terminal UI. Not yet full Ink 8 parity. |
| 2026-10-08 02:33:00 | [Brows.Sys](https://www.nuget.org/packages/Brows.Sys) | 1.0.0 | Ken Yourek | Package Description |
| 2026-10-08 02:33:01 | [Brows.Sys.Composition](https://www.nuget.org/packages/Brows.Sys.Composition) | 1.0.0 | Ken Yourek | Package Description |
| 2026-10-08 02:33:03 | [Brows.Sys.Win32](https://www.nuget.org/packages/Brows.Sys.Win32) | 1.0.0 | Ken Yourek | Package Description |
| 2026-10-08 02:33:04 | [Brows.Sys.Win32.Windows](https://www.nuget.org/packages/Brows.Sys.Win32.Windows) | 1.0.0 | Ken Yourek | Package Description |
| 2026-10-08 02:33:26 | [CodeBrix.PostgresClient.PostgreSqlLicenseForever](https://www.nuget.org/packages/CodeBrix.PostgresClient.PostgreSqlLicenseForever) | 1.0.281.152 | Jeremy Ellis | A fully managed ADO.NET data provider for PostgreSQL, with connection pooling,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
