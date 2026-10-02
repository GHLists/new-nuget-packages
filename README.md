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

## Latest list — 2026-10-02 22:20 UTC

New packages created between 2026-10-02 21:18 UTC and 2026-10-02 22:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-02T22-20-36-647929Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-02 21:43:40 | [PulseTrade.Comm.ResourceNode](https://www.nuget.org/packages/PulseTrade.Comm.ResourceNode) | 0.1.0-alpha1 | PulseTrade.Comm.ResourceNode | Package Description |
| 2026-10-02 21:49:09 | [Anton.SourceGeneration](https://www.nuget.org/packages/Anton.SourceGeneration) | 1.0.0 | Anton Curmanschii | Package Description |
| 2026-10-02 21:49:10 | [Anton.SourceGeneration.Sdk](https://www.nuget.org/packages/Anton.SourceGeneration.Sdk) | 1.1.0 | Anton Curmanschii | Package Description |
| 2026-10-02 21:49:11 | [Anton.SourceGeneration.PackageTesting](https://www.nuget.org/packages/Anton.SourceGeneration.PackageTesting) | 1.0.0 | Anton Curmanschii | Test NuGet packages in temporary consumer projects, including analyzer diagnost… |
| 2026-10-02 21:49:12 | [Anton.SourceGeneration.RoslynTesting](https://www.nuget.org/packages/Anton.SourceGeneration.RoslynTesting) | 1.0.0 | Anton Curmanschii | Build analyzer and code fix tests with typed diagnostic markers. |
| 2026-10-02 22:03:18 | [DynamicEndpoints.Sql](https://www.nuget.org/packages/DynamicEndpoints.Sql) | 0.4.0 | Pawel Pajak | Read-only, parameterized SQL query processor for DynamicEndpoints – works with… |
| 2026-10-02 22:03:19 | [DynamicEndpoints.Yaml](https://www.nuget.org/packages/DynamicEndpoints.Yaml) | 0.4.0 | Pawel Pajak | YAML for DynamicEndpoints: export and import definitions as YAML (GitOps) and i… |
| 2026-10-02 22:03:20 | [DynamicEndpoints.Templates](https://www.nuget.org/packages/DynamicEndpoints.Templates) | 0.4.0 | Pawel Pajak | dotnet new template for an ASP.NET Core minimal API with DynamicEndpoints: EF C… |
| 2026-10-02 22:03:21 | [DynamicEndpoints.OpenTelemetry](https://www.nuget.org/packages/DynamicEndpoints.OpenTelemetry) | 0.4.0 | Pawel Pajak | OpenTelemetry registration of the DynamicEndpoints metrics and traces: per-endp… |
| 2026-10-02 22:03:22 | [DynamicEndpoints.AdminUI](https://www.nuget.org/packages/DynamicEndpoints.AdminUI) | 0.4.0 | Pawel Pajak | Ready-made admin panel for DynamicEndpoints: list, editor (with caching, rate l… |
| 2026-10-02 22:03:23 | [DynamicEndpoints.Cli](https://www.nuget.org/packages/DynamicEndpoints.Cli) | 0.4.0 | Pawel Pajak | Command-line tool for DynamicEndpoints: list, export, diff and push endpoint de… |
| 2026-10-02 22:05:06 | [Soenneker.Librarian.Kv](https://www.nuget.org/packages/Soenneker.Librarian.Kv) | 4.0.54 | Jake Soenneker | Librarian document storage backed by Cloudflare Workers KV snapshots. |
| 2026-10-02 22:06:16 | [Syntrony.Wrapper](https://www.nuget.org/packages/Syntrony.Wrapper) | 1.0.0 | Syntrony Technologies Inc. | Applies Syntrony's Result<T> response contract to the ASP.NET Core pipeline: an… |
| 2026-10-02 22:14:18 | [Chameleon.Net.Extensions.Http](https://www.nuget.org/packages/Chameleon.Net.Extensions.Http) | 0.1.0 | Allan Mercou | IHttpClientFactory and dependency-injection integration for Chameleon.Net: http… |
| 2026-10-02 22:14:19 | [Chameleon.Net](https://www.nuget.org/packages/Chameleon.Net) | 0.1.0 | Allan Mercou | HttpClient handler and WebSocket connector whose TLS ClientHello, HTTP/2 frames… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
