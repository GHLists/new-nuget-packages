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

## Latest list — 2026-10-31 05:19 UTC

New packages created between 2026-10-31 04:20 UTC and 2026-10-31 05:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T05-19-36-844504Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 04:36:32 | [Corely.IAM.Testing](https://www.nuget.org/packages/Corely.IAM.Testing) | 1.0.0 | Corely.IAM.Testing | Test only checks for apps on Corely.IAM: fail when a service method has no cros… |
| 2026-10-31 04:40:03 | [MASS4.StableIdentity](https://www.nuget.org/packages/MASS4.StableIdentity) | 1.0.0 | Bruno Massa | Opaque stable identities, rename maps and identity registries shared by the MAS… |
| 2026-10-31 04:42:59 | [codingpad](https://www.nuget.org/packages/codingpad) | 0.0.1 | Joseph Izang | Placeholder for the CodingPad runtime library (dump, cache, secret, db). Not fu… |
| 2026-10-31 04:42:59 | [cpad](https://www.nuget.org/packages/cpad) | 0.0.1 | Joseph Izang | Placeholder for cpad, the CodingPad command-line runner. Not functional yet. |
| 2026-10-31 04:44:16 | [RvtIO](https://www.nuget.org/packages/RvtIO) | 0.1.0 | mahach666 | Reads Autodesk Revit projects and families (.rvt, .rfa) without Revit or the Re… |
| 2026-10-31 04:44:18 | [RvtIO.Cli](https://www.nuget.org/packages/RvtIO.Cli) | 0.1.0 | mahach666 | Command line tool that reads Autodesk Revit files (.rvt, .rfa) without Revit an… |
| 2026-10-31 05:09:09 | [Praxo.Core](https://www.nuget.org/packages/Praxo.Core) | 0.1.2 | AxisVela | Embeddable MIT-licensed agent framework for .NET: tools, policy, events, memory… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
