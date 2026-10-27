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

## Latest list — 2026-10-27 15:20 UTC

New packages created between 2026-10-27 14:20 UTC and 2026-10-27 15:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T15-20-27-347443Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 14:22:18 | [devdeer.tools.tocpm-plus](https://www.nuget.org/packages/devdeer.tools.tocpm-plus) | 1.4.1 | DEVDEER GmbH | This dotnet tool reads all csproj-files under a given folder and converts them… |
| 2026-10-27 14:28:40 | [Ascon.Pilot.Server.Api.Grpc](https://www.nuget.org/packages/Ascon.Pilot.Server.Api.Grpc) | 26.19.1-alpha | ASCON | gRPC API for ASCON Pilot-Server |
| 2026-10-27 14:30:48 | [SolarIcons.Blazor](https://www.nuget.org/packages/SolarIcons.Blazor) | 2.0.0 | SolarIcons.Blazor | Generated Blazor components for Solar Icons. Unreleased preview. |
| 2026-10-27 14:59:19 | [JSNet.Analyzers](https://www.nuget.org/packages/JSNet.Analyzers) | 0.2.0 | Gravicode Studios (Kang Fadhi… | JS.Net analyzer API: write custom rules in JS.Net with `rule Name { ... }` decl… |
| 2026-10-27 14:59:20 | [JSNet.Web](https://www.nuget.org/packages/JSNet.Web) | 0.2.0 | Gravicode Studios (Kang Fadhi… | ASP.NET Core for JS.Net: Express-style routing (app.get/post/put/delete), middl… |
| 2026-10-27 14:59:22 | [JSNet.Blazor](https://www.nuget.org/packages/JSNet.Blazor) | 0.2.0 | Gravicode Studios (Kang Fadhi… | Blazor for JS.Net: JsComponent base class with setState, mounted hooks, auto-di… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
