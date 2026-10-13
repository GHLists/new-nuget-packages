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

## Latest list — 2026-10-13 00:20 UTC

New packages created between 2026-10-12 23:19 UTC and 2026-10-13 00:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-13T00-20-21-743426Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 23:23:35 | [Crypto.Net.Aptos](https://www.nuget.org/packages/Crypto.Net.Aptos) | 1.2.0 | Gravicode Studios, Kang Fadhil | Aptos adapter for Crypto.Net: ed25519 accounts (SLIP-10 m/44'/637'), AIP-40 add… |
| 2026-10-12 23:23:57 | [Crypto.Net.Cardano](https://www.nuget.org/packages/Crypto.Net.Cardano) | 1.2.0 | Gravicode Studios, Kang Fadhil | Cardano adapter for Crypto.Net: CIP-1852 accounts with BIP32-Ed25519 (Icarus) k… |
| 2026-10-12 23:24:09 | [Crypto.Net.Generators](https://www.nuget.org/packages/Crypto.Net.Generators) | 1.2.0 | Gravicode Studios, Kang Fadhil | Source generators for Crypto.Net: Solidity ABI JSON (*.abi.json, Hardhat/Foundr… |
| 2026-10-12 23:24:10 | [Crypto.Net.Indexer](https://www.nuget.org/packages/Crypto.Net.Indexer) | 1.2.0 | Gravicode Studios, Kang Fadhil | Blockchain indexing for Crypto.Net: EVM log indexer with ABI event decoding, a… |
| 2026-10-12 23:24:11 | [Crypto.Net.Indexer.EntityFrameworkCore](https://www.nuget.org/packages/Crypto.Net.Indexer.EntityFrameworkCore) | 1.2.0 | Gravicode Studios, Kang Fadhil | Entity Framework Core storage for Crypto.Net.Indexer: checkpoints, raw EVM logs… |
| 2026-10-12 23:24:13 | [Crypto.Net.Ledger](https://www.nuget.org/packages/Crypto.Net.Ledger) | 1.2.0 | Gravicode Studios, Kang Fadhil | Ledger hardware wallet support for Crypto.Net: APDU protocol, USB HID and Specu… |
| 2026-10-12 23:24:15 | [Crypto.Net.Near](https://www.nuget.org/packages/Crypto.Net.Near) | 1.2.0 | Gravicode Studios, Kang Fadhil | NEAR Protocol adapter for Crypto.Net: ed25519 keys (SLIP-10 m/44'/397'), implic… |
| 2026-10-12 23:24:36 | [Crypto.Net.Sui](https://www.nuget.org/packages/Crypto.Net.Sui) | 1.2.0 | Gravicode Studios, Kang Fadhil | Sui adapter for Crypto.Net: ed25519 accounts (SLIP-10 m/44'/784'), suiprivkey i… |
| 2026-10-12 23:24:40 | [Crypto.Net.Ton](https://www.nuget.org/packages/Crypto.Net.Ton) | 1.2.0 | Gravicode Studios, Kang Fadhil | TON adapter for Crypto.Net: cells and bags of cells, raw and user-friendly addr… |
| 2026-10-12 23:24:59 | [Crypto.Net.Trezor](https://www.nuget.org/packages/Crypto.Net.Trezor) | 1.2.0 | Gravicode Studios, Kang Fadhil | Trezor hardware wallet support for Crypto.Net: protocol v1 framing, Trezor Brid… |
| 2026-10-12 23:25:02 | [Crypto.Net.WalletConnect](https://www.nuget.org/packages/Crypto.Net.WalletConnect) | 1.2.0 | Gravicode Studios, Kang Fadhil | WalletConnect v2 (Reown) for Crypto.Net: pair with mobile wallets through the r… |
| 2026-10-12 23:28:33 | [RecycleBinToolkit](https://www.nuget.org/packages/RecycleBinToolkit) | 1.0.0 | Denis Tulupov | A high-performance .NET library for the Windows Recycle Bin: move files and dir… |
| 2026-10-12 23:50:53 | [ButterMorph.Contracts](https://www.nuget.org/packages/ButterMorph.Contracts) | 2.1.0 | Mario Perez | Shared contracts and attributes used by ButterMorph generated code and host ser… |
| 2026-10-12 23:50:57 | [ButterMorph.Language](https://www.nuget.org/packages/ButterMorph.Language) | 2.1.0 | Mario Perez | Language adapter contracts, type mapping documents, and code generation models… |
| 2026-10-12 23:50:59 | [ButterMorph.Language.CSharp](https://www.nuget.org/packages/ButterMorph.Language.CSharp) | 2.1.0 | Mario Perez | Official C# language adapter for ButterMorph code generation and type mappings. |
| 2026-10-12 23:54:27 | [Cosmos.Types.UnidadesDeMedida](https://www.nuget.org/packages/Cosmos.Types.UnidadesDeMedida) | 1.0.0 | Cosmos | Value Object UnidadDeMedida para el ERP Cosmos: código UN/ECE Rec. 20 con catál… |
| 2026-10-12 23:59:29 | [Gravicode.ScrapyNet.Redis](https://www.nuget.org/packages/Gravicode.ScrapyNet.Redis) | 0.2.0 | Kang Fadhil (Gravicode Studio… | Distributed crawling for Scrapy.Net on Redis, after scrapy-redis: a shared sche… |
| 2026-10-13 00:04:20 | [Sail.Device.Protocol](https://www.nuget.org/packages/Sail.Device.Protocol) | 0.1.1 | Sail | 独立下位机协议组件：默认旧应用命令及解析、CRC16、流式组帧、宿主传输接口和显式文档协议入口。 |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
