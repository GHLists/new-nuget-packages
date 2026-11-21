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

## Latest list — 2026-11-21 17:19 UTC

New packages created between 2026-11-21 16:21 UTC and 2026-11-21 17:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-21T17-19-26-525641Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-21 16:33:05 | [Alexpivo394.Revit.Families.Files](https://www.nuget.org/packages/Alexpivo394.Revit.Families.Files) | 1.0.0 | Alexpivo394 | Revit family library without Revit: file hash, type catalog parser, library sca… |
| 2026-11-21 16:33:06 | [Alexpivo394.Revit.Families.Revit](https://www.nuget.org/packages/Alexpivo394.Revit.Families.Revit) | 2027.1.0 | Alexpivo394 | UI-free Revit reader of a family document: category, placement, types with thei… |
| 2026-11-21 16:33:57 | [Freenaute.Freebox.Client](https://www.nuget.org/packages/Freenaute.Freebox.Client) | 1.0.0 | AriusII | Fluent Freebox Server HTTP client with dependency injection and NativeAOT-compa… |
| 2026-11-21 16:34:19 | [SwiftDispatch.EntityFrameworkCore](https://www.nuget.org/packages/SwiftDispatch.EntityFrameworkCore) | 2.1.0 | Kamyab Valipour | Attribute-selected Entity Framework Core transactions for SwiftDispatch request… |
| 2026-11-21 16:34:20 | [SwiftDispatch.FluentValidation](https://www.nuget.org/packages/SwiftDispatch.FluentValidation) | 2.1.0 | Kamyab Valipour | Asynchronous FluentValidation request pipeline integration for SwiftDispatch. |
| 2026-11-21 16:39:23 | [DotFluent.Optional](https://www.nuget.org/packages/DotFluent.Optional) | 1.0.0 | Michael Holler | A companion package to DotFluent that adds Option<T> and Result<T> / Result<TVa… |
| 2026-11-21 17:06:58 | [AutoNormalize.Abstractions](https://www.nuget.org/packages/AutoNormalize.Abstractions) | 1.0.0 | DotNet.AutoNormalize Contribu… | Core abstractions, interfaces, and declarative attributes for DotNet.AutoNormal… |
| 2026-11-21 17:06:59 | [AutoNormalize.AspNetCore](https://www.nuget.org/packages/AutoNormalize.AspNetCore) | 1.0.0 | DotNet.AutoNormalize Contribu… | Unified ASP.NET Core integration for DotNet.AutoNormalize: Minimal APIs, MVC Mo… |
| 2026-11-21 17:07:00 | [AutoNormalize.Core](https://www.nuget.org/packages/AutoNormalize.Core) | 1.0.0 | DotNet.AutoNormalize Contribu… | High-performance input normalization engine, built-in rules, metadata caching,… |
| 2026-11-21 17:07:01 | [AutoNormalize.EntityFrameworkCore](https://www.nuget.org/packages/AutoNormalize.EntityFrameworkCore) | 1.0.0 | DotNet.AutoNormalize Contribu… | Entity Framework Core SaveChanges interceptor and entity input normalization fo… |
| 2026-11-21 17:07:03 | [AutoNormalize.Json](https://www.nuget.org/packages/AutoNormalize.Json) | 1.0.0 | DotNet.AutoNormalize Contribu… | System.Text.Json type contract modifiers and metadata-aware deserialization hoo… |
| 2026-11-21 17:11:49 | [GCScript.Secrets.Configuration](https://www.nuget.org/packages/GCScript.Secrets.Configuration) | 1.0.0 | GCScript | Carrega credenciais da API GCScript.Secrets no IConfiguration, como o UserSecre… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
