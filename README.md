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

## Latest list — 2026-11-12 10:20 UTC

New packages created between 2026-11-12 09:19 UTC and 2026-11-12 10:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-12T10-20-12-987255Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-12 09:26:58 | [Kai.Shared.Http](https://www.nuget.org/packages/Kai.Shared.Http) | 0.1.0 | Kai.Shared.Http | HTTP clients with scoped TLS trust, mutual TLS and opt-in safe retries. |
| 2026-11-12 09:27:02 | [Kai.Shared.Vault](https://www.nuget.org/packages/Kai.Shared.Vault) | 0.1.0 | Kai.Shared.Vault | Vault KV v1/v2 clients with Token and AppRole authentication. |
| 2026-11-12 09:27:04 | [Aml.Editor.Plugin.OpcUa](https://www.nuget.org/packages/Aml.Editor.Plugin.OpcUa) | 0.3.0 | Hamied Nabizada | OPC UA for the AutomationML Editor. Imports OPC UA NodeSets as AML libraries ac… |
| 2026-11-12 09:46:35 | [CleanArch.TemplatePack](https://www.nuget.org/packages/CleanArch.TemplatePack) | 1.0.0 | CleanArch | Multi-project .NET solution template modeled after the CleanArch layered archit… |
| 2026-11-12 09:54:09 | [GPUSharp](https://www.nuget.org/packages/GPUSharp) | 0.1.0 | Daniel Berki | Write GPU kernels in C#. Mark a scalar method with [GpuKernel] and call the gen… |
| 2026-11-12 09:57:44 | [Benevia.Core.Dashboards.Contracts](https://www.nuget.org/packages/Benevia.Core.Dashboards.Contracts) | 0.10.4 | Benevia Software | Dashboard JSON contracts shared by the Benevia Core dashboard server and Blazor… |
| 2026-11-12 09:59:05 | [UnambitiousFx.Synapse.ModelContextProtocol](https://www.nuget.org/packages/UnambitiousFx.Synapse.ModelContextProtocol) | 2.7.0 | UnambitiousFx | Model Context Protocol integration for UnambitiousFx.Synapse: exposes Synapse r… |
| 2026-11-12 10:02:56 | [Stil.Charts](https://www.nuget.org/packages/Stil.Charts) | 1.0.0 | Ludvig Andersson | Themeable SVG charts for Stil for Blazor: line, area, bar, donut and sparkline… |
| 2026-11-12 10:02:56 | [Stil.RichText](https://www.nuget.org/packages/Stil.RichText) | 1.0.0 | Ludvig Andersson | Rich text for Stil for Blazor: StilRichTextEditor writes formatted text with a… |
| 2026-11-12 10:02:57 | [Stil.Templates](https://www.nuget.org/packages/Stil.Templates) | 1.0.0 | Ludvig Andersson | dotnet new templates for Stil for Blazor: stil-app creates a Blazor Web App wit… |
| 2026-11-12 10:02:57 | [Stil.Markdown](https://www.nuget.org/packages/Stil.Markdown) | 1.0.0 | Ludvig Andersson | Markdown for Stil for Blazor: StilMarkdown renders Markdown safely with Stil's… |
| 2026-11-12 10:02:58 | [Stil](https://www.nuget.org/packages/Stil) | 1.0.0 | Ludvig Andersson | Themeable Blazor components built on the Stil CSS class library: forms with val… |
| 2026-11-12 10:12:01 | [TheDotSide.Aspire.IdentityServer.Client](https://www.nuget.org/packages/TheDotSide.Aspire.IdentityServer.Client) | 10.0.0 | The Dot Side | Optional, engine-independent OAuth client helpers: configuration binding, RS256… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
