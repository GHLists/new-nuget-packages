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

## Latest list — 2026-10-26 16:22 UTC

New packages created between 2026-10-26 15:21 UTC and 2026-10-26 16:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-26T16-22-36-731785Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-26 15:24:11 | [PlaidClient](https://www.nuget.org/packages/PlaidClient) | 1.0.0 | Tuomas Hietanen | Plaid open banking client: Link tokens, item linking, transactions sync and ver… |
| 2026-10-26 15:25:39 | [Webority.Azure.KeyVault](https://www.nuget.org/packages/Webority.Azure.KeyVault) | 0.29.0 | Webority.Azure.KeyVault | Loads an app's secrets from its own Azure Key Vault at startup for the Webority… |
| 2026-10-26 15:25:49 | [Webority.Cloudflare.R2](https://www.nuget.org/packages/Webority.Cloudflare.R2) | 0.29.0 | Webority.Cloudflare.R2 | Cloudflare R2 object storage for the Webority fleet: put, delete, exists and li… |
| 2026-10-26 15:34:45 | [HttpClient.Resilience.Analyzers.Scan](https://www.nuget.org/packages/HttpClient.Resilience.Analyzers.Scan) | 0.1.213 | George Wall | Scan any .NET solution for HttpClient, IHttpClientFactory, typed-client, Polly,… |
| 2026-10-26 15:36:17 | [MrKWatkins.OakPsg.AY38912](https://www.nuget.org/packages/MrKWatkins.OakPsg.AY38912) | 0.1.0 | Kevin Watkins | Package Description |
| 2026-10-26 15:36:18 | [MrKWatkins.OakPsg.Audio](https://www.nuget.org/packages/MrKWatkins.OakPsg.Audio) | 0.1.0 | Kevin Watkins | Package Description |
| 2026-10-26 15:36:19 | [MrKWatkins.OakPsg.ZXSpectrumBeeper](https://www.nuget.org/packages/MrKWatkins.OakPsg.ZXSpectrumBeeper) | 0.1.0 | Kevin Watkins | Package Description |
| 2026-10-26 15:38:02 | [Maniacal](https://www.nuget.org/packages/Maniacal) | 0.1.0-alpha | Maniacal contributors | Command line player for Maniac Mansion (Commodore 64, DOS 1987 and 1988): dotne… |
| 2026-10-26 15:38:03 | [Maniacal.Scumm](https://www.nuget.org/packages/Maniacal.Scumm) | 0.1.0-alpha | Maniacal contributors | The SCUMM interpreter for Maniac Mansion (V0, V1 and V2), ported from ScummVM. |
| 2026-10-26 15:44:27 | [SoulRipper](https://www.nuget.org/packages/SoulRipper) | 0.1.1 | SuperJMN | Rips the music, jingles and sound effects of NES and Game Boy ROMs to VGM files… |
| 2026-10-26 15:47:20 | [MicroGauge.Avalonia](https://www.nuget.org/packages/MicroGauge.Avalonia) | 1.1.0.2 | Galen Blakeman | MicroGauge controls for Avalonia |
| 2026-10-26 15:54:43 | [FactSet.SDK.Conversational](https://www.nuget.org/packages/FactSet.SDK.Conversational) | 1.0.0 | FactSet Research Systems | Conversational client library for .NET |
| 2026-10-26 16:06:34 | [LIghtJUNction.Jlib](https://www.nuget.org/packages/LIghtJUNction.Jlib) | 0.1.0 | Peter Han,LIghtJUNction | Standalone shared PLib-compatible library for Oxygen Not Included mods. Install… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
