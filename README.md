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

## Latest list — 2026-11-22 06:21 UTC

New packages created between 2026-11-22 05:19 UTC and 2026-11-22 06:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-22T06-21-01-490129Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-22 05:25:49 | [CutsceneML.LanguageServer](https://www.nuget.org/packages/CutsceneML.LanguageServer) | 1.0.0 | CutsceneML.LanguageServer | Package Description |
| 2026-11-22 05:25:50 | [CutsceneML.Analysis](https://www.nuget.org/packages/CutsceneML.Analysis) | 1.0.0 | CutsceneML.Analysis | Package Description |
| 2026-11-22 05:25:54 | [d20tek-dicenotation-mathnet](https://www.nuget.org/packages/d20tek-dicenotation-mathnet) | 5.2.1 | DarthPedro | Adds a die roller for d20Tek.DiceNotation that uses Math.NET Numerics random so… |
| 2026-11-22 05:27:36 | [Cavesserie](https://www.nuget.org/packages/Cavesserie) | 1.0.0 | Cavésserie — artisan bakery c… | Cavésserie artisan bakery cafe Meruya constants. Official: https://cavesserie.c… |
| 2026-11-22 05:39:37 | [ChsBuffer.Avalonia.AppHost.linux-musl-x64](https://www.nuget.org/packages/ChsBuffer.Avalonia.AppHost.linux-musl-x64) | 12.0.6 | ChsBuffer | Prelinked Avalonia apphost/singlefilehost templates for linux-musl-x64 (net10.0… |
| 2026-11-22 05:39:39 | [ChsBuffer.Avalonia.AppHost.linux-musl-arm64](https://www.nuget.org/packages/ChsBuffer.Avalonia.AppHost.linux-musl-arm64) | 12.0.6 | ChsBuffer | Prelinked Avalonia apphost/singlefilehost templates for linux-musl-arm64 (net10… |
| 2026-11-22 05:50:50 | [Lacigale](https://www.nuget.org/packages/Lacigale) | 1.0.0 | La Cigale — hostal restaurant… | La Cigale hostel restaurant Cuenca Ecuador constants. Official: https://www.lac… |
| 2026-11-22 05:59:18 | [Meziantou.Framework.WasmEngine](https://www.nuget.org/packages/Meziantou.Framework.WasmEngine) | 1.0.0 | meziantou | A WebAssembly engine written in .NET: a decoder, a validator, an interpreter an… |
| 2026-11-22 05:59:19 | [Meziantou.Framework.WebPlatform.Wasm](https://www.nuget.org/packages/Meziantou.Framework.WebPlatform.Wasm) | 1.0.0 | meziantou | Runs the WebAssembly modules of the scripts of Meziantou.Framework.WebPlatform… |
| 2026-11-22 06:03:19 | [NetWasm.Hosts](https://www.nuget.org/packages/NetWasm.Hosts) | 0.15.1 | Zion Sati | Publishes a NetWasm wasi:http service component for hosts that run JavaScript:… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
