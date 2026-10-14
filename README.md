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

## Latest list — 2026-10-14 19:20 UTC

New packages created between 2026-10-14 18:21 UTC and 2026-10-14 19:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-14T19-20-03-421746Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 18:26:06 | [nugetgo.github.com.spf13.pflag](https://www.nuget.org/packages/nugetgo.github.com.spf13.pflag) | 1.0.9 | go2cs conversion | unofficial go2cs C# conversion of github.com/spf13/pflag v1.0.9, built on the G… |
| 2026-10-14 18:26:40 | [hakamiroot](https://www.nuget.org/packages/hakamiroot) | 1.0.0 | Ahmed Hakami | Core libraries for hakamiroot. |
| 2026-10-14 18:31:06 | [IkeMtz.AspNetCore.Http.Results](https://www.nuget.org/packages/IkeMtz.AspNetCore.Http.Results) | 10.0.13.3-dev | Microsoft | ASP.NET Core types that implement Microsoft.AspNetCore.Http.IResult. This packa… |
| 2026-10-14 18:33:37 | [RzR.MinimalResultMessage](https://www.nuget.org/packages/RzR.MinimalResultMessage) | 1.0.0 | RzR | A minimal F# result model for methods and processes: a success or failure, an o… |
| 2026-10-14 18:38:41 | [Fuaran.UI.Core.Function](https://www.nuget.org/packages/Fuaran.UI.Core.Function) | 0.94.0 | Andrew J. Willshire | The projection of a Fuaran UI fragment's hole value-spaces and effect classes o… |
| 2026-10-14 18:39:13 | [SC.StatePie](https://www.nuget.org/packages/SC.StatePie) | 1.0.0 | S. van Cauter | A lightweight .NET state-management library for immutable application state, bu… |
| 2026-10-14 18:42:51 | [DotCourier](https://www.nuget.org/packages/DotCourier) | 0.1.0 | Valossa515 | CQRS + Mediator for .NET with batteries included: pipeline behaviors (logging,… |
| 2026-10-14 18:42:52 | [DotCourier.AspNetCore](https://www.nuget.org/packages/DotCourier.AspNetCore) | 0.1.0 | Valossa515 | ASP.NET Core integration for DotCourier: turn a Response<T> into an IResult (Mi… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
