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

## Latest list — 2026-11-19 16:20 UTC

New packages created between 2026-11-19 15:22 UTC and 2026-11-19 16:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-19T16-20-31-997968Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-19 15:22:51 | [DoorstepCO.Core](https://www.nuget.org/packages/DoorstepCO.Core) | 0.1.0 | Samuel Marino | Parses, normalizes and validates free-text Colombian addresses. |
| 2026-11-19 15:28:20 | [ForEach.Infrastructure.External.Vies](https://www.nuget.org/packages/ForEach.Infrastructure.External.Vies) | 0.1.0 | For-Each Smederevo | Client for the VIES REST API of the European Commission: checks whether an EU V… |
| 2026-11-19 15:36:33 | [YotsubaShader.Extensions](https://www.nuget.org/packages/YotsubaShader.Extensions) | 0.9.0 | YotsubaShader contributors | YotsubaShader YotsubaShader.Extensions library. |
| 2026-11-19 15:36:35 | [YotsubaShader.Extensions.FNA](https://www.nuget.org/packages/YotsubaShader.Extensions.FNA) | 0.9.0 | YotsubaShader contributors | YotsubaShader plugin: FNA (.fxb) backend for the yotsuba CLI. |
| 2026-11-19 15:36:36 | [YotsubaShader.Extensions.Godot](https://www.nuget.org/packages/YotsubaShader.Extensions.Godot) | 0.9.0 | YotsubaShader contributors | YotsubaShader plugin: Godot Shading Language (.gdshader) backend for the yotsub… |
| 2026-11-19 15:36:37 | [YotsubaShader.Extensions.KNI](https://www.nuget.org/packages/YotsubaShader.Extensions.KNI) | 0.9.0 | YotsubaShader contributors | YotsubaShader plugin: KNI WebGL (.knifx) backend for the yotsuba CLI. |
| 2026-11-19 15:36:38 | [YotsubaShader.Extensions.MonoGame](https://www.nuget.org/packages/YotsubaShader.Extensions.MonoGame) | 0.9.0 | YotsubaShader contributors | YotsubaShader plugin: MonoGame (MGFX) backend for the yotsuba CLI. |
| 2026-11-19 15:38:58 | [RapidRepo.EntityFrameworkCore](https://www.nuget.org/packages/RapidRepo.EntityFrameworkCore) | 9.0.0 | Tibor Horváth | Package Description |
| 2026-11-19 15:59:10 | [Ina](https://www.nuget.org/packages/Ina) | 0.1.0 | Mayuki Sawatari | Ina (IL to NAtive) compiles .NET applications to native executables without a n… |
| 2026-11-19 15:59:11 | [Ina.Sdk](https://www.nuget.org/packages/Ina.Sdk) | 0.1.0 | Mayuki Sawatari | Publishes .NET applications as native executables with Ina: with the PublishIna… |
| 2026-11-19 16:02:11 | [Ebitex.Commerce.Delivery](https://www.nuget.org/packages/Ebitex.Commerce.Delivery) | 0.1.18 | ebitex software LLC | Server-side client for the ebitex Commerce Delivery API: read a store's catalog… |
| 2026-11-19 16:02:48 | [Flowrensic.Temporal.Dotnet.Sdk](https://www.nuget.org/packages/Flowrensic.Temporal.Dotnet.Sdk) | 0.6.83 | Flowrensic | Flowrensic runs beside your durable workflow engine and finds problems in your… |
| 2026-11-19 16:03:12 | [VolEngine](https://www.nuget.org/packages/VolEngine) | 1.1.0 | Gabriel Matte | GARCH-family and DCC volatility models (rugarch and rmgarch conventions) on a n… |
| 2026-11-19 16:04:08 | [ForEach.Infrastructure.External.Octopus](https://www.nuget.org/packages/ForEach.Infrastructure.External.Octopus) | 0.1.0 | For-Each Smederevo | Typed clients for the four Octopus (Inaras) accounting web services - Rest, Man… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
