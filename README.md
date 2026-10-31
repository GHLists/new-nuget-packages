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

## Latest list — 2026-10-31 09:21 UTC

New packages created between 2026-10-31 08:20 UTC and 2026-10-31 09:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T09-21-30-195976Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 08:30:48 | [Cratis.Showrunner.BoxOffice.Contracts](https://www.nuget.org/packages/Cratis.Showrunner.BoxOffice.Contracts) | 1.1.0 | Cratis | The event contracts for Box Office — what a product's operator decides about a… |
| 2026-10-31 08:31:33 | [CppKana2](https://www.nuget.org/packages/CppKana2) | 2.0.0 | CppKana2 | C# binding for cpp-kana2 (Japanese kana to Hepburn romaji) over its C ABI. The… |
| 2026-10-31 09:03:17 | [Proxoft.FomanticUI.Resources](https://www.nuget.org/packages/Proxoft.FomanticUI.Resources) | 2.0.0 | Proxoft | Package Description |
| 2026-10-31 09:03:48 | [Proxoft.FomanticUI.Core](https://www.nuget.org/packages/Proxoft.FomanticUI.Core) | 2.0.0 | Proxoft s.r.o. | Package Description |
| 2026-10-31 09:06:02 | [Proxoft.FomanticUI.Blazor](https://www.nuget.org/packages/Proxoft.FomanticUI.Blazor) | 2.0.0 | Proxoft s.r.o. | Package Description |
| 2026-10-31 09:06:26 | [Proxoft.FomanticUI.TagHelpers](https://www.nuget.org/packages/Proxoft.FomanticUI.TagHelpers) | 2.0.0 | Proxoft s.r.o. | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
