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

## Latest list — 2026-10-29 04:21 UTC

New packages created between 2026-10-29 03:19 UTC and 2026-10-29 04:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T04-21-24-504979Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 03:26:22 | [Ivetech.ORM.SqlServer.GIS](https://www.nuget.org/packages/Ivetech.ORM.SqlServer.GIS) | 4.0.1 | Lucas Santos | Suporte a dados espaciais (geography/geometry) do ORM (object-relational mappin… |
| 2026-10-29 03:26:25 | [Ivetech.ORM.PostgreSql.GIS](https://www.nuget.org/packages/Ivetech.ORM.PostgreSql.GIS) | 4.0.1 | Lucas Santos | Suporte a dados espaciais (PostGIS geography/geometry) do ORM (object-relationa… |
| 2026-10-29 03:51:54 | [RasgaPdf](https://www.nuget.org/packages/RasgaPdf) | 0.2.6 | Messias Martins | Ultra-fast 2D spatial PDF parser powered by pure Rust for .NET — extract exact… |
| 2026-10-29 03:52:15 | [ConnectionManager](https://www.nuget.org/packages/ConnectionManager) | 1.0.0 | Antonio L. | Utilidad ligera para obtener valores de configuración (como cadenas de conexión… |
| 2026-10-29 03:56:43 | [EC_NET4](https://www.nuget.org/packages/EC_NET4) | 2026.10.29.1000 | EC_NET4 | 版本2026.10.29.1000 使用纯C#代码构建的Ethercat主站,支持DC,Freerun,PDO映射,热插拔,(不支持断电恢复,不支持热插拔第一… |
| 2026-10-29 04:15:47 | [Mitzh.Invoice.Core](https://www.nuget.org/packages/Mitzh.Invoice.Core) | 1.0.0 | Mitzh | Offline invoice recognition for XML, OFD, PDF and images, including railway e-t… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
