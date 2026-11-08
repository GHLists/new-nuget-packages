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

## Latest list — 2026-11-08 11:20 UTC

New packages created between 2026-11-08 10:19 UTC and 2026-11-08 11:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T11-20-50-561861Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-08 10:20:37 | [etunnel](https://www.nuget.org/packages/etunnel) | 1.0.0 | etunnel authors | Expose a local service through an etunnel reverse-tunnel server with one line o… |
| 2026-11-08 10:22:03 | [KitStack.Storage.Abstractions](https://www.nuget.org/packages/KitStack.Storage.Abstractions) | 0.3.2 | ghaith100994 | Storage interfaces, models and the shared provider pipeline for KitStack.Storag… |
| 2026-11-08 10:22:04 | [KitStack.Storage.AspNetCore](https://www.nuget.org/packages/KitStack.Storage.AspNetCore) | 0.3.2 | ghaith100994 | ASP.NET Core integration for KitStack.Storage: an authorised file-download endp… |
| 2026-11-08 10:22:08 | [KitStack.Storage.Fakes](https://www.nuget.org/packages/KitStack.Storage.Fakes) | 0.3.2 | ghaith100994 | In-memory fake storage provider for KitStack.Storage used for tests and local d… |
| 2026-11-08 10:28:45 | [Interlink.Extensions.Telemetry](https://www.nuget.org/packages/Interlink.Extensions.Telemetry) | 1.7.0 | Manojbabu | OpenTelemetry-style Activity instrumentation for Interlink mediator requests, s… |
| 2026-11-08 10:33:04 | [OssmSharp.Runtime.Oem](https://www.nuget.org/packages/OssmSharp.Runtime.Oem) | 0.1.0 | OssmSharp contributors | Bluetooth discovery and control for OSSM devices on Windows and macOS. Includes… |
| 2026-11-08 10:37:16 | [Morph.Email](https://www.nuget.org/packages/Morph.Email) | 1.24.0 | https://github.com/Papyrine/M… | Converts email (.eml and Outlook .msg) to PDF with Morph: the sender, recipient… |
| 2026-11-08 11:14:30 | [TouchKeyboard.Ime.Pinyin.Extended](https://www.nuget.org/packages/TouchKeyboard.Ime.Pinyin.Extended) | 0.2.0 | TouchKeyboard contributors | Optional extended pinyin lexicon for TouchKeyboard.Ime.Pinyin: about 100k commo… |
| 2026-11-08 11:14:30 | [TouchKeyboard.Ime.Pinyin](https://www.nuget.org/packages/TouchKeyboard.Ime.Pinyin) | 0.2.0 | TouchKeyboard contributors | Optional managed pinyin IME for TouchKeyboard: full pinyin, word/sentence segme… |
| 2026-11-08 11:14:31 | [TouchKeyboard.Avalonia](https://www.nuget.org/packages/TouchKeyboard.Avalonia) | 0.2.0 | TouchKeyboard contributors | Avalonia frontend for TouchKeyboard: overlay host, keys, editor surface and con… |
| 2026-11-08 11:14:32 | [TouchKeyboard.Core](https://www.nuget.org/packages/TouchKeyboard.Core) | 0.2.0 | TouchKeyboard contributors | Pure .NET Standard 2.0 core for the TouchKeyboard embedded keyboard: modes, pro… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
