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

## Latest list — 2026-11-21 04:19 UTC

New packages created between 2026-11-21 03:19 UTC and 2026-11-21 04:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T04-19-40-710974Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 03:22:50 | [SinoMatrix.HanXin](https://www.nuget.org/packages/SinoMatrix.HanXin) | 0.4.2 | 码界工坊 | 汉信码（Han Xin Code，GB/T 21049 / ISO/IEC 20830）编码与识别，Windows x64、Linux x64、Linux A… |
| 2026-11-21 03:25:44 | [Plugin.Maui.NativeSwipeMenu](https://www.nuget.org/packages/Plugin.Maui.NativeSwipeMenu) | 1.0.0-preview2 | Ed Giardina | A CollectionView with platform-native swipe actions: UIContextualAction on iOS… |
| 2026-11-21 03:43:34 | [Plasm.Templates](https://www.nuget.org/packages/Plasm.Templates) | 0.1.0 | Plasm contributors | dotnet new plasm-api: an F# domain and its data access on Plasm.Postgres, a C#… |
| 2026-11-21 03:43:34 | [Plasm.Postgres](https://www.nuget.org/packages/Plasm.Postgres) | 0.1.0 | Plasm contributors | PostgreSQL provider for Plasm (Npgsql). Experimental. |
| 2026-11-21 03:43:35 | [Plasm.HotChocolate](https://www.nuget.org/packages/Plasm.HotChocolate) | 0.1.0 | Plasm contributors | Hot Chocolate over Plasm: GraphQL filter and sort input types generated from fi… |
| 2026-11-21 03:43:35 | [Plasm](https://www.nuget.org/packages/Plasm) | 0.1.0 | Plasm contributors | Persistence for F# that stores the domain's own records: conventions for scalar… |
| 2026-11-21 03:43:36 | [Plasm.Annotations](https://www.nuget.org/packages/Plasm.Annotations) | 0.1.0 | Plasm contributors | The attributes a record uses to say how Plasm stores it: Table, Unique, Version… |
| 2026-11-21 03:58:26 | [Dloizides.ServiceDefaults.FastEndpoints](https://www.nuget.org/packages/Dloizides.ServiceDefaults.FastEndpoints) | 0.1.0 | DLoizides | Add-on to Dloizides.ServiceDefaults: FastEndpoints with the house route prefix… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
