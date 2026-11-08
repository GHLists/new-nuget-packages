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

## Latest list — 2026-11-08 07:18 UTC

New packages created between 2026-11-08 06:20 UTC and 2026-11-08 07:18 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T07-18-51-370848Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-08 06:27:39 | [FlowOnRails.AspNetCore](https://www.nuget.org/packages/FlowOnRails.AspNetCore) | 0.1.0 | alguem5381 | ASP.NET Core integration for FlowOnRails with scoped error visibility, generate… |
| 2026-11-08 06:42:21 | [T.Molodoy.MviCore.Net](https://www.nuget.org/packages/T.Molodoy.MviCore.Net) | 0.0.1 | T.Molodoy | A simplified single-threaded MVICore implementation built on R3. |
| 2026-11-08 06:43:16 | [Asyntai.Sitefinity.AiChatbot](https://www.nuget.org/packages/Asyntai.Sitefinity.AiChatbot) | 1.0.0 | Asyntai | Adds the Asyntai AI chat assistant to every public page of your Sitefinity CMS… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
