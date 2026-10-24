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

## Latest list — 2026-10-24 04:22 UTC

New packages created between 2026-10-24 03:20 UTC and 2026-10-24 04:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T04-22-17-024626Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 03:25:26 | [AnyCAD.Engineering.NET](https://www.nuget.org/packages/AnyCAD.Engineering.NET) | 2026.10.24.1110 | AnyCAD Inc. | The professional engineering (FEM) toolkit for .NET developers. |
| 2026-10-24 03:25:30 | [AnyCAD.Manufacturing.NET](https://www.nuget.org/packages/AnyCAD.Manufacturing.NET) | 2026.10.24.1110 | AnyCAD Inc. | The professional CAM toolpath toolkit for .NET developers. |
| 2026-10-24 03:51:29 | [Rulealize.Plugin.SqliteStore](https://www.nuget.org/packages/Rulealize.Plugin.SqliteStore) | 1.0.0 | Reny | A store for a Rulealize rule set that keeps instances: every state document in… |
| 2026-10-24 04:02:30 | [Divisionz.Scaffold.DB.Oracle](https://www.nuget.org/packages/Divisionz.Scaffold.DB.Oracle) | 1.0.0-rc857 | Isaychev Konstantin Mikhailov… | Package Description |
| 2026-10-24 04:10:51 | [Zespy.EzPlan.Integration.Client](https://www.nuget.org/packages/Zespy.EzPlan.Integration.Client) | 1.1.1 | Zespy | Management API-key client for ezPlan partner integrations. |
| 2026-10-24 04:10:54 | [Zespy.EzPlan.Integration.Contracts](https://www.nuget.org/packages/Zespy.EzPlan.Integration.Contracts) | 1.1.1 | Zespy | Partner-facing ezPlan integration contracts. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
