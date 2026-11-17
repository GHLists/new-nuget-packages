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

## Latest list — 2026-11-17 00:19 UTC

New packages created between 2026-11-16 23:20 UTC and 2026-11-17 00:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-17T00-19-43-584668Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-16 23:25:30 | [ByondWire.Cli](https://www.nuget.org/packages/ByondWire.Cli) | 0.1.0 | Wirewraith | Command-line BYOND Topic client. |
| 2026-11-16 23:25:30 | [ByondWire](https://www.nuget.org/packages/ByondWire) | 0.1.0 | Wirewraith | Small standard-library BYOND Topic client. |
| 2026-11-16 23:34:30 | [TurkishText](https://www.nuget.org/packages/TurkishText) | 0.1.0 | Nejat Berk Şener | Turkish text helpers that do not depend on the current culture or ICU: correct… |
| 2026-11-16 23:49:02 | [AgentToolkit](https://www.nuget.org/packages/AgentToolkit) | 1.7.2 | Maxxx | AgentToolkit: MVVM primitives, agent core and shared product models in one pack… |
| 2026-11-17 00:12:50 | [CritterStack.TestHarness](https://www.nuget.org/packages/CritterStack.TestHarness) | 1.3.3 | Ryan Anthony | Fluent Given/When/Then test harness for Marten and Wolverine. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
