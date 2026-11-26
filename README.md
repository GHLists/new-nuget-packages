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

## Latest list — 2026-11-26 03:19 UTC

New packages created between 2026-11-26 02:20 UTC and 2026-11-26 03:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-26T03-19-13-496486Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-26 02:21:37 | [ElBruno.AI.Decisions.Llama](https://www.nuget.org/packages/ElBruno.AI.Decisions.Llama) | 0.10.0 | Bruno Capuano (ElBruno) | Local Llama App System One decision models for text, images and audio. Confiden… |
| 2026-11-26 02:25:37 | [Flagpost.Client](https://www.nuget.org/packages/Flagpost.Client) | 1.0.0 | flagpost contributors | Feature flags with client-side evaluation for .NET. Polls a Flagpost API, keeps… |
| 2026-11-26 02:34:08 | [EpubPostProcessor](https://www.nuget.org/packages/EpubPostProcessor) | 0.0.1 | Max Guernsey III | Post-process EPUB files for different publishing destinations. |
| 2026-11-26 02:39:35 | [103KNN.Neuromorphic](https://www.nuget.org/packages/103KNN.Neuromorphic) | 1.0.0 | Erisnel Lora Sugve | Pure C# SIMD-accelerated Spiking Neural Network (SNN) engine with TTFS encoding… |
| 2026-11-26 02:55:56 | [Du.Abp](https://www.nuget.org/packages/Du.Abp) | 10.5.1 | Abp | Abp |
| 2026-11-26 02:57:05 | [Du.AutoMapper](https://www.nuget.org/packages/Du.AutoMapper) | 14.0.0 | Jimmy Bogard | A convention-based object-object mapper. |
| 2026-11-26 02:57:18 | [EasyInjector.DependencyInjection.WebApi](https://www.nuget.org/packages/EasyInjector.DependencyInjection.WebApi) | 1.0.0 | EasyInjector.DependencyInject… | Microsoft.Extensions.DependencyInjection 整合至 ASP.NET Web API 2 / OWIN (.NET Fra… |
| 2026-11-26 02:57:49 | [EasyApiProxy.Core.WebApi](https://www.nuget.org/packages/EasyApiProxy.Core.WebApi) | 1.0.0 | EasyApiProxy.Core.WebApi | EasyApiProxy.Core 整合至 ASP.NET Web API 2 / OWIN (.NET Framework 4.7.2) |
| 2026-11-26 03:01:16 | [Ambysto.Kit.Process](https://www.nuget.org/packages/Ambysto.Kit.Process) | 0.3.0 | Ambysto | Process reading for Ambysto apps on Windows: process snapshot, identity by (pid… |
| 2026-11-26 03:07:54 | [Du.Abp.AspNetCore.SignalR](https://www.nuget.org/packages/Du.Abp.AspNetCore.SignalR) | 10.5.1 | Abp.AspNetCore.SignalR | Abp.AspNetCore.SignalR |
| 2026-11-26 03:08:31 | [Du.Abp.Castle.Log4Net](https://www.nuget.org/packages/Du.Abp.Castle.Log4Net) | 10.5.1 | Abp.Castle.Log4Net | Abp.Castle.Log4Net |
| 2026-11-26 03:08:55 | [Du.Abp.EntityFramework.Common](https://www.nuget.org/packages/Du.Abp.EntityFramework.Common) | 10.5.1 | Abp.EntityFramework.Common | Abp.EntityFramework.Common |
| 2026-11-26 03:09:27 | [Du.Abp.Web.Common](https://www.nuget.org/packages/Du.Abp.Web.Common) | 10.5.1 | Abp.Web.Common | Abp.Web.Common |
| 2026-11-26 03:09:53 | [Du.Abp.Zero.Common](https://www.nuget.org/packages/Du.Abp.Zero.Common) | 10.5.1 | Abp.Zero.Common | Abp.Zero.Common |
| 2026-11-26 03:10:16 | [Du.AutoMapper.Collection](https://www.nuget.org/packages/Du.AutoMapper.Collection) | 11.0.0 | Tyler Carlson | Collection Add/Remove/Update support for AutoMapper. AutoMapper.Collection adds… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
