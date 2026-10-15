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

## Latest list — 2026-10-15 21:22 UTC

New packages created between 2026-10-15 20:21 UTC and 2026-10-15 21:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-15T21-22-17-427951Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-15 20:22:28 | [RuleLoom](https://www.nuget.org/packages/RuleLoom) | 0.5.0 | Stefan Totev | RuleLoom: an event-driven business rule engine for .NET. Rules are written as J… |
| 2026-10-15 20:22:29 | [RuleLoom.Extensions.DependencyInjection](https://www.nuget.org/packages/RuleLoom.Extensions.DependencyInjection) | 0.5.0 | Stefan Totev | Microsoft.Extensions.DependencyInjection integration for RuleLoom: services.Add… |
| 2026-10-15 20:22:30 | [RuleLoom.Abstractions](https://www.nuget.org/packages/RuleLoom.Abstractions) | 0.5.0 | Stefan Totev | Contracts and models for RuleLoom: rule definitions, conditions, actions, resul… |
| 2026-10-15 20:30:12 | [AffluentAssertions](https://www.nuget.org/packages/AffluentAssertions) | 7.2.0 | Dennis Doomen,Jonas Nyrup | A very extensive set of extension methods that allow you to more naturally spec… |
| 2026-10-15 20:42:43 | [Themis.Common](https://www.nuget.org/packages/Themis.Common) | 1.0.0 | Rldc contributors | Shared request, response, and typed-answer contracts for the Themis library. |
| 2026-10-15 20:42:45 | [Themis.Core](https://www.nuget.org/packages/Themis.Core) | 1.0.0 | Rldc contributors | Decision routing and provider abstractions for applications built on Themis. |
| 2026-10-15 20:42:47 | [Themis.Inference](https://www.nuget.org/packages/Themis.Inference) | 1.0.0 | Rldc contributors | Prepared ONNX and Laya GGUF inference, bundle validation, and model packing for… |
| 2026-10-15 20:42:49 | [Themis.Inference.Ollama](https://www.nuget.org/packages/Themis.Inference.Ollama) | 1.0.0 | Rldc contributors | Ollama chat and System One inference without ONNX runtime dependencies. |
| 2026-10-15 20:42:51 | [Themis](https://www.nuget.org/packages/Themis) | 1.0.0 | Rldc contributors | Typed model decisions for .NET apps, with dependency-injection registration and… |
| 2026-10-15 20:42:53 | [Themis.Maf](https://www.nuget.org/packages/Themis.Maf) | 1.0.0 | Rldc contributors | Expose Themis conversational inference through Microsoft.Extensions.AI and Micr… |
| 2026-10-15 20:42:55 | [Themis.Inference.WinML](https://www.nuget.org/packages/Themis.Inference.WinML) | 1.0.0 | Rldc contributors | Optional Windows ML execution-provider integration for Themis ONNX inference. |
| 2026-10-15 20:44:59 | [ITSOL.Basal.Client](https://www.nuget.org/packages/ITSOL.Basal.Client) | 0.1.0 | IT SOL | HTTP client for the native Basal API, with typed decisions and asynchronous req… |
| 2026-10-15 20:45:24 | [Cackle.PrettyFluentMail](https://www.nuget.org/packages/Cackle.PrettyFluentMail) | 2.0.1 | Will Branch | Pretty HTML email from MJML and Scriban templates, composed with a Fluent API a… |
| 2026-10-15 20:45:25 | [Cackle.PrettyFluentMail.Extensions.DependencyInjection](https://www.nuget.org/packages/Cackle.PrettyFluentMail.Extensions.DependencyInjection) | 2.0.1 | Will Branch | Dependency injection for Cackle.PrettyFluentMail: one AddPrettyFluentMail call… |
| 2026-10-15 20:47:19 | [Pondhawk.Logging.Migration](https://www.nuget.org/packages/Pondhawk.Logging.Migration) | 1.0.62 | Pond Hawk Technologies Inc. | Roslyn analyzer and code fixes that rewrite Fabrica.Watch logging calls to Micr… |
| 2026-10-15 20:47:42 | [Haley.Helpers.Identity](https://www.nuget.org/packages/Haley.Helpers.Identity) | 0.1.0 | The Haley Project | Reusable accounts, credentials, MFA and opaque sessions with embedded or remote… |
| 2026-10-15 20:47:43 | [Haley.Helpers.Identity.Server](https://www.nuget.org/packages/Haley.Helpers.Identity.Server) | 0.1.0 | The Haley Project | Reusable accounts, credentials, MFA and opaque sessions with embedded or remote… |
| 2026-10-15 20:48:25 | [SyntaxCircus.Seo.Analysis](https://www.nuget.org/packages/SyntaxCircus.Seo.Analysis) | 0.1.1 | Syntax Circus LLC | Headless content preparation and focused SEO authoring analysis. |
| 2026-10-15 20:51:00 | [SteamKitSDK.Windows](https://www.nuget.org/packages/SteamKitSDK.Windows) | 0.9.1 | pat2381 | Windows desktop authentication helpers for SteamKitSDK, with UI-agnostic prompt… |
| 2026-10-15 20:51:01 | [SteamKitSDK](https://www.nuget.org/packages/SteamKitSDK) | 0.9.1 | pat2381 | Modern .NET SDK for authorized Steam application-content and Workshop downloads… |
| 2026-10-15 21:03:28 | [Cogito.MassTransit.DependencyInjection](https://www.nuget.org/packages/Cogito.MassTransit.DependencyInjection) | 3.1.0 | Alethic Solutions | Registers MassTransit consumers, sagas and activities from attributes, onto any… |
| 2026-10-15 21:03:29 | [Cogito.MassTransit.EntityFrameworkCore.DependencyInjection](https://www.nuget.org/packages/Cogito.MassTransit.EntityFrameworkCore.DependencyInjection) | 3.1.0 | Alethic Solutions | Keeps MassTransit saga instances in Entity Framework Core, registered from an a… |
| 2026-10-15 21:09:31 | [PA.CacheAside.Core](https://www.nuget.org/packages/PA.CacheAside.Core) | 1.0.0 | PA.CacheAside.Core | Package Description |
| 2026-10-15 21:16:01 | [DotCourier.SourceGenerator](https://www.nuget.org/packages/DotCourier.SourceGenerator) | 0.10.0 | Valossa515 | Compile-time registration for DotCourier: generates the handler registrations a… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
