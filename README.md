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

## Latest list — 2026-10-08 04:20 UTC

New packages created between 2026-10-08 03:20 UTC and 2026-10-08 04:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T04-20-07-724131Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 03:28:48 | [Ling.Configuration.Database](https://www.nuget.org/packages/Ling.Configuration.Database) | 0.1.0 | Ling | Database backed Microsoft.Extensions.Configuration provider with polling reload… |
| 2026-10-08 03:31:05 | [Database.LiteDb](https://www.nuget.org/packages/Database.LiteDb) | 1.0.0 | Dio Liew | A LiteDb databse package wrapper. |
| 2026-10-08 03:33:37 | [Taskblockslip](https://www.nuget.org/packages/Taskblockslip) | 0.1.0 | jay-tank | Static analyzer that flags the classic .NET "sync over async" footgun: a direct… |
| 2026-10-08 03:37:49 | [AnyCAD.Robot.NET](https://www.nuget.org/packages/AnyCAD.Robot.NET) | 2026.10.8.1124 | AnyCAD Inc. | The professional graphics toolkit for .NET developers. |
| 2026-10-08 04:12:45 | [TurtlePath.Automations.AspNetCore](https://www.nuget.org/packages/TurtlePath.Automations.AspNetCore) | 1.11.0 | Elysium Coding | ASP.NET Core endpoint integration for TurtlePath automation profiles. |
| 2026-10-08 04:12:46 | [TurtlePath.Automations.Pigeon](https://www.nuget.org/packages/TurtlePath.Automations.Pigeon) | 1.11.0 | Elysium Coding | Pigeon consumer integration for TurtlePath automation profiles. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
