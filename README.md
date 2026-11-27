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

## Latest list — 2026-11-27 11:19 UTC

New packages created between 2026-11-27 10:21 UTC and 2026-11-27 11:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-27T11-19-06-445969Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-27 10:32:53 | [Hakiri.Toolkit](https://www.nuget.org/packages/Hakiri.Toolkit) | 0.2.0 | Jattac | Package Description |
| 2026-11-27 10:33:07 | [Comandus](https://www.nuget.org/packages/Comandus) | 0.1.0 | vdasus | Turn a short typed string into a typed set of commands: fast data entry with de… |
| 2026-11-27 10:56:54 | [Molyom.Merge](https://www.nuget.org/packages/Molyom.Merge) | 3.2026.11.27 | Moly Omidvar | Merge duplicate records of ANY table in Microsoft Dataverse / Dynamics 365 - al… |
| 2026-11-27 11:04:44 | [Hmz.Core.Activities](https://www.nuget.org/packages/Hmz.Core.Activities) | 0.1.0 | Hmz | Durable activity log and live activity streaming engine for Hmz backends on EF… |
| 2026-11-27 11:04:45 | [Hmz.Core.Activities.Abstractions](https://www.nuget.org/packages/Hmz.Core.Activities.Abstractions) | 0.1.0 | Hmz | Contracts of the Hmz durable activity log and live activity streaming engine: a… |
| 2026-11-27 11:09:44 | [Sdcb.SimdPaddleOCR.Models.DocumentOrientation](https://www.nuget.org/packages/Sdcb.SimdPaddleOCR.Models.DocumentOrientation) | 1.0.0 | sdcb | Embedded PP-LCNet_x1_0_doc_ori four-way page orientation (0/90/180/270) ONNX mo… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
