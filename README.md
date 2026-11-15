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

## Latest list — 2026-11-15 22:19 UTC

New packages created between 2026-11-15 21:21 UTC and 2026-11-15 22:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T22-19-56-72418Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 21:32:17 | [MVFC.Pack.HttpClient](https://www.nuget.org/packages/MVFC.Pack.HttpClient) | 5.0.0 | Marcus Vinicius de Freitas Co… | Metapacote para clientes HTTP tipados com Refit, HttpClientFactory e resiliênci… |
| 2026-11-15 21:38:03 | [Nethermind.Multiformats.Hash](https://www.nuget.org/packages/Nethermind.Multiformats.Hash) | 1.5.3 | Nethermind, Trond Bråthen | Multihash implementation in C# |
| 2026-11-15 21:49:02 | [Hexalith.Agents.UI](https://www.nuget.org/packages/Hexalith.Agents.UI) | 2.0.1 | Hexalith Contributors | FrontComposer admin-setup UI for the Hexalith Agents module: the Agents domain/… |
| 2026-11-15 21:50:29 | [Nethermind.Multiformats.Address](https://www.nuget.org/packages/Nethermind.Multiformats.Address) | 1.1.11 | Nethermind, Trond Bråthen | Multiaddr implementation in C# |
| 2026-11-15 21:58:34 | [ai-factory](https://www.nuget.org/packages/ai-factory) | 0.1.0 | Kurt Mabery | A Claude Code software factory: ideas are grilled into specs, built, reviewed b… |
| 2026-11-15 22:00:34 | [Ikon.Teleport](https://www.nuget.org/packages/Ikon.Teleport) | 3.23.0 | IKON | Teleport, the binary serialization format of the IKON protocol. The IKON C# SDK… |
| 2026-11-15 22:06:37 | [KspGonogo.Sitrep.Contract](https://www.nuget.org/packages/KspGonogo.Sitrep.Contract) | 1.0.0 | ksp-gonogo | The C# Uplink surface for Gonogo, a mission-control dashboard for Kerbal Space… |
| 2026-11-15 22:13:44 | [BorrowedTorch.Persistency](https://www.nuget.org/packages/BorrowedTorch.Persistency) | 1.0.0 | Vladyslav Pysarenko | Borrowed Torch persistency: documents, a format-neutral data tree with a JSON c… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
