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

## Latest list — 2026-11-02 04:20 UTC

New packages created between 2026-11-02 03:20 UTC and 2026-11-02 04:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T04-20-16-357262Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-02 03:38:18 | [PiSharp.CustomAgents](https://www.nuget.org/packages/PiSharp.CustomAgents) | 1.2.0.2 | PiSharp contributors | EXPERIMENTAL. Custom agents for PiSharp on the durable harness: typed workflows… |
| 2026-11-02 03:38:22 | [PiSharp.CustomAgents.JavaScript](https://www.nuget.org/packages/PiSharp.CustomAgents.JavaScript) | 1.2.0.2 | PiSharp contributors | EXPERIMENTAL. JavaScript tools and workflow actions for PiSharp.CustomAgents, i… |
| 2026-11-02 03:38:30 | [PiSharp.CustomAgents.Scripting](https://www.nuget.org/packages/PiSharp.CustomAgents.Scripting) | 1.2.0.2 | PiSharp contributors | EXPERIMENTAL. C# script tools and workflow actions for PiSharp.CustomAgents, co… |
| 2026-11-02 03:39:07 | [victor-wiki.HuggingFaceHubSharp](https://www.nuget.org/packages/victor-wiki.HuggingFaceHubSharp) | 1.0.0 | victor-wiki | C# implementation of HuggingfaceHub. |
| 2026-11-02 03:45:06 | [Foldable.Maui](https://www.nuget.org/packages/Foldable.Maui) | 1.0.1 | Quoc Thao | Modern .NET MAUI library for detecting foldable device posture, hinge angle, an… |
| 2026-11-02 04:02:06 | [IPCalci](https://www.nuget.org/packages/IPCalci) | 0.1.0-beta | Kasali | High-performance .NET library for calculating and parsing IPv4 and IPv6 subnets… |
| 2026-11-02 04:09:47 | [FauxGraph.Datastore.MsGraph](https://www.nuget.org/packages/FauxGraph.Datastore.MsGraph) | 0.1.0 | J. Burnett | File-based datastore for native Microsoft Graph responses, used as test data. |
| 2026-11-02 04:09:48 | [FauxGraph.Datastore.Abstractions](https://www.nuget.org/packages/FauxGraph.Datastore.Abstractions) | 0.1.0 | J. Burnett | Shared abstractions, tenant facade and file engine for the FauxGraph graph data… |
| 2026-11-02 04:09:48 | [FauxGraph.Datastore.AzGraph](https://www.nuget.org/packages/FauxGraph.Datastore.AzGraph) | 0.1.0 | J. Burnett | File-based datastore for native Azure Resource Graph responses, used as test da… |
| 2026-11-02 04:11:44 | [Fulcrum](https://www.nuget.org/packages/Fulcrum) | 1.0.0 | Fulcrum contributors | Turn System One model answers into committed outcomes: typed questions, first-m… |
| 2026-11-02 04:13:34 | [EASYTools.CoreAdmin](https://www.nuget.org/packages/EASYTools.CoreAdmin) | 4.0.0 | Libor Svoboda | Automagically add an Admin Panel to your .NET 6 web app. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
