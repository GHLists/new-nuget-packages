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

## Latest list — 2026-11-01 02:18 UTC

New packages created between 2026-11-01 01:19 UTC and 2026-11-01 02:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-01T02-18-27-758875Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-01 01:29:38 | [Clashawaun.Depot.Contracts](https://www.nuget.org/packages/Clashawaun.Depot.Contracts) | 1.0.0 | Clashawaun | Wire contracts, signed document schemas, scope vocabulary and the platform tabl… |
| 2026-11-01 01:29:38 | [Clashawaun.Depot.Licensing](https://www.nuget.org/packages/Clashawaun.Depot.Licensing) | 1.0.0 | Clashawaun | Offline verification of Depot licence documents for products to embed: chain, E… |
| 2026-11-01 01:29:39 | [Clashawaun.Depot.Signing](https://www.nuget.org/packages/Clashawaun.Depot.Signing) | 1.0.0 | Clashawaun | The one signer and verifier for Depot release lines, manifests, promotions and… |
| 2026-11-01 01:29:39 | [Clashawaun.Depot.Sdk](https://www.nuget.org/packages/Clashawaun.Depot.Sdk) | 1.0.0 | Clashawaun | Client SDK for Depot: publishing, resolving and downloading releases, the store… |
| 2026-11-01 01:29:40 | [Clashawaun.Depot.Agent.Runtime](https://www.nuget.org/packages/Clashawaun.Depot.Agent.Runtime) | 1.0.0 | Clashawaun | The Depot builder and signer agent loops as a library: a host supplies options,… |
| 2026-11-01 01:54:05 | [Zendiator.CodeFixes](https://www.nuget.org/packages/Zendiator.CodeFixes) | 0.5.0 | tkym | Optional C# code fixes for explicit Zendiator handler registrations. |
| 2026-11-01 01:59:03 | [VYaml.JsonSchema](https://www.nuget.org/packages/VYaml.JsonSchema) | 1.6.0 | hadashiA | JSON Schema generation for VYaml [YamlObject] types |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
