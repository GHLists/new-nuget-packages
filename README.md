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

## Latest list — 2026-10-25 23:22 UTC

New packages created between 2026-10-25 22:20 UTC and 2026-10-25 23:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-25T23-22-31-621414Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-25 22:31:17 | [Trazos.UI](https://www.nuget.org/packages/Trazos.UI) | 1.0.0 | carandev | A warm, artisanal, hand-crafted Blazor component library and design system with… |
| 2026-10-25 22:34:03 | [FlaUI.Window.Extensions](https://www.nuget.org/packages/FlaUI.Window.Extensions) | 1.0.3 | chrisvasqm | Playwright-style locators, auto-waiting actions, and state queries for FlaUI. |
| 2026-10-25 22:40:11 | [ComplexityAnalysis.Mcp](https://www.nuget.org/packages/ComplexityAnalysis.Mcp) | 1.0.0 | Rodrigo de Oliveira | Local read-only MCP server for deterministic C# project complexity analysis, me… |
| 2026-10-25 22:41:14 | [MonoSmith.Plugin.Sdk](https://www.nuget.org/packages/MonoSmith.Plugin.Sdk) | 0.1.0 | Eduardo Russo | The C# SDK for writing smith plugins: the protocol's types, the serve loop, a h… |
| 2026-10-25 22:45:37 | [Singulink.Net.Http.Api.Client.WinUI](https://www.nuget.org/packages/Singulink.Net.Http.Api.Client.WinUI) | 4.0.0 | Singulink | Passkey (WebAuthn) support and session token storage for WinUI 3 and Uno Platfo… |
| 2026-10-25 22:45:38 | [Singulink.Net.Http.Api.Service.Passkeys](https://www.nuget.org/packages/Singulink.Net.Http.Api.Service.Passkeys) | 4.0.0 | Singulink | Passkey (WebAuthn) ceremonies and a passkey hand-off page for services built wi… |
| 2026-10-25 22:45:39 | [Singulink.Net.Http.Api.Service.Cloudflare](https://www.nuget.org/packages/Singulink.Net.Http.Api.Service.Cloudflare) | 4.0.0 | Singulink | Cloudflare support for services built with the Singulink HTTP API Toolkit: trus… |
| 2026-10-25 22:45:40 | [Singulink.Net.Http.Api.Service.Testing](https://www.nuget.org/packages/Singulink.Net.Http.Api.Service.Testing) | 4.0.0 | Singulink | Test helpers for services built with the Singulink HTTP API Toolkit: a session… |
| 2026-10-25 22:57:23 | [Clashawaun.Pkie.Agent.Runtime](https://www.nuget.org/packages/Clashawaun.Pkie.Agent.Runtime) | 1.0.0 | Clashawaun | The pki.ie signing agent as a library: hold a CA key on this host, long-poll pk… |
| 2026-10-25 22:57:23 | [Clashawaun.Pkie.Contracts](https://www.nuget.org/packages/Clashawaun.Pkie.Contracts) | 1.0.0 | Clashawaun | Wire contracts shared by the pki.ie server, SDK and signing agents. |
| 2026-10-25 22:57:24 | [Clashawaun.Pkie.Crypto](https://www.nuget.org/packages/Clashawaun.Pkie.Crypto) | 1.0.0 | Clashawaun | Key custody providers, X.509 assembly, CRL/OCSP and ceremony bundle handling fo… |
| 2026-10-25 22:57:24 | [Clashawaun.Pkie.Sdk](https://www.nuget.org/packages/Clashawaun.Pkie.Sdk) | 1.0.0 | Clashawaun | Client SDK for pki.ie — certificate enrolment, trust distribution and signing a… |
| 2026-10-25 23:00:45 | [SimplArchive.Sapass](https://www.nuget.org/packages/SimplArchive.Sapass) | 0.52.0 | sapass | sapass — a pass-like store of passwords and secrets, sealed on your machine and… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
