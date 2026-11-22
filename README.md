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

## Latest list — 2026-11-22 14:19 UTC

New packages created between 2026-11-22 13:18 UTC and 2026-11-22 14:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T14-19-41-977346Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 13:20:23 | [SumireCraft.Core](https://www.nuget.org/packages/SumireCraft.Core) | 1.1.0 | StartBits | A value for a date and a time that are entered separately and can each be empty… |
| 2026-11-22 13:22:27 | [Darp.CodeEditor](https://www.nuget.org/packages/Darp.CodeEditor) | 0.1.0 | rosslight GmbH | Avalonia code editor: TextMate highlighting, search, and completion, hover and… |
| 2026-11-22 13:29:14 | [DecisionsDotNet.Caching](https://www.nuget.org/packages/DecisionsDotNet.Caching) | 1.1.0 | Adam Holm | Caches DecisionsDotNet evaluations in Microsoft.Extensions.Caching.Hybrid, keye… |
| 2026-11-22 13:29:15 | [DecisionsDotNet.Testing](https://www.nuget.org/packages/DecisionsDotNet.Testing) | 1.1.0 | Adam Holm | A scripted fake and a recording wrapper for the DecisionsDotNet IDecisionsClien… |
| 2026-11-22 13:30:35 | [GridAPI](https://www.nuget.org/packages/GridAPI) | 1.0.0 | BugyLabs | Official server-side .NET SDK for the GridAPI public REST API. |
| 2026-11-22 13:35:45 | [Yautbox.Testing](https://www.nuget.org/packages/Yautbox.Testing) | 2.0.1 | maximiliysiss | Unit-testing helpers for Yautbox: builds OutboxMessage instances so outbox hand… |
| 2026-11-22 13:37:37 | [Sashimi343.D3Fragments.Identity.EFCore](https://www.nuget.org/packages/Sashimi343.D3Fragments.Identity.EFCore) | 0.2.0 | sashimi343 | ASP.NET Core Identity integration for D3Fragments: Identity stores that leave s… |
| 2026-11-22 13:41:08 | [DarkNet.UI](https://www.nuget.org/packages/DarkNet.UI) | 1.1.0 | Dark-Net UI | Dark-Net UI: customizable modern WPF controls. |
| 2026-11-22 13:50:25 | [ZeroCSharp.Bflat.osx-arm64](https://www.nuget.org/packages/ZeroCSharp.Bflat.osx-arm64) | 0.3.0 | Zero C# contributors | bflat (OnurGumus/bflat fork), trimmed to what Zero C# builds use, for osx-arm64… |
| 2026-11-22 13:58:39 | [AgentKit.Push](https://www.nuget.org/packages/AgentKit.Push) | 0.1.7 | Lenka Scherfel | Web Push on the BCL, no vendor SDK: message encryption (RFC 8291, aes128gcm per… |
| 2026-11-22 13:58:40 | [AgentKit.Secrets](https://www.nuget.org/packages/AgentKit.Secrets) | 0.1.7 | Lenka Scherfel | Secrets at rest for a self-hosted service: a keyring of 32-byte master keys rea… |
| 2026-11-22 13:58:40 | [AgentKit.Fetch](https://www.nuget.org/packages/AgentKit.Fetch) | 0.1.7 | Lenka Scherfel | Outgoing HTTP to addresses someone else chose (a URL an agent names, a webhook,… |
| 2026-11-22 14:07:53 | [AgentKit.Channels](https://www.nuget.org/packages/AgentKit.Channels) | 0.1.7 | Lenka Scherfel | Outgoing messages to the places people read, without a vendor SDK: Discord and… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
