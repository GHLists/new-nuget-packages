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

## Latest list — 2026-10-31 12:20 UTC

New packages created between 2026-10-31 11:19 UTC and 2026-10-31 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-31T12-20-48-678614Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-31 11:21:42 | [HostLoom.RateLimiting](https://www.nuget.org/packages/HostLoom.RateLimiting) | 0.20.0 | Aleksandr Pavlov | Backend-neutral distributed token-bucket rate limiting with an in-process refer… |
| 2026-10-31 11:21:43 | [HostLoom.RateLimiting.DependencyInjection](https://www.nuget.org/packages/HostLoom.RateLimiting.DependencyInjection) | 0.20.0 | Aleksandr Pavlov | Named dependency-injection registration, options validation, and readiness for… |
| 2026-10-31 11:21:45 | [HostLoom.RateLimiting.HttpClient](https://www.nuget.org/packages/HostLoom.RateLimiting.HttpClient) | 0.20.0 | Aleksandr Pavlov | Outgoing HttpClient rate limiting with bounded local waits over HostLoom limite… |
| 2026-10-31 11:32:40 | [Fuaran.UI.Operability](https://www.nuget.org/packages/Fuaran.UI.Operability) | 0.100.0 | Andrew J. Willshire | Fuaran operability — a tree's operable surface as a specified projection of it.… |
| 2026-10-31 11:42:41 | [Aore.Camstar.InSiteXMLClient](https://www.nuget.org/packages/Aore.Camstar.InSiteXMLClient) | 9.0.0 | WEI.ZHOU (Willis) | Camstar InSite XML 客户端合并库：将原 Camstar.Constants.dll、Camstar.Exceptions.dll、Camst… |
| 2026-10-31 11:50:39 | [Inngest.UserContext.AspNetCore](https://www.nuget.org/packages/Inngest.UserContext.AspNetCore) | 1.0.0 | inngest-dotnet contributors | ASP.NET Core support for Inngest.UserContext: takes the user an event is sent f… |
| 2026-10-31 11:54:35 | [MacroDeck.Localization](https://www.nuget.org/packages/MacroDeck.Localization) | 3.0.0 | Macro Deck | Renderer-independent localization for Macro Deck: localization keys, deferred l… |
| 2026-10-31 11:54:35 | [MacroDeck.Plugin.Analyzers](https://www.nuget.org/packages/MacroDeck.Plugin.Analyzers) | 3.0.0 | Macro Deck | Roslyn analyzers for Macro Deck plugin authors: invalid ids and metadata, unsup… |
| 2026-10-31 11:54:36 | [MacroDeck.Plugin.Cli](https://www.nuget.org/packages/MacroDeck.Plugin.Cli) | 3.0.0 | Macro Deck | macrodeck-plugin: the Macro Deck plugin developer CLI. Validate a manifest, ins… |
| 2026-10-31 11:54:37 | [MacroDeck.Plugin.Hosting](https://www.nuget.org/packages/MacroDeck.Plugin.Hosting) | 3.0.0 | Macro Deck | DI-first hosting model for out-of-process Macro Deck plugins. Write a plugin as… |
| 2026-10-31 11:54:38 | [MacroDeck.Plugin.Packaging](https://www.nuget.org/packages/MacroDeck.Plugin.Packaging) | 3.0.0 | Macro Deck | The Macro Deck plugin manifest and artifact format: parsing and validating mani… |
| 2026-10-31 11:54:39 | [MacroDeck.Plugin.Protocol](https://www.nuget.org/packages/MacroDeck.Plugin.Protocol) | 3.0.0 | Macro Deck | Wire contracts for the Macro Deck plugin protocol: envelope, handshake, capabil… |
| 2026-10-31 11:54:39 | [MacroDeck.Plugin.Serilog](https://www.nuget.org/packages/MacroDeck.Plugin.Serilog) | 3.0.0 | Macro Deck | Serilog sink for Macro Deck plugins. Forwards a plugin's own logs to the host o… |
| 2026-10-31 11:54:40 | [MacroDeck.Plugin.Testing](https://www.nuget.org/packages/MacroDeck.Plugin.Testing) | 3.0.0 | Macro Deck | Test host, fakes and assertions for a Macro Deck plugin built on MacroDeck.Plug… |
| 2026-10-31 11:54:41 | [MacroDeck.Sdk](https://www.nuget.org/packages/MacroDeck.Sdk) | 3.0.0 | Macro Deck | Capability contracts for Macro Deck integrations and plugins: actions, config f… |
| 2026-10-31 11:54:41 | [MacroDeck.Signing](https://www.nuget.org/packages/MacroDeck.Signing) | 3.0.0 | Macro Deck | Macro Deck package signing: the Ed25519 primitives, creator certificate chain v… |
| 2026-10-31 11:54:42 | [MacroDeck.Ui](https://www.nuget.org/packages/MacroDeck.Ui) | 3.0.0 | Macro Deck | The declarative Macro Deck UI DSL and reactive runtime: a view compiles to a tr… |
| 2026-10-31 11:54:43 | [MacroDeck.Ui.Model](https://www.nuget.org/packages/MacroDeck.Ui.Model) | 3.0.0 | Macro Deck | The transport-neutral Macro Deck UI model: node identity, properties and patche… |
| 2026-10-31 11:54:43 | [MacroDeck.Ui.Testing](https://www.nuget.org/packages/MacroDeck.Ui.Testing) | 3.0.0 | Macro Deck | The headless Macro Deck UI test host: render a view, query it by id, type or te… |
| 2026-10-31 11:56:35 | [Shiny.Controls.BarcodeReader.Shared](https://www.nuget.org/packages/Shiny.Controls.BarcodeReader.Shared) | 2.3.0-beta-0003 | Allan Ritchie | Host-neutral long-range barcode reading engine behind the Shiny CameraView long… |
| 2026-10-31 12:06:12 | [OpenIGI.Net](https://www.nuget.org/packages/OpenIGI.Net) | 0.5.4 | OpenIGI Contributors | Package Description |
| 2026-10-31 12:08:50 | [XLibur.RBush](https://www.nuget.org/packages/XLibur.RBush) | 5.0.0 | viceroypenguin | Spatial Index data structure; used to make it easier to find data points on a t… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
