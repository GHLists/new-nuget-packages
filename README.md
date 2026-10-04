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

## Latest list — 2026-10-04 04:20 UTC

New packages created between 2026-10-04 03:21 UTC and 2026-10-04 04:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-04T04-20-32-720301Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-04 03:24:38 | [StdUnit.Sharp7](https://www.nuget.org/packages/StdUnit.Sharp7) | 0.7.3 | StdUnit.Sharp7 | Package Description |
| 2026-10-04 03:35:09 | [UniverseGenerator](https://www.nuget.org/packages/UniverseGenerator) | 1.0.0 | Mark Rogers | Seeded universe, galaxy, star system, planet and moon generator for games and f… |
| 2026-10-04 03:42:19 | [myNOC.Remootio](https://www.nuget.org/packages/myNOC.Remootio) | 1.0.1 | myNOC LLC | A .NET client library for the Remootio smart gate/garage door controller WebSoc… |
| 2026-10-04 03:49:54 | [Elsa.Actors.ProtoActor.PubSub.Redis](https://www.nuget.org/packages/Elsa.Actors.ProtoActor.PubSub.Redis) | 3.9.0 | Elsa Workflows Community | Provides Redis-backed storage for Proto.Actor Pub/Sub subscribers. |
| 2026-10-04 03:50:10 | [Elsa.Ldap](https://www.nuget.org/packages/Elsa.Ldap) | 3.9.0 | Elsa Workflows Community | Provides LDAP activities for integrations to LDAP servers (e.g. Active Director… |
| 2026-10-04 03:50:15 | [Elsa.Mqtt](https://www.nuget.org/packages/Elsa.Mqtt) | 3.9.0 | Elsa Workflows Community | Provides an integration to send and receive messages via MQTT. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
