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

## Latest list — 2026-11-10 02:20 UTC

New packages created between 2026-11-10 01:20 UTC and 2026-11-10 02:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-10T02-20-20-248782Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-10 01:54:52 | [JDMallen.Toolbox.AI.Azure](https://www.nuget.org/packages/JDMallen.Toolbox.AI.Azure) | 4.6.0 | J.D. Mallen | Microsoft Entra ID sign-in for JDMallen.Toolbox.AI's Azure OpenAI client via Az… |
| 2026-11-10 02:10:39 | [Orson.Alpm](https://www.nuget.org/packages/Orson.Alpm) | 0.2.1 | shanoaice | C# binding for libalpm, the library behind pacman. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
