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

## Latest list — 2026-10-28 11:19 UTC

New packages created between 2026-10-28 10:20 UTC and 2026-10-28 11:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-28T11-19-10-223896Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-28 10:22:36 | [Biz.Bizadm.KMS.NetFramework](https://www.nuget.org/packages/Biz.Bizadm.KMS.NetFramework) | 1.0.0 | SeongSikChae | Independent .NET Framework 4.8 KMS implementation. |
| 2026-10-28 10:22:37 | [Thinkmine.Kobo.Lang](https://www.nuget.org/packages/Thinkmine.Kobo.Lang) | 0.1.12 | Thinkmine | Command-line compiler for Kobo language files. |
| 2026-10-28 10:22:55 | [thinkmine.kobo.lang.buildtools](https://www.nuget.org/packages/thinkmine.kobo.lang.buildtools) | 0.1.12 | Thinkmine | Incremental Kobo-to-C# source generator and automatic SDK-style project integra… |
| 2026-10-28 10:36:18 | [McpPlayground](https://www.nuget.org/packages/McpPlayground) | 1.0.0 | Alim Iusufov | Swagger-like playground for MCP servers hosted in ASP.NET Core: one line (app.M… |
| 2026-10-28 10:37:21 | [Unclaimable.Files](https://www.nuget.org/packages/Unclaimable.Files) | 1.0.0 | Perry3D.nl | Filename policies powered by the Unclaimable engine: portable naming rules, res… |
| 2026-10-28 10:42:16 | [AppWeaver.ResultMapping](https://www.nuget.org/packages/AppWeaver.ResultMapping) | 1.0.0 | Team AppWeaver | Result-to-IResult mapper with DI extensions using AppWeaver.ProblemDetails. |
| 2026-10-28 10:57:51 | [Zespy.Signing.Contracts](https://www.nuget.org/packages/Zespy.Signing.Contracts) | 0.7.1 | Zespy | Explicit organisation and product-account managed signing contracts. |
| 2026-10-28 10:57:53 | [Zespy.Signing.Verification](https://www.nuget.org/packages/Zespy.Signing.Verification) | 0.7.1 | Zespy | Bounded invoice assertions and independent portable issuer proof verification. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
