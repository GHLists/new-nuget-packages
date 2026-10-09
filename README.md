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

## Latest list — 2026-10-09 19:19 UTC

New packages created between 2026-10-09 18:20 UTC and 2026-10-09 19:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T19-19-36-723408Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 18:21:33 | [ErtisAuth.Sdk.AspNetCore](https://www.nuget.org/packages/ErtisAuth.Sdk.AspNetCore) | 10.0.0 | Ertuğrul Özcan | ErtisAuth SDK AspNetCore Extension |
| 2026-10-09 18:27:32 | [ManagedCode.Prostir.Cli.linux-x64](https://www.nuget.org/packages/ManagedCode.Prostir.Cli.linux-x64) | 0.4.261009.3 | ManagedCode | Prostir creator worker and MCP command-line tool. |
| 2026-10-09 18:27:40 | [ManagedCode.Prostir.Cli.win-x64](https://www.nuget.org/packages/ManagedCode.Prostir.Cli.win-x64) | 0.4.261009.3 | ManagedCode | Prostir creator worker and MCP command-line tool. |
| 2026-10-09 18:27:49 | [ManagedCode.Prostir.Cli.osx-x64](https://www.nuget.org/packages/ManagedCode.Prostir.Cli.osx-x64) | 0.4.261009.3 | ManagedCode | Prostir creator worker and MCP command-line tool. |
| 2026-10-09 18:27:58 | [ManagedCode.Prostir.Cli.osx-arm64](https://www.nuget.org/packages/ManagedCode.Prostir.Cli.osx-arm64) | 0.4.261009.3 | ManagedCode | Prostir creator worker and MCP command-line tool. |
| 2026-10-09 18:27:59 | [ManagedCode.Prostir.Cli](https://www.nuget.org/packages/ManagedCode.Prostir.Cli) | 0.4.261009.3 | ManagedCode | Prostir creator worker and MCP command-line tool. |
| 2026-10-09 18:47:23 | [Cendia.SchemaGenerator](https://www.nuget.org/packages/Cendia.SchemaGenerator) | 0.0.1 | Cendia | Placeholder. Cendia packages are not distributed on nuget.org. Add the Cendia f… |
| 2026-10-09 18:47:24 | [Cendia.Storage.AzureBlob](https://www.nuget.org/packages/Cendia.Storage.AzureBlob) | 0.0.1 | Cendia | Placeholder. Cendia packages are not distributed on nuget.org. Add the Cendia f… |
| 2026-10-09 18:47:25 | [Cendia.Templates](https://www.nuget.org/packages/Cendia.Templates) | 0.0.1 | Cendia | Placeholder. Cendia packages are not distributed on nuget.org. Add the Cendia f… |
| 2026-10-09 18:47:25 | [Cendia.UI](https://www.nuget.org/packages/Cendia.UI) | 0.0.1 | Cendia | Placeholder. Cendia packages are not distributed on nuget.org. Add the Cendia f… |
| 2026-10-09 18:47:26 | [Cendia.AspNetCore](https://www.nuget.org/packages/Cendia.AspNetCore) | 0.0.1 | Cendia | Placeholder. Cendia packages are not distributed on nuget.org. Add the Cendia f… |
| 2026-10-09 18:47:26 | [Cendia.Captcha.Turnstile](https://www.nuget.org/packages/Cendia.Captcha.Turnstile) | 0.0.1 | Cendia | Placeholder. Cendia packages are not distributed on nuget.org. Add the Cendia f… |
| 2026-10-09 18:47:27 | [Cendia.Core](https://www.nuget.org/packages/Cendia.Core) | 0.0.1 | Cendia | Placeholder. Cendia packages are not distributed on nuget.org. Add the Cendia f… |
| 2026-10-09 18:47:27 | [Cendia.Data](https://www.nuget.org/packages/Cendia.Data) | 0.0.1 | Cendia | Placeholder. Cendia packages are not distributed on nuget.org. Add the Cendia f… |
| 2026-10-09 18:47:28 | [Cendia.License](https://www.nuget.org/packages/Cendia.License) | 0.0.1 | Cendia | Placeholder. Cendia packages are not distributed on nuget.org. Add the Cendia f… |
| 2026-10-09 18:56:12 | [Sxnnyside.Pollux](https://www.nuget.org/packages/Sxnnyside.Pollux) | 0.1.0 | Sxnnyside Project | Deterministic Execution Authority and Sandboxing SDK for the .NET Runtime |
| 2026-10-09 18:59:15 | [Agile.Maui.PdfGen](https://www.nuget.org/packages/Agile.Maui.PdfGen) | 1.2.0 | Micael Otowicz | Biblioteca open source de geração de PDF para .NET MAUI com API fluente inspira… |
| 2026-10-09 19:02:33 | [CommunityToolkit.VectorData.Chroma](https://www.nuget.org/packages/CommunityToolkit.VectorData.Chroma) | 1.0.0-preview | Microsoft.Toolkit,dotnetfound… | Chroma provider for Microsoft.Extensions.VectorData by the .NET Community Toolk… |
| 2026-10-09 19:07:00 | [HexDB.EntityFrameworkCore](https://www.nuget.org/packages/HexDB.EntityFrameworkCore) | 1.0.0 | Dream In Hex | Entity Framework Core provider for HexDB: LINQ queries translated to HexDB's fi… |
| 2026-10-09 19:07:00 | [HexDB.Client](https://www.nuget.org/packages/HexDB.Client) | 1.0.0 | Dream In Hex | Client for HexDB, the hexagonal document database. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
