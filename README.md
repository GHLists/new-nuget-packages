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

## Latest list — 2026-10-01 14:20 UTC

New packages created between 2026-10-01 13:20 UTC and 2026-10-01 14:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-01T14-20-59-988201Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-01 13:33:32 | [NetMurmurHash3](https://www.nuget.org/packages/NetMurmurHash3) | 1.0.0 | gitPhate | MurmurHash3 (x86_32, x64_128) for .NET 8/10, built on System.IO.Hashing. |
| 2026-10-01 13:44:51 | [makeITeasy.SystemDesign.BlazorTemplate](https://www.nuget.org/packages/makeITeasy.SystemDesign.BlazorTemplate) | 1.0.0 | makeITeasy | makeITeasy design system for Blazor Server applications: layout, navigation, Ra… |
| 2026-10-01 13:48:38 | [AngryMonkey.CDM.FormActions](https://www.nuget.org/packages/AngryMonkey.CDM.FormActions) | 8.2.5 | Angry Monkey | CDM build-time local and server form action discovery, extraction, and registra… |
| 2026-10-01 13:51:00 | [NBB.Application.Mediator](https://www.nuget.org/packages/NBB.Application.Mediator) | 10.1.0 | Totalsoft | Mediator (source generated mediator) integration for NBB applications: in-proce… |
| 2026-10-01 13:51:03 | [NBB.Application.Mediator.Effects](https://www.nuget.org/packages/NBB.Application.Mediator.Effects) | 10.1.0 | Totalsoft | Effects for sending requests and publishing notifications with Mediator (source… |
| 2026-10-01 13:51:38 | [NBB.Messaging.Mediator](https://www.nuget.org/packages/NBB.Messaging.Mediator) | 10.1.0 | Totalsoft | Mediator (source generated mediator) integration for the NBB messaging host: su… |
| 2026-10-01 13:51:40 | [NBB.Messaging.MediatR](https://www.nuget.org/packages/NBB.Messaging.MediatR) | 10.1.0 | Totalsoft | MediatR integration for the NBB messaging host: subscriber discovery from Media… |
| 2026-10-01 13:51:52 | [NBB.ProcessManager.Mediator](https://www.nuget.org/packages/NBB.ProcessManager.Mediator) | 10.1.0 | Totalsoft | Mediator (source generated mediator) integration for the NBB process manager: d… |
| 2026-10-01 13:51:54 | [NBB.ProcessManager.MediatR](https://www.nuget.org/packages/NBB.ProcessManager.MediatR) | 10.1.0 | Totalsoft | MediatR integration for the NBB process manager: dispatches MediatR notificatio… |
| 2026-10-01 13:51:57 | [NBB.ProjectR.Mediator](https://www.nuget.org/packages/NBB.ProjectR.Mediator) | 10.1.0 | Totalsoft | Mediator (source generated mediator) integration for NBB.ProjectR: dispatches M… |
| 2026-10-01 13:51:58 | [NBB.ProjectR.MediatR](https://www.nuget.org/packages/NBB.ProjectR.MediatR) | 10.1.0 | Totalsoft | MediatR integration for NBB.ProjectR: dispatches MediatR notifications to proje… |
| 2026-10-01 13:55:48 | [Aura3D.Pipeline.PBR.Common](https://www.nuget.org/packages/Aura3D.Pipeline.PBR.Common) | 0.0.5 | CeSun | Three Dimensional Control for Avalonia |
| 2026-10-01 13:55:48 | [Aura3D.Pipeline.PBRForward](https://www.nuget.org/packages/Aura3D.Pipeline.PBRForward) | 0.0.5 | CeSun | Three Dimensional Control for Avalonia |
| 2026-10-01 14:10:35 | [Gum.Topten.RichTextKit](https://www.nuget.org/packages/Gum.Topten.RichTextKit) | 0.4.167.1 | Topten Software, Victor Chela… | Temporary fork of Topten.RichTextKit 0.4.167 used by Gum.SkiaSharp, patched wit… |
| 2026-10-01 14:11:43 | [Argon2DotnetFast](https://www.nuget.org/packages/Argon2DotnetFast) | 1.0.0 | Marius Vitkevičius | Argon2id, Argon2i and Argon2d (RFC 9106) in managed C#, with AVX-512, AVX2, NEO… |
| 2026-10-01 14:12:20 | [DynamicEndpoints.EntityFrameworkCore](https://www.nuget.org/packages/DynamicEndpoints.EntityFrameworkCore) | 0.1.0 | Pawel Pajak | Entity Framework Core persistence for DynamicEndpoints definitions. |
| 2026-10-01 14:12:21 | [DynamicEndpoints.FluentValidation](https://www.nuget.org/packages/DynamicEndpoints.FluentValidation) | 0.1.0 | Pawel Pajak | Use FluentValidation validators as custom validators of DynamicEndpoints. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
