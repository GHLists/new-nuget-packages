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

## Latest list — 2026-11-21 08:20 UTC

New packages created between 2026-11-21 07:21 UTC and 2026-11-21 08:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T08-20-48-528654Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 07:23:30 | [Closient.Client](https://www.nuget.org/packages/Closient.Client) | 0.0.1 | Closient | Closient: placeholder package reserving the name. SDK coming soon. |
| 2026-11-21 07:31:06 | [MyMathLibTuzova](https://www.nuget.org/packages/MyMathLibTuzova) | 1.0.0 | ТвоёИмя | Библиотека с примерами public и internal методов |
| 2026-11-21 07:37:41 | [CodexFlow.Storage.EntityFramework](https://www.nuget.org/packages/CodexFlow.Storage.EntityFramework) | 0.1.19 | iwaitu | Entity Framework adapters for managed CodexFlow hosts that share a relational c… |
| 2026-11-21 08:02:16 | [Duxel.Gallery](https://www.nuget.org/packages/Duxel.Gallery) | 0.3.0-preview | dimohy | Duxel controls and graphics gallery. |
| 2026-11-21 08:10:15 | [Jtext103.CFET2.Things.MDSplusServerThing](https://www.nuget.org/packages/Jtext103.CFET2.Things.MDSplusServerThing) | 1.0.1 | MDSplusServerThing | Package Description |
| 2026-11-21 08:13:06 | [Progmasoft.Tazel.Dsl](https://www.nuget.org/packages/Progmasoft.Tazel.Dsl) | 0.1.0 | Progmasoft | The types MODULE.csx and BUILD.csx files of Tazel are written against. |
| 2026-11-21 08:13:16 | [Progmasoft.Tazel.PluginSdk](https://www.nuget.org/packages/Progmasoft.Tazel.PluginSdk) | 0.1.0 | Progmasoft | The MSBuild project SDK of Tazel plugins: it references the plugin API, checks… |
| 2026-11-21 08:13:20 | [Progmasoft.Tazel.PluginTemplates](https://www.nuget.org/packages/Progmasoft.Tazel.PluginTemplates) | 0.1.0 | Progmasoft | dotnet new tazel-plugin: a Tazel plugin with a build step. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
