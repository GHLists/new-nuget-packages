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

## Latest list — 2026-10-29 05:20 UTC

New packages created between 2026-10-29 04:21 UTC and 2026-10-29 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T05-20-13-727952Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 04:34:13 | [CryptoDecryptor](https://www.nuget.org/packages/CryptoDecryptor) | 1.0.0 | Antonio L. | Utilidad para descifrar de forma segura textos cifrados con RSA (OAEP-SHA256) a… |
| 2026-10-29 05:06:49 | [NextLevel.Access](https://www.nuget.org/packages/NextLevel.Access) | 1.0.0 | NextLevel | Player and admin access for NextLevel services, behind one AddAccess call. Repl… |
| 2026-10-29 05:10:07 | [IRI.Maptor.Core.Astronomy](https://www.nuget.org/packages/IRI.Maptor.Core.Astronomy) | 3.0.0-alpha | Hossein Narimani Rad | A .NET standard library for positional astronomy: astronomical time scales, sid… |
| 2026-10-29 05:10:09 | [IRI.Maptor.Core.FileGdb](https://www.nuget.org/packages/IRI.Maptor.Core.FileGdb) | 3.0.0-alpha | Hossein Narimani Rad | A dependency-free .NET standard library to read ESRI File Geodatabases (*.gdb f… |
| 2026-10-29 05:10:14 | [IRI.Maptor.Core.Satellite](https://www.nuget.org/packages/IRI.Maptor.Core.Satellite) | 3.0.0-alpha | Hossein Narimani Rad | A .NET standard library for satellite orbits: TLE and OMM reading, SGP4 propaga… |
| 2026-10-29 05:10:18 | [IRI.Maptor.Infrastructure.EfCore.PostgreSql](https://www.nuget.org/packages/IRI.Maptor.Infrastructure.EfCore.PostgreSql) | 3.0.0-alpha | Hossein Narimani Rad | EF Core PostgreSQL/PostGIS support for IRI.Maptor Geometry<Point>: maps geometr… |
| 2026-10-29 05:10:19 | [IRI.Maptor.Infrastructure.EfCore.SqlServer](https://www.nuget.org/packages/IRI.Maptor.Infrastructure.EfCore.SqlServer) | 3.0.0-alpha | Hossein Narimani Rad | EF Core SQL Server support for materializing geometry/geography columns directl… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
