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

## Latest list — 2026-11-26 10:20 UTC

New packages created between 2026-11-26 09:19 UTC and 2026-11-26 10:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T10-20-53-292087Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 09:28:37 | [Olax.Auditing.Messaging](https://www.nuget.org/packages/Olax.Auditing.Messaging) | 1.1.0 | OLAX Innovative Lab | Forwards a service's sealed audit entries to the central Audit.API through the… |
| 2026-11-26 09:55:43 | [EncoreBilisim.VisionSecurity.Sco](https://www.nuget.org/packages/EncoreBilisim.VisionSecurity.Sco) | 1.0.0 | Encore Bilisim | Self-checkout integration layer for EncoreBilisim.VisionSecurity. |
| 2026-11-26 10:02:25 | [Dor.Automations.MatchEngine.InMemory](https://www.nuget.org/packages/Dor.Automations.MatchEngine.InMemory) | 0.2.0 | dør | An in-memory alias store for the dør Match Engine SDK, held to the same conform… |
| 2026-11-26 10:02:26 | [Dor.Automations.MatchEngine.Grpc](https://www.nuget.org/packages/Dor.Automations.MatchEngine.Grpc) | 0.2.0 | dør | The dør Match Engine SDK's transport to the kernel over gRPC, with the contract… |
| 2026-11-26 10:02:27 | [Dor.Automations.MatchEngine.Hosting.Aspire](https://www.nuget.org/packages/Dor.Automations.MatchEngine.Hosting.Aspire) | 0.2.0 | dør | The dør Match Engine Kernel in an Aspire AppHost, from its published image or f… |
| 2026-11-26 10:02:27 | [Dor.Automations.MatchEngine.Testing](https://www.nuget.org/packages/Dor.Automations.MatchEngine.Testing) | 0.2.0 | dør | Test support for hosts of the dør Match Engine SDK: a scripted kernel, a manual… |
| 2026-11-26 10:02:28 | [Dor.Automations.MatchEngine.PostgreSql](https://www.nuget.org/packages/Dor.Automations.MatchEngine.PostgreSql) | 0.2.0 | dør | The dør Match Engine SDK's state in PostgreSQL: the alias, import and stored-do… |
| 2026-11-26 10:02:28 | [Dor.Automations.MatchEngine](https://www.nuget.org/packages/Dor.Automations.MatchEngine) | 0.2.0 | dør | The dør Match Engine SDK's core: document-line matching that learns from correc… |
| 2026-11-26 10:02:29 | [Dor.Automations.MatchEngine.Jev](https://www.nuget.org/packages/Dor.Automations.MatchEngine.Jev) | 0.2.0 | dør | Jev, through OpenRouter, as a decision model for the dør Match Engine SDK: sugg… |
| 2026-11-26 10:05:09 | [Qowaiv.Locale.NL](https://www.nuget.org/packages/Qowaiv.Locale.NL) | 11.0.0 | Ad van der Hoeven,Corniel Nob… | Qowaiv is a (Single) Value Object library. It aims to model reusable (Single) V… |
| 2026-11-26 10:06:24 | [minhson.uit.Ax2012](https://www.nuget.org/packages/minhson.uit.Ax2012) | 1.0.0 | minhson.uit | Microsoft Dynamics AX 2012 integration adapter for .NET: resilient WCF AIF NetT… |
| 2026-11-26 10:07:38 | [StudioElf.IssueTracker.Helpdesk](https://www.nuget.org/packages/StudioElf.IssueTracker.Helpdesk) | 1.0.0 | StudioElf | Optional headless bridge between StudioElf CRM Helpdesk tickets and Issue Track… |
| 2026-11-26 10:10:35 | [Eremex.Avalonia.Icons](https://www.nuget.org/packages/Eremex.Avalonia.Icons) | 1.5.86 | EREMEX JSC | SVG icon set for the Eremex Avalonia UI Controls. Ships the built-in icons used… |
| 2026-11-26 10:11:30 | [dlebansais.MpfrDotNet](https://www.nuget.org/packages/dlebansais.MpfrDotNet) | 1.1.0 | David Le Bansais | Binding of MPFR and MPIR (Multiple Precision Floating-Point and Integer) for .N… |
| 2026-11-26 10:12:01 | [dlebansais.MpfrDotNet-Debug](https://www.nuget.org/packages/dlebansais.MpfrDotNet-Debug) | 1.1.0 | David Le Bansais | Binding of MPFR and MPIR (Multiple Precision Floating-Point and Integer) for .N… |
| 2026-11-26 10:12:56 | [PlayGrifball.InfiniteSpartanRender.Client](https://www.nuget.org/packages/PlayGrifball.InfiniteSpartanRender.Client) | 0.1.42 | PlayGrifball | .NET client for the Infinite Spartan Render API: ask for a Halo Infinite Sparta… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
