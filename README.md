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

## Latest list — 2026-11-25 22:20 UTC

New packages created between 2026-11-25 21:19 UTC and 2026-11-25 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-25T22-20-41-672038Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-25 21:26:23 | [TylerWarner.Inventor.Templates](https://www.nuget.org/packages/TylerWarner.Inventor.Templates) | 1.0.0 | Tyler Warner and Curtis Wague… | Project templates for creating Autodesk Inventor add-ins. |
| 2026-11-25 21:28:53 | [SparqlQueryLib.Runtime](https://www.nuget.org/packages/SparqlQueryLib.Runtime) | 0.1.0 | David Habgood | Runs the parameterised SPARQL queries of an exported sqlib bundle from .NET, wi… |
| 2026-11-25 21:29:00 | [ROCratePCC](https://www.nuget.org/packages/ROCratePCC) | 0.3.1 | nfdi4plants, Lukas Weil, Eli… | Polyglot library for creation of RO-Crate Profile Crates. |
| 2026-11-25 21:29:06 | [ROCratePCC.Javascript](https://www.nuget.org/packages/ROCratePCC.Javascript) | 0.3.1 | nfdi4plants, Lukas Weil, Eli… | Polyglot library for creation of RO-Crate Profile Crates. |
| 2026-11-25 21:29:15 | [ROCratePCC.Python](https://www.nuget.org/packages/ROCratePCC.Python) | 0.3.1 | nfdi4plants, Lukas Weil, Eli… | Polyglot library for creation of RO-Crate Profile Crates. |
| 2026-11-25 21:47:06 | [MushCOA.Authentication.Windows](https://www.nuget.org/packages/MushCOA.Authentication.Windows) | 1.0.0 | MushCOA | Reusable Windows Authentication and Active Directory authorization library for… |
| 2026-11-25 21:54:46 | [device-check.shared-kernel](https://www.nuget.org/packages/device-check.shared-kernel) | 1.0.0 | Rafael Ruan | Shared Kernel containing common concepts and abstractions shared across DeviceC… |
| 2026-11-25 21:58:58 | [ChampUI](https://www.nuget.org/packages/ChampUI) | 0.3.1 | Sadeem Systems | Open-source Blazor UI component library developed by Sadeem Systems. |
| 2026-11-25 22:01:31 | [Bellatrix.Cli](https://www.nuget.org/packages/Bellatrix.Cli) | 3.2.0 | Automate The Planet Ltd. | Model-free automation CLI for AI coding agents. Drives desktop (WinAppDriver),… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
