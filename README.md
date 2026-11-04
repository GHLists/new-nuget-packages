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

## Latest list — 2026-11-04 20:19 UTC

New packages created between 2026-11-04 19:20 UTC and 2026-11-04 20:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-04T20-19-14-386338Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-04 19:20:17 | [Webority.Chat.Support](https://www.nuget.org/packages/Webority.Chat.Support) | 0.130.2 | Webority Technologies | The support bridge for Webority Chat: handoff from the assistant to a person, t… |
| 2026-11-04 19:26:13 | [WithEffect.Testkit](https://www.nuget.org/packages/WithEffect.Testkit) | 10.0.14 | WithEffect.Services | WithEffect.Core assembles well-known packages for rapid application prototyping… |
| 2026-11-04 19:27:23 | [PersistentAIConversationEngine.Ds.Mdb](https://www.nuget.org/packages/PersistentAIConversationEngine.Ds.Mdb) | 0.1.0 | PACE.Ds.Mdb | Package Description |
| 2026-11-04 19:28:50 | [PersistentAIConversationEngine.Core](https://www.nuget.org/packages/PersistentAIConversationEngine.Core) | 0.1.0 | PACE.Core | Package Description |
| 2026-11-04 19:34:40 | [Solhigson.Testing](https://www.nuget.org/packages/Solhigson.Testing) | 10.0.0 | Solhigson | Test-only support for Solhigson projects: the census base, the census of census… |
| 2026-11-04 19:35:04 | [Nafes.Logging.Slack](https://www.nuget.org/packages/Nafes.Logging.Slack) | 1.0.0 | Nafes.Logging.Slack | Serilog sink that posts classified, deduplicated and rate-limited error alerts… |
| 2026-11-04 19:36:49 | [LogicBuilder.App.Maui](https://www.nuget.org/packages/LogicBuilder.App.Maui) | 1.0.1 | BlaiseD | Consolidates .NET MAUI UI generation functions into a shared library. |
| 2026-11-04 19:40:52 | [Rocket.Unity](https://www.nuget.org/packages/Rocket.Unity) | 1.0.0-alpha | Rocket.Unity | Package Description |
| 2026-11-04 19:48:45 | [Corfedo.Work.SqlServer](https://www.nuget.org/packages/Corfedo.Work.SqlServer) | 0.2.0 | Wojciech Wentland | SQL Server store for Corfedo Work, over Microsoft.Data.SqlClient: background jo… |
| 2026-11-04 20:01:47 | [SlideRule.Guidance.DotNet](https://www.nuget.org/packages/SlideRule.Guidance.DotNet) | 0.3.0 | Andrew Gray | SlideRule.Guidance.DotNet is a Roslyn analyzer that reports code departing from… |
| 2026-11-04 20:07:23 | [Webority.Support.HelpCentre](https://www.nuget.org/packages/Webority.Support.HelpCentre) | 0.48.0 | Webority Technologies | The public help centre for Webority products: the article list, search and arti… |
| 2026-11-04 20:07:34 | [Nullean.HttpFileParser](https://www.nuget.org/packages/Nullean.HttpFileParser) | 0.3.0 | Nullean and contributors | Parse, lint and run .http request files (Visual Studio, VS Code REST Client and… |
| 2026-11-04 20:07:37 | [Nullean.Snapshots.Browser](https://www.nuget.org/packages/Nullean.Snapshots.Browser) | 0.3.0 | Nullean and contributors | Browser journeys for Nullean.Snapshots: run agent-browser style journeys with N… |
| 2026-11-04 20:07:38 | [Nullean.Snapshots.Browser.Assertions](https://www.nuget.org/packages/Nullean.Snapshots.Browser.Assertions) | 0.3.0 | Nullean and contributors | AwesomeAssertions extensions for Nullean.Snapshots.Browser: MatchJourneySnapsho… |
| 2026-11-04 20:07:47 | [Nullean.Snapshots.Http](https://www.nuget.org/packages/Nullean.Snapshots.Http) | 0.3.0 | Nullean and contributors | HTTP snapshots for Nullean.Snapshots: snapshot an HttpResponseMessage, or run a… |
| 2026-11-04 20:07:48 | [Nullean.Snapshots.Http.Assertions](https://www.nuget.org/packages/Nullean.Snapshots.Http.Assertions) | 0.3.0 | Nullean and contributors | AwesomeAssertions extensions for Nullean.Snapshots.Http: MatchHttpSnapshot, Mat… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
