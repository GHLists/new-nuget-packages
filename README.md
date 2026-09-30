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

## Latest list — 2026-09-30 11:20 UTC

New packages created between 2026-09-30 10:20 UTC and 2026-09-30 11:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-30T11-20-38-303251Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-30 10:22:53 | [Dataverse.ConnectionStringProvider.Modern](https://www.nuget.org/packages/Dataverse.ConnectionStringProvider.Modern) | 1.1.0 | Łukasz Grzybowski-Glikman | Provides flexible Dataverse connection string resolution for modern .NET, allow… |
| 2026-09-30 10:23:40 | [LibPlayground](https://www.nuget.org/packages/LibPlayground) | 1.0.0 | LibPlayground | SAP OData, REST, Excel (okuma/yazma), veritabanı (ADO.NET, SqlBulkCopy), e-post… |
| 2026-09-30 10:39:37 | [ZeroLlm.Core](https://www.nuget.org/packages/ZeroLlm.Core) | 1.0.0 | Phong Võ | Pure C# in-process Small Language Model (SLM) runtime, GGUF v2/v3 binary parser… |
| 2026-09-30 10:45:47 | [L33.Configuration.KeyVault](https://www.nuget.org/packages/L33.Configuration.KeyVault) | 1.0.0 | L33 Solutions | Azure Key Vault configuration provider for L33 apps. AddL33KeyVault() layers a… |
| 2026-09-30 10:45:58 | [Sdcb.GgufWeights.Hy-MT2-1.8B-1.25Bit](https://www.nuget.org/packages/Sdcb.GgufWeights.Hy-MT2-1.8B-1.25Bit) | 1.0.0 | sdcb | Hy-MT2-1.8B-1.25Bit.gguf as embedded .NET resources (part 1/2). Installing this… |
| 2026-09-30 11:05:20 | [CoralCore.Forms](https://www.nuget.org/packages/CoralCore.Forms) | 8.0.11 | Robert Persson | UI functionallity for CoralCore framework |
| 2026-09-30 11:11:01 | [Sdcb.GgufWeights.Hy-MT2-1.8B-Q6_K.Part5](https://www.nuget.org/packages/Sdcb.GgufWeights.Hy-MT2-1.8B-Q6_K.Part5) | 1.0.0 | sdcb | Hy-MT2-1.8B-Q6_K.gguf part 5/7. Installed automatically by Sdcb.GgufWeights.Hy-… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
