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

## Latest list — 2026-10-29 13:21 UTC

New packages created between 2026-10-29 12:20 UTC and 2026-10-29 13:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-29T13-21-59-820342Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-29 12:23:46 | [Mnml.Sdk](https://www.nuget.org/packages/Mnml.Sdk) | 0.1.0 | mnml | The official .NET client for the mnml API: architecture renders, edits, enhance… |
| 2026-10-29 12:24:22 | [IODream.Vault.CLI](https://www.nuget.org/packages/IODream.Vault.CLI) | 0.6.1 | IODream | IODream Vault command line. Sign in, then run any app with its secrets as envir… |
| 2026-10-29 12:24:23 | [IODream.Vault.NET](https://www.nuget.org/packages/IODream.Vault.NET) | 1.0.4 | IODream | Loads IODream Vault app secrets into .NET configuration (IConfiguration), so Ge… |
| 2026-10-29 12:42:19 | [RoeiRedler.XTB.FlowsInspector](https://www.nuget.org/packages/RoeiRedler.XTB.FlowsInspector) | 1.2026.10.29 | Roei Redler | Flows Inspector reads all cloud flows of the connected Dataverse environment an… |
| 2026-10-29 12:43:49 | [Cloudflare.Kit.Api](https://www.nuget.org/packages/Cloudflare.Kit.Api) | 3.7.0.2 | Alos Engineering | Independently maintained Cloudflare.Kit fork of Alos-no/Cloudflare.NET API 3.7.… |
| 2026-10-29 12:43:50 | [Cloudflare.Kit.R2](https://www.nuget.org/packages/Cloudflare.Kit.R2) | 2.5.0.1 | Alos Engineering | Independently maintained Cloudflare.Kit fork of Alos-no/Cloudflare.NET.R2 2.5.0… |
| 2026-10-29 12:43:51 | [Cloudflare.Kit](https://www.nuget.org/packages/Cloudflare.Kit) | 0.1.3 | Cloudflare.Kit | Cloudflare clients for DNS, KV, D1, R2, Tunnel management and Worker uploads. |
| 2026-10-29 12:44:21 | [BorrowedTorch.Ormh](https://www.nuget.org/packages/BorrowedTorch.Ormh) | 1.0.0 | Vladyslav Pysarenko | Packs ambient occlusion, roughness, metallic and height into one RGBA texture:… |
| 2026-10-29 12:48:13 | [Rotex.Rtm](https://www.nuget.org/packages/Rotex.Rtm) | 1.0.0 | Rotex.Agora | Package Description |
| 2026-10-29 12:48:52 | [Monq.Core.MicroserviceAddressing](https://www.nuget.org/packages/Monq.Core.MicroserviceAddressing) | 0.1.0 | MONQ Digital lab | Shared microservice address resolution policies for MONQ applications. |
| 2026-10-29 12:54:15 | [Uniform.Matrix.WebRtc](https://www.nuget.org/packages/Uniform.Matrix.WebRtc) | 0.1.8-rc3 | Uniform.Matrix.WebRtc | A WebRTC subset in pure C# for voice calls: SDP, STUN, TURN, ICE, DTLS-SRTP and… |
| 2026-10-29 12:54:17 | [Uniform.Matrix.Audio](https://www.nuget.org/packages/Uniform.Matrix.Audio) | 0.1.8-rc3 | Uniform.Matrix.Audio | Voice audio for Matrix calls: Opus encoding and decoding, 20 ms voice frames fr… |
| 2026-10-29 12:54:17 | [Uniform.Matrix.Calls](https://www.nuget.org/packages/Uniform.Matrix.Calls) | 0.1.8-rc3 | Uniform.Matrix.Calls | Matrix 1:1 voice calls (m.call.*) for the Uniform.Matrix client engine: signall… |
| 2026-10-29 12:54:32 | [BorrowedTorch.ContentPipeline](https://www.nuget.org/packages/BorrowedTorch.ContentPipeline) | 1.0.0 | Vladyslav Pysarenko | A MonoGame content pipeline extension that builds ORMH textures - ambient occlu… |
| 2026-10-29 12:56:45 | [BirthdayWebsite.UrlTools](https://www.nuget.org/packages/BirthdayWebsite.UrlTools) | 0.1.0 | wangneo276-lgtm | Birthday Website Maker helps you create a personalized birthday website with ph… |
| 2026-10-29 12:58:27 | [Tharga.Team.Support.OpenAI](https://www.nuget.org/packages/Tharga.Team.Support.OpenAI) | 4.6.2 | Daniel Bohlin | Lets each team's support assistant answer through OpenAI with its own key, or t… |
| 2026-10-29 13:12:46 | [FoothillSolutions.Foundation.Cli](https://www.nuget.org/packages/FoothillSolutions.Foundation.Cli) | 0.13.0 | Foothill Solutions | `fts` - seven commands for a project consuming the FTS platform packages, inclu… |
| 2026-10-29 13:12:47 | [FoothillSolutions.Foundation.Templates](https://www.nuget.org/packages/FoothillSolutions.Foundation.Templates) | 0.18.0 | Foothill Solutions | `dotnet new` templates for the FTS platform: `fts-api` scaffolds a service comp… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
