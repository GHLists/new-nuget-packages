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

## Latest list — 2026-10-23 03:20 UTC

New packages created between 2026-10-23 02:21 UTC and 2026-10-23 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T03-20-07-779244Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 02:37:42 | [Lyo.Algorithms](https://www.nuget.org/packages/Lyo.Algorithms) | 3.0.0 | Matthew Wherry | Keyed algorithm registry: startup C# strategies, compile-once expressions, and… |
| 2026-10-23 02:37:45 | [Lyo.Algorithms.Api](https://www.nuget.org/packages/Lyo.Algorithms.Api) | 3.0.0 | Matthew Wherry | HTTP API surface for the Lyo algorithm catalog: definitions, revisions, revert,… |
| 2026-10-23 02:37:46 | [Lyo.Algorithms.Client](https://www.nuget.org/packages/Lyo.Algorithms.Client) | 3.0.0 | Matthew Wherry | HTTP client for the Lyo algorithm catalog API. |
| 2026-10-23 02:37:47 | [Lyo.Algorithms.Models](https://www.nuget.org/packages/Lyo.Algorithms.Models) | 3.0.0 | Matthew Wherry | Request and response DTOs and route constants for the Lyo Algorithms catalog AP… |
| 2026-10-23 02:37:48 | [Lyo.Algorithms.Postgres](https://www.nuget.org/packages/Lyo.Algorithms.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL catalog for Lyo.Algorithms. Schema algorithms, append-only revisions… |
| 2026-10-23 02:37:49 | [Lyo.Algorithms.Seed](https://www.nuget.org/packages/Lyo.Algorithms.Seed) | 3.0.0 | Matthew Wherry | EF seed of algorithm definitions, revisions, and labels. |
| 2026-10-23 02:37:50 | [Lyo.Algorithms.Sqlite](https://www.nuget.org/packages/Lyo.Algorithms.Sqlite) | 3.0.0 | Matthew Wherry | SQLite catalog for Lyo.Algorithms. Same IAlgorithmDefinitionStore as Postgres,… |
| 2026-10-23 02:37:51 | [Lyo.Algorithms.Web.Components](https://www.nuget.org/packages/Lyo.Algorithms.Web.Components) | 3.0.0 | Matthew Wherry | Blazor workbench for authoring algorithm revisions, typed context bags, and liv… |
| 2026-10-23 02:37:55 | [Lyo.Api.Export.Toml](https://www.nuget.org/packages/Lyo.Api.Export.Toml) | 3.0.0 | Matthew Wherry | TOML export format handler for Lyo.Api export service. |
| 2026-10-23 02:37:58 | [Lyo.Api.Export.Xml](https://www.nuget.org/packages/Lyo.Api.Export.Xml) | 3.0.0 | Matthew Wherry | XML export format handler for Lyo.Api export service. |
| 2026-10-23 02:37:59 | [Lyo.Api.Export.Yaml](https://www.nuget.org/packages/Lyo.Api.Export.Yaml) | 3.0.0 | Matthew Wherry | YAML export format handler for Lyo.Api export service. |
| 2026-10-23 02:38:01 | [Lyo.Api.Import](https://www.nuget.org/packages/Lyo.Api.Import) | 3.0.0 | Matthew Wherry | Import API for Lyo. JSON is built in. YAML, XML, TOML, CSV, and XLSX register a… |
| 2026-10-23 02:38:02 | [Lyo.Api.Import.Csv](https://www.nuget.org/packages/Lyo.Api.Import.Csv) | 3.0.0 | Matthew Wherry | CSV import format handler for Lyo.Api.Import. |
| 2026-10-23 02:38:04 | [Lyo.Api.Import.Toml](https://www.nuget.org/packages/Lyo.Api.Import.Toml) | 3.0.0 | Matthew Wherry | TOML import format handler for Lyo.Api.Import. |
| 2026-10-23 02:38:05 | [Lyo.Api.Import.Xlsx](https://www.nuget.org/packages/Lyo.Api.Import.Xlsx) | 3.0.0 | Matthew Wherry | XLSX import format handler for Lyo.Api.Import. |
| 2026-10-23 02:38:06 | [Lyo.Api.Import.Xml](https://www.nuget.org/packages/Lyo.Api.Import.Xml) | 3.0.0 | Matthew Wherry | XML import format handler for Lyo.Api.Import. |
| 2026-10-23 02:38:07 | [Lyo.Api.Import.Yaml](https://www.nuget.org/packages/Lyo.Api.Import.Yaml) | 3.0.0 | Matthew Wherry | YAML import format handler for Lyo.Api.Import. |
| 2026-10-23 02:38:08 | [Lyo.Audiobook](https://www.nuget.org/packages/Lyo.Audiobook) | 3.0.0 | Matthew Wherry | Domain contracts for an audiobook catalog: works, series, chapters, credits, id… |
| 2026-10-23 02:38:09 | [Lyo.Audiobook.Postgres](https://www.nuget.org/packages/Lyo.Audiobook.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL implementation of Lyo.Audiobook using Entity Framework Core. Stores… |
| 2026-10-23 02:38:10 | [Lyo.Audiobook.Seed](https://www.nuget.org/packages/Lyo.Audiobook.Seed) | 3.0.0 | Matthew Wherry | EF seed of audiobook genres, one series, and works with a narrator, an ISBN, an… |
| 2026-10-23 02:38:11 | [Lyo.Audiobook.Web.Components](https://www.nuget.org/packages/Lyo.Audiobook.Web.Components) | 3.0.0 | Matthew Wherry | Blazor components for browsing an audiobook catalog: search and work detail. |
| 2026-10-23 02:38:14 | [Lyo.Audit.Seed](https://www.nuget.org/packages/Lyo.Audit.Seed) | 3.0.0 | Matthew Wherry | EF seed of audit events and change rows. |
| 2026-10-23 02:38:18 | [Lyo.Authentication.Entra](https://www.nuget.org/packages/Lyo.Authentication.Entra) | 3.0.0 | Matthew Wherry | Microsoft Entra SAML profile for Lyo.Authentication.Saml. Uses the app federati… |
| 2026-10-23 02:38:21 | [Lyo.Authentication.Okta](https://www.nuget.org/packages/Lyo.Authentication.Okta) | 3.0.0 | Matthew Wherry | Okta SAML profile for Lyo.Authentication.Saml. Uses the public exk metadata URL… |
| 2026-10-23 02:38:24 | [Lyo.Authentication.Saml](https://www.nuget.org/packages/Lyo.Authentication.Saml) | 3.0.0 | Matthew Wherry | SAML 2.0 service provider for Lyo.Authentication.Sso. SP-initiated HTTP-Redirec… |
| 2026-10-23 02:38:25 | [Lyo.Authentication.Seed](https://www.nuget.org/packages/Lyo.Authentication.Seed) | 3.0.0 | Matthew Wherry | EF seed of local users, expired tokens, linked identities, claims, scopes, and… |
| 2026-10-23 02:38:26 | [Lyo.Authentication.Sso](https://www.nuget.org/packages/Lyo.Authentication.Sso) | 3.0.0 | Matthew Wherry | Protocol-neutral SSO host for Lyo.Authentication. Maps /auth login, callback, h… |
| 2026-10-23 02:38:30 | [Lyo.Authorization](https://www.nuget.org/packages/Lyo.Authorization) | 3.0.0 | Matthew Wherry | Resource grants. A check asks whether a subject may perform an action on a reso… |
| 2026-10-23 02:38:31 | [Lyo.Authorization.AspNetCore](https://www.nuget.org/packages/Lyo.Authorization.AspNetCore) | 3.0.0 | Matthew Wherry | ASP.NET Core grant authorization. RequireGrant works on controllers and minimal… |
| 2026-10-23 02:38:32 | [Lyo.Authorization.Postgres](https://www.nuget.org/packages/Lyo.Authorization.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL grant store. Schema authorization, table grant. One active row per s… |
| 2026-10-23 02:38:33 | [Lyo.Authorization.Web.Components](https://www.nuget.org/packages/Lyo.Authorization.Web.Components) | 3.0.0 | Matthew Wherry | Blazor grant list, editor, and check form. Talks to IGrantStore in-process. |
| 2026-10-23 02:38:34 | [Lyo.Avalonia.Components](https://www.nuget.org/packages/Lyo.Avalonia.Components) | 3.0.0 | Matthew Wherry | Shared Avalonia controls for Lyo desktop apps. Tool windows dock inside a windo… |
| 2026-10-23 02:38:38 | [Lyo.Billing](https://www.nuget.org/packages/Lyo.Billing) | 3.0.0 | Matthew Wherry | Billing contracts: unbilled charges, invoices, payments. Books change only by p… |
| 2026-10-23 02:38:39 | [Lyo.Billing.Api](https://www.nuget.org/packages/Lyo.Billing.Api) | 3.0.0 | Matthew Wherry | HTTP API surface for Lyo Billing: charges, invoices, issue/void/pay. No PDF. |
| 2026-10-23 02:38:40 | [Lyo.Billing.Client](https://www.nuget.org/packages/Lyo.Billing.Client) | 3.0.0 | Matthew Wherry | HTTP client for the Lyo Billing API. |
| 2026-10-23 02:38:41 | [Lyo.Billing.Postgres](https://www.nuget.org/packages/Lyo.Billing.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL storage for Lyo.Billing: charges, invoices, payments, and encrypted… |
| 2026-10-23 02:38:42 | [Lyo.Billing.Seed](https://www.nuget.org/packages/Lyo.Billing.Seed) | 3.0.0 | Matthew Wherry | EF seed of billing clients, each with one draft invoice and one line. |
| 2026-10-23 02:38:44 | [Lyo.Billing.Web.Components](https://www.nuget.org/packages/Lyo.Billing.Web.Components) | 3.0.0 | Matthew Wherry | Blazor billing dashboard: clients, charges, invoices, payments, and ledger view… |
| 2026-10-23 02:38:45 | [Lyo.Book](https://www.nuget.org/packages/Lyo.Book) | 3.0.0 | Matthew Wherry | Domain contracts for a library catalog: books, series, genres, types, formats,… |
| 2026-10-23 02:38:46 | [Lyo.Book.Postgres](https://www.nuget.org/packages/Lyo.Book.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL implementation of Lyo.Book using Entity Framework Core. Stores catal… |
| 2026-10-23 02:38:50 | [Lyo.ChangeTracker.Seed](https://www.nuget.org/packages/Lyo.ChangeTracker.Seed) | 3.0.0 | Matthew Wherry | EF seed of change tracker entries. |
| 2026-10-23 02:38:51 | [Lyo.ClamAv.Client](https://www.nuget.org/packages/Lyo.ClamAv.Client) | 3.0.0 | Matthew Wherry | HTTP client for a self-hosted clamav-rest scan service. |
| 2026-10-23 02:38:56 | [Lyo.Comment.Seed](https://www.nuget.org/packages/Lyo.Comment.Seed) | 3.0.0 | Matthew Wherry | EF seed of comments on a fixed seed subject. |
| 2026-10-23 02:39:08 | [Lyo.Config.Seed](https://www.nuget.org/packages/Lyo.Config.Seed) | 3.0.0 | Matthew Wherry | EF seed of plaintext config definitions and one binding each. |
| 2026-10-23 02:39:11 | [Lyo.ContactUs.Seed](https://www.nuget.org/packages/Lyo.ContactUs.Seed) | 3.0.0 | Matthew Wherry | EF seed of contact-form submissions. |
| 2026-10-23 02:39:13 | [Lyo.ContentThreatScan.ClamAv](https://www.nuget.org/packages/Lyo.ContentThreatScan.ClamAv) | 3.0.0 | Matthew Wherry | Maps clamav-rest scan verdicts into Lyo content-threat reputation envelopes. |
| 2026-10-23 02:39:18 | [Lyo.Desktop](https://www.nuget.org/packages/Lyo.Desktop) | 3.0.0 | Matthew Wherry | Shared desktop helpers for Linux and Windows apps: global hotkeys, clipboard, w… |
| 2026-10-23 02:39:21 | [Lyo.Diagram](https://www.nuget.org/packages/Lyo.Diagram) | 3.0.0 | Matthew Wherry | Build a diagram from pages and cells, and read or write it as an uncompressed o… |
| 2026-10-23 02:39:22 | [Lyo.Diagram.Models](https://www.nuget.org/packages/Lyo.Diagram.Models) | 3.0.0 | Matthew Wherry | Diagram contracts: pages, cells, geometry, and the store used to save them. |
| 2026-10-23 02:39:23 | [Lyo.Diagram.Postgres](https://www.nuget.org/packages/Lyo.Diagram.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL persistence for Lyo diagram documents (page and cell JSONB) using En… |
| 2026-10-23 02:39:27 | [Lyo.Discord.Seed](https://www.nuget.org/packages/Lyo.Discord.Seed) | 3.0.0 | Matthew Wherry | EF seed of Discord guilds and their users, members, channels, roles, emojis, me… |
| 2026-10-23 02:39:28 | [Lyo.Docx](https://www.nuget.org/packages/Lyo.Docx) | 3.0.0 | Matthew Wherry | Reads WordprocessingML documents and fills {Token} placeholders. |
| 2026-10-23 02:39:33 | [Lyo.Drift.Seed](https://www.nuget.org/packages/Lyo.Drift.Seed) | 3.0.0 | Matthew Wherry | EF seed of drift instances, structure snapshots, diffs, and change events. |
| 2026-10-23 02:39:36 | [Lyo.Email.Seed](https://www.nuget.org/packages/Lyo.Email.Seed) | 3.0.0 | Matthew Wherry | EF seed of email logs and attachment logs. |
| 2026-10-23 02:39:37 | [Lyo.Email.SendGrid](https://www.nuget.org/packages/Lyo.Email.SendGrid) | 3.0.0 | Matthew Wherry | Twilio SendGrid implementation of Lyo.Email. |
| 2026-10-23 02:39:38 | [Lyo.Email.Smtp](https://www.nuget.org/packages/Lyo.Email.Smtp) | 3.0.0 | Matthew Wherry | MailKit SMTP implementation of Lyo.Email. |
| 2026-10-23 02:39:44 | [Lyo.Endato.Seed](https://www.nuget.org/packages/Lyo.Endato.Seed) | 3.0.0 | Matthew Wherry | EF seed of Endato person-search and contact-enrichment queries. |
| 2026-10-23 02:39:50 | [Lyo.FantasyFootball](https://www.nuget.org/packages/Lyo.FantasyFootball) | 3.0.0 | Matthew Wherry | Fantasy football chats, trades, and league roster stored apart from the ESPN cl… |
| 2026-10-23 02:39:51 | [Lyo.FantasyFootball.Api](https://www.nuget.org/packages/Lyo.FantasyFootball.Api) | 3.0.0 | Matthew Wherry | HTTP API for fantasy football chats and trades. Reads the plugin store and sync… |
| 2026-10-23 02:39:52 | [Lyo.FantasyFootball.Postgres](https://www.nuget.org/packages/Lyo.FantasyFootball.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL persistence for fantasy football chats, trades, and rosters. Schema… |
| 2026-10-23 02:39:53 | [Lyo.FantasyFootball.Web.Components](https://www.nuget.org/packages/Lyo.FantasyFootball.Web.Components) | 3.0.0 | Matthew Wherry | Blazor workbench for fantasy football chats and trades. Talks to the FantasyFoo… |
| 2026-10-23 02:39:56 | [Lyo.Favorite.Seed](https://www.nuget.org/packages/Lyo.Favorite.Seed) | 3.0.0 | Matthew Wherry | EF seed of favorites on a fixed seed subject. |
| 2026-10-23 02:39:57 | [Lyo.FeatureFlags](https://www.nuget.org/packages/Lyo.FeatureFlags) | 3.0.0 | Matthew Wherry | Named feature flags for apps and hosts: on, off, percentage rollout, and caller… |
| 2026-10-23 02:39:58 | [Lyo.FeatureFlags.AspNetCore](https://www.nuget.org/packages/Lyo.FeatureFlags.AspNetCore) | 3.0.0 | Matthew Wherry | ASP.NET Core feature-flag gate. RequireFeature returns 404 when the flag is off. |
| 2026-10-23 02:39:59 | [Lyo.FeatureFlags.Web.Components](https://www.nuget.org/packages/Lyo.FeatureFlags.Web.Components) | 3.0.0 | Matthew Wherry | Blazor switch list and show/hide wrapper for feature flags. |
| 2026-10-23 02:40:00 | [Lyo.FileManager](https://www.nuget.org/packages/Lyo.FileManager) | 3.0.0 | Matthew Wherry | Desktop file manager session for a remote FileStorage API or a local disk store. |
| 2026-10-23 02:40:02 | [Lyo.FileMetadataStore.Seed](https://www.nuget.org/packages/Lyo.FileMetadataStore.Seed) | 3.0.0 | Matthew Wherry | EF seed of file metadata, blobs, revisions, audit events, multipart sessions, a… |
| 2026-10-23 02:40:12 | [Lyo.FileSystemWatcher.Seed](https://www.nuget.org/packages/Lyo.FileSystemWatcher.Seed) | 3.0.0 | Matthew Wherry | EF seed of file system watches, snapshots, and changes. |
| 2026-10-23 02:40:13 | [Lyo.FileTags](https://www.nuget.org/packages/Lyo.FileTags) | 3.0.0 | Matthew Wherry | Generic file tag catalog and dispatcher. Providers for audio, video, and pictur… |
| 2026-10-23 02:40:14 | [Lyo.FileTags.FFmpeg](https://www.nuget.org/packages/Lyo.FileTags.FFmpeg) | 3.0.0 | Matthew Wherry | ffprobe and stream-copy ffmpeg provider for audio and video file tags. |
| 2026-10-23 02:40:16 | [Lyo.FileTags.Images](https://www.nuget.org/packages/Lyo.FileTags.Images) | 3.0.0 | Matthew Wherry | EXIF provider for picture file tags. Pixel size and format stay on Lyo.Images. |
| 2026-10-23 02:40:18 | [Lyo.Formatter.Algorithms](https://www.nuget.org/packages/Lyo.Formatter.Algorithms) | 3.0.0 | Matthew Wherry | Formatter addon that evaluates Algo("key") and score("key") through Lyo.Algorit… |
| 2026-10-23 02:40:22 | [Lyo.Geolocation.Seed](https://www.nuget.org/packages/Lyo.Geolocation.Seed) | 3.0.0 | Matthew Wherry | EF seed of geolocation addresses. |
| 2026-10-23 02:40:24 | [Lyo.Google.Youtube.Client](https://www.nuget.org/packages/Lyo.Google.Youtube.Client) | 3.0.0 | Matthew Wherry | YouTube Data API client. Returns Lyo.Google.Youtube.Models types. |
| 2026-10-23 02:40:25 | [Lyo.Google.Youtube.Models](https://www.nuget.org/packages/Lyo.Google.Youtube.Models) | 3.0.0 | Matthew Wherry | YouTube Data API models: video links, videos, channels, and playlist items. |
| 2026-10-23 02:40:29 | [Lyo.HomeInventory.FileStorage](https://www.nuget.org/packages/Lyo.HomeInventory.FileStorage) | 3.0.0 | Matthew Wherry | Optional IFileStorageService helper that saves inventory attachments and writes… |
| 2026-10-23 02:40:30 | [Lyo.HomeInventory.Models](https://www.nuget.org/packages/Lyo.HomeInventory.Models) | 3.0.0 | Matthew Wherry | Shared request/response DTOs, enums, and route constants for the Lyo HomeInvent… |
| 2026-10-23 02:40:32 | [Lyo.HomeInventory.Seed](https://www.nuget.org/packages/Lyo.HomeInventory.Seed) | 3.0.0 | Matthew Wherry | EF seed of a home-inventory category, location, items, stock, and movements. |
| 2026-10-23 02:40:33 | [Lyo.HomeInventory.Web.Components](https://www.nuget.org/packages/Lyo.HomeInventory.Web.Components) | 3.0.0 | Matthew Wherry | Blazor / MudBlazor workbench for household inventory: items, rooms, categories,… |
| 2026-10-23 02:40:34 | [Lyo.Html](https://www.nuget.org/packages/Lyo.Html) | 3.0.0 | Matthew Wherry | Parses HTML, returns visible text, and sanitizes with an allowlist. |
| 2026-10-23 02:40:39 | [Lyo.Idempotency](https://www.nuget.org/packages/Lyo.Idempotency) | 3.0.0 | Matthew Wherry | Shared idempotency store. A scope and key claim one in-progress row; the same r… |
| 2026-10-23 02:40:40 | [Lyo.Idempotency.AspNetCore](https://www.nuget.org/packages/Lyo.Idempotency.AspNetCore) | 3.0.0 | Matthew Wherry | ASP.NET Core idempotency middleware. Place it after UseRouting. It honors Requi… |
| 2026-10-23 02:40:41 | [Lyo.Idempotency.Postgres](https://www.nuget.org/packages/Lyo.Idempotency.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL persistence for Lyo.Idempotency. Schema idempotency, table entry. AP… |
| 2026-10-23 02:40:50 | [Lyo.Job.Seed](https://www.nuget.org/packages/Lyo.Job.Seed) | 3.0.0 | Matthew Wherry | EF seed of disabled job definitions, one parameter and one schedule each. |
| 2026-10-23 02:40:53 | [Lyo.Job.Workers.Notification](https://www.nuget.org/packages/Lyo.Job.Workers.Notification) | 3.0.0 | Matthew Wherry | Job workers that send notifications as workflow steps: webhook POST, email, and… |
| 2026-10-23 02:40:54 | [Lyo.Json](https://www.nuget.org/packages/Lyo.Json) | 3.0.0 | Matthew Wherry | JSON parse and export for a typed document: file, stream, string, and bytes, ov… |
| 2026-10-23 02:40:57 | [Lyo.Law](https://www.nuget.org/packages/Lyo.Law) | 3.0.0 | Matthew Wherry | State statute store contract. Federal law is a separate database and is rejecte… |
| 2026-10-23 02:40:58 | [Lyo.Law.Api](https://www.nuget.org/packages/Lyo.Law.Api) | 3.0.0 | Matthew Wherry | HTTP API surface for state statutes: query, jurisdiction and code CRUD, and nod… |
| 2026-10-23 02:40:59 | [Lyo.Law.Client](https://www.nuget.org/packages/Lyo.Law.Client) | 3.0.0 | Matthew Wherry | HTTP client for Law node upsert, citation lookup, children, ancestors, and deta… |
| 2026-10-23 02:41:00 | [Lyo.Law.Models](https://www.nuget.org/packages/Lyo.Law.Models) | 3.0.0 | Matthew Wherry | Shared request/response DTOs, enums, and route constants for state statute stor… |
| 2026-10-23 02:41:01 | [Lyo.Law.Postgres](https://www.nuget.org/packages/Lyo.Law.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL storage for US state statutes (EF Core). Federal law is a separate d… |
| 2026-10-23 02:41:02 | [Lyo.Law.Seed](https://www.nuget.org/packages/Lyo.Law.Seed) | 3.0.0 | Matthew Wherry | EF seed of law jurisdictions, codes, nodes, annotations, and revisions. |
| 2026-10-23 02:41:03 | [Lyo.Law.Web.Components](https://www.nuget.org/packages/Lyo.Law.Web.Components) | 3.0.0 | Matthew Wherry | Blazor components for browsing and editing state statute nodes. |
| 2026-10-23 02:41:04 | [Lyo.Leaderboard](https://www.nuget.org/packages/Lyo.Leaderboard) | 3.0.0 | Matthew Wherry | Leaderboard domain: custom scoring properties, membership, invites, entries, an… |
| 2026-10-23 02:41:05 | [Lyo.Leaderboard.Api](https://www.nuget.org/packages/Lyo.Leaderboard.Api) | 3.0.0 | Matthew Wherry | HTTP API for Lyo.Leaderboard. Embed via AddLeaderboardApi / MapLeaderboardApiEn… |
| 2026-10-23 02:41:06 | [Lyo.Leaderboard.Api.Client](https://www.nuget.org/packages/Lyo.Leaderboard.Api.Client) | 3.0.0 | Matthew Wherry | HTTP client for the Lyo Leaderboard API. |
| 2026-10-23 02:41:07 | [Lyo.Leaderboard.Api.Models](https://www.nuget.org/packages/Lyo.Leaderboard.Api.Models) | 3.0.0 | Matthew Wherry | Wire contracts for the Lyo Leaderboard HTTP API. |
| 2026-10-23 02:41:08 | [Lyo.Leaderboard.Postgres](https://www.nuget.org/packages/Lyo.Leaderboard.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL persistence for Lyo.Leaderboard (boards, scoring properties, members… |
| 2026-10-23 02:41:09 | [Lyo.Leaderboard.Seed](https://www.nuget.org/packages/Lyo.Leaderboard.Seed) | 3.0.0 | Matthew Wherry | EF seed of leaderboard boards, members, entries, and standings. |
| 2026-10-23 02:41:12 | [Lyo.Leaderboard.Web.Components](https://www.nuget.org/packages/Lyo.Leaderboard.Web.Components) | 3.0.0 | Matthew Wherry | Blazor / MudBlazor dashboard for Lyo.Leaderboard. Add LeaderboardManagement to… |
| 2026-10-23 02:41:14 | [Lyo.Ledger](https://www.nuget.org/packages/Lyo.Ledger) | 3.0.0 | Matthew Wherry | Double-entry ledger contracts: chart of accounts, journals, post/void, and clie… |
| 2026-10-23 02:41:15 | [Lyo.Ledger.Api](https://www.nuget.org/packages/Lyo.Ledger.Api) | 3.0.0 | Matthew Wherry | HTTP API surface for Lyo Ledger: chart of accounts, journals, post/void, and AR… |
| 2026-10-23 02:41:16 | [Lyo.Ledger.Postgres](https://www.nuget.org/packages/Lyo.Ledger.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL storage for Lyo.Ledger (EF Core): chart of accounts, journals, and j… |
| 2026-10-23 02:41:17 | [Lyo.Ledger.Seed](https://www.nuget.org/packages/Lyo.Ledger.Seed) | 3.0.0 | Matthew Wherry | EF seed of a cash account, a revenue account, and balanced journals. |
| 2026-10-23 02:41:27 | [Lyo.Music](https://www.nuget.org/packages/Lyo.Music) | 3.0.0 | Matthew Wherry | Domain contracts for a music catalog: release groups, releases, tracks, credits… |
| 2026-10-23 02:41:28 | [Lyo.Music.Postgres](https://www.nuget.org/packages/Lyo.Music.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL implementation of Lyo.Music using Entity Framework Core. Stores rele… |
| 2026-10-23 02:41:29 | [Lyo.Music.Seed](https://www.nuget.org/packages/Lyo.Music.Seed) | 3.0.0 | Matthew Wherry | EF seed of music genres, formats, release groups, releases, tracks, and credits. |
| 2026-10-23 02:41:30 | [Lyo.Music.Web.Components](https://www.nuget.org/packages/Lyo.Music.Web.Components) | 3.0.0 | Matthew Wherry | Blazor components for browsing music releases: search and a release detail with… |
| 2026-10-23 02:41:31 | [Lyo.Nfc](https://www.nuget.org/packages/Lyo.Nfc) | 3.0.0 | Matthew Wherry | Type 2 NFC tag access and NDEF read/write. Page I/O is behind INfcTag so a PC/S… |
| 2026-10-23 02:41:32 | [Lyo.Nfc.Pcsc](https://www.nuget.org/packages/Lyo.Nfc.Pcsc) | 3.0.0 | Matthew Wherry | PC/SC driver for Lyo.Nfc. Reads and writes Type 2 pages through an ACR122U-styl… |
| 2026-10-23 02:41:35 | [Lyo.Note.Seed](https://www.nuget.org/packages/Lyo.Note.Seed) | 3.0.0 | Matthew Wherry | EF seed of notes on a fixed seed subject. |
| 2026-10-23 02:41:36 | [Lyo.OpenSubtitles.Client](https://www.nuget.org/packages/Lyo.OpenSubtitles.Client) | 3.0.0 | Matthew Wherry | Typed HTTP client for the OpenSubtitles consumer REST API. |
| 2026-10-23 02:41:37 | [Lyo.Outbox](https://www.nuget.org/packages/Lyo.Outbox) | 3.0.0 | Matthew Wherry | Outbox contract. Enqueue records a message on the caller's transaction. Publish… |
| 2026-10-23 02:41:38 | [Lyo.Outbox.Dispatcher](https://www.nuget.org/packages/Lyo.Outbox.Dispatcher) | 3.0.0 | Matthew Wherry | Outbox dispatcher. Claims due rows from the idempotency store and publishes the… |
| 2026-10-23 02:41:39 | [Lyo.Outbox.Postgres](https://www.nuget.org/packages/Lyo.Outbox.Postgres) | 3.0.0 | Matthew Wherry | Postgres outbox. Enqueue writes kind=outbox through the shared idempotency stor… |
| 2026-10-23 02:41:42 | [Lyo.PackageMetadata.Seed](https://www.nuget.org/packages/Lyo.PackageMetadata.Seed) | 3.0.0 | Matthew Wherry | EF seed of package metadata rows and stack prefixes. |
| 2026-10-23 02:41:44 | [Lyo.Payments](https://www.nuget.org/packages/Lyo.Payments) | 3.0.0 | Matthew Wherry | Payment collector contracts and an internal (non-Stripe) implementation for wor… |
| 2026-10-23 02:41:50 | [Lyo.Podcast](https://www.nuget.org/packages/Lyo.Podcast) | 3.0.0 | Matthew Wherry | Domain contracts for a podcast catalog: shows, seasons, episodes, credits, iden… |
| 2026-10-23 02:41:51 | [Lyo.Podcast.Postgres](https://www.nuget.org/packages/Lyo.Podcast.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL implementation of Lyo.Podcast using Entity Framework Core. Stores sh… |
| 2026-10-23 02:41:52 | [Lyo.Podcast.Seed](https://www.nuget.org/packages/Lyo.Podcast.Seed) | 3.0.0 | Matthew Wherry | EF seed of podcast genres, one show, a season, and two episodes. |
| 2026-10-23 02:41:53 | [Lyo.Podcast.Web.Components](https://www.nuget.org/packages/Lyo.Podcast.Web.Components) | 3.0.0 | Matthew Wherry | Blazor components for browsing a podcast catalog: search and show detail. |
| 2026-10-23 02:42:01 | [Lyo.Query.Postgres](https://www.nuget.org/packages/Lyo.Query.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL translation for Lyo.Query Fuzzy operators via pg_trgm similarity(). |
| 2026-10-23 02:42:02 | [Lyo.Query.Sql](https://www.nuget.org/packages/Lyo.Query.Sql) | 3.0.0 | Matthew Wherry | Translates Lyo concrete, projection, and root query requests into parameterized… |
| 2026-10-23 02:42:04 | [Lyo.RateLimit](https://www.nuget.org/packages/Lyo.RateLimit) | 3.0.0 | Matthew Wherry | Quota rate limiting for a single process: fixed window, sliding window, and tok… |
| 2026-10-23 02:42:05 | [Lyo.RateLimit.Redis](https://www.nuget.org/packages/Lyo.RateLimit.Redis) | 3.0.0 | Matthew Wherry | Redis quota store. Same fixed, sliding, and token-bucket rules as Lyo.RateLimit… |
| 2026-10-23 02:42:07 | [Lyo.Rating.Seed](https://www.nuget.org/packages/Lyo.Rating.Seed) | 3.0.0 | Matthew Wherry | EF seed of ratings on a fixed seed subject. |
| 2026-10-23 02:42:08 | [Lyo.Recipe](https://www.nuget.org/packages/Lyo.Recipe) | 3.0.0 | Matthew Wherry | Household recipes: catalog ingredients, ordered steps, hierarchical categories,… |
| 2026-10-23 02:42:09 | [Lyo.Recipe.Api](https://www.nuget.org/packages/Lyo.Recipe.Api) | 3.0.0 | Matthew Wherry | HTTP API surface for Lyo Recipe: categories, ingredients, recipes, lines, steps… |
| 2026-10-23 02:42:10 | [Lyo.Recipe.Client](https://www.nuget.org/packages/Lyo.Recipe.Client) | 3.0.0 | Matthew Wherry | HTTP client for extra Recipe routes: ingredient lines, steps, notes, tags, and… |
| 2026-10-23 02:42:11 | [Lyo.Recipe.FileStorage](https://www.nuget.org/packages/Lyo.Recipe.FileStorage) | 3.0.0 | Matthew Wherry | Optional IFileStorageService helper that saves recipe attachments and writes Re… |
| 2026-10-23 02:42:13 | [Lyo.Recipe.Models](https://www.nuget.org/packages/Lyo.Recipe.Models) | 3.0.0 | Matthew Wherry | Shared request/response DTOs, enums, and route constants for the Lyo Recipe API… |
| 2026-10-23 02:42:13 | [Lyo.Recipe.Postgres](https://www.nuget.org/packages/Lyo.Recipe.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL storage for Lyo.Recipe (EF Core): recipes, ingredients, categories,… |
| 2026-10-23 02:42:15 | [Lyo.Recipe.Seed](https://www.nuget.org/packages/Lyo.Recipe.Seed) | 3.0.0 | Matthew Wherry | EF seed of a recipe category, ingredients, recipes, lines, steps, links, and at… |
| 2026-10-23 02:42:16 | [Lyo.Recipe.Web.Components](https://www.nuget.org/packages/Lyo.Recipe.Web.Components) | 3.0.0 | Matthew Wherry | Blazor / MudBlazor workbench for household recipes: recipes, ingredients, categ… |
| 2026-10-23 02:42:17 | [RecursiveAI.OneImage.Svg](https://www.nuget.org/packages/RecursiveAI.OneImage.Svg) | 1.3.0 | Recursive AI, LLC | SVG support for OneImage: reads static SVG (shapes, paths, gradients, patterns,… |
| 2026-10-23 02:42:19 | [Lyo.Reporting.Seed](https://www.nuget.org/packages/Lyo.Reporting.Seed) | 3.0.0 | Matthew Wherry | EF seed of the report design sample definitions. |
| 2026-10-23 02:42:22 | [Lyo.RequestSigning](https://www.nuget.org/packages/Lyo.RequestSigning) | 3.0.0 | Matthew Wherry | Timestamped HMAC request signatures. The HMAC key comes from configuration. |
| 2026-10-23 02:42:23 | [Lyo.RequestSigning.AspNetCore](https://www.nuget.org/packages/Lyo.RequestSigning.AspNetCore) | 3.0.0 | Matthew Wherry | ASP.NET Core middleware that checks a timestamped HMAC request signature. |
| 2026-10-23 02:42:25 | [Lyo.Rfid](https://www.nuget.org/packages/Lyo.Rfid) | 3.0.0 | Matthew Wherry | ISO 15693 RFID access. IRfidTag reads and writes blocks. IIso15693Transceiver s… |
| 2026-10-23 02:42:26 | [Lyo.Rfid.Tonie](https://www.nuget.org/packages/Lyo.Rfid.Tonie) | 3.0.0 | Matthew Wherry | Toniebox SLIX-L helpers: UID content path, privacy-password XOR from the tag ra… |
| 2026-10-23 02:42:31 | [Lyo.Screenshot](https://www.nuget.org/packages/Lyo.Screenshot) | 3.0.0 | Matthew Wherry | Region screen capture for Linux and Windows, with still PNG, animated GIF, and… |
| 2026-10-23 02:42:32 | [Lyo.Search.Postgres](https://www.nuget.org/packages/Lyo.Search.Postgres) | 3.0.0 | Matthew Wherry | Shared Postgres full-text mapping: a stored tsvector column and a GIN index. |
| 2026-10-23 02:42:36 | [Lyo.ShortUrl.Seed](https://www.nuget.org/packages/Lyo.ShortUrl.Seed) | 3.0.0 | Matthew Wherry | EF seed of short URLs and one click each. |
| 2026-10-23 02:42:40 | [Lyo.Sms.Seed](https://www.nuget.org/packages/Lyo.Sms.Seed) | 3.0.0 | Matthew Wherry | EF seed of SMS logs. |
| 2026-10-23 02:42:42 | [Lyo.Sms.Twilio.Seed](https://www.nuget.org/packages/Lyo.Sms.Twilio.Seed) | 3.0.0 | Matthew Wherry | EF seed of Twilio SMS logs. |
| 2026-10-23 02:42:44 | [Lyo.StateMachine](https://www.nuget.org/packages/Lyo.StateMachine) | 3.0.0 | Matthew Wherry | Strongly typed, reusable state machine: immutable definitions with typed trigge… |
| 2026-10-23 02:42:45 | [Lyo.StateMachine.Models](https://www.nuget.org/packages/Lyo.StateMachine.Models) | 3.0.0 | Matthew Wherry | Contracts for Lyo state machines: versioned state snapshots, transition results… |
| 2026-10-23 02:42:46 | [Lyo.StateMachine.Postgres](https://www.nuget.org/packages/Lyo.StateMachine.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL state store for Lyo state machines with optimistic concurrency and t… |
| 2026-10-23 02:42:47 | [Lyo.StateMachine.Seed](https://www.nuget.org/packages/Lyo.StateMachine.Seed) | 3.0.0 | Matthew Wherry | EF seed of state machine definitions, instances, and transitions. |
| 2026-10-23 02:42:49 | [Lyo.Story](https://www.nuget.org/packages/Lyo.Story) | 3.0.0 | Matthew Wherry | Play-graph contracts for interactive stories and quests: nodes, choices, named… |
| 2026-10-23 02:42:50 | [Lyo.Story.Api](https://www.nuget.org/packages/Lyo.Story.Api) | 3.0.0 | Matthew Wherry | HTTP API surface for Lyo Story: graph CRUD, playthrough play routes, and aggreg… |
| 2026-10-23 02:42:51 | [Lyo.Story.Client](https://www.nuget.org/packages/Lyo.Story.Client) | 3.0.0 | Matthew Wherry | HTTP client for the Lyo Story API: graph save and load, delete, and play. |
| 2026-10-23 02:42:53 | [Lyo.Story.Models](https://www.nuget.org/packages/Lyo.Story.Models) | 3.0.0 | Matthew Wherry | Request and response DTOs and route constants for the Lyo Story API. |
| 2026-10-23 02:42:54 | [Lyo.Story.Postgres](https://www.nuget.org/packages/Lyo.Story.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL implementation of Lyo.Story using Entity Framework Core. Stores play… |
| 2026-10-23 02:42:55 | [Lyo.Story.Sqlite](https://www.nuget.org/packages/Lyo.Story.Sqlite) | 3.0.0 | Matthew Wherry | Local SQLite storage for Lyo.Story (EF Core): the same story graph and playthro… |
| 2026-10-23 02:42:58 | [Lyo.Story.Web.Components](https://www.nuget.org/packages/Lyo.Story.Web.Components) | 3.0.0 | Matthew Wherry | Blazor story builder for the Lyo Story API: library, play graph, and playthroug… |
| 2026-10-23 02:43:02 | [Lyo.Tag.Seed](https://www.nuget.org/packages/Lyo.Tag.Seed) | 3.0.0 | Matthew Wherry | EF seed of tags on a fixed seed subject. |
| 2026-10-23 02:43:04 | [Lyo.Toml](https://www.nuget.org/packages/Lyo.Toml) | 3.0.0 | Matthew Wherry | TOML parse and export for a typed document, and conversion to and from JSON, ov… |
| 2026-10-23 02:43:05 | [Lyo.Trakt.Client](https://www.nuget.org/packages/Lyo.Trakt.Client) | 3.0.0 | Matthew Wherry | Typed HTTP client for the Trakt catalog and OAuth APIs. |
| 2026-10-23 02:43:17 | [Lyo.Validation.Seed](https://www.nuget.org/packages/Lyo.Validation.Seed) | 3.0.0 | Matthew Wherry | EF seed of validation schemas. |
| 2026-10-23 02:43:18 | [Lyo.Video](https://www.nuget.org/packages/Lyo.Video) | 3.0.0 | Matthew Wherry | Domain contracts for a movie and television catalog: titles, seasons, episodes,… |
| 2026-10-23 02:43:19 | [Lyo.Video.Postgres](https://www.nuget.org/packages/Lyo.Video.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL implementation of Lyo.Video using Entity Framework Core. Stores movi… |
| 2026-10-23 02:43:21 | [Lyo.Video.Seed](https://www.nuget.org/packages/Lyo.Video.Seed) | 3.0.0 | Matthew Wherry | EF seed of video genres, a collection, and series titles with seasons and episo… |
| 2026-10-23 02:43:22 | [Lyo.Video.Web.Components](https://www.nuget.org/packages/Lyo.Video.Web.Components) | 3.0.0 | Matthew Wherry | Blazor components for browsing movies and series: search, season and episode li… |
| 2026-10-23 02:43:24 | [Lyo.Web.Automation.Api](https://www.nuget.org/packages/Lyo.Web.Automation.Api) | 3.0.0 | Matthew Wherry | HTTP API that runs an automation plan on a host-supplied browser session and se… |
| 2026-10-23 02:43:25 | [Lyo.Web.Automation.Client](https://www.nuget.org/packages/Lyo.Web.Automation.Client) | 3.0.0 | Matthew Wherry | HTTP client for starting an automation plan run and reading its log and viewpor… |
| 2026-10-23 02:43:26 | [Lyo.Web.Automation.FileStorage](https://www.nuget.org/packages/Lyo.Web.Automation.FileStorage) | 3.0.0 | Matthew Wherry | Stores automation step screenshots through a host-configured IFileStorageServic… |
| 2026-10-23 02:43:28 | [Lyo.Web.Automation.Postgres](https://www.nuget.org/packages/Lyo.Web.Automation.Postgres) | 3.0.0 | Matthew Wherry | PostgreSQL store for automation plans, with a query endpoint for the plan grid. |
| 2026-10-23 02:43:29 | [Lyo.Web.Automation.PuppeteerSharp](https://www.nuget.org/packages/Lyo.Web.Automation.PuppeteerSharp) | 3.0.0 | Matthew Wherry | PuppeteerSharp automation: Chromium sessions, tabs, frames, dialogs, keyboard h… |
| 2026-10-23 02:43:31 | [Lyo.Web.Automation.Web.Components](https://www.nuget.org/packages/Lyo.Web.Automation.Web.Components) | 3.0.0 | Matthew Wherry | Blazor workbench for editing an automation plan and running it through the auto… |
| 2026-10-23 02:43:34 | [Lyo.Web.Components.Export.Toml](https://www.nuget.org/packages/Lyo.Web.Components.Export.Toml) | 3.0.0 | Matthew Wherry | TOML export menu item for Lyo data grids. |
| 2026-10-23 02:43:36 | [Lyo.Web.Components.Export.Xml](https://www.nuget.org/packages/Lyo.Web.Components.Export.Xml) | 3.0.0 | Matthew Wherry | XML export menu item for Lyo data grids. |
| 2026-10-23 02:43:37 | [Lyo.Web.Components.Export.Yaml](https://www.nuget.org/packages/Lyo.Web.Components.Export.Yaml) | 3.0.0 | Matthew Wherry | YAML export menu item for Lyo data grids. |
| 2026-10-23 02:43:38 | [Lyo.Web.Components.Import](https://www.nuget.org/packages/Lyo.Web.Components.Import) | 3.0.0 | Matthew Wherry | Import preview UI. JSON is built in. The host persists returned rows. |
| 2026-10-23 02:43:39 | [Lyo.Web.Components.Import.Csv](https://www.nuget.org/packages/Lyo.Web.Components.Import.Csv) | 3.0.0 | Matthew Wherry | CSV format choice for the import workbench. |
| 2026-10-23 02:43:41 | [Lyo.Web.Components.Import.Toml](https://www.nuget.org/packages/Lyo.Web.Components.Import.Toml) | 3.0.0 | Matthew Wherry | TOML format choice for the import workbench. |
| 2026-10-23 02:43:42 | [Lyo.Web.Components.Import.Xlsx](https://www.nuget.org/packages/Lyo.Web.Components.Import.Xlsx) | 3.0.0 | Matthew Wherry | XLSX format choice for the import workbench. |
| 2026-10-23 02:43:43 | [Lyo.Web.Components.Import.Xml](https://www.nuget.org/packages/Lyo.Web.Components.Import.Xml) | 3.0.0 | Matthew Wherry | XML format choice for the import workbench. |
| 2026-10-23 02:43:46 | [Lyo.Web.WebRenderer.Models](https://www.nuget.org/packages/Lyo.Web.WebRenderer.Models) | 3.0.0 | Matthew Wherry | Serializable HTML capture request and response for Lyo.Web.WebRenderer. No Blaz… |
| 2026-10-23 02:43:49 | [Lyo.Yaml](https://www.nuget.org/packages/Lyo.Yaml) | 3.0.0 | Matthew Wherry | YAML parse and export for a typed document, and conversion to and from JSON, ov… |
| 2026-10-23 03:08:05 | [VBaseFramework.Core.Contracts](https://www.nuget.org/packages/VBaseFramework.Core.Contracts) | 0.0.1 | VBaseFramework.Core.Contracts | Package Description |
| 2026-10-23 03:09:58 | [Lyo.Web.Components.Import.Yaml](https://www.nuget.org/packages/Lyo.Web.Components.Import.Yaml) | 3.0.0 | Matthew Wherry | YAML format choice for the import workbench. |
| 2026-10-23 03:10:00 | [Lyo.Xml](https://www.nuget.org/packages/Lyo.Xml) | 3.0.0 | Matthew Wherry | XML parse and export for a typed document, and conversion to and from JSON, ove… |
| 2026-10-23 03:11:34 | [CYS.Extensions.Hosting.Testing](https://www.nuget.org/packages/CYS.Extensions.Hosting.Testing) | 1.0.0 | Chris Trout | Provides integration testing support for applications built on the .NET Generic… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
