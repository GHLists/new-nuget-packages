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

## Latest list — 2026-11-11 11:22 UTC

New packages created between 2026-11-11 10:21 UTC and 2026-11-11 11:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-11T11-22-00-650941Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-11 10:22:29 | [TechTeaStudio.Auth.OAuthServer](https://www.nuget.org/packages/TechTeaStudio.Auth.OAuthServer) | 0.13.0 | Ronald Ryan | OAuth 2.1 authorization server module for ASP.NET Core hosts: authorization cod… |
| 2026-11-11 10:22:31 | [TechTeaStudio.Auth.OAuthServer.EFCore](https://www.nuget.org/packages/TechTeaStudio.Auth.OAuthServer.EFCore) | 0.13.0 | Ronald Ryan | EF Core stores and fluent mapping for TechTeaStudio.Auth.OAuthServer: clients,… |
| 2026-11-11 10:23:15 | [SagaFlow.Core](https://www.nuget.org/packages/SagaFlow.Core) | 1.0.0 | Kemal Karadag | Core models and contracts for SagaFlow saga workflows. |
| 2026-11-11 10:23:36 | [SagaFlow.Engine](https://www.nuget.org/packages/SagaFlow.Engine) | 1.0.0 | Kemal Karadag | Process definition and execution engine for SagaFlow saga workflows. |
| 2026-11-11 10:24:24 | [Tinyeval](https://www.nuget.org/packages/Tinyeval) | 0.11.0 | tinyeval | Run your C# app's AI calls against tinyeval's test cases: a worker that answers… |
| 2026-11-11 10:24:25 | [Tinyeval.Tool](https://www.nuget.org/packages/Tinyeval.Tool) | 0.11.0 | tinyeval | The tinyeval command for .NET: runs the evals in evals/*.sh against your app an… |
| 2026-11-11 10:24:41 | [SagaFlow.Hosting](https://www.nuget.org/packages/SagaFlow.Hosting) | 1.0.0 | Kemal Karadag | ASP.NET Core hosting integration and embedded dashboard for SagaFlow. |
| 2026-11-11 10:25:02 | [SagaFlow.Messaging.RabbitMQ](https://www.nuget.org/packages/SagaFlow.Messaging.RabbitMQ) | 1.0.0 | Kemal Karadag | RabbitMQ messaging transport for SagaFlow saga workflows. |
| 2026-11-11 10:25:16 | [SagaFlow.Storage.InMemory](https://www.nuget.org/packages/SagaFlow.Storage.InMemory) | 1.0.0 | Kemal Karadag | In-memory state storage provider for SagaFlow saga workflows. |
| 2026-11-11 10:25:30 | [SagaFlow.Storage.PostgreSQL](https://www.nuget.org/packages/SagaFlow.Storage.PostgreSQL) | 1.0.0 | Kemal Karadag | PostgreSQL state storage provider for SagaFlow saga workflows. |
| 2026-11-11 10:28:56 | [Nordmann.LUI](https://www.nuget.org/packages/Nordmann.LUI) | 0.1.0-alpha | Nordmann | Autocomplete suggestions for .NET, straight out of your own SQLite database. FT… |
| 2026-11-11 10:28:57 | [Nordmann.LUI.Hosting](https://www.nuget.org/packages/Nordmann.LUI.Hosting) | 0.1.0-alpha | Nordmann | Nordmann.LUI in an ASP.NET Core or worker application: AddLui puts the catalog… |
| 2026-11-11 10:29:16 | [Jumoo.UmbracoAI.Translations](https://www.nuget.org/packages/Jumoo.UmbracoAI.Translations) | 17.3.0 | Jumoo | Installs Translation Manager, Umbraco.AI and the Translation Manager Umbraco.AI… |
| 2026-11-11 10:29:49 | [DwgIO](https://www.nuget.org/packages/DwgIO) | 0.4.0 | mahach666 | Reads Autodesk DWG drawings (.dwg) without AutoCAD and exposes sections, metada… |
| 2026-11-11 10:29:51 | [DwgIO.Cli](https://www.nuget.org/packages/DwgIO.Cli) | 0.4.0 | mahach666 | Command line tool that reads Autodesk DWG drawings (.dwg) without AutoCAD and w… |
| 2026-11-11 10:30:57 | [WithEffect.Frontend.Applications](https://www.nuget.org/packages/WithEffect.Frontend.Applications) | 10.0.18 | WithEffect.Services | WithEffect.Core assembles well-known packages for rapid application prototyping… |
| 2026-11-11 10:39:29 | [Srcmap.Probe.K7Q2](https://www.nuget.org/packages/Srcmap.Probe.K7Q2) | 1.0.0 | probe | Throwaway package for a package-source resolution test. Safe to ignore. One con… |
| 2026-11-11 10:41:05 | [Intropy.Testing.EndToEnd](https://www.nuget.org/packages/Intropy.Testing.EndToEnd) | 0.1.0 | Integrio | Helpers for end-to-end tests on the local Intropy environment (intropy-dev-env)… |
| 2026-11-11 10:44:00 | [Bibui.Glyphs](https://www.nuget.org/packages/Bibui.Glyphs) | 1.2.0 | Navisurg ApS | Bibui.Glyphs: glyphs as coverage masks, for a rasterizer that draws text itself… |
| 2026-11-11 10:44:03 | [OpenMoca.Reader.Extensions.AI](https://www.nuget.org/packages/OpenMoca.Reader.Extensions.AI) | 0.6.0 | MOCA Standard Contributors | Use any Microsoft.Extensions.AI embedding generator as a MOCA Reader embedder. |
| 2026-11-11 10:44:03 | [OpenMoca.Reader.Onnx](https://www.nuget.org/packages/OpenMoca.Reader.Onnx) | 0.6.0 | MOCA Standard Contributors | MOCA's standard embedding models (bge-small-en-v1.5, nomic-embed-text-v1.5, all… |
| 2026-11-11 10:44:04 | [OpenMoca.Reader.Sigstore](https://www.nuget.org/packages/OpenMoca.Reader.Sigstore) | 0.6.0 | MOCA Standard Contributors | Verify Sigstore-signed MOCA attestations offline, against a trusted root the ho… |
| 2026-11-11 10:44:06 | [OpenMoca.Reader.VectorData](https://www.nuget.org/packages/OpenMoca.Reader.VectorData) | 0.6.0 | MOCA Standard Contributors | Search MOCA packages through any Microsoft.Extensions.VectorData vector store,… |
| 2026-11-11 10:47:54 | [OpenDCP.Framework.ShareLink](https://www.nuget.org/packages/OpenDCP.Framework.ShareLink) | 0.1.0 | OpenDCP.Framework.ShareLink | Package Description |
| 2026-11-11 10:49:28 | [OpenDCP.Framework.Security](https://www.nuget.org/packages/OpenDCP.Framework.Security) | 0.2.0 | OpenDCP.Framework.Security | Package Description |
| 2026-11-11 10:53:04 | [HyperDev.Text.Json.Schema](https://www.nuget.org/packages/HyperDev.Text.Json.Schema) | 1.2.0 | Ivan Senatore, Wemake Informa… | JSON Schema Draft 7 validator. |
| 2026-11-11 10:53:19 | [HyperDev.Text.Json.Transform](https://www.nuget.org/packages/HyperDev.Text.Json.Transform) | 1.2.4 | Ivan Senatore, Wemake Informa… | HyperDev Fatum Framework: JsonTransform and the Newtonsoft.Json.Schema helpers… |
| 2026-11-11 11:08:41 | [TedToolkit.CppBindings.Manifold.Linux](https://www.nuget.org/packages/TedToolkit.CppBindings.Manifold.Linux) | 2026.11.11.109 | TedToolkit | Generated Manifold bindings and their native libraries for Linux x64. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
