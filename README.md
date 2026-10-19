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

## Latest list — 2026-10-19 03:21 UTC

New packages created between 2026-10-19 02:22 UTC and 2026-10-19 03:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-19T03-21-59-280102Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-19 02:44:17 | [Ebitex.Data.Delivery](https://www.nuget.org/packages/Ebitex.Data.Delivery) | 0.1.11 | ebitex software LLC | Server-side client for the ebitex Data Delivery API: list the models a key can… |
| 2026-10-19 02:44:32 | [HtmlToPdfDotNet](https://www.nuget.org/packages/HtmlToPdfDotNet) | 1.0.0 | Guillermo Castillo | A fully managed library for converting HTML and CSS to PDF in .NET, with no bro… |
| 2026-10-19 02:47:56 | [FaQemSharp](https://www.nuget.org/packages/FaQemSharp) | 0.1.0 | Frédéric Lopez | Independent C# FA-QEM implementation: GLB simplification, successive mapping, c… |
| 2026-10-19 03:13:02 | [Aiursoft.AlertCenter.Client](https://www.nuget.org/packages/Aiursoft.AlertCenter.Client) | 10.4.0 | alertcenter | Create, query, resolve and change severity of application-scoped AlertCenter in… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
