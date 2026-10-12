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

## Latest list — 2026-10-12 20:18 UTC

New packages created between 2026-10-12 19:20 UTC and 2026-10-12 20:18 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T20-18-52-157607Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 19:20:38 | [Belin.FreeMobile.FSharp](https://www.nuget.org/packages/Belin.FreeMobile.FSharp) | 1.0.0 | CedX | Send SMS messages to your Free Mobile device. |
| 2026-10-12 19:21:26 | [DnsToolkit.Net](https://www.nuget.org/packages/DnsToolkit.Net) | 1.0.0 | Alexander Reinert, Matheis1992 | A complete managed .Net DNS and DNSSEC client, a DNS server (UDP, TCP, TLS), DA… |
| 2026-10-12 19:23:30 | [Shiny.AspNet.DocumentDb](https://www.nuget.org/packages/Shiny.AspNet.DocumentDb) | 1.0.0 | aritchie,ShinyLib | REST and live-query (SSE) endpoints for Shiny.DocumentDb on ASP.NET Core — a do… |
| 2026-10-12 19:23:31 | [Shiny.AspNet.Ssh](https://www.nuget.org/packages/Shiny.AspNet.Ssh) | 1.0.0 | aritchie,ShinyLib | SSH remote port forwarding for ASP.NET Core. Publishes a Kestrel app through an… |
| 2026-10-12 19:23:31 | [Shiny.AspNet.Acme](https://www.nuget.org/packages/Shiny.AspNet.Acme) | 1.0.0 | aritchie,ShinyLib | Automatic TLS certificates for ASP.NET Core and Kestrel from Let's Encrypt, Zer… |
| 2026-10-12 19:23:32 | [Shiny.AspNet.Idempotency](https://www.nuget.org/packages/Shiny.AspNet.Idempotency) | 1.0.0 | aritchie,ShinyLib | Idempotency-Key (draft-ietf-httpapi-idempotency-key-header) middleware for ASP.… |
| 2026-10-12 19:23:32 | [Shiny.AspNet.Discovery](https://www.nuget.org/packages/Shiny.AspNet.Discovery) | 1.0.0 | aritchie,ShinyLib | mDNS/DNS-SD (Bonjour) discovery for ASP.NET Core — advertises the app on the lo… |
| 2026-10-12 19:23:33 | [Shiny.AspNet.ContentDigest](https://www.nuget.org/packages/Shiny.AspNet.ContentDigest) | 1.0.0 | aritchie,ShinyLib | RFC 9530 Content-Digest and Repr-Digest for ASP.NET Core - verifies request bod… |
| 2026-10-12 19:23:33 | [Shiny.AspNet.Npm](https://www.nuget.org/packages/Shiny.AspNet.Npm) | 1.0.0 | aritchie,ShinyLib | A private npm registry for ASP.NET Core - the registry API npm, pnpm and Yarn s… |
| 2026-10-12 19:23:34 | [Shiny.AspNet.NuGet](https://www.nuget.org/packages/Shiny.AspNet.NuGet) | 1.0.0 | aritchie,ShinyLib | A private NuGet feed for ASP.NET Core - the NuGet V3 protocol (service index, p… |
| 2026-10-12 19:23:34 | [Shiny.AspNet.Tunnels](https://www.nuget.org/packages/Shiny.AspNet.Tunnels) | 1.0.0 | aritchie,ShinyLib | Agent-backed tunnels for ASP.NET Core — publishes a Kestrel app through cloudfl… |
| 2026-10-12 19:23:35 | [Shiny.AspNet.WebDav](https://www.nuget.org/packages/Shiny.AspNet.WebDav) | 1.0.0 | aritchie,ShinyLib | A WebDAV (RFC 4918) class 1 and 2 server for ASP.NET Core - mount a directory i… |
| 2026-10-12 19:23:35 | [Shiny.AspNet.JsonPatch](https://www.nuget.org/packages/Shiny.AspNet.JsonPatch) | 1.0.0 | aritchie,ShinyLib | RFC 6902 JSON Patch for ASP.NET Core over System.Text.Json.Nodes — an RFC 6901… |
| 2026-10-12 19:23:36 | [Shiny.AspNet.Tus](https://www.nuget.org/packages/Shiny.AspNet.Tus) | 1.0.0 | aritchie,ShinyLib | Resumable uploads for ASP.NET Core over the tus 1.0.0 protocol — a phone upload… |
| 2026-10-12 19:23:36 | [Shiny.AspNet.FileSync](https://www.nuget.org/packages/Shiny.AspNet.FileSync) | 1.0.0 | aritchie,ShinyLib | Dropbox-style file sync for ASP.NET Core. Files are split into content-defined… |
| 2026-10-12 19:23:36 | [Shiny.AspNet.WebHosting](https://www.nuget.org/packages/Shiny.AspNet.WebHosting) | 1.0.0 | aritchie,ShinyLib | Web hosting module infrastructure for ASP.NET Core applications |
| 2026-10-12 19:23:37 | [Shiny.AspNet.Webhooks](https://www.nuget.org/packages/Shiny.AspNet.Webhooks) | 1.0.0 | aritchie,ShinyLib | Webhook signature verification and signing for ASP.NET Core - GitHub, Stripe, S… |
| 2026-10-12 19:23:37 | [Shiny.AspNet.CalDav](https://www.nuget.org/packages/Shiny.AspNet.CalDav) | 1.0.0 | aritchie,ShinyLib | CalDAV (RFC 4791) and CardDAV (RFC 6352) for ASP.NET Core - serve calendars and… |
| 2026-10-12 19:25:17 | [Shiny.Geofencing.Regions](https://www.nuget.org/packages/Shiny.Geofencing.Regions) | 6.1.0 | Allan Ritchie | Shiny Region Geofencing - GPS-driven geofencing over unlimited polygon, radius… |
| 2026-10-12 19:25:36 | [Shiny.Geofencing.Regions.DocumentDb](https://www.nuget.org/packages/Shiny.Geofencing.Regions.DocumentDb) | 6.1.0 | Allan Ritchie | Shiny Region Geofencing provider for Shiny.DocumentDb on SQLite - monitor polyg… |
| 2026-10-12 19:32:03 | [PdfPecker](https://www.nuget.org/packages/PdfPecker) | 1.0.0 | Moonwalker1307 | Fast, dependency-free HTML and Markdown to PDF converter for .NET. Its own HTML… |
| 2026-10-12 19:36:48 | [Glacier.Inference.Distributed.Cli](https://www.nuget.org/packages/Glacier.Inference.Distributed.Cli) | 1.1.0 | Ian Cowley | Command-line interface (glacier-distributed) for the Glacier Distributed MoE Cl… |
| 2026-10-12 19:36:49 | [Glacier.Inference.Distributed](https://www.nuget.org/packages/Glacier.Inference.Distributed) | 1.1.0 | Ian Cowley | Distributed heterogeneous pipeline inference, cluster activation transport, and… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
