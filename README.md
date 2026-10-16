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

## Latest list — 2026-10-16 10:20 UTC

New packages created between 2026-10-16 09:20 UTC and 2026-10-16 10:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-16T10-20-15-554457Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-16 09:29:40 | [KetPsi.Endpoints.Grpc](https://www.nuget.org/packages/KetPsi.Endpoints.Grpc) | 1.3.0 | KetPsi ,MohamadArsalan Imamve… | Code-first gRPC endpoints for KetPsi (compile-time codecs, no protobuf-net) |
| 2026-10-16 09:43:07 | [xRMProducts.HealthScan](https://www.nuget.org/packages/xRMProducts.HealthScan) | 0.6.0.1 | xRM PRODUCTS | Free read-only Dataverse health scan for XrmToolBox. Unpublished local test: da… |
| 2026-10-16 09:51:13 | [ApiForge.Application](https://www.nuget.org/packages/ApiForge.Application) | 1.0.2 | Pilar Pérez de Inestrosa Sánc… | ApiForge.ApplicationCore is the core library of the ApiForge application, provi… |
| 2026-10-16 09:51:13 | [ApiForge.Generator](https://www.nuget.org/packages/ApiForge.Generator) | 1.0.2 | Pilar Pérez de Inestrosa Sánc… | Generates a typed C# client solution (Domain/Application/Infrastructure/Client)… |
| 2026-10-16 09:51:13 | [ApiForge.Domain](https://www.nuget.org/packages/ApiForge.Domain) | 1.0.2 | Pilar Pérez de Inestrosa Sánc… | ApiForge.Domain is the core library of the ApiForge application, providing esse… |
| 2026-10-16 09:51:14 | [ApiForge.Infrastructure](https://www.nuget.org/packages/ApiForge.Infrastructure) | 1.0.2 | Pilar Pérez de Inestrosa Sánc… | ApiForge.Infrastructure is the infrastructure library of the ApiForge applicati… |
| 2026-10-16 10:05:15 | [XUnitAssured.Camunda](https://www.nuget.org/packages/XUnitAssured.Camunda) | 6.21.3 | Carlos Andrew Costa Bezerra | Camunda 8 process testing for XUnitAssured. Deploys BPMN, starts real process i… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
