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

## Latest list — 2026-10-07 21:20 UTC

New packages created between 2026-10-07 20:22 UTC and 2026-10-07 21:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-07T21-20-27-158352Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-07 20:29:41 | [Dloizides.Testing](https://www.nuget.org/packages/Dloizides.Testing) | 0.2.0 | DLoizides | A [MethodUnderTest] attribute plus a two-line guard that fails the build when a… |
| 2026-10-07 20:29:44 | [Dloizides.Testing.Postgres](https://www.nuget.org/packages/Dloizides.Testing.Postgres) | 0.2.0 | DLoizides | A PostgreSQL Testcontainers fixture for xUnit v2 whose connect and command time… |
| 2026-10-07 20:30:38 | [Quartz.Weasel.Firebird](https://www.nuget.org/packages/Quartz.Weasel.Firebird) | 4.4.0 | Marko Lahma, Quartz.NET | Quartz.NET Weasel integration for Firebird - the ADO.NET job store's tables as… |
| 2026-10-07 20:30:39 | [Quartz.Weasel.MySQL](https://www.nuget.org/packages/Quartz.Weasel.MySQL) | 4.4.0 | Marko Lahma, Quartz.NET | Quartz.NET Weasel integration for MySQL - the ADO.NET job store's tables as a W… |
| 2026-10-07 20:30:40 | [Quartz.Weasel.Oracle](https://www.nuget.org/packages/Quartz.Weasel.Oracle) | 4.4.0 | Marko Lahma, Quartz.NET | Quartz.NET Weasel integration for Oracle - the ADO.NET job store's tables as a… |
| 2026-10-07 20:45:10 | [OverShell](https://www.nuget.org/packages/OverShell) | 0.1.0 | Moaid Hathot | Overseer Shell - a Windows terminal built on the Windows Terminal engine that w… |
| 2026-10-07 20:45:23 | [CuriousDev.LabKit](https://www.nuget.org/packages/CuriousDev.LabKit) | 1.0.0 | Vlad Timchenko | Lab endpoints for Curious Dev courses: lets the course platform verify the serv… |
| 2026-10-07 20:54:14 | [Ivanngoc.EventDrivenDesign](https://www.nuget.org/packages/Ivanngoc.EventDrivenDesign) | 0.1.0 | Tran Ngoc Anh | Package Description |
| 2026-10-07 20:56:02 | [Dloizides.Testing.Report](https://www.nuget.org/packages/Dloizides.Testing.Report) | 0.2.0 | DLoizides | dotnet tool test-report: turns the .trx files of a test run into a static HTML… |
| 2026-10-07 20:59:18 | [Bitbound.ComputerUseDotnet](https://www.nuget.org/packages/Bitbound.ComputerUseDotnet) | 0.1.7 | Jared Goodwin | A Model Context Protocol (MCP) server that lets an agent see the screen and sim… |
| 2026-10-07 20:59:37 | [Avorix.Sefhs.Client](https://www.nuget.org/packages/Avorix.Sefhs.Client) | 3.1.0 | Avorix | file handling microservice integration sdk for Avorix internal use only. |
| 2026-10-07 21:13:59 | [RonCS](https://www.nuget.org/packages/RonCS) | 0.1.0 | CriusNyx | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
