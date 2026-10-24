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

## Latest list — 2026-10-24 16:20 UTC

New packages created between 2026-10-24 15:21 UTC and 2026-10-24 16:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T16-20-38-333003Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 15:32:15 | [HaramFarooq.MyMathLibrary](https://www.nuget.org/packages/HaramFarooq.MyMathLibrary) | 1.0.0 | Haramlibrary | A reusable C# math library. |
| 2026-10-24 15:32:26 | [AvaloniaLight.Reactive](https://www.nuget.org/packages/AvaloniaLight.Reactive) | 1.0.0 | AvaloniaLight.Reactive contri… | A lightweight reactive core for Avalonia: notifying objects and the [Reactive]… |
| 2026-10-24 15:39:53 | [BlockCount](https://www.nuget.org/packages/BlockCount) | 1.17.0 | Farshadudheen k | Add powerful validation rules to Umbraco Block List content, helping editors en… |
| 2026-10-24 15:41:26 | [ISO22900.II-Sharp.Abstractions](https://www.nuget.org/packages/ISO22900.II-Sharp.Abstractions) | 1.4.0-beta | Joerg Frank | Interfaces (IDiagPduApiOneSysLevel, IModule, IComLogicalLink, IComPrimitive), d… |
| 2026-10-24 15:54:22 | [Specrig.Reqnroll](https://www.nuget.org/packages/Specrig.Reqnroll) | 0.1.0 | Denis Daschenko | Binds the specrig harness to Reqnroll: the step a record belongs to, the checks… |
| 2026-10-24 15:54:23 | [Specrig.Surface](https://www.nuget.org/packages/Specrig.Surface) | 0.1.0 | Denis Daschenko | The Roslyn pass behind specrig's tests/surface.yaml and tests/checks.yaml: what… |
| 2026-10-24 15:54:23 | [Specrig.Postgres](https://www.nuget.org/packages/Specrig.Postgres) | 0.1.0 | Denis Daschenko | Postgres as a specrig resource: a real database in a container, provisioned onc… |
| 2026-10-24 15:54:24 | [Specrig.RabbitMQ](https://www.nuget.org/packages/Specrig.RabbitMQ) | 0.1.0 | Denis Daschenko | Events in and out over RabbitMQ.Client for the specrig harness, in process: wha… |
| 2026-10-24 15:54:24 | [Specrig.Grpc](https://www.nuget.org/packages/Specrig.Grpc) | 0.1.0 | Denis Daschenko | gRPC both ways for the specrig harness: a typed client to the service, and a ne… |
| 2026-10-24 15:54:25 | [Specrig.Tool](https://www.nuget.org/packages/Specrig.Tool) | 0.1.0 | Denis Daschenko | The specrig dotnet tool: init lays a specification-first suite out beside a ser… |
| 2026-10-24 15:54:26 | [Specrig.Hosting](https://www.nuget.org/packages/Specrig.Hosting) | 0.1.0 | Denis Daschenko | The specrig harness for any service on the Generic Host: boots Program, answers… |
| 2026-10-24 15:54:26 | [Specrig](https://www.nuget.org/packages/Specrig) | 0.1.0 | Denis Daschenko | The core of specrig for .NET, independent of the host: the records, the contrac… |
| 2026-10-24 15:54:26 | [Specrig.Redis](https://www.nuget.org/packages/Specrig.Redis) | 0.1.0 | Denis Daschenko | Redis as a specrig resource: a real server in a container, provisioned once per… |
| 2026-10-24 15:54:27 | [Specrig.Quartz](https://www.nuget.org/packages/Specrig.Quartz) | 0.1.0 | Denis Daschenko | A Quartz job run in a specrig case as the scheduler runs it, with the detail th… |
| 2026-10-24 15:54:44 | [AnointedAutomation.SSO.UI](https://www.nuget.org/packages/AnointedAutomation.SSO.UI) | 1.0.0 | Anointed Automation LLC, Alex… | Front end for Sign in with Anointed Automation in ASP.NET Core: brand-styled ac… |
| 2026-10-24 15:54:45 | [AnointedAutomation.Templates](https://www.nuget.org/packages/AnointedAutomation.Templates) | 1.0.0 | Anointed Automation LLC, Alex… | dotnet new templates for Sign in with Anointed Automation: anointed-razor (Razo… |
| 2026-10-24 15:54:51 | [AnointedAutomation.SSO.Owin](https://www.nuget.org/packages/AnointedAutomation.SSO.Owin) | 1.0.0 | Anointed Automation LLC, Alex… | Sign in with Anointed Automation for classic ASP.NET (.NET Framework 4.7.2+, MV… |
| 2026-10-24 16:00:14 | [Hipsy.Net](https://www.nuget.org/packages/Hipsy.Net) | 1.0.0 | Paul Appeldoorn | Unofficial typed .NET client for the Hipsy API (https://docs.hipsy.nl). Not aff… |
| 2026-10-24 16:08:51 | [PinkRooster.Extensions.AI.Antigravity](https://www.nuget.org/packages/PinkRooster.Extensions.AI.Antigravity) | 0.1.0 | PinkRooster | Microsoft.Extensions.AI chat client for Google Antigravity (agy). |
| 2026-10-24 16:08:53 | [Blasphemous.FrameRateUnlimiter](https://www.nuget.org/packages/Blasphemous.FrameRateUnlimiter) | 1.0.0 | NewbieElton | Enables frame rate customization (fixed/variable FPS) |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
